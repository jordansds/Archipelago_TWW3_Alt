from typing import Any, Mapping, ClassVar, Optional

from Options import Option
from worlds.AutoWorld import World
from BaseClasses import Region, ItemClassification as IC
import math
import settings
from worlds.tww3.options import TWW3Options
from worlds.tww3 import items, locations, rules, sanityRules
from worlds.tww3.item_tables import factions as fm, settlements as sm
from worlds.tww3 import settlementRandomiser as sr
from worlds.tww3 import factionItemManager
from worlds.tww3.dataStructs import itemType
import logging
#from rule_builder.cached_world import CachedRuleBuilderWorld

class TWW3Settings(settings.Group):
    class TWW3Path(settings.UserFolderPath):
        """Installation Path to the TWW3 folder, so that input and output files can be written."""
        description = "Total War Warhammer 3 Installation Folder. Where the .exe is."

    tww3_path: TWW3Path = TWW3Path("C:/Program Files (x86)/Steam/steamapps/common/Total War WARHAMMER III")

class TWW3World(World):
    """Insert description of the world/game here."""
    game = "Total War Warhammer III"  # name of the game/world
    options_dataclass = TWW3Options  # options the player can set
    options: TWW3Options  # typing hints for option results
    settings: ClassVar[TWW3Settings]  # will be automatically assigned from type hint
    origin_region_name = "Keys"
    topology_present = True # show path to required location checks in spoiler
    logger = logging.getLogger("Total War Warhammer III")
    ut_can_gen_without_yaml = True
    glitches_item_name: str = "Glitch Logic"

    item_name_to_id = {item.readableName: key for key, item in items.itemDict.items()}
    location_name_to_id = {}

    # Need to create the 9 key locations
    keys = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th"]
    location_name_to_id.update({
        f"The {key} Key": index + 1 for index, key in enumerate(keys)
    })
    location_name_to_id.update({
        f"The {key} Key: Item {j+1}": (index + 1) * 10 + j for index, key in enumerate(keys) for j in range(5)
    })
    # Conquerer Locations starting at index 1001
    location_name_to_id.update({
        f"Empire Size {index+1}": index + 1001 for index in range(sm.getMaximumSettlementCount())
    })
    # SettlementLocations starting at index 2001
    location_name_to_id.update({
        f"{settlement.readableName}":(index + 2001)
        # offset conquest locations
        for index, settlement in sm.getAllSettlements().items()
    })

    sanityLocationNames = {}
    for key, item in factionItemManager.getAllItems().items():
        if (item.type == itemType.building or item.type == itemType.tech or item.type == itemType.ritual) and (item.progressionGroup is not None and item.progressionGroup != ""):
            sanityLocationNames.update({key + 1000000: item.readableName})
    for i in range(1,100):
        sanityLocationNames.update({i+3000: f"Won {i*5} Battles", i+3100: f"Sacked {i*2} Settlements", i+3200: f"Razed {i*2} Settlements"})
    location_name_to_id.update({item: key for key, item in sanityLocationNames.items()})

    settlementRandomiser: sr.settlementRandomiser = None

    def generate_early(self) -> None:

        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        # YAML-less tracker generation
        if re_gen_passthrough and self.game in re_gen_passthrough:
            slotData: dict[str, Any] = re_gen_passthrough[self.game]
            slotOptions: dict[str, Any] = slotData.get("options", {})[0]
            for key, value in slotOptions.items():
                opt: Optional[Option] = getattr(self.options, key, None)
                if opt is not None:
                    setattr(self.options, key, opt.from_any(value))


        fm.addModdedFactions(self.options.mod_list)

        #Handle random faction from race selection.
        if self.options.starting_faction.value % 10 == 0 and self.options.starting_faction.value > 90000:
            randomRace = fm.factionDict[self.options.starting_faction.value]
            self.options.starting_faction.value = self.random.choice(randomRace.readableName) #Yes, I reused readableName for a list of ints. Fight me.

        self.playerFaction = fm.factionDict[self.options.starting_faction.value]
        self.map = "immortal empires" #Potential for additional map support in future?
        self.settlementRandomiser: sr.settlementRandomiser = sr.settlementRandomiser(self.random, self.playerFaction,
                                                                                     self.options.starting_faction.value,
                                                                                     self.options.starting_settlements, self.map)

        if self.options.faction_shuffle:
            self.settlements = self.settlementRandomiser.randomiseSettlements()
        else:
            self.settlements = self.settlementRandomiser.getSettlements()
        self.playerSettlements = [settlement for settlement in self.settlements.values()
                                  if settlement.faction == self.playerFaction.name]
        self.keyLocations = []

        #if self.options.ritual_sanity:
        #    self.options.sanity.value = True
        #    self.options.ritual_shuffle.value = True
        self.options.ritual_shuffle = False #Disabled for now
        self.options.ritual_sanity = False #Disabled for now
        if self.options.sanity:
            #self.options.unit_shuffle.value = True
            #self.options.building_shuffle.value = True
            #self.options.tech_shuffle.value = True

            self.options.progressive_buildings.value = True
            self.options.starting_tier.value = 1
            self.sanityRules = sanityRules.ruleManager(self)

        #if not self.options.hard_logic:
        #    self.logger.warning(f"Total War Warhammer player {self.player_name} has soft logic enabled, if this is a large sync or async, then this may cause issues.")

    def create_regions(self) -> None:
        worldRegion = Region("Keys", self.player, self.multiworld)
        self.multiworld.regions.append(worldRegion)

        if self.options.sanity:
            region = Region("Buildings", self.player, self.multiworld)
            self.multiworld.regions.append(region)
            worldRegion.connect(region, "Buildings")
            region = Region("Techs", self.player, self.multiworld)
            self.multiworld.regions.append(region)
            worldRegion.connect(region, "Techs")

        if self.options.conquerer_sanity:
            region = Region("Empire", self.player, self.multiworld)
            self.multiworld.regions.append(region)
            worldRegion.connect(region, "Empire")

        #if self.options.ritual_sanity:
        #    region = Region("Rituals", self.player, self.multiworld)
        #    self.multiworld.regions.append(region)
        #    worldRegion.connect(region, "Rituals")

        if self.options.battle_sanity:
            region = Region("Battles", self.player, self.multiworld)
            self.multiworld.regions.append(region)
            worldRegion.connect(region, "Battles")

        if self.options.despoiler_sanity:
            region = Region("Despoiler", self.player, self.multiworld)
            self.multiworld.regions.append(region)
            worldRegion.connect(region, "Despoiler")

        locations.createAllLocations(self)

    def create_items(self) -> None:
        self.itemKeys = []
        items.updateItemDict(self)
        items.createAllItems(self)
        #if self.options.balance > 0:
        rules.setBalance(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        slotData = self.options.as_dict("starting_faction",
                                                    "starting_settlements",
                                                    "sanity",
                                                    "conquerer_sanity",
                                                    "explorer_sanity",
                                                    "battle_sanity",
                                                    "despoiler_sanity",
                                                    "progressive_technologies",
                                                    "progressive_buildings",
                                                    "progressive_units",
                                                    "starting_tier",
                                                    "hard_logic",
                                                    "mod_list",
                                                    "death_link",
                                                    "death_link_effects",
                                                    "randomize_personalities",
                                                    "faction_shuffle",
                                                    "fast_research",
                                                    "reveal_hints",)

        slotData["settlements"] = {settlement.name: settlement.faction for settlement in self.settlements.values()}
        slotData["hordes"] = self.settlementRandomiser.randomiseHordes()
        slotData["faction_capitals"] = self.settlementRandomiser.capitals
        slotData["items"] = self.itemKeys #Filled in items.py createAllItems
        slotData["seed"] = self.multiworld.seed
        slotData["key_locations"] = self.keyLocations

        slotData["version"] = self.world_version.as_simple_string()

        return slotData


    def create_item(self, name: str) -> items.TWW3Item:
        if name == "Glitch Logic":
            return items.TWW3Item("Glitch Logic", IC.progression, None, self.player)

        key: int = self.item_name_to_id[name]
        return items.TWW3Item(name, items.itemDict[key].classification, key, player=self.player)

    def get_filler_item_name(self) -> str:
        fillerFunctions = [items.generateFiller, items.generateTrap]  # List of functions for generating filler
        weights = [self.options.filler.value, 100 - self.options.filler.value]  # list of weights defined in YAML

        fillerFunction = self.random.choices(fillerFunctions, weights=weights, k=1)[0]
        item = fillerFunction(self)
        return item.name