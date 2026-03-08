from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .world import TWW3World

from BaseClasses import Item
from BaseClasses import ItemClassification as IC
import math

from .item_tables.filler_item_table import fillerWeakDict, fillerStrongDict, trapHarmlessDict, trapStrongDict, trapWeakDict
from .item_tables.ancillaries_table import ancillariesRegularDict, ancillariesLegendaryDict
from .item_tables.ritual_table import ritualDict
from .item_tables.progression_table import progressionDict
#from . import settlementManager as sm
from . import factionTables

from worlds.tww3.item_types import ItemData, ItemType
from .options import TWW3Options

itemDict: dict[int, ItemData] = {}
itemDict.update(factionTables.getAllItems())
itemDict.update(fillerWeakDict)
itemDict.update(fillerStrongDict)
itemDict.update(trapHarmlessDict)
itemDict.update(trapWeakDict)
itemDict.update(trapStrongDict)
#itemDict.update(globalEffectTable) #disabled as a large number of these checks don't do anything
itemDict.update(ancillariesRegularDict)
itemDict.update(ancillariesLegendaryDict)
#itemDict.update(ritualDict)
itemDict.update(progressionDict)

class TWW3Item(Item):  # or from Items import MyGameItem
    game = "Total War Warhammer 3"  # name of the game/world this item is from

    options_dataclass = TWW3Options  # options the player can set
    options: TWW3Options  # typing hints for option results

def updateItemDict(world: TWW3World) -> None:
    if world.options.force_early_units:
        for key, item in factionTables.getUnits(world.playerFaction.race, world.options.progressive_units):
            itemDict[key] = ItemData(IC.progression, *item[1:])
    if world.options.force_early_buildings:
        for key, item in factionTables.getBuildings(world.playerFaction.race, world.options.progressive_buildings):
            if item.classification != IC.progression:
                itemDict[key] = ItemData(IC.progression, *item[1:])
    if world.options.force_early_techs:
        for key, item in factionTables.getTechs(world.playerFaction.race, world.options.progressive_technologies):
            itemDict[key] = ItemData(IC.progression, *item[1:])

def createAllItems(world: TWW3World) -> None:
    pool: list[TWW3Item] = []

    pool = generateUnitItems(world, pool)
    pool = generateBuildingItems(world, pool)
    pool = generateTechnologyItems(world, pool)
    pool = generateSpecialItems(world, pool)
    pool = generateModdedItems(world, pool)

    pool = generateExpansionItems(world, pool)

    pool = generateFillerItems(world, pool)

    world.multiworld.itempool += pool

    #print(pool)

def generateUnitItems(world: TWW3World, pool: list) -> list:
    if world.options.unit_shuffle:
        for key, item in factionTables.getUnits(world.playerFaction.race, world.options.progressive_units):
            if item.tier > world.options.starting_tier:
                for i in range(item.count - world.options.starting_tier if item.count > 1 else 1):
                    tww3_item = world.create_item(item.readableName)
                    pool.append(tww3_item)
                    if not world.options.progressive_units:
                        world.itemKeys.append(key)
    return pool

def generateBuildingItems(world: TWW3World, pool: list) -> list:
    if world.options.building_shuffle:
        for key, item in factionTables.getBuildings(world.playerFaction.race, world.options.progressive_buildings):
            if "settlement_major" in item.name:
                if item.progressionGroup is None:
                        world.multiworld.local_early_items[world.player][item.readableName] = max(item.count - world.options.starting_tier - 2, 0)
                elif item.tier <= 2:
                    world.multiworld.local_early_items[world.player][item.readableName] = 1
            if item.tier > world.options.starting_tier - 1: #ALL BUILDINGS ARE OFFSET BY 1 IN THE DATABASE. WHY!!!!!!!!
                #Need to change so that if progressive buildings, generate 1 less item
                reduce = 0
                if world.options.progressive_buildings: #ALL BUILDINGS ARE OFFSET BY 1 IN THE DATABASE. WHY!!!!!!!!
                    reduce = 1
                for i in range(item.count - world.options.starting_tier if item.count > 1 else 1 - reduce):
                    tww3_item = world.create_item(item.readableName)
                    pool.append(tww3_item)
                    if not world.options.progressive_buildings:
                        world.itemKeys.append(key)
    return pool

def generateTechnologyItems(world: TWW3World, pool: list) -> list:
    if world.options.tech_shuffle:
        for key, item in factionTables.getTechs(world.playerFaction.race, world.options.progressive_technologies):
            for i in range(item.count):
                tww3_item = world.create_item(item.readableName)
                pool.append(tww3_item)
                if not world.options.progressive_technologies:
                    world.itemKeys.append(key)
    return pool

