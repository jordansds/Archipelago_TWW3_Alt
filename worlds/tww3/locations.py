from __future__ import annotations
from typing import TYPE_CHECKING

from worlds.oot import location_name_to_id
from worlds.tww3.dataStructs import itemType, itemData

if TYPE_CHECKING:
    from worlds.tww3.world import TWW3World

from BaseClasses import Location, ItemClassification as IC
from rule_builder.rules import Has
from worlds.tww3 import items, rules, factionItemManager
from worlds.tww3.item_tables import factions as fm
from worlds.generic.Rules import forbid_item

class TWW3Location(Location):
    game = "Total War Warhammer III"
    
def createAllLocations(world: TWW3World) -> None:
    createKeyLocations(world)
    createVictoryLocation(world)

    if world.options.sanity:
        createBuildingLocations(world, True)
        if not world.options.fast_research:
            createTechLocations(world)
        if world.options.ritual_sanity:
            createRitualLocations(world)
        #Run a second pass where we grab the locations that we couldn't risk generating the first time and lock them to filler items
        #In case of generation issues E.g. Ports in Spheres mode.
        createBuildingLocations(world, False)

    if world.options.conquerer_sanity:
        createConquererLocations(world)

    if world.options.battle_sanity:
        createBattleLocations(world)

    if world.options.despoiler_sanity:
        createDespoilerLocations(world)

def createVictoryLocation(world: TWW3World) -> None:
    worldRegion = world.get_region("Keys")

    location = TWW3Location(world.player, "Victory", None, worldRegion)
    worldRegion.locations.append(location)

    victory = items.TWW3Item("Victory", IC.progression, None, world.player)
    location.place_locked_item(victory)

    rules.setVictoryRule(world, location)

def createKeyLocations(world: TWW3World) -> None:
    worldRegion = world.get_region("Keys")

    keys = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th"]
    for index, key in enumerate(keys):
        #locName = world.settlementRandomiser.getSettlementWithinRange(i)
        locName = f"The {key} Key"
        locId = world.location_name_to_id[locName]
        location = TWW3Location(world.player, locName, locId, worldRegion)
        worldRegion.locations.append(location)
        locations = [location]

        #Add 5 items that spawn in each key location as a reward
        for j in range(5):
            locName = f"The {key} Key: Item {j+1}"
            locId = world.location_name_to_id[locName]
            location = TWW3Location(world.player, locName, locId, worldRegion)
            worldRegion.locations.append(location)
            locations.append(location)

        rules.setKeyRule(world, locations, index)

def createBuildingLocations(world: TWW3World, firstPass: bool) -> None:
    region = world.get_region("Buildings")

    specialBuildings = [item for key, item in factionItemManager.getSpecial(world, True) if
                        item.type == itemType.building]
    buildings = [item for key, item in factionItemManager.getBuildings(world.playerFaction.race, False)]
    buildings += [itemData(*item[:2], *item[3:6], item[6], item[9]) for item in specialBuildings if item.progressionGroup is not None]

    #Remove allied outposts
    #buildings = [building for building in buildings if not "allied" in building.name]

    if firstPass:
        # Remove t1 settlements and ports as they can only be built in razed settlements
        buildings = [building for building in buildings if
                     not ("settlement" in building.name
                          or "port" in building.name
                          or "settlement" in building.progressionGroup
                          or "horde_main" in building.progressionGroup)]

    buildings = [building for building in buildings if not "allied" in building.name] #remove allied outposts for now

    for item in buildings:
        locName = item.readableName
        locId = world.location_name_to_id[locName]

        #Check if we already generated this building
        try:
            location = world.multiworld.get_location(locName, world.player)
        except KeyError:
            location = TWW3Location(world.player, locName, locId, region)

            region.locations.append(location)

    if not firstPass:
        rules.setBuildingLocationRules(world, buildings)

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

minCheck, maxCheck = 1, 21

def createBattleLocations(world: TWW3World) -> None:
    worldRegion = world.get_region("Battles")

    for i in range(minCheck, maxCheck):
        locName = f"Won {i*5} Battles"
        locId = world.location_name_to_id[locName]
        location = TWW3Location(world.player, locName, locId, worldRegion)

        rules.setGenericLocationRule(world, location, i, maxCheck) #Hard logic handled on client

        worldRegion.locations.append(location)

def createDespoilerLocations(world: TWW3World) -> None:
    worldRegion = world.get_region("Despoiler")

    for i in range(minCheck, maxCheck):
        for decision in ["Sacked", "Razed"]:
            locName = f"{decision} {i*2} Settlements"
            locId = world.location_name_to_id[locName]
            location = TWW3Location(world.player, locName, locId, worldRegion)

            rules.setGenericLocationRule(world, location, i, maxCheck) #Hard logic handled on client

            worldRegion.locations.append(location)

def createConquererLocations(world: TWW3World) -> None:
    worldRegion = world.get_region("Empire")

    # Check if player has starting regions. If they do, then skip the player's starting settlements to prevent the game from fulfilling checks before game start.
    if world.playerFaction.name == "wh3_dlc24_tze_the_deceivers":
        startingCheck = 2
    elif world.playerFaction.name in fm.hordeList:
        startingCheck = 1
    else:
        startingCheck = world.options.starting_settlements + 1

    # Fill location checks based on number of locations and checks per location
    for i in range(startingCheck, maxCheck):
        locName = f"Empire Size {i})"
        locId = world.location_name_to_id[locName]
        location = TWW3Location(world.player, locName, locId, worldRegion)

        rules.setGenericLocationRule(world, location, i, maxCheck)  # Hard logic handled on client

        worldRegion.locations.append(location)