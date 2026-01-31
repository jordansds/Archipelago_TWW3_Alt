from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .world import TWW3World

from BaseClasses import Item, ItemClassification as IC
import math

from .item_tables.filler_item_table import fillerWeakTable, fillerStrongTable, trapHarmlessTable, trapWeakTable, trapStrongDict
from .item_tables.effect_table import globalEffectTable
from .item_tables.ancillaries_table import ancillariesRegularTable, ancillariesLegendaryTable
from .item_tables.unique_item_table import unique_item_table
from .item_tables.ritual_table import ritualDict
from .item_tables.progressive_buildings_table import progressiveBuildingsDict
from .item_tables.progressive_units_table import progressiveUnitsDict
from .item_tables.progressive_techs_table import progressiveTechsDict
from .item_tables.progression_table import progressionDict

from .item_tables.item_types import ItemType, ItemData
from .options import TWW3Options

itemDict = {}
itemDict.update(fillerWeakTable)
itemDict.update(fillerStrongTable)
itemDict.update(trapHarmlessTable)
itemDict.update(trapWeakTable)
itemDict.update(trapStrongDict)
#itemDict.update(globalEffectTable) #disabled as a large number of these checks don't do anything
itemDict.update(ancillariesRegularTable)
itemDict.update(ancillariesLegendaryTable)
itemDict.update(unique_item_table)
itemDict.update(progressiveBuildingsDict)
itemDict.update(progressiveUnitsDict)
itemDict.update(progressiveTechsDict)
itemDict.update(ritualDict)
itemDict.update(progressionDict)

class TWW3Item(Item):  # or from Items import MyGameItem
    game = "Total War Warhammer 3"  # name of the game/world this item is from

    options_dataclass = TWW3Options  # options the player can set
    options: TWW3Options  # typing hints for option results

def updateItemDict(world: TWW3World) -> None:
    # Handle non-progressive items
    for key, item in unique_item_table.items():
        if item.type == ItemType.tech and world.options.force_early_techs and not world.options.progressive_technologies:
            itemDict[key] = ItemData(IC.progression, item[1], item[2], item[3], item[4], item[5], item[6])
        elif item.type == ItemType.unit and world.options.force_early_units and not world.options.progressive_units:
            itemDict[key] = ItemData(IC.progression, item[1], item[2], item[3], item[4], item[5], item[6])
        elif item.type == ItemType.building and world.options.force_early_buildings and not world.options.progressive_buildings:
            itemDict[key] = ItemData(IC.progression, item[1], item[2], item[3], item[4], item[5], item[6])

    # Handle progressive items
    if world.options.tech_shuffle and world.options.force_early_techs and world.options.progressive_technologies:
        for key, item in progressiveTechsDict.items():
            itemDict[key] = ItemData(IC.progression, item[1], item[2], item[3], item[4], item[5], item[6])
    if world.options.unit_shuffle and world.options.force_early_units and world.options.progressive_units:
        for key, item in progressiveUnitsDict.items():
            itemDict[key] = ItemData(IC.progression, item[1], item[2], item[3], item[4], item[5], item[6])
    if world.options.building_shuffle and world.options.force_early_buildings and world.options.progressive_buildings:
        for key, item in progressiveBuildingsDict.items():
            itemDict[key] = ItemData(IC.progression, item[1], item[2], item[3], item[4], item[5], item[6])

def createAllItems(world: TWW3World) -> None:
    pool: list[TWW3Item] = []

    for key, item in unique_item_table.items():
        if (item.faction == world.player_faction or
            (world.player_faction == "wh3_dlc27_hef_aislinn" and item.faction == "wh2_main_hef_eataine") or
            (world.player_faction == "wh3_dlc27_nor_sayl" and item.faction == "wh_dlc08_nor_norsca") or
            (world.player_faction == "wh3_dlc27_sla_the_tormentors" and item.faction == "wh3_main_sla_seducers_of_slaanesh") or
            (world.player_faction == "wh3_dlc27_sla_masque_of_slaanesh" and item.faction == "wh3_main_sla_seducers_of_slaanesh")):
            if item.tier is not None:
                if (item.tier > world.options.starting_tier) and (item.type == ItemType.unit) and world.options.unit_shuffle and not world.options.progressive_units:
                    for i in range(item.count):
                        tww3_item = world.create_item(item.name)
                        pool.append(tww3_item)
                        #world.item_list.append(key)
                elif (item.tier + 1 > world.options.starting_tier.value) and (item.type == ItemType.building) and world.options.building_shuffle and not world.options.progressive_buildings:
                    for i in range(item.count):
                        tww3_item = world.create_item(item.name)
                        pool.append(tww3_item)
                        #world.item_list.append(key)
                elif (world.options.tech_shuffle.value == True) and (item.type == ItemType.tech) and  not world.options.progressive_technologies:
                    for i in range(item.count):
                        tww3_item = world.create_item(item.name)
                        pool.append(tww3_item)
                        #world.item_list.append(key)

    pool = generateTechnologyItems(world, pool)
    pool = generateUnitItems(world, pool)
    pool = generateBuildingItems(world, pool)
    pool = generateRitualItems(world, pool)
    pool = generateExpansionItems(world, pool)
    pool = generateFillerItems(world, pool)

    world.multiworld.itempool += pool

