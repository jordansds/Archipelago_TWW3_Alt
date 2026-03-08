from CommonClient import CommonContext, ClientCommandProcessor, server_loop, get_base_parser, gui_enabled, logger, handle_url_arg
import Utils
import asyncio
import colorama
import logging
from collections.abc import Sequence
import random

from BaseClasses import ItemClassification as IC
from worlds.tww3.item_types import ItemType
from .item_tables.filler_item_table import fillerWeakDict, fillerStrongDict, trapHarmlessDict, trapWeakDict, trapStrongDict
from .item_tables.ancillaries_table import ancillariesRegularDict, ancillariesLegendaryDict
from .item_tables.ritual_table import ritualDict
from .item_tables.progression_table import progressionDict
from . import TWW3World, factionTables
from . import settlementManager as sm
from . import deathLink
import os
from NetUtils import ClientStatus

path = "."

class TWW3CommandProcessor(ClientCommandProcessor):    

    def _cmd_traps(self):
        """Turn Traps off and on."""
        if isinstance(self.ctx, TWW3Context):
            self.ctx.are_traps_enabled = not self.ctx.are_traps_enabled
            logger.info(f"Traps are now turned {'on' if self.ctx.are_traps_enabled else 'off'}.")

    def _cmd_capitals(self):
        """Prints a list of starting Capitals."""
        if isinstance(self.ctx, TWW3Context):
            for faction, capital in self.ctx.capitals.items():
                logger.info("Faction: " + faction + " Capital: " + capital)

    def _cmd_ac(self):
        """Prints the current number of settlements you can control"""
        if isinstance(self.ctx, TWW3Context):
            self.ctx.messenger.run(f"set_admin_capacity({self.ctx.expansionItems})")
            self.ctx.messenger.run(f"set_settlements_per_admin_capacity({self.ctx.adminCapacity})")
            logger.info(f"You now have: {self.ctx.expansionItems} Administrative Capacity")
            logger.info(f"You can now control {self.ctx.expansionItems * self.ctx.adminCapacity} settlements without penalties")

    def _cmd_orbs(self):
        """Prints the current number of orbs of dominance that you own"""
        if isinstance(self.ctx, TWW3Context):
            logger.info(f"You currently hold: {self.ctx.numberOfOrbs} Orbs of dominance")

    def _cmd_logging(self):
        """Toggles location logging"""
        if isinstance(self.ctx, TWW3Context):
            self.ctx.logChecks = not self.ctx.logChecks
            logger.info(f"Location logging is now set to {self.ctx.logChecks}")

    def _cmd_teleport(self):
        """Teleports lords and heroes to starting location (use if your lord did not teleport)"""
        if isinstance(self.ctx, TWW3Context):
            for faction, settlement in self.ctx.capitals.items():
                if faction == self.ctx.playerFaction:
                    self.ctx.messenger.run(f'teleport_all_heroes_of_faction_to_region("{faction}", "{settlement}")')
                    self.ctx.messenger.run(f'teleport_all_lords_of_faction_to_region("{faction}", "{settlement}")')
                    break
            for faction, settlement in self.ctx.hordes.items():
                if faction == self.ctx.playerFaction:
                    self.ctx.messenger.run(f'teleport_all_heroes_of_faction_to_region("{faction}", "{settlement}")')
                    self.ctx.messenger.run(f'teleport_all_lords_of_faction_to_region("{faction}", "{settlement}")')
                    break
class Messenger:
    def __init__(self, path):
        self.file = open(path, 'w+')

    def run(self, message):
        self.file.write(message + '\n')
        self.file.flush()

    def flush(self):
        self.file.flush()

