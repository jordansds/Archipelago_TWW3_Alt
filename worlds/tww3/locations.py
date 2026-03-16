from __future__ import annotations
from typing import TYPE_CHECKING

from worlds.tww3.itemTypes import itemType, itemData

if TYPE_CHECKING:
    from worlds.tww3.world import TWW3World

from BaseClasses import Location, ItemClassification as IC
from worlds.generic.Rules import set_rule, add_rule
from rule_builder.rules import Has, HasAllCounts
from worlds.tww3 import items, factionItemManager, settlementManager as sm
from worlds.tww3.item_tables import sanityRules
import math

class TWW3Location(Location):
    game = "Total War Warhammer 3"
    
def createAllLocations(world: TWW3World) -> None:

    if world.options.game_mode == "conquest":
        createRegularLocations(world)

    elif world.options.game_mode == "spheres":
        createDiploRangeLocations(world)

    if world.options.building_sanity and world.options.building_shuffle:
        createBuildingLocations(world)

    if world.options.tech_sanity and world.options.tech_shuffle:
        createTechLocations(world)

    if world.options.ritual_sanity and world.options.ritual_shuffle:
        createRitualLocations(world)

    createEvents(world)
    
def createRegularLocations(world: TWW3World) -> None:
    worldRegion = world.get_region("Old World")
    # Check if player has starting regions. If they do, then skip the player's starting settlements to prevent the game from fulfilling checks before game start.
    startingCheck = world.options.starting_settlements + 1
    if world.playerFaction.name in sm.hordeList:
        startingCheck = 1
    # Generate all but last location, which is saved for the victory event
    # Fill location checks based on number of locations and checks per location
    for i in range(startingCheck, world.options.number_of_settlements):
        for j in range(world.options.checks_per_settlement):
            locName = f"Empire Size {i} ({j})"
            
            locId = world.location_name_to_id[locName]
            location = TWW3Location(world.player, locName, locId, worldRegion)

            requiredAdminCapacity = math.floor(i / world.options.admin_capacity) #max(0, math.floor(i / world.options.admin_capacity))
            #set_rule(location, lambda state: state.has("Administrative Capacity", world.player, requiredAdminCapacity))
            set_rule(location, lambda state, count=requiredAdminCapacity: state.has("Administrative Capacity", world.player, count))

            worldRegion.locations.append(location)

def createEvents(world: TWW3World) -> None:
    worldRegion = world.get_region("Old World")
    if world.options.game_mode == "conquest":
        # Add victory event in the last location
        locName = f"Empire Size {world.options.number_of_settlements}"
        location = TWW3Location(world.player, locName, None, worldRegion)
        #count = math.floor(world.options.number_of_settlements / world.options.admin_capacity) - 1
        set_rule(location, lambda state, count=math.floor(world.options.number_of_settlements / world.options.admin_capacity) - 1: state.has("Administrative Capacity", world.player, count))

    elif world.options.game_mode == "spheres":
        location = TWW3Location(world.player, "Victory", None, worldRegion)

    worldRegion.locations.append(location)
    # Create Victory item and place it in the last location
    victory = items.TWW3Item("Victory", IC.progression, None, world.player)
    location.place_locked_item(victory)

def createDiploRangeLocations(world: TWW3World) -> None:
    worldRegion = world.get_region("Old World")

    settlementDiploRange, factionDiploRange = world.settlementManager.getRequiredDiploRange(world.options.sphere_count, world.options.sphere_radius)

    key = -1
    for settlement in world.settlements.values():
        key += 1
        from collections import Counter
        for i in range(world.options.checks_per_settlement):
            locId = world.location_name_to_id[f"{settlement.readableName} ({i})"]
            location = TWW3Location(world.player, f"{settlement.readableName} ({i})", locId, worldRegion)

            #print(f"{location} : {settlementDiploRange[key]}")

            if settlementDiploRange[key] > world.options.sphere_count:
                continue

            elif settlementDiploRange[key] == 0:
                if settlement.faction != world.playerFaction.name:
                    worldRegion.locations.append(location)

            elif settlementDiploRange[key] > 0:
                set_rule(location, lambda state, count=settlementDiploRange[key]: state.has("Diplomatic Range", world.player, count))
                worldRegion.locations.append(location)
                    #print(location)

    #print(len(worldRegion.locations))

