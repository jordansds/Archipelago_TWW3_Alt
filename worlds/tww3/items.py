from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from worlds.tww3.world import TWW3World

from BaseClasses import Item
from BaseClasses import ItemClassification as IC
import math

from worlds.tww3.item_tables.filler_item_table import fillerDict, trapDict
from worlds.tww3.item_tables.ancillaries_table import ancillariesRegularDict, ancillariesLegendaryDict
from worlds.tww3.item_tables.progression_table import progressionDict
from worlds.tww3 import factionItemManager
from worlds.tww3.dataStructs import itemData, itemType
from .options import TWW3Options

itemDict: dict[int, itemData] = {}
itemDict.update(factionItemManager.getAllItems())
itemDict.update(fillerDict)
itemDict.update(trapDict)
#itemDict.update(globalEffectTable) #disabled as a large number of these checks don't do anything
itemDict.update(ancillariesRegularDict)
itemDict.update(ancillariesLegendaryDict)
itemDict.update(progressionDict)

class TWW3Item(Item):  # or from Items import MyGameItem
    game = "Total War Warhammer III"  # name of the game/world this item is from

    options_dataclass = TWW3Options  # options the player can set
    options: TWW3Options  # typing hints for option results

def updateItemDict(world: TWW3World) -> None: #Make items progressive if we need them for logic due to yaml settings
    if world.options.balance > 0:
        for key, item in factionItemManager.getUnits(world.playerFaction.race, world.options.progressive_units):
            itemDict[key] = itemData(IC.progression, *item[1:])
        for key, item in factionItemManager.getBuildings(world.playerFaction.race, world.options.progressive_buildings):
            itemDict[key] = itemData(IC.progression, *item[1:])
        for key, item in factionItemManager.getTechs(world.playerFaction.race, world.options.progressive_technologies):
                itemDict[key] = itemData(IC.progression, *item[1:])
    """if world.options.force_early_units:
        for key, item in factionItemManager.getUnits(world.playerFaction.race, world.options.progressive_units):
            itemDict[key] = itemData(IC.progression, *item[1:])

    if world.options.force_early_buildings:
        for key, item in factionItemManager.getBuildings(world.playerFaction.race, world.options.progressive_buildings):
            if item.classification != IC.progression:
                itemDict[key] = itemData(IC.progression, *item[1:])

    if world.options.force_early_techs:
        for key, item in factionItemManager.getTechs(world.playerFaction.race, world.options.progressive_technologies):
            itemDict[key] = itemData(IC.progression, *item[1:])"""

    if world.options.sanity:
        for key, item in factionItemManager.getUnits(world.playerFaction.race, world.options.progressive_units):
            itemDict[key] = itemData(IC.progression, *item[1:])
        for key, item in factionItemManager.getBuildings(world.playerFaction.race, world.options.progressive_buildings):
            itemDict[key] = itemData(IC.progression, *item[1:])
        for key, item in factionItemManager.getTechs(world.playerFaction.race, world.options.progressive_technologies):
            itemDict[key] = itemData(IC.progression, *item[1:])
        for key, item in factionItemManager.getSpecial(world, True):
            if item.type == itemType.building or item.type == itemType.tech:
                itemDict[key] = itemData(IC.progression, *item[1:2], *item[3:6], item[6], item[9])

    if world.options.ritual_sanity:
        for key, item in factionItemManager.getRituals(world):
            itemDict[key] = itemData(IC.progression, *item[1:2], *item[3:6], item[6], item[9])

def createAllItems(world: TWW3World) -> None:
    #world.itemKeys = []
    pool: list[TWW3Item] = []

    pool = generateUnitItems(world, pool)
    pool = generateBuildingItems(world, pool)
    pool = generateTechnologyItems(world, pool)
    pool = generateSpecialItems(world, pool)
    pool = generateModdedItems(world, pool)

    pool = generateExpansionItems(world, pool)
    pool = generateRitualItems(world, pool)

    # Remove traps based on yaml settings
    if len(world.options.trap_blacklist.value) < len(trapDict):
        for trap in world.options.trap_blacklist:
            try:
                for key, item in trapDict.items():
                    if item.readableName[6:] == trap:
                        del trapDict[key]
                        break
            except KeyError:
                world.logger.warn(f"Invalid YAML: {trap} set in yaml is invalid, check your spelling.")

    pool = generateFillerItems(world, pool)

    world.multiworld.itempool += pool
    #print(pool)