class Watcher:
    def __init__(self, path, context):
        self.file = open(path, "w+")
        self.context = context

    async def watch(self, gameMode):
        print('Watching for Waaagh...')
        self.file.seek(0, 2)
        activeInode = os.fstat(self.file.fileno()).st_ino
        path = self.file.name
        while True:
            line = self.file.readline()
            if line:
                line = line.strip()
                if line.split(" ")[0]  == "deathlink":
                    await self.context.send_death(line.split(" ")[1])
                else:
                    self.logChecks = self.context.logChecks
                    if self.logChecks:
                        if gameMode == "conquest":
                            logger.info("Sending Empire Size " + line)
                        elif gameMode == "spheres":
                            logger.info("Sending Location " + line)
                    await self.context.check(line)
                    continue
            await asyncio.sleep(0.1)

            try:
                st = os.stat(path)
            except FileNotFoundError:
                # File temporarily missing during rotation
                continue
            try:
                rotated = st.st_ino != activeInode
                truncated = self.file.tell() > st.st_size

                if rotated or truncated:
                    # Reopen the file
                    self.file.close()
                    self.file = open(path, "r", encoding="utf-8", errors="replace")
                    activeInode = os.fstat(self.file.fileno()).st_ino
                    self.file.seek(0, os.SEEK_END)
            except Exception as e:
                print(e)