def createBuildingLocations(world: TWW3World) -> None:
    region = world.get_region("Buildings")

    specialBuildings = [item for key, item in factionItemManager.getSpecial(world, True) if
                        item.type == itemType.building]
    buildings = [item for key, item in factionItemManager.getBuildings(world.playerFaction.race, False)]
    progBuildings = [item for key, item in factionItemManager.getBuildings(world.playerFaction.race, True)]
    buildings += [itemData(*item[:2], *item[3:6], item[6], item[9]) for item in specialBuildings if item.progressionGroup is not None]
    progBuildings += [itemData(*item[:2], *item[3:6], item[6], item[9]) for item in specialBuildings if item.progressionGroup is None]

    for item in buildings:
        #Skip t1 settlements and ports as they can only be built in razed settlements
        if ("settlement" in item.name or "port" in item.name) and item.tier == 0:
            continue
        else:
            locName = item.readableName
            locId = world.location_name_to_id[locName]

            location = TWW3Location(world.player, locName, locId, region)

            if item.tier > 0 and item.tier > world.options.starting_tier - 1 and not("settlement" in item.name):

                if world.options.progressive_buildings:
                    progressiveItemCount = item.tier - (world.options.starting_tier - 1)
                    for progBuilding in progBuildings:
                        if item.progressionGroup == progBuilding.name:
                            progressiveItem = progBuilding.readableName
                            #print(f"{item.readableName} requires {progressiveItemCount} x {progressiveItem}")
                            world.set_rule(location, Has(progressiveItem, progressiveItemCount))
                            #set_rule(location, lambda state, count=progressiveItemCount: state.has(progressiveItem, world.player, count))
                            break

                else:
                    requiredItems = {}
                    for building in buildings:
                        if building.progressionGroup == item.progressionGroup and world.options.starting_tier - 1 < building.tier <= item.tier:
                            #print(f"{item.readableName} requires {building.readableName} to be reachable")
                            requiredItems.update({building.readableName: 1})
                    #print(f"{location}: {requiredItems}")
                    world.set_rule(location, HasAllCounts(requiredItems))

            region.locations.append(location)

def createTechLocations(world: TWW3World) -> None:
    region = world.get_region("Techs")

    specialTechs = [item for key, item in factionItemManager.getSpecial(world, True) if
                        item.type == itemType.tech]
    techs = [item for key, item in factionItemManager.getTechs(world.playerFaction.race, False)]
    progTechs = [item for key, item in factionItemManager.getTechs(world.playerFaction.race, True)]
    techs += [itemData(*item[:2], *item[3:6], item[6], item[9]) for item in specialTechs if item.progressionGroup is not None]
    progTechs += [itemData(*item[:2], *item[3:6], item[6], item[9]) for item in specialTechs if item.progressionGroup is None]

    for item in techs:
        locName = item.readableName
        locId = world.location_name_to_id[locName]

        location = TWW3Location(world.player, locName, locId, region)

        if item.tier > 1 and item.tier > world.options.starting_tier:

            if world.options.progressive_technologies:
                progressiveItemCount = item.tier - world.options.starting_tier
                for progTech in progTechs:
                    if item.progressionGroup == progTech.name:
                        progressiveItem = progTech.readableName
                        world.set_rule(location, Has(progressiveItem, progressiveItemCount))
                        break

                else:
                    world.set_rule(location, Has(locName))
                    world.set_rule(location, world.sanityRules.getTechRules(location)) #Get Specific Rules if they exist
                    """requiredItems = {}
                    for tech in techs:
                        if tech.progressionGroup == item.progressionGroup and world.options.starting_tier < tech.tier <= item.tier:
                            # print(f"{item.readableName} requires {building.readableName} to be reachable")
                            requiredItems.update({tech.readableName: 1})
                    # print(f"{location}: {requiredItems}")
                    world.set_rule(location, HasAllCounts(requiredItems))"""

        region.locations.append(location)

def createRitualLocations(world: TWW3World) -> None:
    region = world.get_region("Rituals")
    rituals = [item for key, item in factionItemManager.getRituals(world)]

    for item in rituals:
        locName = item.readableName
        locId = world.location_name_to_id[locName]

        location = TWW3Location(world.player, locName, locId, region)

        if item.tier > 1 and not item.spcLogic:# and item.tier > world.options.starting_tier:
            #requiredItems = {}
            for ritual in rituals:
                if ritual.progressionGroup == item.progressionGroup and ritual.tier == 1 and (ritual.tier < item.tier or ritual.readableName == item.readableName):
                    #requiredItems.update({ritual.readableName: 1})
                    world.set_rule(location, HasAllCounts(ritual.readableName))
                    break



        region.locations.append(location)