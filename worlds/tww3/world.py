from typing import Any, Mapping, ClassVar, Optional

from Options import Option
from worlds.AutoWorld import World
from BaseClasses import Region, ItemClassification as IC
import math
import settings
from worlds.tww3.options import TWW3Options
from worlds.tww3 import items, locations, rules, sanityRules
from worlds.tww3 import settlementManager as sm
from worlds.tww3 import factionItemManager
from worlds.tww3.dataStructs import itemType
import logging
#from rule_builder.cached_world import CachedRuleBuilderWorld

class TWW3Settings(settings.Group):
    class TWW3Path(settings.FolderPath):
        """Installation Path to the TWW3 folder, so that input and output files can be written."""
        description = "Total War Warhammer 3 Installation Folder. Where the .exe is."

    tww3_path: TWW3Path = TWW3Path("C:/Program Files (x86)/Steam/steamapps/common/Total War WARHAMMER III")

class TWW3World(World):
    """Insert description of the world/game here."""
    game = "Total War Warhammer III"  # name of the game/world
    options_dataclass = TWW3Options  # options the player can set
    options: TWW3Options  # typing hints for option results
    settings: ClassVar[TWW3Settings]  # will be automatically assigned from type hint
    origin_region_name = "Settlements"
    topology_present = True # show path to required location checks in spoiler
    logger = logging.getLogger("Total War Warhammer III")
    ut_can_gen_without_yaml = True
    glitches_item_name: str = "Glitch Logic"

    #Holds the keys that will be sent to the client for locking techs/buildings/units
    #Will be populated in items.createAllItems
    #itemKeys = []

    item_name_to_id = {item.readableName: key for key, item in items.itemDict.items()}
    #item_name_to_id = {}

    #locationNames = [f"Empire Size {i} ({j})" for i in range(1,len(sm.settlementDict) + 1) for j in range(10)] #conquest gamemode locations
    #locationNames += [f"{settlement.readableName} ({i})" for settlement in sm.settlementDict.values() for i in range(10)]  # spheres gamemode locations
    #location_name_to_id = {location: index for index, location in enumerate(locationNames, start=1)}

    locations = [f"Empire Size {i} ({j})"
                 for i in range(1,len(sm.settlementDict) + 1) for j in range(10)] #conquest gamemode locations
    locations += [f"{settlement.readableName} ({i})"
                  for settlement in sm.settlementDict.values() for i in range(10)]  # spheres gamemode locations
    location_name_to_id = {location: index for index, location in enumerate(locations, start=1)}

    sanityLocationNames = {}
    for key, item in factionItemManager.getAllItems().items():
        if (item.type == itemType.building or item.type == itemType.tech or item.type == itemType.ritual) and (item.progressionGroup is not None and item.progressionGroup != ""):
            sanityLocationNames.update({key + 1000000: item.readableName})
    for i in range(1,21):
        sanityLocationNames.update({i+20000: f"Won {i*5} Battles", i+20020: f"Sacked {i} Settlements", i+20040: f"Razed {i} Settlements"})
    location_name_to_id.update({item: key for key, item in sanityLocationNames.items()})

    #print(location_name_to_id)

    settlementManager: sm.SettlementManager = None



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

        sm.addModdedFactions(self.options.mod_list)
        self.playerFaction = sm.factionDict[self.options.starting_faction.value]
        self.settlementManager: sm.SettlementManager = sm.SettlementManager(self.random, self.playerFaction,
                                                                            self.options.starting_faction.value,
                                                                            self.options.starting_settlements)

        if self.options.faction_shuffle:
            self.settlements = self.settlementManager.randomiseSettlements()
        else:
            self.settlements = self.settlementManager.getSettlements()
        self.playerSettlements = [settlement for settlement in self.settlements.values()
                                  if settlement.faction == self.playerFaction.name]

        self.locationToDiploRange = {}

        self.options.local_items.value.add("Orb of Domination")
        self.options.non_local_items.value.add("Administrative Capacity")
        self.adminCapacity = 5
        if self.options.game_mode == "conquest":
            if self.playerFaction.race == "beastmen":
                self.adminCapacity = 1
        elif self.options.game_mode == "spheres":
            self.orbCount = 9
            self.sphereRadius = 150
            self.settlementDiploRange, self.factionDiploRange = self.settlementManager.getRequiredDiploRange(
                self.options.sphere_count, self.sphereRadius)
        if self.options.ritual_sanity:
            self.options.sanity.value = True
            self.options.ritual_shuffle.value = True
            if self.options.number_of_settlements < 3 * self.adminCapacity:
                self.options.number_of_settlements.value = 3 * self.adminCapacity
            if self.options.sphere_count < 3:
                self.options.sphere_count.value = 3
        if self.options.sanity:
            self.options.unit_shuffle.value = True
            self.options.building_shuffle.value = True
            self.options.tech_shuffle.value = True

            self.options.progressive_buildings.value = True
            self.options.starting_tier.value = 1
            self.sanityRules = sanityRules.ruleManager(self)

        if self.options.balance > 0 or not self.options.hard_logic:
            self.logger.warning(f"Total War Warhammer player {self.player} has soft logic enabled, if this is a large sync or async, then this may cause issues.")

    def create_regions(self) -> None:

        worldRegion = Region("Settlements", self.player, self.multiworld)
        self.multiworld.regions.append(worldRegion)

        if self.options.sanity:
            region = Region("Buildings", self.player, self.multiworld)
            self.multiworld.regions.append(region)
            worldRegion.connect(region, "Buildings")
            region = Region("Techs", self.player, self.multiworld)
            self.multiworld.regions.append(region)
            worldRegion.connect(region, "Techs")
        if self.options.ritual_sanity:
            region = Region("Rituals", self.player, self.multiworld)
            self.multiworld.regions.append(region)
            worldRegion.connect(region, "Rituals")
        if self.options.battle_sanity:
            region = Region("Battles", self.player, self.multiworld)
            self.multiworld.regions.append(region)
            worldRegion.connect(region, "Battles")
        if self.options.despoiler_sanity:
            region = Region("Despoiler", self.player, self.multiworld)
            self.multiworld.regions.append(region)
            worldRegion.connect(region, "Despoiler")

        locations.createAllLocations(self)#, self.locationToDiploRange)

    def create_items(self) -> None:
        self.itemKeys = []
        items.updateItemDict(self)
        items.createAllItems(self)
        if self.options.balance > 0:
            rules.setBalance(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        """
        Return the `slot_data` field that will be in the `Connected` network package.

        This is a way the generator can give custom data to the client.
        The client will receive this as JSON in the `Connected` response.

        :return: A dictionary to be sent to the client when it connects to the server.
        """
        slotData = self.options.as_dict("game_mode",
                                        "starting_faction",
                                        "progressive_technologies",
                                        "progressive_buildings",
                                        "progressive_units",
                                        "starting_tier",
                                        "randomize_personalities",
                                        "death_link",
                                        "death_link_effects",
                                        "mod_list",
                                        "game_mode",
                                        "faction_shuffle",
                                        "checks_per_settlement",
                                        "sanity",
                                        "ritual_sanity",
                                        "battle_sanity",
                                        "despoiler_sanity",
                                        "hard_logic",
                                        "fast_research",)
                                        #"location_balancing",)

        if self.options.game_mode == "conquest":
            slotData["number_of_settlements"] = self.options.number_of_settlements.value
            slotData["admin_capacity"] = self.adminCapacity
            slotData["max_expansion_items"] = math.floor(self.options.number_of_settlements / self.adminCapacity)
        if self.options.game_mode == "spheres":
            slotData["orbs"] = self.orbCount
            #settlementDiploRange, factionDiploRange = self.settlementManager.getRequiredDiploRange(
            #    self.options.sphere_count, self.sphereRadius)
            slotData["spheres"] = self.factionDiploRange
            slotData["max_expansion_items"] = self.options.sphere_count.value

        slotData["settlements"] = {settlement.name: settlement.faction for settlement in self.settlements.values()}
        slotData["hordes"] = self.settlementManager.randomiseHordes()
        slotData["faction_capitals"] = self.settlementManager.capitals
        slotData["items"] = self.itemKeys #Filled in items.py createAllItems
        slotData["seed"] = self.multiworld.seed
        slotData["options"] =  self.options.as_dict("starting_faction",
                                                    "game_mode",
                                                    "starting_settlements",
                                                    "checks_per_settlement",
                                                    "sanity",
                                                    "ritual_sanity",
                                                    "battle_sanity",
                                                    "despoiler_sanity",
                                                    "number_of_settlements",
                                                    "sphere_count",
                                                    "tech_shuffle",
                                                    "progressive_technologies",
                                                    "building_shuffle",
                                                    "progressive_buildings",
                                                    "unit_shuffle",
                                                    "progressive_units",
                                                    "ritual_shuffle",
                                                    "starting_tier",
                                                    "balance",
                                                    "hard_logic",
                                                    "mod_list",
                                                    "fast_research"),

        slotData["version"] = self.world_version.as_simple_string()
        return slotData


    def create_item(self, name: str) -> items.TWW3Item:
        if name == "Glitch Logic":
            return items.TWW3Item("Glitch Logic", IC.progression, None, self.player)

        key: int = self.item_name_to_id[name]
        return items.TWW3Item(name, items.itemDict[key].classification, key, player=self.player)

    def get_filler_item_name(self) -> str:
        fillerFunctions = [items.generateFillerWeak, items.generateFillerStrong, items.generateTrapHarmless,
                           items.generateTrapWeak, items.generateTrapStrong]  # List of functions for generating filler
        weights = [self.options.filler_weak.value, self.options.filler_strong.value, self.options.trap_harmless.value,
                   self.options.trap_weak.value, self.options.trap_strong.value]  # list of weights defined in YAML
        fillerFunction = self.random.choices(fillerFunctions, weights=weights, k=1)[0]
        item = fillerFunction(self)
        return item.name
        #item = items.generateFillerWeak(self)