class TWW3Context(CommonContext):
    game = 'Total War Warhammer III'
    command_processor = TWW3CommandProcessor
    items_handling = 0b111
    are_traps_enabled = True

    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.initialized = False
        self.adminCapacity = 0
        self.expansionItems = 0
        self.numberOfOrbs = 0
        self.numberOfDiploRanges = 0
        self.itemDict = {}
        self.deathLinkPending = False
        self.logChecks = False

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(TWW3Context, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def on_package(self, cmd: str, args: dict):
        if cmd == 'Connected':
            self.on_connected(args)
        elif cmd == "ReceivedItems":
            self.on_received_items(args)
        elif cmd == "Bounced":
            if "tags" in args:
                if "DeathLink" in args["tags"]:
                    self.on_deathlink(args["data"])


    def on_connected(self, args: dict):
        version = TWW3World.world_version.as_simple_string()
        try:
            if version != args['slot_data']['version']:
                logger.error(f"WARNING: Server ({args['slot_data']['version']}) and client ({version}) are using different versions of the TWW3 APWorld!")
            else:
                logger.info(f"The client is running: {version} of the TWW3 APWorld")
        except:
            logger.error(f"WARNING: Client ({version}) does not match the server. Server must be using the old TWW3 APWorld!")

        self.path = TWW3World.settings.tww3_path
        self.path.replace("\\", "/")


        if not self.path or not os.path.exists(self.path):
            logger.error('ERROR: Could not find Warhammer folder. Please correct the path in your host.yaml.')
            Utils.async_start(self.disconnect())
        if not os.path.isfile(os.path.join(self.path, "Warhammer3.exe")):
            logger.error('ERROR: Could not find Warhammer3.exe. Please correct the path in your host.yaml.')
            Utils.async_start(self.disconnect())

        self.gameMode = args['slot_data']['game_mode']
        logger.info(f"The game mode is: {self.gameMode}")

        self.watcher = Watcher(os.path.join(self.path, "engine.out"), self)
        watcher_task = asyncio.create_task(self.watcher.watch(self.gameMode), name='watcher')
        self.messenger = Messenger(os.path.join(self.path, "engine.in"))

        self.deathLinkEnabled = args['slot_data']["death_link"]
        if self.deathLinkEnabled:
            asyncio.create_task(self.update_death_link(True))
            logger.info("DeathLink is enabled, good luck...")

        self.deathLinkEffects = args['slot_data']["death_link_effects"]

        self.deathLinkOptions = deathLink.createDeathLinkFunctions(self.deathLinkEffects)

        self.modList = args['slot_data']['mod_list']
        sm.addModdedFactions(self.modList)
        self.playerFaction = sm.factionDict[args["slot_data"]["starting_faction"]].name

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
            logger.info("The player faction is: " + sm.factionDict[args["slot_data"]["starting_faction"]].readableName)

        self.playerRace = sm.factionDict[args["slot_data"]["starting_faction"]].race
        print(self.playerRace)

        self.settlements = args['slot_data']['settlements']
        self.hordes = args['slot_data']['hordes']
        self.itemKeys = args['slot_data']['items']
        self.capitals = args['slot_data']['faction_capitals']
        self.progressiveTechs = args['slot_data']['progressive_technologies']
        self.progressiveBuildings = args['slot_data']['progressive_buildings']
        self.progressiveUnits = args['slot_data']['progressive_units']
        self.startingTier = args['slot_data']['starting_tier']
        #self.shuffleRituals = args['slot_data']['ritual_shuffle']
        self.randomizePersonalities = args['slot_data']['randomize_personalities']
        self.factionShuffle = args['slot_data']['faction_shuffle']

        if self.gameMode == "conquest":
            self.checksPerLocation = args['slot_data']['checks_per_settlement']
            self.numberOfLocations = args['slot_data']['number_of_settlements']
            self.adminCapacity = args['slot_data']['admin_capacity']

            self.expansionItems = 2  # Begins with 2 fake items so that the player can own settlements at the start and prevent early bk
        elif self.gameMode == "spheres":
            self.orbGoal = args['slot_data']['orbs']
            self.spheres = args['slot_data']['spheres']

            self.locationLookup = dict()
            offset = sum([1 for i in range(1, len(sm.settlementDict) + 1) for j in range(10)]) + 1
            for key, settlement in sm.settlementDict.items():
                self.locationLookup[settlement.readableName] = key + offset

        logger.info(f"The following mods are enabled: {[mod for mod in self.modList]}")
        #Pull unit/building/tech Items
        self.itemDict.update(factionTables.getAllItems(self.playerRace, self.modList))
        #print(self.itemDict)
        self.itemDict.update(fillerWeakDict)
        self.itemDict.update(fillerStrongDict)
        self.itemDict.update(ancillariesRegularDict)
        self.itemDict.update(ancillariesLegendaryDict)
        self.itemDict.update(trapHarmlessDict)
        self.itemDict.update(trapWeakDict)
        self.itemDict.update(trapStrongDict)
        self.itemDict.update(ritualDict)
        self.itemDict.update(progressionDict)

        self.progressiveItemFlags = {key: 0 for key in self.itemDict.keys()}

        EngineInitializer.initialize(self, self.itemDict, self.progressiveItemFlags)

    def on_received_items(self, args: dict):
        # for entry in self.items_received:
        for entry in args["items"]:
            try:
                item = self.itemDict[entry.item]
            except KeyError as e:
                logger.error(e)
                logger.error(f"There is a Key Mismatch. This item has a false key, please report the false Key and the faction you were playing to the discord server (@jordansds). Key is: {entry.item}")
                continue
            except Exception as e:
                logger.error(f"Something went horribly wrong. Please report this error the discord server (@jordansds). Key is: {entry.item}, faction is {self.playerFaction}")
                continue

            #sender = "You" if entry.player == self.slot else f"Player {entry.player}"
            #logger.info(f"From: {sender} | Item: {item.name}")

            if item.type == ItemType.building:
                if self.progressiveBuildings:
                    self.sendProgressiveItem(item.name)
                else:
                    self.messenger.run(f'cm:remove_event_restricted_building_record_for_faction("{item.name}", "{self.playerFaction}")')
            elif item.type == ItemType.unit:
                if self.progressiveUnits:
                    self.sendProgressiveItem(item.name)
                else:
                    self.messenger.run(f'cm:remove_event_restricted_unit_record_for_faction("{item.name}", "{self.playerFaction}")')
            elif item.type == ItemType.tech:
                if self.progressiveTechs:
                    self.sendProgressiveItem(item.name)
                else:
                    self.messenger.run(f'cm:unlock_technology("{self.playerFaction}", "{item.name}")')

            elif item.type == ItemType.progression:
                if self.gameMode == "conquest":
                    self.expansionItems += 1
                    self.messenger.run(f"set_admin_capacity({self.expansionItems})")
                    self.messenger.run(f"set_settlements_per_admin_capacity({self.adminCapacity})")
                    logger.info(f"You now have: {self.expansionItems} Administrative Capacity")
                    logger.info(f"You can now control {self.expansionItems*self.adminCapacity} settlements without penalties")
                elif self.gameMode == "spheres":
                    self.numberOfDiploRanges += 1
                    self.triggerSphereExpansion(self.numberOfDiploRanges)
                    logger.info("You now have: " + str(self.numberOfDiploRanges) + " Spheres of Influence")
            elif item.type == ItemType.goal:
                if self.gameMode == "spheres":
                    self.numberOfOrbs += 1
                    logger.info("You now have: " + str(self.numberOfOrbs) + "/" + str(self.orbGoal) + " Orbs of Domination")

            elif item.classification == IC.filler:
                if item.readableName == "Get-Rich-Quick Scroll":
                    self.messenger.run(f'cm:treasury_mod("{self.playerFaction}", cm:random_number(10000,1))')

                elif item.type == ItemType.ancillaries_regular or item.type == ItemType.ancillaries_legendary:
                    self.messenger.run(f'give_player_ancillary("{item.name}")')
                else:
                    self.messenger.run(item.name)

            elif item.classification == IC.trap:
                if self.are_traps_enabled:
                    self.messenger.run(item.name)
                else:
                    self.messenger.run('out("Skipped a Trap")')

            elif item.type == ItemType.effect_faction:
                self.messenger.run(f'give_player_faction_effect({item.name})')

            elif item.type == ItemType.ritual:
                self.messenger.run(f'cm:unlock_ritual(cm:get_faction("{self.playerFaction}"), "{item.name}", 0)')

            self.messenger.flush()

        if self.gameMode == "spheres":
            if self.numberOfOrbs == self.orbGoal:
                asyncio.create_task(self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}]))

        self.messenger.flush()

    def sendProgressiveItem(self, progressionGroup):
        for key, item in self.itemDict.items():
            if item.progressionGroup == progressionGroup:
                self.progressiveItemFlags[key] += 1
                if item.tier == self.progressiveItemFlags[key]:
                    if item.type == ItemType.building:
                        self.messenger.run(f'cm:remove_event_restricted_building_record_for_faction("{item.name}", "{self.playerFaction}")')
                    elif item.type == ItemType.unit:
                        self.messenger.run(f'cm:remove_event_restricted_unit_record_for_faction("{item.name}", "{self.playerFaction}")')
                    else:
                        self.messenger.run(f'cm:unlock_technology("{self.playerFaction}", "{item.name}")')

    def triggerSphereExpansion(self, numberOfSphereItems):
        oldSphere = []
        newSphere = []
        allOthers = []
        for faction, sphere in self.spheres.items():
            if sphere < numberOfSphereItems:
                oldSphere.append(faction)
            elif sphere == numberOfSphereItems:
                newSphere.append(faction)
            else:
                allOthers.append(faction)
        for oldFaction in oldSphere:
            for newFaction in newSphere:
                self.messenger.run("cm:force_diplomacy(\"faction:%s\", \"faction:%s\", \"all\", true, true, true)" % (oldFaction, newFaction))
        for newFaction in newSphere:
            for otherFaction in allOthers:
                self.messenger.run("cm:force_make_peace(\"%s\", \"%s\")" % (newFaction, otherFaction))
                self.messenger.run("cm:force_diplomacy(\"faction:%s\", \"faction:%s\", \"all\", false, false, true)" % (newFaction, otherFaction))
        return

    async def check(self, location):
        try:
            if self.gameMode == "conquest":

                if str(location) != str(self.numberOfLocations):
                    for i in range(int(self.checksPerLocation)):
                        await self.check_locations([int(location)*10-9 + i])
                else:
                    await self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])

            elif self.gameMode == "spheres":
                key = next((key for key, value in sm.settlementDict.items() if value.name == location), None)
                for i in range(int(self.checksPerLocation)):
                    await self.check_locations([self.locationLookup[f"{sm.settlementDict[key].readableName} ({i})"]])
                
        except KeyError as e:
            logger.error(e)
            logger.error(f"There is a Key Mismatch. Release location manually and please report the false Key to the discord server (@jordansds). Key is: {location}")


    #Deathlink handlers
    def on_deathlink(self, data: dict):
        if self.deathLinkPending:
            return
        self.deathLinkPending = True
        effectKey = random.choice([key for key in self.deathLinkOptions.keys()])
        logger.info(f"Death Link Received, triggering {effectKey}")
        super().on_deathlink(data)
        self.messenger.run(self.deathLinkOptions[effectKey])
        asyncio.create_task(self.resetDeathLinkFlag())

    async def send_death(self, death_text: str = ""):
        if self.deathLinkPending:
            return
        if self.deathLinkEnabled:
            self.deathLinkPending = True
            asyncio.create_task(super().send_death(death_text))
            asyncio.create_task(self.resetDeathLinkFlag())

    async def resetDeathLinkFlag(self):
        await asyncio.sleep(1)
        self.deathLinkPending = False

    def run_gui(self):
        from kvui import GameManager

        class TWW3Manager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = self.game + " Client"

        self.ui = TWW3Manager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