def generateUnitItems(world: TWW3World, pool: list) -> list:
    if world.options.unit_shuffle:
        for key, item in factionItemManager.getUnits(world.playerFaction.race, world.options.progressive_units):
            if item.tier > world.options.starting_tier:
                for i in range(item.count - world.options.starting_tier if item.count > 1 else 1):
                    tww3_item = world.create_item(item.readableName)
                    pool.append(tww3_item)
                    if not world.options.progressive_units:
                        world.itemKeys.append(key)
    return pool

def generateBuildingItems(world: TWW3World, pool: list) -> list:
    if world.options.building_shuffle:
        for key, item in factionItemManager.getBuildings(world.playerFaction.race, world.options.progressive_buildings):
            if "settlement" in item.name: #and world.options.building_sanity:
                continue
            #if "settlement_major" in item.name:
            #    if item.progressionGroup is None:
            #        world.multiworld.local_early_items[world.player][item.readableName] = max(item.count - world.options.starting_tier - 2, 0)
            #    elif world.options.starting_tier - 1 < item.tier <= 2:
            #        world.multiworld.local_early_items[world.player][item.readableName] = 1
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

                    #print(f"{item.readableName} x {i+1}")
    return pool

def generateTechnologyItems(world: TWW3World, pool: list) -> list:
    if world.options.tech_shuffle:
        for key, item in factionItemManager.getTechs(world.playerFaction.race, world.options.progressive_technologies):
            if item.tier > 0:
                for i in range(item.count):
                    tww3_item = world.create_item(item.readableName)
                    pool.append(tww3_item)
                    if not world.options.progressive_technologies:
                        world.itemKeys.append(key)
    return pool

def generateSpecialItems(world: TWW3World, pool: list) -> list:
    for key, item in factionItemManager.getSpecial(world):
        if item.spcLogic:
            world.multiworld.local_early_items[world.player][item.readableName] = item.count
        if item.type == itemType.building and item.tier > world.options.starting_tier - 1:
            for i in range(item.count):
                tww3_item = world.create_item(item.readableName)
                pool.append(tww3_item)
                if not item.isProgressiveItem:
                    world.itemKeys.append(key)
        elif (item.type == itemType.unit and item.tier > world.options.starting_tier) or item.type == itemType.tech:
            for i in range(item.count):
                tww3_item = world.create_item(item.readableName)
                pool.append(tww3_item)
                if not item.isProgressiveItem:
                    world.itemKeys.append(key)
    return pool

def generateModdedItems(world: TWW3World, pool: list) -> list:
    for key, item in factionItemManager.getModdedItems(world):
        if item.tier > world.options.starting_tier:
            if ((item.type == itemType.unit and item.progressionGroup is not None and world.options.progressive_units) or
                (item.type == itemType.unit and item.progressionGroup is None and not world.options.progressive_units) or
                (item.type == itemType.building and item.progressionGroup is not None and world.options.progressive_buildings) or
                (item.type == itemType.building and item.progressionGroup is None and not world.options.progressive_buildings) or
                (item.type == itemType.tech and item.progressionGroup is not None and world.options.progressive_technologies) or
                (item.type == itemType.tech and item.progressionGroup is None and not world.options.progressive_technologies)):
                continue
            for i in range(item.count - world.options.starting_tier if item.count > 1 else 1):
                tww3_item = world.create_item(item.readableName)
                pool.append(tww3_item)
                if not world.options.progressive_units:
                    world.itemKeys.append(key)
    return pool

def generateRitualItems(world: TWW3World, pool: list) -> list:
    try:
        if world.options.ritual_shuffle:
            for key, item in factionItemManager.getRituals(world):
                if not item.spcLogic:
                    for i in range(item.count):
                        tww3_item = world.create_item(item.readableName)
                        pool.append(tww3_item)
                        world.itemKeys.append(key)
    except AttributeError:
        print(f"{world.playerFaction.race} Do not have a ritual table yet")
    return pool

def generateExpansionItems(world: TWW3World, pool: list) -> list:
    if world.options.game_mode == "conquest":
        for i in range(math.floor(world.options.number_of_settlements / world.adminCapacity)):
            item = world.create_item("Administrative Capacity")
            pool.append(item)
    elif world.options.game_mode == "spheres":
        for i in range(world.options.sphere_count):# + world.options.extra_sphere_count):
            item = world.create_item("Diplomatic Range")
            pool.append(item)
        for i in range(world.options.orb_count):# + world.options.extra_orb_count):
            item = world.create_item("Orb of Domination")
            pool.append(item)
        #world.multiworld.local_items[world.player]["Orb of Domination"] = world.options.orb_count + world.options.extra_orb_count
        #world.multiworld.local_early_items[world.player][item.readableName] = max(
        #    item.count - world.options.starting_tier - 2, 0)
    return pool

