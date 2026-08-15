from CommonClient import ClientCommandProcessor, server_loop, get_base_parser, gui_enabled, logger, handle_url_arg
tracker_loaded = False
try:
    from worlds.tracker.TrackerClient import TrackerGameContext as CommonContext
    tracker_loaded = True
except ModuleNotFoundError:
    from CommonClient import CommonContext
import Utils
import asyncio
import colorama
import logging
from collections.abc import Sequence
import random
import math

from BaseClasses import ItemClassification as IC
from worlds.tww3.dataStructs import itemType
from worlds.tww3.item_tables import factions as fm, settlements as sm
from worlds.tww3.item_tables.filler_item_table import fillerDict, trapDict
from worlds.tww3.item_tables.ancillaries_table import ancillariesDict
from worlds.tww3.item_tables.progression_table import progressionDict
from worlds.tww3 import TWW3World, factionItemManager, deathLink
import os
from NetUtils import ClientStatus

path = "."

class TWW3CommandProcessor(ClientCommandProcessor):    

    def _cmd_traps(self):
        """Turn Traps off and on."""
        if isinstance(self.ctx, TWW3Context):
            self.ctx.are_traps_enabled = not self.ctx.are_traps_enabled
            logger.info(f"Traps are now turned {'on' if self.ctx.are_traps_enabled else 'off'}.")
            return

    def _cmd_capitals(self):
        """Prints a list of starting Capitals."""
        if isinstance(self.ctx, TWW3Context):
            for faction, capital in self.ctx.capitals.items():
                factionName = [f.readableName for f in fm.factionDict.values() if f.name == faction][0]
                logger.info(f"Faction: {factionName} Capital: {sm.mapDict[self.ctx.map][capital]}")
            return

    def _cmd_inrange(self):
        """Prints a list of all factions that are within diplomatic range"""
        if isinstance(self.ctx, TWW3Context):
            for faction in self.ctx.inRangeFactions:
                factionName = [f.readableName for f in fm.factionDict.values() if f.name == faction][0]
                logger.info(f"Faction: {factionName}")
            return

    def _cmd_ac(self):
        """Prints the current number of settlements you can control."""
        if isinstance(self.ctx, TWW3Context):
            logger.info(f"You now have: {self.ctx.expansionItems} Administrative Capacity")
            logger.info(f"You can now control {self.ctx.expansionItems * self.ctx.adminCapacity} settlements without penalties")
            logger.info(f"You currently control {self.ctx.settlementCount} settlements")
            return

    def _cmd_orbs(self):
        """Prints the current number of orbs of dominance that you own."""
        if isinstance(self.ctx, TWW3Context):
            logger.info(f"You currently hold: {self.ctx.numberOfOrbs} Orbs of dominance")
            return

    def _cmd_logging(self):
        """Toggles location logging."""
        if isinstance(self.ctx, TWW3Context):
            self.ctx.logChecks = not self.ctx.logChecks
            logger.info(f"Location logging is now set to {self.ctx.logChecks}")
            return

    def _cmd_version(self):
        """Prints the version of the client."""
        if isinstance(self.ctx, TWW3Context):
            logger.info(f"You are running version {self.ctx.version}")
            return

    def _cmd_teleport(self):
        """Teleports lords and heroes to starting location (use if your lord did not teleport)."""
        if isinstance(self.ctx, TWW3Context):
            for faction, settlement in self.ctx.capitals.items():
                if faction == self.ctx.playerFaction:
                    #self.ctx.messenger.runTemp(f'teleport_all_heroes_of_faction_to_region("{faction}", "{settlement}")')
                    self.ctx.messenger.runTemp(f'archipelago.teleport_all_units_of_faction_to_region("{faction}", "{settlement}")')
                    break
            for faction, settlement in self.ctx.hordes.items():
                if faction == self.ctx.playerFaction:
                    #self.ctx.messenger.runTemp(f'teleport_all_heroes_of_faction_to_region("{faction}", "{settlement}")')
                    self.ctx.messenger.runTemp(f'archipelago.teleport_all_units_of_faction_to_region("{faction}", "{settlement}")')
                    break
            return

    def _cmd_deathlink(self):
        """Turn Deathlink off and on."""
        if isinstance(self.ctx, TWW3Context):
            self.ctx.deathLinkEnabled = not self.ctx.deathLinkEnabled
            logger.info(f"Deathlink is now set to {self.ctx.deathLinkEnabled}")
            return

    def _cmd_debug(self):
        """Set Admin Capacity to Maximum"""
        if isinstance(self.ctx, TWW3Context):
            #if "jordan" in self.ctx.player_names:
            self.ctx.adminCapacity = 1000
            return

    def _cmd_resync(self):
        """Resend all units, techs, buildings and progression items"""
        if isinstance(self.ctx, TWW3Context):
            TWW3Context.resync(self.ctx)
            return

        #Need to rewrite on_received_items to allow for writing to temp file when this function is ran.
        #Or just make this a copy of on_received_items with only the relevant details
        #if isinstance(self.ctx, TWW3Context):
        #    if self.ctx.gameMode == "conquest":
        #        self.ctx.expansionItems = 1
        #    else:
        #        self.ctx.expansionItems = 0
        #
        #    itemArchiveDict = {"items": self.ctx.itemArchive.copy()}
        #    self.ctx.itemArchive = []
        #    self.ctx.on_received_items(itemArchiveDict)