class EngineInitializer:

    @classmethod
    def initialize(self, context, itemDictionary, progressiveItemFlags):
        settlements = context.settlements
        hordes = context.hordes
        self.playerFaction = context.playerFaction
        self.playerRace = context.playerRace
        self.itemDict = itemDictionary
        capitals = context.capitals
        startingTier = context.startingTier
        messenger = context.messenger

        ###
        #Randomise AI Personalities
        ###
        if context.randomizePersonalities:
            messenger.run("cm:cai_force_personality_change(\"All\")")

        if context.factionShuffle:#
            ###
            #Randomise Settlements
            ###
            #Ignore the player on the first sweep to prevent early check triggers
            for settlement, faction in settlements.items():
                if faction == self.playerFaction:
                    continue
                messenger.run("cm:transfer_region_to_faction(\"%s\", \"%s\")" % (settlement, faction))
                messenger.run("cm:heal_garrison(cm:get_region(\"%s\"):cqi())" % settlement)

            isFirstPlayerSettlement = True
            for settlement, faction in settlements.items():
                messenger.run("cm:transfer_region_to_faction(\"%s\", \"%s\")" % (settlement, faction))
                messenger.run("cm:heal_garrison(cm:get_region(\"%s\"):cqi())" % settlement)
                if faction == self.playerFaction and isFirstPlayerSettlement:
                    messenger.run("cm:scroll_camera_to_region(\"%s\", \"%s\", 1)" % (faction, settlement))
                    isFirstPlayerSettlement = False

            ###
            #Teleport armies to new settlement
            ###
            for faction, settlement in capitals.items():
                messenger.run("teleport_all_heroes_of_faction_to_region(\"%s\", \"%s\")" % (faction, settlement))
                messenger.run("teleport_all_lords_of_faction_to_region(\"%s\", \"%s\")" % (faction, settlement))
            for faction, settlement in hordes.items():
                messenger.run("teleport_all_heroes_of_faction_to_region(\"%s\", \"%s\")" % (faction, settlement))
                messenger.run("teleport_all_lords_of_faction_to_region(\"%s\", \"%s\")" % (faction, settlement))

            messenger.run("cm:reset_shroud()")
                
        ###
        #Locks rituals if randomised
        ###            
        #if context.shuffleRituals:
        #    for key, ritual in ritualDict.items():
        #        if ritual.faction == self.playerFaction:
        #            messenger.run("cm:lock_ritual(cm:get_faction(\"%s\"), \"%s\")" % (self.playerFaction, ritual.name))
                    
        ###
        #Disables techs/buildings/units if randomised
        ###
        for key in context.itemKeys:
            itemData = self.itemDict[key]
            if (itemData.type == ItemType.tech) and (not context.progressiveTechs) and (itemData.progressionGroup is not None):
                messenger.run("cm:lock_one_technology_node(\"%s\", \"%s\")" % (self.playerFaction, itemData.name))
            elif (itemData.type == ItemType.building) and (not context.progressiveBuildings) and (itemData.progressionGroup is not None):
                messenger.run("cm:add_event_restricted_building_record_for_faction(\"%s\", \"%s\")" % (itemData.name, self.playerFaction))
            elif (itemData.type == ItemType.unit) and (not context.progressiveUnits) and (itemData.progressionGroup is not None):
                messenger.run("cm:add_event_restricted_unit_record_for_faction(\"%s\", \"%s\")" % (itemData.name, self.playerFaction))

        if context.progressiveTechs:
            self.lock_progressiveTechs(self, messenger, self.itemDict, progressiveItemFlags)
        if context.progressiveBuildings:
            self.lock_progressiveBuildings(self, startingTier, messenger, self.itemDict, progressiveItemFlags)
        if context.progressiveUnits:
            self.lock_progressiveUnits(self, startingTier, messenger, self.itemDict, progressiveItemFlags)

        if context.gameMode == "conquest":
            ###
            #Set Administrative Capacity
            ###
            messenger.run(f"set_settlements_per_admin_capacity({context.adminCapacity})")
            messenger.run(f"set_admin_capacity({context.expansionItems})")

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
                    messenger.run("cm:force_make_peace(\"%s\", \"%s\")" % (factionZero, faction))
                    messenger.run(
                        "cm:force_diplomacy(\"faction:%s\", \"faction:%s\", \"all\", false, false, true)" % (
                            factionZero, faction))
        messenger.flush()

    def lock_progressiveTechs(self, messenger, item_table, progressive_items_flags):
        for key, item in item_table.items():
            if item.type == ItemType.tech and item.progressionGroup is not None:# and item.race == self.playerRace:
                messenger.run("cm:lock_one_technology_node(\"%s\", \"%s\")" % (self.playerFaction, item.name))

    def lock_progressiveBuildings(self, startingTier, messenger, item_table, progressive_items_flags):
        for key, item in item_table.items():
            if item.type == ItemType.building and item.progressionGroup is not None:# and item.race == self.playerRace:
                print(item.readableName)
                progressive_items_flags[key] = startingTier - 1
                if item.tier > startingTier - 1: #ALL BUILDINGS ARE OFFSET BY 1 IN THE DATABASE. WHY!!!!!!!!
                    messenger.run("cm:add_event_restricted_building_record_for_faction(\"%s\", \"%s\")" % (item.name, self.playerFaction))
                #else:
                #    progressive_items_flags[key] = 0

    def lock_progressiveUnits(self, startingTier, messenger, item_table, progressive_items_flags):
        for key, item in item_table.items():
            if item.type == ItemType.unit and item.progressionGroup is not None:# and item.race == self.playerRace:
                progressive_items_flags[key] = startingTier
                if item.tier > startingTier:
                    messenger.run("cm:add_event_restricted_unit_record_for_faction(\"%s\", \"%s\")" % (item.name, self.playerFaction))

def launchClient(*args: Sequence[str]):
    Utils.init_logging('TWW3Client')
    logging.getLogger().setLevel(logging.INFO)

    async def main(args):
        ctx = TWW3Context(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name='ServerLoop')

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