def generateFillerItems(world: TWW3World, pool: list) -> list:

    #fillerFunctions = [generateFillerWeak, generateFillerStrong, generateTrapHarmless, generateTrapWeak, generateTrapStrong] #List of functions for generating filler
    #weights = [world.options.filler_weak.value, world.options.filler_strong.value, world.options.trap_harmless.value, world.options.trap_weak.value, world.options.trap_strong.value] #list of weights defined in YAML
    fillerFunctions = [generateFiller, generateTrap] #List of functions for generating filler
    weights = [world.options.filler.value, 100 - world.options.filler.value] #list of weights defined in YAML

    #if sum(weights) == 0:
    #    world.logger.warn("Invalid YAML: Sum of filler and trap weighting must not be zero, filler set to 1.")
    #    weights = [1,0]

    fillerCount = - len(pool) - 1
    for region in world.get_regions():
        fillerCount += len(region.locations)
    #fillerCount = len(world.get_region("Old World").locations) - len(pool) - 1
    fillerFunctions = world.random.choices(fillerFunctions, weights=weights, k=fillerCount)
    
    for func in fillerFunctions:
        item = func(world)
        pool.append(item)
        
    return pool

def generateFiller(world: TWW3World) -> TWW3Item:
    key = world.random.choice(tuple(fillerDict.keys()))
    if key == 1207 and world.options.game_mode == "conquest":
        key = 1205
    if key == 1203:
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

def generateTrap(world: TWW3World) -> TWW3Item:
    key = world.random.choice(tuple(trapDict.keys()))
    if key == 1504 and world.options.game_mode == "spheres":
        key = world.random.randint(1500, 1503)

    name = itemDict[key].readableName
    item = world.create_item(name)
    return item

#def generateFillerWeak(world: TWW3World) -> TWW3Item:
#    key = world.random.choice(tuple(fillerDict.keys()))
#
#    # apply random effect
#    """
#    if key == 1201:
#        effect_table = globalEffectTable
#        name = world.random.choice(tuple(effect_table.values())).name
#        key = world.item_name_to_id[name]
#    """
#    # get random ancillary
#    if key == 1203 or key == 1201:
#        ancillaries_table = ancillariesRegularDict
#        name = world.random.choice(tuple(ancillaries_table.values())).readableName
#        #key = world.item_name_to_id[name]
#    elif key == 1205:
#        ancillaries_table = ancillariesLegendaryDict
#        name = world.random.choice(tuple(ancillaries_table.values())).readableName
#        # key = world.item_name_to_id[name]
#    else:
#        name = itemDict[key].readableName
#
#    item = world.create_item(name)
#    return item

#def generateFillerStrong(world: TWW3World) -> TWW3Item:
#    key = world.random.choice(tuple(fillerStrongDict.keys()))
#    #This item is considered a trap in conquest
#    if key == 1301 and world.options.game_mode == "conquest":
#        key = 1205
#    # get legendary ancillary
#    if key == 1205:
#        ancillaries_table = ancillariesLegendaryDict
#        name = world.random.choice(tuple(ancillaries_table.values())).readableName
#        #key = world.item_name_to_id[name]
#    else:
#        name = itemDict[key].readableName
        
#    item = world.create_item(name)
#    return item

#def generateTrapHarmless(world: TWW3World) -> TWW3Item:
#    key = world.random.choice(tuple(trapHarmlessDict.keys()))
#    name = itemDict[key].readableName
#
#    item = world.create_item(name)
#    return item

#def generateTrapWeak(world: TWW3World) -> TWW3Item:
#    key = world.random.choice(tuple(trapDict.keys()))
#    if key == 1504 and world.options.game_mode == "spheres":
#        key = world.random.randint(1500, 1503)

#    name = itemDict[key].readableName

#    item = world.create_item(name)
#    return item

#def generateTrapStrong(world: TWW3World) -> TWW3Item:
#    key = world.random.choice(tuple(trapStrongDict.keys()))
#    name = itemDict[key].readableName
#
#    item = world.create_item(name)
#    return item