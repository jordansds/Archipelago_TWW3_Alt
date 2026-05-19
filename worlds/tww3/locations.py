from __future__ import annotations
from typing import TYPE_CHECKING

from worlds.tww3.dataStructs import itemType, itemData

if TYPE_CHECKING:
    from worlds.tww3.world import TWW3World

from BaseClasses import Location, ItemClassification as IC
from rule_builder.rules import Has
from worlds.tww3 import items, rules, factionItemManager, settlementManager as sm
import math
from worlds.generic.Rules import forbid_item

class TWW3Location(Location):
    game = "Total War Warhammer III"
    
def createAllLocations(world: TWW3World) -> None:
    createVictoryLocation(world)

    if world.options.game_mode == "conquest":
        createRegularLocations(world)

    elif world.options.game_mode == "spheres":
        createDiploRangeLocations(world)

    if world.options.sanity:
        createBuildingLocations(world, True)
        createTechLocations(world)
        if world.options.ritual_sanity:
            createRitualLocations(world)
        #Run a second pass where we grab the locations that we couldn't risk generating the first time and lock them to filler items
        #In case of generation issues E.g. Ports in Spheres mode.
        createBuildingLocations(world, False)

    if world.options.battle_sanity:
        createBattleLocations(world)

    if world.options.despoiler_sanity:
        createDespoilerLocations(world)

def createVictoryLocation(world: TWW3World) -> None:
    worldRegion = world.get_region("Settlements")

    location = TWW3Location(world.player, "Victory", None, worldRegion)
    worldRegion.locations.append(location)

    victory = items.TWW3Item("Victory", IC.progression, None, world.player)
    location.place_locked_item(victory)

    rules.setVictoryRule(world, location)

def createRegularLocations(world: TWW3World) -> None:
    worldRegion = world.get_region("Settlements")
    # Check if player has starting regions. If they do, then skip the player's starting settlements to prevent the game from fulfilling checks before game start.
    if world.playerFaction.name == "wh3_dlc24_tze_the_deceivers":
        startingCheck = 2
    elif world.playerFaction.name in sm.hordeList:
        startingCheck = 1
    else:
        startingCheck = world.options.starting_settlements + 1
    # Fill location checks based on number of locations and checks per location
    for i in range(startingCheck, world.options.number_of_settlements + 1):
        requiredAdminCapacity = math.floor(i / world.adminCapacity)
        for j in range(world.options.checks_per_settlement):
            locName = f"Empire Size {i} ({j})"
            
            locId = world.location_name_to_id[locName]
            location = TWW3Location(world.player, locName, locId, worldRegion)

            world.set_rule(location, Has("Administrative Capacity", requiredAdminCapacity))

            worldRegion.locations.append(location)

def createDiploRangeLocations(world: TWW3World) -> None:
    worldRegion = world.get_region("Settlements")

    for key, settlement in enumerate(world.settlements.values()):
        for i in range(world.options.checks_per_settlement):
            locId = world.location_name_to_id[f"{settlement.readableName} ({i})"]
            location = TWW3Location(world.player, f"{settlement.readableName} ({i})", locId, worldRegion)

            if world.settlementDiploRange[key] > world.options.sphere_count or settlement.faction == world.playerFaction.name:
                continue

            worldRegion.locations.append(location)
            if world.settlementDiploRange[key] > 0:
                world.set_rule(location, Has("Diplomatic Range", world.settlementDiploRange[key]))

                if world.settlementDiploRange[key] < world.options.sphere_count - 1:
                    forbid_item(location, "Orb of Domination", world.player)

def createBuildingLocations(world: TWW3World, firstPass: bool) -> None:
    region = world.get_region("Buildings")

    specialBuildings = [item for key, item in factionItemManager.getSpecial(world, True) if
                        item.type == itemType.building]
    buildings = [item for key, item in factionItemManager.getBuildings(world.playerFaction.race, False)]
    buildings += [itemData(*item[:2], *item[3:6], item[6], item[9]) for item in specialBuildings if item.progressionGroup is not None]


    if firstPass:
        # Remove t1 settlements and ports as they can only be built in razed settlements
        buildings = [building for building in buildings if not ("settlement" in building.name or "port" in building.name and building.tier == 0)]

    for item in buildings:
        locName = item.readableName
        locId = world.location_name_to_id[locName]

        if firstPass and world.options.game_mode == "spheres" and ("resource" in item.name or "port" in item.name):
            continue
        #Check if we already generated this building
        try:
            location = world.multiworld.get_location(locName, world.player)
            #location = TWW3Location(world.player, locName, locId, region)
            #region.locations.append(location)
        except KeyError:
            location = TWW3Location(world.player, locName, locId, region)
            region.locations.append(location)

    if not firstPass:
        rules.setBuildingLocationRules(world, buildings, firstPass)


def createTechLocations(world: TWW3World) -> None:
    region = world.get_region("Techs")
    specialTechs = [item for key, item in factionItemManager.getSpecial(world, True) if
                    item.type == itemType.tech]
    techs = [item for key, item in factionItemManager.getTechs(world.playerFaction.race, False)]
    techs += [itemData(*item[:2], *item[3:6], item[6], item[9]) for item in specialTechs if item.progressionGroup is not None]

    for item in techs:
        locName = item.readableName
        locId = world.location_name_to_id[locName]

        location = TWW3Location(world.player, locName, locId, region)

        region.locations.append(location)

    rules.setTechnologyLocationRules(world, techs)

def createRitualLocations(world: TWW3World) -> None:
    region = world.get_region("Rituals")
    rituals = [item for key, item in factionItemManager.getRituals(world)]

    for item in rituals:
        locId = world.location_name_to_id[item.readableName]

        location = TWW3Location(world.player, item.readableName, locId, region)

        region.locations.append(location)

    rules.setRitualRules(world, rituals)

def createBattleLocations(world: TWW3World) -> None:
    worldRegion = world.get_region("Battles")
    for i in range(1, 21):
        locName = f"Won {i*5} Battles"
        locId = world.location_name_to_id[locName]
        location = TWW3Location(world.player, locName, locId, worldRegion)

        rules.setGenericLocationRule(world, location, i) #Hard logic handled on client

        worldRegion.locations.append(location)

def createDespoilerLocations(world: TWW3World) -> None:
    worldRegion = world.get_region("Despoiler")
    for i in range(1, 21):
        for decision in ["Sacked", "Razed"]:
            locName = f"{decision} {i} Settlements"
            locId = world.location_name_to_id[locName]
            location = TWW3Location(world.player, locName, locId, worldRegion)

            rules.setGenericLocationRule(world, location, i) #Hard logic handled on client

            worldRegion.locations.append(location)