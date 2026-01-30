from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .world import TWW3World
from BaseClasses import ItemClassification
import math
from worlds.generic.Rules import add_rule
from .item_tables.progression_table import progression_table

def setVictoryEvent(world: TWW3World) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)

def setBalance(world: TWW3World) -> None:
    if world.options.force_early_units or world.options.force_early_buildings or world.options.force_early_techs:
        worldRegion = world.get_region("Old World")

        world.item_name_groups = {
            "Unlocks": set()
        }
        #The counter that will determine the maximum number of items that can be prioritised
        counter = 0
        for item in world.multiworld.itempool:
            if item.classification == ItemClassification.progression and item.player == world.player:
                # Check if the item is in progression_table (to prevent strange logic around the progression items)
                if not item.name in [item[1][2] for item in progression_table.items()]:
                    world.item_name_groups["Unlocks"].add(item.name)
                    counter += 1

        for index, location in enumerate(worldRegion.locations):
            #This increments by 1 every 5 empire size in locations. E.g. Empire size 10 = 2, empire size 30 = 6
            empireSizeInterval = math.floor(index / (world.options.admin_capacity * world.options.checks_per_settlement))
            # This sets the weighting for the item balancing.
            # The -1 ensures space is left for the admin capacity items.
            weight = world.options.checks_per_settlement * world.options.admin_capacity * world.options.balance / 100 - 1
            requiredUnlockItems = min(empireSizeInterval * weight, counter)
            #print(f"{location}: {requiredUnlockItems}")
            add_rule(location, lambda state, count=requiredUnlockItems: state.has_group("Unlocks", world.player, count))
