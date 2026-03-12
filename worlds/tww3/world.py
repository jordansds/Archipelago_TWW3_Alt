from typing import Any, Mapping, ClassVar
from worlds.AutoWorld import World
from BaseClasses import Region
import settings
from worlds.tww3.options import TWW3Options
from worlds.tww3 import items, locations, rules
from worlds.tww3 import settlementManager as sm
#from .item_tables.ancillaries_table import ancillariesRegularDict

#class TWW3Location(Location):  # or from Locations import MyGameLocation
#    game = "Total War Warhammer 3"  # name of the game/world this location is in

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
    origin_region_name = "Old World"
    topology_present = False # show path to required location checks in spoiler

    #Holds the keys that will be sent to the client for locking techs/buildings/units
    #Will be populated in items.createAllItems
    itemKeys = []

    item_name_to_id = {item.readableName: key for key, item in items.itemDict.items()}
    #item_name_to_id = {}

    locations = [f"Empire Size {i} ({j})" for i in range(1,len(sm.settlementDict) + 1) for j in range(10)] #conquest gamemode locations
    locations += [f"{settlement.readableName} ({i})" for settlement in sm.settlementDict.values() for i in range(10)]  # spheres gamemode locations

    location_name_to_id = {k: v for v, k in enumerate(locations, start=1)}

    settlementManager: sm.SettlementManager = None

    def generate_early(self) -> None:
        #self.item_name_to_id.update({item.readableName: key for key, item in items.itemDict.items()})
        sm.addModdedFactions(self.options.mod_list)

        self.playerFaction = sm.factionDict[self.options.starting_faction.value]
        self.settlementManager: sm.SettlementManager = sm.SettlementManager(self.random, self.playerFaction, self.options.starting_faction.value, self.options.starting_settlements)

        if self.options.faction_shuffle:
            self.settlements = self.settlementManager.randomiseSettlements()
        else:
            self.settlements = self.settlementManager.getSettlements()
        self.playerSettlements = [settlement for settlement in self.settlements.values() if settlement.faction == self.playerFaction.name]
        #print(self.settlements)

        self.locationToDiploRange = {}

        self.options.local_items.value.add("Orb of Domination")
        #self.options.non_local_items.value.add("Diplomatic Range")
        self.options.non_local_items.value.add("Administrative Capacity")

    def create_regions(self) -> None:
        
        worldRegion = Region("Old World", self.player, self.multiworld)
        self.multiworld.regions.append(worldRegion)

        locations.createAllLocations(self)#, self.locationToDiploRange)
        rules.setVictoryEvent(self)

    def create_items(self) -> None:
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
        slotData = self.options.as_dict("starting_faction",
                                        "progressive_technologies",
                                        "progressive_buildings",
                                        "progressive_units",
                                        "starting_tier",
                                        "randomize_personalities",
                                        #"ritual_shuffle",
                                        "death_link",
                                        "death_link_effects",
                                        "mod_list"
                                         )
        #print(self.options.death_link_effects.value)
        slotData["checks_per_settlement"] = self.options.checks_per_settlement.value

        if self.options.game_mode == "conquest":
            slotData["number_of_settlements"] = self.options.number_of_settlements.value
            slotData["admin_capacity"] = self.options.admin_capacity.value
        elif self.options.game_mode == "spheres":
            slotData["orbs"] = self.options.orb_count.value
            settlementDiploRange, factionDiploRange = self.settlementManager.getRequiredDiploRange(
                self.options.sphere_count, self.options.sphere_radius)
            slotData["spheres"] = factionDiploRange #self.settlementManager.factionsToSpheres(self.options.sphere_count, self.options.sphere_radius)
        slotData["settlements"] = {settlement.name: settlement.faction for settlement in self.settlements.values()}
        slotData["hordes"] = self.settlementManager.randomiseHordes()
        slotData["faction_capitals"] = self.settlementManager.capitals
        slotData["items"] = self.itemKeys #Filled in items.py createAllItems
        slotData["game_mode"] = self.options.game_mode.value
        slotData["faction_shuffle"] = self.options.faction_shuffle.value
        slotData["version"] = self.world_version.as_simple_string()

        return slotData

    def create_item(self, name: str) -> items.TWW3Item:
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