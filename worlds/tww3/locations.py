from __future__ import annotations
from typing import TYPE_CHECKING

from worlds.tww3.itemTypes import itemType, itemData

if TYPE_CHECKING:
    from worlds.tww3.world import TWW3World

from BaseClasses import Location, ItemClassification as IC
from rule_builder.rules import Has, HasAllCounts
from worlds.tww3 import items, factionItemManager, settlementManager as sm
import math

class TWW3Location(Location):
    game = "Total War Warhammer III"
    
def createAllLocations(world: TWW3World) -> None:

    if world.options.game_mode == "conquest":
        createRegularLocations(world)

    elif world.options.game_mode == "spheres":
        createDiploRangeLocations(world)

    if world.options.sanity:
        createBuildingLocations(world)
        createTechLocations(world)

    if world.options.ritual_sanity:
        createRitualLocations(world)

    createVictoryLocation(world)
    
def createRegularLocations(world: TWW3World) -> None:
    worldRegion = world.get_region("Settlements")
    # Check if player has starting regions. If they do, then skip the player's starting settlements to prevent the game from fulfilling checks before game start.
    if world.playerFaction.name in sm.hordeList:
        startingCheck = 1
    else:
        startingCheck = world.options.starting_settlements + 1
    # Generate all but last location, which is saved for the victory event
    # Fill location checks based on number of locations and checks per location
    for i in range(startingCheck, world.options.number_of_settlements):
        requiredAdminCapacity = math.floor(i / world.options.admin_capacity)
        for j in range(world.options.checks_per_settlement):
            locName = f"Empire Size {i} ({j})"
            
            locId = world.location_name_to_id[locName]
            location = TWW3Location(world.player, locName, locId, worldRegion)

            #max(0, math.floor(i / world.options.admin_capacity))
            #set_rule(location, lambda state: state.has("Administrative Capacity", world.player, requiredAdminCapacity))
            #set_rule(location, lambda state, count=requiredAdminCapacity: state.has("Administrative Capacity", world.player, count))
            world.set_rule(location, Has("Administrative Capacity", requiredAdminCapacity))

            worldRegion.locations.append(location)

def createDiploRangeLocations(world: TWW3World) -> None:
    worldRegion = world.get_region("Settlements")

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
                #set_rule(location, lambda state, count=settlementDiploRange[key]: state.has("Diplomatic Range", world.player, count))
                world.set_rule(location, Has("Diplomatic Range", settlementDiploRange[key]))
                worldRegion.locations.append(location)

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

            if item.tier > world.options.starting_tier - 1 and not("settlement" in item.name):

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

        if world.options.progressive_technologies:
            for progTech in progTechs:
                if item.progressionGroup == progTech.name:
                    world.set_rule(location, Has(progTech.readableName, item.tier))
                    break
        else:
            world.set_rule(location, Has(locName))
        try:
            world.set_rule(location, world.sanityRules.getTechRules(location)) #Get Specific Rules if they exist
        except KeyError:
            pass

        region.locations.append(location)

def createRitualLocations(world: TWW3World) -> None:
    region = world.get_region("Rituals")
    rituals = [item for key, item in factionItemManager.getRituals(world)]

    for item in rituals:
        locName = item.readableName
        locId = world.location_name_to_id[locName]

        location = TWW3Location(world.player, locName, locId, region)

        for ritual in rituals:
            if ritual.progressionGroup == item.progressionGroup and ritual.tier == 1 and (ritual.tier <= item.tier or ritual.readableName == item.readableName) and not ritual.spcLogic:
                #requiredItems.update({ritual.readableName: 1})
                world.set_rule(location, Has(ritual.readableName))
                try:
                    world.set_rule(location, world.sanityRules.getRitualRules(location))
                except KeyError:
                    pass

        region.locations.append(location)

def createVictoryLocation(world: TWW3World) -> None:
    worldRegion = world.get_region("Settlements")

    if world.options.game_mode == "conquest":
        location = TWW3Location(world.player, f"Empire Size {world.options.number_of_settlements}", None, worldRegion)
        world.set_rule(location, Has("Administrative Capacity", math.floor(world.options.number_of_settlements / world.options.admin_capacity) - 1))

    elif world.options.game_mode == "spheres":
        location = TWW3Location(world.player, "Victory", None, worldRegion)
        world.set_rule(location, Has("Orb of Domination", world.options.orb_count.value))

    worldRegion.locations.append(location)
    victory = items.TWW3Item("Victory", IC.progression, None, world.player)
    location.place_locked_item(victory)
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)