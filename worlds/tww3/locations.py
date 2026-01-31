from __future__ import annotations
from typing import TYPE_CHECKING

from .locations_table.settlements import settlementTable, lordToFactionDict

if TYPE_CHECKING:
    from .world import TWW3World

from BaseClasses import Location, ItemClassification
from worlds.generic.Rules import set_rule
from . import items
import math

class TWW3Location(Location):
    game = "Total War Warhammer 3"
    
def createAllLocations(world: TWW3World, locationToDiploRange) -> None:

    if world.options.game_mode == "conquest":
        createRegularLocations(world)

    elif world.options.game_mode == "spheres":
        createDiploRangeLocations(world, locationToDiploRange)

    createEvents(world)
    
def createRegularLocations(world: TWW3World) -> None:
    worldRegion = world.get_region("Old World")
    # Check if player has a starting region. If they do, then skip the first few checks to prevent the game from fulfilling checks before game start.
    # If the player is really lucky and starts with more than 4 settlements, then they will still autocomplete some checks, but not as many.    
    startingCheck = 5
    for horde in world.horde_table.items():
        if horde[1] == world.player_faction:
            startingCheck = 1
    
    # Generate all but last location, which is saved for the victory event
    # Fill location checks based on number of locations and checks per location
    for i in range(startingCheck, world.options.number_of_settlements):
        for j in range(world.options.checks_per_settlement):
            locName = f"Empire Size {i} ({j})"
            
            locId = world.location_name_to_id[locName]
            location = TWW3Location(world.player, locName, locId, worldRegion)

            requiredAdminCapacity = max(0, math.floor(i / world.options.admin_capacity) - 1)
            set_rule(location, lambda state, count=requiredAdminCapacity: state.has("Administrative Capacity", world.player, count))
            worldRegion.locations.append(location)

def createEvents(world: TWW3World) -> None:
    worldRegion = world.get_region("Old World")
    if world.options.game_mode == "conquest":
        # Add victory event in the last location
        locName = f"Empire Size {world.options.number_of_settlements}"

        location = TWW3Location(world.player, locName, None, worldRegion)
        set_rule(location, lambda state, count=math.floor(world.options.number_of_settlements / world.options.admin_capacity) - 1: state.has("Administrative Capacity", world.player, count))
        #print(f"{locName}: {math.floor(world.options.number_of_locations/5) - 1}")
        worldRegion.locations.append(location)

        # Create Victory item and place it in the last location
        victory = items.TWW3Item("Victory", ItemClassification.progression, None, world.player)
        location.place_locked_item(victory)

    elif world.options.game_mode == "spheres":

        location = TWW3Location(world.player, "Victory", None, worldRegion)
        worldRegion.locations.append(location)

        victory = items.TWW3Item("Victory", ItemClassification.progression, None, player=world.player)
        location.place_locked_item(victory)

#In Spheres mode, the range in which you can interact with each location is set by the number of diplomatic range items you own.
#This dictionary contains each location, and the number of range items you need to be able to interact with the faction.
#will be used to set balancing in rules.py if balancing is enabled

def createDiploRangeLocations(world: TWW3World, locationToDiploRange) -> None:
    worldRegion = world.get_region("Old World")

    for location in settlementTable:
        locId = world.location_name_to_id[location[0]]
        location = TWW3Location(world.player, location[0], locId, worldRegion)

        faction: str = world.settlementManager.settlementToFaction(location.name)
        requiredDiploRange: int = int(world.settlementManager.getDistance(faction) / world.options.sphere_radius)

        if requiredDiploRange == 0:
            worldRegion.locations.append(location)

        elif 0 < requiredDiploRange < world.options.sphere_count:
            if faction != lordToFactionDict[world.options.starting_faction]:
                set_rule(location, lambda state, spheres=requiredDiploRange: state.has("Diplomatic Range", world.player, spheres))
                locationToDiploRange[location] = requiredDiploRange
                worldRegion.locations.append(location)
