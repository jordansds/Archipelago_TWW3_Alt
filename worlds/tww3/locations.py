from __future__ import annotations
from typing import TYPE_CHECKING

from . import settlementManager as sm

if TYPE_CHECKING:
    from .world import TWW3World

from BaseClasses import Location, ItemClassification
from worlds.generic.Rules import set_rule
from . import items
import math

class TWW3Location(Location):
    game = "Total War Warhammer 3"
    
def createAllLocations(world: TWW3World) -> None:

    if world.options.game_mode == "conquest":
        createRegularLocations(world)

    elif world.options.game_mode == "spheres":
        createDiploRangeLocations(world)

    createEvents(world)
    
def createRegularLocations(world: TWW3World) -> None:
    worldRegion = world.get_region("Old World")
    # Check if player has starting regions. If they do, then skip the player's starting settlements to prevent the game from fulfilling checks before game start.
    startingCheck = world.options.starting_settlements + 1
    if world.playerFaction.name in sm.trueHordeList:
        startingCheck = 1
    # Generate all but last location, which is saved for the victory event
    # Fill location checks based on number of locations and checks per location
    for i in range(startingCheck, world.options.number_of_settlements):
        for j in range(world.options.checks_per_settlement):
            locName = f"Empire Size {i} ({j})"
            
            locId = world.location_name_to_id[locName]
            location = TWW3Location(world.player, locName, locId, worldRegion)

            #if i > startingCheck:
            #    location.access_rule = lambda state: state.can_reach(f"Empire Size {i-1} (0)", locName, world.player)

            requiredAdminCapacity = max(0, math.floor(i / world.options.admin_capacity) - 1)
            set_rule(location, lambda state: state.has("Administrative Capacity", world.player, requiredAdminCapacity))

            worldRegion.locations.append(location)

def createEvents(world: TWW3World) -> None:
    worldRegion = world.get_region("Old World")
    if world.options.game_mode == "conquest":
        # Add victory event in the last location
        locName = f"Empire Size {world.options.number_of_settlements}"
        location = TWW3Location(world.player, locName, None, worldRegion)
        count = math.floor(world.options.number_of_settlements / world.options.admin_capacity) - 1
        set_rule(location, lambda state: state.has("Administrative Capacity", world.player, count))

    elif world.options.game_mode == "spheres":
        location = TWW3Location(world.player, "Victory", None, worldRegion)

    worldRegion.locations.append(location)
    # Create Victory item and place it in the last location
    victory = items.TWW3Item("Victory", ItemClassification.progression, None, world.player)
    location.place_locked_item(victory)

def createDiploRangeLocations(world: TWW3World) -> None:
    worldRegion = world.get_region("Old World")

    settlementDiploRange, factionDiploRange = world.settlementManager.getRequiredDiploRange(world.options.sphere_count, world.options.sphere_radius)

    for key, settlement in world.settlements.items():
        locId = world.location_name_to_id[settlement.name]
        location = TWW3Location(world.player, settlement.name, locId, worldRegion)

        if settlementDiploRange[key] == 0:
            worldRegion.locations.append(location)
            print(location)

        elif 0 < settlementDiploRange[key] <= world.options.sphere_count:
            if settlement.faction != world.playerFaction.name:
                set_rule(location,
                         lambda state: state.has("Diplomatic Range", world.player, settlementDiploRange[key]))
                worldRegion.locations.append(location)