def generateTechnologyItems(world: TWW3World, pool: list) -> list:
    if world.options.progressive_technologies and world.options.tech_shuffle:
        for key, item in progressiveTechsDict.items():
            if ((item.faction == world.player_faction or 
                (world.player_faction == "wh3_dlc27_hef_aislinn" and item.faction == "wh2_main_hef_eataine") or 
                (world.player_faction == "wh3_dlc27_nor_sayl" and item.faction == "wh_dlc08_nor_norsca") or
                (world.player_faction == "wh3_dlc27_sla_the_tormentors" and item.faction == "wh3_main_sla_seducers_of_slaanesh") or
                (world.player_faction == "wh3_dlc27_sla_masque_of_slaanesh" and item.faction == "wh3_main_sla_seducers_of_slaanesh"))
                and (world.options.tech_shuffle.value == True)):
                for i in range(item.count):
                    tww3_item = world.create_item(item.name)
                    pool.append(tww3_item)
    return pool

def generateUnitItems(world: TWW3World, pool: list) -> list:
    if world.options.progressive_units and world.options.unit_shuffle:
        for key, item in progressiveUnitsDict.items():
            if ((item.faction == world.player_faction or 
                (world.player_faction == "wh3_dlc27_hef_aislinn" and item.faction == "wh2_main_hef_eataine") or 
                (world.player_faction == "wh3_dlc27_nor_sayl" and item.faction == "wh_dlc08_nor_norsca") or
                (world.player_faction == "wh3_dlc27_sla_the_tormentors" and item.faction == "wh3_main_sla_seducers_of_slaanesh") or
                (world.player_faction == "wh3_dlc27_sla_masque_of_slaanesh" and item.faction == "wh3_main_sla_seducers_of_slaanesh"))
                and (item.tier > world.options.starting_tier.value) and (world.options.unit_shuffle.value == True)):
                for i in range(item.count):
                    tww3_item = world.create_item(item.name)
                    pool.append(tww3_item)
    return pool
    
def generateBuildingItems(world: TWW3World, pool: list) -> list:
    if world.options.progressive_buildings and world.options.building_shuffle:
        for key, item in progressiveBuildingsDict.items():
            if ((item.faction == world.player_faction or 
                (world.player_faction == "wh3_dlc27_hef_aislinn" and item.faction == "wh2_main_hef_eataine") or 
                (world.player_faction == "wh3_dlc27_nor_sayl" and item.faction == "wh_dlc08_nor_norsca") or
                (world.player_faction == "wh3_dlc27_sla_the_tormentors" and item.faction == "wh3_main_sla_seducers_of_slaanesh") or
                (world.player_faction == "wh3_dlc27_sla_masque_of_slaanesh" and item.faction == "wh3_main_sla_seducers_of_slaanesh"))
                and (item.tier +1 > world.options.starting_tier.value) and (world.options.building_shuffle.value == True)):
                for i in range(item.count):
                    tww3_item = world.create_item(item.name)
                    pool.append(tww3_item)
    return pool

def generateRitualItems(world: TWW3World, pool: list) -> list:
    if world.options.ritual_shuffle:
        for key, item in ritualDict.items():
            if (item.faction == world.player_faction or 
                (world.player_faction == "wh3_dlc27_hef_aislinn" and item.faction == "wh2_main_hef_eataine") or 
                (world.player_faction == "wh3_dlc27_nor_sayl" and item.faction == "wh_dlc08_nor_norsca") or
                (world.player_faction == "wh3_dlc27_sla_the_tormentors" and item.faction == "wh3_main_sla_seducers_of_slaanesh") or
                (world.player_faction == "wh3_dlc27_sla_masque_of_slaanesh" and item.faction == "wh3_main_sla_seducers_of_slaanesh")):
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
        for i in range(world.options.sphere_count + world.options.extra_sphere_count - 1):
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
    key = world.random.choice(tuple(fillerWeakTable.keys()))

    # apply random effect
    """
    if key == 2001:
        effect_table = globalEffectTable
        name = world.random.choice(tuple(effect_table.values())).name
        key = world.item_name_to_id[name]
    """
    # get random ancillary
    if key == 2003 or key == 2001:
        ancillaries_table = ancillariesRegularTable
        name = world.random.choice(tuple(ancillaries_table.values())).name
        key = world.item_name_to_id[name]
    else:
        name = itemDict[key].name

    item = world.create_item(name)
    return item

def generateFillerStrong(world: TWW3World) -> TWW3Item:
    key = world.random.choice(tuple(fillerStrongTable.keys()))
    # get legendary ancillary
    if key == 2502:
        ancillaries_table = ancillariesLegendaryTable
        name = world.random.choice(tuple(ancillaries_table.values())).name
        key = world.item_name_to_id[name]
    else:
        name = itemDict[key].name
        
    item = world.create_item(name)
    return item

def generateTrapHarmless(world: TWW3World) -> TWW3Item:
    key = world.random.choice(tuple(trapHarmlessTable.keys()))
    name = itemDict[key].name

    item = world.create_item(name)
    return item

def generateTrapWeak(world: TWW3World) -> TWW3Item:
    key = world.random.choice(tuple(trapWeakTable.keys()))
    name = itemDict[key].name
    
    item = world.create_item(name)
    return item

def generateTrapStrong(world: TWW3World) -> TWW3Item:
    key = world.random.choice(tuple(trapStrongDict.keys()))
    name = itemDict[key].name
    
    item = world.create_item(name)
    return item


        