class Messenger:
    def __init__(self, path):
        self.file = open(path, 'w+')
        self.tempFile = open(f"{path[:-3]}-temp.in", 'w+')
        self.firstLine = True

    def run(self, message):
        self.file.write(f"\n{message}")
        self.file.flush()

    def firstWrite(self, message):
        self.file.write(message)
        self.file.flush()

    def runTemp(self, message):
        if self.firstLine:
            self.tempFile.write(f"{message}")
            self.firstLine = False
        else:
            self.tempFile.write(f"\n{message}")
        self.tempFile.flush()

    def flush(self):
        self.file.flush()

class Watcher:
    def __init__(self, path, context):
        self.context = context
        if os.path.isfile(os.path.join(path, "engine.out")):
            self.file = open(os.path.join(path, "engine.out"), "r")
        else:
            self.file = open(os.path.join(path, "engine.out"), "w+")
        line = self.file.readline()
        if line != f"{self.context.seed}\n":
            print(f"File seed: {line} != Multiworld seed: {self.context.seed}")
            self.file = open(os.path.join(path, "engine.out"), "w+")
            self.file.write(f"{self.context.seed}\n")
        self.tempFile = file = open(os.path.join(path, "engine-temp.out"), "w+")

        self.files = {
            "engine.out": self.file,
            "engine-temp.out": self.tempFile
        }

    async def watch(self, fileName, gameMode):
        print(f"Watching {fileName}...")
        file = self.files[fileName]
        file.seek(0, 2)
        activeInode = os.fstat(file.fileno()).st_ino
        path = file.name
        while True:
            line = file.readline()
            if line:
                line = line.strip()
                prefix = line.split(" ")[0]
                match prefix:
                    case "":
                        pass

                    case "deathlink":
                        await self.context.send_death(line.split(" ")[1])

                    case "building" | "tech":
                        if self.context.sanity:
                            if self.context.logChecks:
                                logger.info(f"Sending {line}")
                            await self.context.checkSanity(line.split(" ")[1], prefix)

                    case "ritual":
                        if self.context.ritualSanity:
                            if self.context.logChecks:
                                logger.info(f"Sending {line}")
                            if line.split("_")[-1] == "upgraded": #Check for upgraded rituals
                                line = line[:-9]
                            await self.context.checkSanity(line.split(" ")[1], prefix)

                    case "battles":
                        if self.context.battleSanity:
                            if self.context.logChecks:
                                logger.info(f"Sending {line}")
                            await self.context.checkBattleSanity(line.split(" ")[1])

                    case "sacked" | "razed":
                        if self.context.despoilerSanity:
                            if self.context.logChecks:
                                logger.info(f"Sending {line}")
                            await self.context.checkDespoilerSanity(line)
                    case _:
                        if self.context.logChecks:
                            if gameMode == "conquest":
                                logger.info(f"Sending Empire Size {line}")
                            elif gameMode == "spheres":
                                logger.info(f"Sending Location {line}")
                        await self.context.check(line)

            await asyncio.sleep(0.1)

            try:
                st = os.stat(path)
            except FileNotFoundError:
                continue
            try:
                rotated = st.st_ino != activeInode
                truncated = file.tell() > st.st_size

                if rotated or truncated:
                    file.close()
                    file = open(path, "r", encoding="utf-8", errors="replace")
                    activeInode = os.fstat(file.fileno()).st_ino
                    file.seek(0, os.SEEK_END)
            except Exception as e:
                print(e)