def generateSpecialItems(world: TWW3World, pool: list) -> list:
    for key, item in factionTables.getSpecial(world):
        if item.forceEarly:
            world.multiworld.local_early_items[world.player][item.readableName] = item.count
        if item.tier > world.options.starting_tier or item.type == ItemType.tech:
            for i in range(item.count):
                tww3_item = world.create_item(item.readableName)
                pool.append(tww3_item)
                if not item.isProgressiveItem:
                    world.itemKeys.append(key)

    return pool

def generateModdedItems(world: TWW3World, pool: list) -> list:
    for key, item in factionTables.getModdedItems(world.playerFaction.race, world.playerFaction.race, world.options.mod_list):
        if item.tier > world.options.starting_tier:
            for i in range(item.count - world.options.starting_tier if item.count > 1 else 1):
                tww3_item = world.create_item(item.readableName)
                pool.append(tww3_item)
                if not world.options.progressive_units:
                    world.itemKeys.append(key)

    return pool

#Unused - code does not appear to have ever worked since Sinthoras created mod
def generateRitualItems(world: TWW3World, pool: list) -> list:
    if world.options.ritual_shuffle:
        for key, item in ritualDict.items():
            if item.faction == world.playerFaction.name:
                for i in range(item.count):
                    tww3_item = world.create_item(item.name)
                    pool.append(tww3_item)
    return pool

def generateExpansionItems(world: TWW3World, pool: list) -> list:
    if world.options.game_mode == "conquest":
        for i in range(1, math.floor(world.options.number_of_settlements / world.options.admin_capacity)):
            item = world.create_item("Administrative Capacity")
            pool.append(item)
    elif world.options.game_mode == "spheres":
        for i in range(world.options.sphere_count + world.options.extra_sphere_count):
            item = world.create_item("Diplomatic Range")
            pool.append(item)
        for i in range(world.options.orb_count + world.options.extra_orb_count):
            item = world.create_item("Orb of Domination")
            pool.append(item)
    return pool

def generateFillerItems(world: TWW3World, pool: list) -> list:

    fillerFunctions = [generateFillerWeak, generateFillerStrong, generateTrapHarmless, generateTrapWeak, generateTrapStrong] #List of functions for generating filler
    weights = [world.options.filler_weak.value, world.options.filler_strong.value, world.options.trap_harmless.value, world.options.trap_weak.value, world.options.trap_strong.value] #list of weights defined in YAML
    
    if sum(weights) == 0:
        raise Exception("Invalid YAML: Sum of all filler and trap weighting must not be zero.")

    fillerCount = len(world.get_region("Old World").locations) - len(pool) - 1
    fillerFunctions = world.random.choices(fillerFunctions, weights=weights, k=fillerCount)
    
    for func in fillerFunctions:
        item = func(world)
        pool.append(item)
        
    return pool

def generateFillerWeak(world: TWW3World) -> TWW3Item:
    key = world.random.choice(tuple(fillerWeakDict.keys()))

    # apply random effect
    """
    if key == 1201:
        effect_table = globalEffectTable
        name = world.random.choice(tuple(effect_table.values())).name
        key = world.item_name_to_id[name]
    """
    # get random ancillary
    if key == 1203 or key == 1201:
        ancillaries_table = ancillariesRegularDict
        name = world.random.choice(tuple(ancillaries_table.values())).readableName
        #key = world.item_name_to_id[name]
    elif key == 1205:
        ancillaries_table = ancillariesLegendaryDict
        name = world.random.choice(tuple(ancillaries_table.values())).readableName
        # key = world.item_name_to_id[name]
    else:
        name = itemDict[key].readableName

    item = world.create_item(name)
    return item

def generateFillerStrong(world: TWW3World) -> TWW3Item:
    key = world.random.choice(tuple(fillerStrongDict.keys()))
    #This item is considered a trap in conquest
    if key == 1301 and world.options.game_mode == "conquest":
        key = 1205
    # get legendary ancillary
    if key == 1205:
        ancillaries_table = ancillariesLegendaryDict
        name = world.random.choice(tuple(ancillaries_table.values())).readableName
        #key = world.item_name_to_id[name]
    else:
        name = itemDict[key].readableName
        
    item = world.create_item(name)
    return item

def generateTrapHarmless(world: TWW3World) -> TWW3Item:
    key = world.random.choice(tuple(trapHarmlessDict.keys()))
    name = itemDict[key].readableName

    item = world.create_item(name)
    return item

def generateTrapWeak(world: TWW3World) -> TWW3Item:
    key = world.random.choice(tuple(trapWeakDict.keys()))
    if key == 1504 and world.options.game_mode == "spheres":
        key = world.random.randint(1500, 1503)

    name = itemDict[key].readableName

    item = world.create_item(name)
    return item

def generateTrapStrong(world: TWW3World) -> TWW3Item:
    key = world.random.choice(tuple(trapStrongDict.keys()))
    name = itemDict[key].readableName
    
    item = world.create_item(name)
    return item


        
