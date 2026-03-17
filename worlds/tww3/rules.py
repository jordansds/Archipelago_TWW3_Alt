from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from worlds.tww3.world import TWW3World
from BaseClasses import ItemClassification
import math
from worlds.generic.Rules import add_rule, set_rule
from worlds.tww3.item_tables.progression_table import progressionDict
from collections import Counter

def setVictoryEvent(world: TWW3World) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)

    if world.options.game_mode == "spheres":
        worldRegion = world.get_region("Settlements")
        victoryLocation = [location for location in worldRegion.locations if location.name == "Victory"][0]

        set_rule(victoryLocation, lambda state: state.has("Orb of Domination", world.player, world.options.orb_count))

def setBalance(world: TWW3World) -> None:
    if world.options.force_early_units or world.options.force_early_buildings or world.options.force_early_techs:
        worldRegion = world.get_region("Settlements")

        world.item_name_groups.update({"Unlocks": set()})
        #The counter that will determine the maximum number of items that can be prioritised
        counter = 0
        for item in world.multiworld.itempool:
            if item.classification == ItemClassification.progression and item.player == world.player:
                # Check if the item is in progression_table (to prevent strange logic around the progression items)
                if not item.name in [item[1][2] for item in progressionDict.items()]:
                    world.item_name_groups["Unlocks"].add(item.name)
                    counter += 1

        if world.options.game_mode == "conquest":
            for index, location in enumerate(worldRegion.locations):
                #This increments by 1 every 5 empire size in locations. E.g. Empire size 10 = 2, empire size 30 = 6
                empireSizeInterval = math.floor(index / (world.options.admin_capacity * world.options.checks_per_settlement))
                # This sets the weighting for the item balancing.
                # The -1 ensures space is left for the admin capacity items.
                weight = world.options.checks_per_settlement * world.options.admin_capacity * world.options.balance / 100
                requiredUnlockItems = min(empireSizeInterval * weight, counter)
                #print(f"{location}: {requiredUnlockItems}")
                add_rule(location, lambda state, count=requiredUnlockItems: state.has_group("Unlocks", world.player, count))

        elif world.options.game_mode == "spheres":

            settlementDiploRange, factionDiploRange = world.settlementManager.getRequiredDiploRange(world.options.sphere_count, world.options.sphere_radius)

            #Number of settlements contained within each diplo range
            settlementsPerDiploRange = [value for key, value in sorted(Counter(settlementDiploRange).items())]

            #Number of items to assign to the locations within each diplo range
            itemsPerDiploRange = [int(settlement * world.options.balance / 100) for settlement in settlementsPerDiploRange]

            settlementToDiploRange = [settlement.readableName for settlement in world.settlementManager.shuffledSettlementDict.values()]
            settlementToDiploRange = {settlementToDiploRange[i]: count for i, count in enumerate(settlementDiploRange) if count <= world.options.sphere_count}

            for locationName, requiredDiploRange in settlementToDiploRange.items():
                if requiredDiploRange > 0:
                    for i in range(world.options.checks_per_settlement):
                        location = world.get_location(f"{locationName} ({i})")
                        requiredUnlockItems = min(sum(itemsPerDiploRange[:requiredDiploRange]), counter)

                        add_rule(location, lambda state, count=requiredUnlockItems: state.has_group("Unlocks", world.player, count))