class TWW3Context(CommonContext):
    tags = {"AP"}
    game = 'Total War Warhammer III'
    command_processor = TWW3CommandProcessor
    items_handling = 0b111
    are_traps_enabled = True

    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        #self.initialized = False
        self.itemDict = {}
        self.deathLinkPending = False
        self.notificationPending = False
        self.logChecks = False
        self.settlementCount = 0
        self.locationMapping = False
        self.descriptions = {}

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(TWW3Context, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def on_package(self, cmd: str, args: dict):
        match cmd:
            case "Connected":
                self.on_connected(args)

            case "Bounced":
                if "tags" in args:
                    if "DeathLink" in args["tags"]:
                        self.on_deathlink(args["data"])

            case "ReceivedItems":
                self.on_received_items(args)

            case "LocationInfo":
                if self.locationMapping:
                    self.locationMapping = False
                    for networkItem in args["locations"]:

                        if self.revealHints:
                            playerName = self.player_names[networkItem.player]
                            itemName = self.item_names.lookup_in_slot(networkItem.item, networkItem.player)
                        else:
                            playerName = "someone"
                            itemName = "item"
                        itemTypeLookup = {
                            0: f"How boring... This contains {playerName}'s {itemName}",
                            1: f"I'm {random.randint(1,100)}% sure that this {itemName} is important to {playerName}.",
                            2: f"This could come come in handy for {playerName}, it contains their {itemName}.",
                            3: f"I have a sneaking suspicious that {playerName} really wants this {itemName}.",
                            4: f"I'm sure {playerName} will thank you for sending them this {itemName}. ;-)",
                            5: f"This contains {playerName}'s {itemName}, but make sure they read the fine print.",
                            6: f"I'm {random.randint(1,100)}% confident that {playerName} needs this {itemName}. They may not realise it yet.",
                            7: f"How curious, {playerName}'s {itemName} seems very important. Side effects may include death."
                        }
                        location = self.location_names.lookup_in_slot(networkItem.location)
                        self.descriptions[location] = itemTypeLookup[networkItem.flags]

                        #print(f"{location} contains {playerName}'s {itemName}.\n{itemTypeLookup[networkItem.flags]}")
                    if self.sanity:
                        self.createBuildingMissions()
                    if not self.fastResearch and self.sanity:
                        self.createTechMissions()

                    self.messenger.runTemp("archipelago.initialise()")

                super().on_package(cmd, args)


        super().on_package(cmd, args)

    def on_connected(self, args: dict):
        self.lineCount = 0
        self.itemArchive = {"items": []}
        self.inRangeFactions = []

        self.version = TWW3World.world_version.as_simple_string()
        if self.version != args['slot_data']['version']:
            raise Exception(f"ERROR: Host ({args['slot_data']['version']}) and player ({self.version}) are using different versions of the TWW3 APWorld!")
        else:
            logger.info(f"You are running: {self.version} of the TWW3 APWorld")

        self.path = TWW3World.settings.tww3_path
        #self.path = "/home/jordan/Documents/"
        #self.path = "C:/Users/jordan.whiteley/Desktop/"
        self.seed = args['slot_data']['seed']

        if not self.path or not os.path.exists(self.path):
            raise Exception('ERROR: Could not find Warhammer folder. Please correct the path in your host.yaml.')
        if not os.path.isfile(os.path.join(self.path, "Warhammer3.exe")) and not os.path.isfile(os.path.join(self.path, "TotalWarhammer3.sh")):
            raise Exception('ERROR: Could not find Warhammer3.exe/Warhammer3.sh Please correct the path in your host.yaml.')

        self.gameMode = args['slot_data']['game_mode']
        logger.info(f"The game mode is: {self.gameMode}")

        self.watcher = Watcher(self.path, self)
        temp_watcher_task = asyncio.create_task(self.watcher.watch("engine-temp.out", self.gameMode), name='temp_watcher')
        watcher_task = asyncio.create_task(self.watcher.watch("engine.out", self.gameMode), name='watcher')
        self.messenger = Messenger(os.path.join(self.path, "engine.in"))

        self.deathLinkEnabled = args['slot_data']["death_link"]
        if self.deathLinkEnabled:
            asyncio.create_task(self.update_death_link(True))
            logger.warning("DeathLink is enabled, good luck...")

        self.deathLinkEffects = args['slot_data']["death_link_effects"]

        self.deathLinkOptions = deathLink.createDeathLinkFunctions(self.deathLinkEffects)

        self.modList = args['slot_data']['mod_list']
        fm.addModdedFactions(self.modList)
        self.playerFaction = fm.factionDict[args["slot_data"]["starting_faction"]].name

        #The Settra handler
        if self.playerFaction == "wh2_dlc09_tmb_khemri":
            logger.info("""The player faction is: Settra... Great King, the Imperishable, Khemrikhara, The Great King of Nehekhara, King of Kings, Opener of the Way, Wielder of the Divine Flame, Punisher of Nomads, The Great Unifier, 
                          'Commander of the Golden Legion, Sacred of Appearance, Bringer of Light, Father of Hawks, Builder of Cities, Protector of the Two Worlds, Keeper of the Hours, Chosen of Ptra, High Steward of '
                          'the Horizon, Sailor of the Great Vitae, Sentinel of the Two Realms, The Undisputed, Begetter of the Begat, Scourge of the Faithless, Carrion-feeder, First of the Charnel Valley, Rider of the '
                          'Sacred Chariot, Vanquisher of Vermin, Champion of the Death Arena, Mighty Lion of the Infinite Desert, Emperor of the Shifting Sands, He Who Holds The Sceptre, Great Hawk Of The Heavens, '
                          'Arch-Sultan of Atalan, Waker of the Hierotitan, Monarch of the Sky, Majestic Emperor of the Shifting Sands, Champion of the Desert Gods, Breaker of the Ogre Clans, Builder of the Great '
                          Pyramid, Terror of the Living, Master of the Never-Ending Horizon, Master of the Necropolises, Taker of Souls, Tyrant to the Foolish, Bearer of Ptra's Holy Blade, Scion of Usirian, Scion of 
                          'Nehek, The Great, Chaser of Nightmares, Keeper of the Royal Herat, Founder of the Mortuary Cult, Banisher of the Grand Hierophant, High Lord Admiral of the Deathfleets, Guardian of the '
                          'Charnal Pass, Tamer of the Liche King, Unliving Jackal Lord, Dismisser of the Warrior Queen, Charioteer of the Gods, He Who Does Not Serve, Slayer off Reddittras, Scarab Purger, Favoured of '
                          Usirian, Player of the Great Game, Liberator of Life, Lord Sand, Wrangler of Scorpions, Emperor of the Dunes, Eternal Sovereign of Khemri's Legions, Seneschal of the Great Sandy Desert, 
                          'Curserer of the Living, Regent of the Eastern Mountains, Warden of the Eternal Necropolis, Herald of all Heralds, Caller of the Bitter Wind, God-Tamer, Master of the Mortis River, Guardian of '
                          'the Dead, Great Keeper of the Obelisks, Deacon of the Ash River, Belated of Wakers, General of the Mighty Frame, Summoner of Sandstorms, Master of all Necrotects, Prince of Dust, Tyrant of '
                          Araby, Purger of the Greenskin Breathers, Killer of the False God's Champions, Tyrant of the Gold Dunes, Golden Bone Lord, Avenger of the Dead, Carrion Master, Eternal Warden of Nehek's 
                          Lands, Breaker of Djaf's Bonds... and many, many more... (Tomb Kings)""")
        else:
            logger.info("The player faction is: " + fm.factionDict[args["slot_data"]["starting_faction"]].readableName)

        self.playerRace = fm.factionDict[args["slot_data"]["starting_faction"]].race

        self.settlements = args['slot_data']['settlements']
        self.hordes = args['slot_data']['hordes']
        self.itemKeys = args['slot_data']['items']
        self.capitals = args['slot_data']['faction_capitals']
        self.progressiveTechs = args['slot_data']['progressive_technologies']
        self.progressiveBuildings = args['slot_data']['progressive_buildings']
        self.progressiveUnits = args['slot_data']['progressive_units']
        self.startingTier = args['slot_data']['starting_tier']
        self.randomizePersonalities = args['slot_data']['randomize_personalities']
        self.factionShuffle = args['slot_data']['faction_shuffle']
        self.checksPerLocation = args['slot_data']['checks_per_settlement']
        self.hardLogic = args['slot_data']['hard_logic']
        self.maxExpansionItems = args['slot_data']['max_expansion_items']
        self.fastResearch = args['slot_data']['fast_research']
        self.revealHints = args['slot_data']['reveal_hints']

        self.locationLookup = {}

        if self.gameMode == "conquest":
            self.maxEmpireSize = args['slot_data']['number_of_settlements']
            self.adminCapacity = args['slot_data']['admin_capacity']
            self.expansionItems = 1 # Begins with 1 fake item so that the player can own settlements at the start and prevent early bk

            self.sendMessage(f"archipelago.set_admin_capacity({self.expansionItems})")
            self.sendMessage(f"archipelago.set_admin_capacity_mult({self.adminCapacity})")

        elif self.gameMode == "spheres":
            self.orbGoal = args['slot_data']['orbs']
            self.spheres = args['slot_data']['spheres']
            self.numberOfOrbs = 0
            self.expansionItems = 0
            self.map = "immortal empires"
            self.settlementDict = sm.mapDict[self.map]

            offset = sum([1 for i in range(1, len(self.settlementDict) + 1) for j in range(10)]) + 1
            for key, settlement in self.settlementDict.items():
                for i in range(self.checksPerLocation):
                    self.locationLookup[f"{settlement.readableName} ({i})"] = offset + (key)*10 + i

        logger.warning(f"The following mods are enabled: {[mod for mod in self.modList]}")
        #Pull unit/building/tech Items
        self.itemDict.update(factionItemManager.getAllItems(self.playerRace, self.playerFaction, self.modList))
        #print(self.itemDict)
        self.itemDict.update(fillerDict)
        self.itemDict.update(ancillariesDict)
        self.itemDict.update(trapDict)
        self.itemDict.update(progressionDict)

        self.itemNameToReadableName = {item.name: item.readableName for item in self.itemDict.values()}

        self.progressiveItemFlags = {key: 0 for key, item in self.itemDict.items() if item.progressionGroup is None and key >= 10000}

        self.sanity = args['slot_data']['sanity']
        self.ritualSanity = args['slot_data']['ritual_sanity']
        self.battleSanity = args['slot_data']['battle_sanity']
        self.despoilerSanity = args['slot_data']['despoiler_sanity']
        if self.sanity:
            for key, item in self.itemDict.items():
                if (item.type == itemType.building or item.type == itemType.tech)and item.progressionGroup is not None:
                    self.locationLookup[item.readableName] = key + 1000000
        if self.ritualSanity:
            for key, item in self.itemDict.items():
                if item.type == itemType.ritual and item.progressionGroup is not None:
                    self.locationLookup[item.readableName] = key + 1000000
        if self.battleSanity:
            for i in range(1,21):
                self.locationLookup[f"Won {i*5} Battles"] = i + 20000
        if self.despoilerSanity:
            for i in range(1,21):
                self.locationLookup[f"Sacked {i*2} Settlements"] = i + 20020
                self.locationLookup[f"Razed {i*2} Settlements"] = i + 20040

        self.locationMapping = True
        Utils.async_start(self.send_msgs([{"cmd": "LocationScouts", "locations": self.server_locations, "create_as_hint": 0}]))
        self.receivedItems = []

        self.initialized = False
        self.engine = EngineInitializer.initialize(self, self.itemDict)

    def on_received_items(self, args: dict, resync=False):
        if resync:
            send = self.messenger.runTemp
        else:
            send = self.sendMessage

        for entry in args["items"]:
            try:
                item = self.itemDict[entry.item]
            except KeyError as e:
                logger.error(e)
                logger.error(f"There is a Key Mismatch. This item has a false key, please report the false Key and the faction you were playing to the discord server (@jordansds). Key is: {entry.item}")
                continue
            except Exception as e:
                logger.error(f"Something went horribly wrong. Please report this error the discord server (@jordansds). Key: {entry.item}, Faction: {self.playerFaction}\nError: {e}")
                continue

            match item.type:
                case itemType.building:
                    if not resync:
                        self.itemArchive["items"].append(entry)
                    if self.progressiveBuildings:
                        self.sendProgressiveItem(item.name, send)
                    else:
                        send(f'cm:remove_event_restricted_building_record_for_faction("{item.name}", "{self.playerFaction}")')

                case itemType.unit:
                    if not resync:
                        self.itemArchive["items"].append(entry)
                    if self.progressiveUnits:
                        self.sendProgressiveItem(item.name, send)
                    else:
                        send(f'cm:remove_event_restricted_unit_record_for_faction("{item.name}", "{self.playerFaction}")')

                case itemType.tech:
                    if not resync:
                        self.itemArchive["items"].append(entry)
                    if self.progressiveTechs:
                        self.sendProgressiveItem(item.name, send)
                    else:
                        if self.fastResearch:
                            send(f'cm:instantly_research_technology("{self.playerFaction}", "{item.name}", true)')
                        else:
                            send(f'cm:unlock_technology("{self.playerFaction}", "{item.name}")')

                case itemType.progression:
                    if not resync:
                        self.itemArchive["items"].append(entry)
                    if self.gameMode == "conquest":
                        self.expansionItems += 1
                        if self.expansionItems == self.maxExpansionItems:
                            logger.info(f"You now have all of your Administrative Capacity")
                            logger.info(f"You can now control an unlimited number of settlements without penalties")
                            self.adminCapacity = 1000
                        else:
                            logger.info(f"You now have: {self.expansionItems} Administrative Capacity")
                            logger.info(f"You can now control {self.expansionItems*self.adminCapacity} settlements without penalties")
                        send(f"archipelago.set_admin_capacity({self.expansionItems})")
                        #self.sendMessage(f"archipelago.set_admin_capacity_mult({self.adminCapacity})")

                    elif self.gameMode == "spheres":
                        self.expansionItems += 1
                        self.triggerSphereExpansion(self.expansionItems, send)
                        logger.info("You now have: " + str(self.expansionItems) + " Spheres of Influence")

                case itemType.goal:
                    if not resync:
                        self.itemArchive["items"].append(entry)
                    if self.gameMode == "spheres":
                        self.numberOfOrbs += 1
                        logger.info("You now have: " + str(self.numberOfOrbs) + "/" + str(self.orbGoal) + " Orbs of Domination")
                        if self.numberOfOrbs == self.orbGoal:
                            asyncio.create_task(self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}]))

                case itemType.filler:
                    if item.progressionGroup == "gold":
                        self.sendMessage(f'cm:treasury_mod("{self.playerFaction}", {item.name})')
                    else:
                        self.sendMessage(item.name)
                        
                case itemType.ancillary:
                        self.sendMessage(f'archipelago.give_player_ancillary("{item.name}")')

                case itemType.trap:
                    if self.initialized:
                        if self.are_traps_enabled:
                            #self.sendMessage(item.name)
                            self.messenger.runTemp(item.name)
                        else:
                            logger.info("Skipped a Trap")

                case itemType.effect_faction:
                    self.sendMessage(f'archipelago.give_player_faction_effect({item.name})')

                case itemType.ritual:
                    self.sendMessage(f'cm:unlock_ritual(cm:get_faction("{self.playerFaction}"), "{item.name}", 0)')

            self.messenger.flush()

            if resync:
                self.receivedItems.append("Resync Complete")
            else:
                self.receivedItems.append(item.readableName)

        asyncio.create_task(self.sendNotification())

    def resync(self):
        if self.gameMode == "conquest":
            self.expansionItems = 1
        elif self.gameMode == "spheres":
            self.expansionItems = 0
            self.numberOfOrbs = 1

        self.progressiveItemFlags = {key: 0 for key, item in self.itemDict.items() if item.progressionGroup is None and key >= 10000}
        if self.progressiveTechs:
            self.lockProgressiveTechs()
        if self.progressiveBuildings:
            self.lockProgressiveBuildings()
        if self.progressiveUnits:
            self.lockProgressiveUnits()
        self.on_received_items(self.itemArchive, True)
        #self.itemArchive.clear()

    async def sendNotification(self):
        if self.notificationPending:
            return
        if not self.initialized:
            self.receivedItems = []
            self.initialized = True
            return

        self.notificationPending = True

        await asyncio.sleep(1)
        notificationDesc = "\\n-".join(self.receivedItems)
        self.receivedItems = []
        #print(notificationDesc)
        self.messenger.runTemp(f'archipelago.createNotification("Received Item(s)", "You have received:\\n{notificationDesc}")')

        self.notificationPending = False

    def sendMessage(self, message):
        if self.lineCount == 0:
            self.messenger.firstWrite(message)
        else:
            self.messenger.run(message)
        self.lineCount += 1

    def sendProgressiveItem(self, itemName, send):
        keys = [key for key, item in self.itemDict.items() if item.name == itemName]
        for key in keys:
            self.progressiveItemFlags[key] += 1

        #unlockedItems = [item for item in self.itemDict.values()
        #                 if item.progressionGroup == itemName and item.tier == self.progressiveItemFlags[key]]

        unlockedItems = []
        for item in self.itemDict.values():
            try:
                if item.progressionGroup.lower() == itemName.lower() and item.tier == self.progressiveItemFlags[key]:
                    unlockedItems.append(item)
            except:
                pass


        for item in unlockedItems:
            if item.type == itemType.building:
                send(
                    f'cm:remove_event_restricted_building_record_for_faction("{item.name}", "{self.playerFaction}")')
            elif item.type == itemType.unit:
                send(
                    f'cm:remove_event_restricted_unit_record_for_faction("{item.name}", "{self.playerFaction}")')
            else:
                if self.fastResearch:
                    send(f'cm:instantly_research_technology("{self.playerFaction}", "{item.name}", true)')
                else:
                    send(f'cm:unlock_technology("{self.playerFaction}", "{item.name}")')

    def lockProgressiveTechs(self):
        for key, item in self.itemDict.items():
            if item.type == itemType.tech and item.progressionGroup is None:
                self.sendMessage("cm:lock_one_technology_node(\"%s\", \"%s\")" % (self.playerFaction, item.name))

    def lockProgressiveBuildings(self):
        for key, item in self.itemDict.items():
            if item.type == itemType.building and item.progressionGroup is None:
                if "settlement" in item.name or "horde_main" in item.name:
                    continue
                self.progressiveItemFlags[key] = self.startingTier - 1
                if item.tier > self.startingTier - 1: #ALL BUILDINGS ARE OFFSET BY 1 IN THE DATABASE. WHY!!!!!!!!
                    self.sendMessage("cm:add_event_restricted_building_record_for_faction(\"%s\", \"%s\")" % (item.name, self.playerFaction))

    def lockProgressiveUnits(self):
        for key, item in self.itemDict.items():
            if item.type == itemType.unit and item.progressionGroup is None:
                self.progressiveItemFlags[key] = self.startingTier
                if item.tier > self.startingTier:
                    self.sendMessage("cm:add_event_restricted_unit_record_for_faction(\"%s\", \"%s\")" % (item.name, self.playerFaction))

    def triggerSphereExpansion(self, sphereCount, send):
        oldSphere = []
        newSphere = []
        #allOthers = []
        for faction, sphere in self.spheres.items():
            if sphere < sphereCount:
                oldSphere.append(faction)
            elif sphere == sphereCount:
                newSphere.append(faction)
                self.inRangeFactions.append(faction)
            #else:
                #allOthers.append(faction)
        for oldFaction in oldSphere:
            for newFaction in newSphere:
                send(f'cm:force_diplomacy("faction:{oldFaction}", "faction:{newFaction}", "all", true, true, true)')
                #self.sendMessage("cm:force_diplomacy(\"faction:%s\", \"faction:%s\", \"all\", true, true, true)" % (oldFaction, newFaction))
        #for newFaction in newSphere:
        #    for otherFaction in allOthers:
        #        self.sendMessage(f'cm:force_make_peace("{newFaction}", "{otherFaction}")')
        #        self.sendMessage(f'cm:force_diplomacy("{newFaction}", "{otherFaction}", "all", false, false, true)')
        return

    # Location handlers
    async def check(self, location):
        try:
            location = int(location)
            if self.gameMode == "conquest":
                if location < int(self.maxEmpireSize):
                    if location <= self.adminCapacity * self.expansionItems or not self.hardLogic:
                        for i in range(1, location + 1):
                            for j in range(int(self.checksPerLocation)):
                                await self.check_locations([i*10-9 + j])
                        if location > self.settlementCount:
                            self.settlementCount = location
                    else:
                        logger.info(f"Administrative Capacity Exceeded, {location} Settlements > {self.adminCapacity * self.expansionItems} Capacity")
                elif location == int(self.maxEmpireSize):
                    if self.expansionItems < 1000:
                        self.expansionItems = 1000
                        self.sendMessage(f"archipelago.set_admin_capacity_mult({self.expansionItems})")
                    #await self.check_locations([location * 10 - 9])
                    await self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
        except ValueError:
            if self.gameMode == "spheres":
                location = next((value for value in sm.mapDict[self.map].values() if value.name == location), None).readableName
                for i in range(int(self.checksPerLocation)):
                    await self.check_locations([self.locationLookup[f"{location} ({i})"]])
                    #print(f"{location} ({i})")
        except KeyError:
            logger.error(f"There is a Key Mismatch. Release location manually and please report the false Key to the discord server (@jordansds). Key is: {location}")
        except AttributeError as e:
            logger.error(e)



    async def checkSanity(self, location, sanityType):
        try:
            await self.check_locations([self.locationLookup[self.itemNameToReadableName[location]]])
        except KeyError:
            if sanityType == "ritual":
                logger.error(f"To help in development, please send this key to the warhammer thread in the archipelago discord server (@jordansds). Key is: {location}, type: {sanityType}")
            if not "special" in location and not "bastion_primary" in location:
                if sanityType != "ritual":
                    logger.error(f"To help in development, please send this key to the warhammer thread in the archipelago discord server (@jordansds). Key is: {location}, type: {sanityType}")

    async def checkBattleSanity(self, location):
        location = int(location)
        if location % 5 != 0 or location > 100:
            return
        locations = [i * 5 for i in range(1, int(location / 5 + 1))]
        try:
            for location in locations:
                if self.hardLogic:
                    #Need to check if player has enough expansion items
                    if math.floor(location/100 * self.maxExpansionItems) <= self.expansionItems:
                        await self.check_locations([self.locationLookup[f"Won {location} Battles"]])
                else:
                    for i in range(1, location + 1):
                        await self.check_locations([self.locationLookup[f"Won {location} Battles"]])
        except KeyError:
            pass

    async def checkDespoilerSanity(self, location):
        type = location.split(" ")[0].title()
        location = int(location.split(" ")[1])
        print(location)

        if location % 2 != 0 or location > 40:
            return
        locations = [i * 2 for i in range(1, int(location / 2 + 1))]
        try:
            for location in locations:
                if self.hardLogic:
                    #Need to check if player has enough expansion items
                    if math.floor(location/40 * self.maxExpansionItems) <= self.expansionItems:
                        await self.check_locations([self.locationLookup[f"{type} {location} Settlements"]])
                else:
                    for i in range(2, location + 2):
                        await self.check_locations([self.locationLookup[f"{type} {i} Settlements"]])
        except KeyError:
            pass

    # Deathlink handlers
    def on_deathlink(self, data: dict):
        if self.deathLinkPending or not self.deathLinkEnabled:
            return
        self.deathLinkPending = True
        effectKey = random.choice([key for key in self.deathLinkOptions.keys()])
        logger.info(f"Death Link Received, triggering {effectKey}")
        super().on_deathlink(data)
        #self.sendMessage(self.deathLinkOptions[effectKey])
        self.messenger.runTemp(self.deathLinkOptions[effectKey])
        asyncio.create_task(self.resetDeathLinkFlag())

    async def send_death(self, death_text: str = ""):
        if self.deathLinkPending or not self.deathLinkEnabled:
            return
        self.deathLinkPending = True
        asyncio.create_task(super().send_death(death_text))
        asyncio.create_task(self.resetDeathLinkFlag())

    async def resetDeathLinkFlag(self):
        await asyncio.sleep(2)
        self.deathLinkPending = False

    def make_gui(self):
        ui = super().make_gui()
        ui.base_title = self.game + " Client"#"Total War Warhammer III Client"
        return ui

    # Mission creation functions
    def createTechMissions(self):
        #Faction, Tech, DB Key, Title, Description
        techs = [item[1] for item in factionItemManager.getTechs(self.playerRace, False)]
        for i, item in enumerate(techs):
            key = f"archipelago_research_{i+1}"
            objective = item.readableName[item.readableName.find(":")+2:]
            self.messenger.runTemp(f'archipelago.createMission("{item.name}", "{key}", "Research {objective}", "{self.descriptions[item.readableName]}")')

    def createBuildingMissions(self):
        buildings = [item[1] for item in factionItemManager.getBuildings(self.playerRace, False)]
        for i, item in enumerate(buildings):
            key = f"archipelago_construct_{i + 1}"
            objective = item.readableName[item.readableName.find(":")+2:]
            try:
                self.messenger.runTemp(f'archipelago.createMission("{item.name}", "{key}", "Construct {objective}", "{self.descriptions[item.readableName]}")')
            except KeyError:
                pass

    # Currently Unused
    def createConquestMissions(self):
        locations = [f"Empire Size {i} " for i in range(self.maxEmpireSize)]
        for i, location in enumerate(locations):
            key = f"archipelago_empiresize_{i}"
            items = "By expanding to this size:\n"
            for j in range(self.checksPerLocation):
                items += f"{self.descriptions[f'{location} ({j})']}\n"
            self.messenger.runTemp(f'archipelago.createMission({location}, "{key}", "{location}", "{items}")')

    # Currently Unused
    def createSphereMissions(self):
        for i, settlement in self.settlements.items():
            key = f"archipelago_{settlement.readableName}"
            items = "Within this settlement:\n"
            for j in range(self.checksPerLocation):
                items += f"{self.descriptions[f'{settlement.readableName} ({i})']}\n"
            self.messenger.runTemp(f'archipelago.createSpheresMission({settlement.name}, "{key}", "{settlement.readableName}", "{items}")')

    # Currently Unused
    def createBattleSanity(self):
        locations = [f"Won {i * 5} Battles" for i in range(1, 21)]
        for i, location in enumerate(locations):
            key = f"archipelago_battle_{i + 1}"
            self.messenger.runTemp(f'archipelago.createMission({i}, "{key}", "Win {i} Battles", "{self.descriptions[location]}")')

    # Currently Unused
    def createDespoilerMissions(self):
        locations = [f"Sacked {i} Settlements" for i in range(1, 21)] + [f"Razed {i} Settlements" for i in range(1, 21)]
        for i, location in enumerate(locations):
            key = f"archipelago_sack_{i + 1}"
            self.messenger.runTemp(f'archipelago.createMission("{i}, "{key}", "Sack {i} Settlements", "{self.descriptions[location]}")')
            key = f"archipelago_raze_{i + 1}"
            self.messenger.runTemp(f'archipelago.createMission({i}, "{key}", "Raze {i} Settlements", "{self.descriptions[location]}")')

