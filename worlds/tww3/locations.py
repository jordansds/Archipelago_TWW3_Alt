from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .world import TWW3World

from BaseClasses import Location, ItemClassification
from worlds.generic.Rules import add_rule
from . import items
from . import rules
import math

class TWW3Location(Location):
    game = "Total War Warhammer 3"
    
def createAllLocations(world: TWW3World) -> None:
    
    createRegularLocations(world)
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
            add_rule(location, lambda state, count=requiredAdminCapacity: state.has("Administrative Capacity", world.player, count))
            worldRegion.locations.append(location)

def createEvents(world: TWW3World) -> None:
    worldRegion = world.get_region("Old World")
    
    # Add victory event in the last location
    locName = f"Empire Size {world.options.number_of_settlements}"

    location = TWW3Location(world.player, locName, None, worldRegion)
    add_rule(location, lambda state, count=math.floor(world.options.number_of_settlements / world.options.admin_capacity) - 1: state.has("Administrative Capacity", world.player, count))
    #print(f"{locName}: {math.floor(world.options.number_of_locations/5) - 1}")
    worldRegion.locations.append(location)  
    
    # Create Victory item and place it in the last location
    victory = items.TWW3Item("Victory", ItemClassification.progression, None, world.player)
    location.place_locked_item(victory)
    
    rules.setVictoryEvent(world)
    