class EngineInitializer:

    @classmethod
    def initialize(self, context, itemDict):
        self.playerFaction = context.playerFaction
        sendMessage = context.sendMessage

        sendMessage(f'archipelago.set_game_mode("{context.gameMode}")')

        if self.playerFaction == "wh2_main_skv_clan_skryre":
            sendMessage(f'cm:add_event_restricted_building_record_for_faction("wh2_dlc12_special_warpstone_tractor_beam_2", "{self.playerFaction}")')

        ###
        #Randomise AI Personalities
        ###
        if context.randomizePersonalities:
            sendMessage('cm:cai_force_personality_change("All")')

        if context.factionShuffle:#
            ###
            #Randomise Settlements
            ###
            #Ignore the player on the first sweep to prevent early check triggers
            for settlement, faction in context.settlements.items():
                if faction == self.playerFaction:
                    continue
                sendMessage(f'cm:transfer_region_to_faction("{settlement}", "{faction}")')
                sendMessage(f'cm:heal_garrison(cm:get_region("{settlement}"):cqi())')

            isFirstPlayerSettlement = True
            for settlement, faction in context.settlements.items():
                if faction == self.playerFaction:
                    sendMessage(f'cm:transfer_region_to_faction("{settlement}", "{faction}")')
                    sendMessage(f'cm:heal_garrison(cm:get_region("{settlement}"):cqi())')
                if isFirstPlayerSettlement:
                    sendMessage(f'cm:scroll_camera_to_region("{faction}", "{settlement}", 1)')
                    isFirstPlayerSettlement = False

            ###
            #Teleport armies to new settlement
            ###
            for faction, settlement in context.capitals.items():
                sendMessage(f'archipelago.teleport_all_units_of_faction_to_region("{faction}", "{settlement}")')
            for faction, settlement in context.hordes.items():
                sendMessage(f'archipelago.teleport_all_units_of_faction_to_region("{faction}", "{settlement}")')

            sendMessage("cm:reset_shroud()")

        ###
        #Disables techs/buildings/units/rituals if randomised
        ###
        for key in context.itemKeys:
            item = itemDict[key]
            if (item.type == itemType.tech) and (not context.progressiveTechs) and (item.progressionGroup is not None):
                sendMessage(f'cm:lock_one_technology_node("{self.playerFaction}", "{item.name}")')
            elif (item.type == itemType.building) and (not context.progressiveBuildings) and (item.progressionGroup is not None):
                sendMessage(f'cm:add_event_restricted_building_record_for_faction("{item.name}", "{self.playerFaction}")')
            elif (item.type == itemType.unit) and (not context.progressiveUnits) and (item.progressionGroup is not None):
                sendMessage(f'cm:add_event_restricted_unit_record_for_faction("{item.name}", "{self.playerFaction}")')
            elif item.type == itemType.ritual:
                sendMessage(f'cm:lock_ritual(cm:get_faction("{self.playerFaction}"), "{item.name}")')
            #messenger.flush()

        if context.progressiveTechs:
            context.lockProgressiveTechs()
        if context.progressiveBuildings:
            context.lockProgressiveBuildings()
        if context.progressiveUnits:
            context.lockProgressiveUnits()

        if context.gameMode == "conquest":
            ###
            #Set Administrative Capacity
            ###
            sendMessage(f"archipelago.set_admin_capacity_mult({context.adminCapacity})")
            sendMessage(f"archipelago.set_admin_capacity({context.expansionItems})")

        elif context.gameMode == "spheres":
            sphereZeroFactions = []
            sphereAllOthers = []
            for faction, sphere in context.spheres.items():
                if sphere == 0:
                    sphereZeroFactions.append(faction)
                else:
                    sphereAllOthers.append(faction)
                continue
            for factionZero in sphereZeroFactions:
                for faction in sphereAllOthers:
                    sendMessage(f'cm:force_make_peace("{factionZero}", "{faction}")')
                    sendMessage(f'cm:force_diplomacy("faction:{factionZero}", "faction:{faction}", "all", false, false, true)')

        sendMessage("archipelago.initialise()")

        context.messenger.flush()

def launchClient(*args: Sequence[str]):
    Utils.init_logging('TWW3Client')
    logging.getLogger().setLevel(logging.INFO)

    async def main(args):
        ctx = TWW3Context(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name='ServerLoop')

        if tracker_loaded:
            ctx.run_generator()
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        await ctx.exit_event.wait()
        await ctx.shutdown()

    parser = get_base_parser()
    parser.add_argument("--name", default=None, help="Slot Name to connect as.")
    parser.add_argument("url", nargs="?", help="Archipelago connection url")

    launch_args = handle_url_arg(parser.parse_args(args))

    colorama.just_fix_windows_console()

    asyncio.run(main(launch_args))
    colorama.deinit()


