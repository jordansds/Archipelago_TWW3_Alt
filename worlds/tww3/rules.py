from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from worlds.tww3.world import TWW3World
from BaseClasses import ItemClassification, LocationProgressType
import math
from rule_builder.rules import HasGroup, Has, True_, False_, CanReachLocation
from worlds.tww3 import factionItemManager
from worlds.tww3.item_tables.progression_table import progressionDict
from worlds.tww3.dataStructs import itemType, itemData
from collections import Counter

def setVictoryRule(world: TWW3World, location):
    if world.options.game_mode == "conquest":
        rule = Has("Administrative Capacity", math.ceil(world.options.number_of_settlements / world.adminCapacity - 1))

    elif world.options.game_mode == "spheres":
        rule = Has("Orb of Domination", world.orbCount)

    world.set_rule(location, rule)

    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)

def setGenericLocationRule(world: TWW3World, location, i: int):
    rule = None
    if world.options.game_mode == "conquest":
        requiredAdminCapacity = math.floor(i / 20 * world.options.number_of_settlements / world.adminCapacity)
        if requiredAdminCapacity > 0:
            rule = Has("Administrative Capacity", requiredAdminCapacity)

    elif world.options.game_mode == "spheres":
        requiredDiploRange = math.floor(i / 20 * world.options.sphere_count)
        if requiredDiploRange > 0:
            rule = Has("Diplomatic Range", requiredDiploRange)

    if rule is not None:
        world.set_rule(location, rule)

def setBuildingLocationRules(world: TWW3World, buildings, firstPass: bool):

    specialBuildings = [item for key, item in factionItemManager.getSpecial(world, True) if
                        item.type == itemType.building]
    progBuildings = [item for key, item in factionItemManager.getBuildings(world.playerFaction.race, True)]
    progBuildings += [itemData(*item[:2], *item[3:6], item[6], item[9]) for item in specialBuildings if item.progressionGroup is None]

    for item in buildings:

        if world.options.game_mode == "spheres" and ("resource" in item.name or "port" in item.name):
            #if firstPass:
            #    continue
            #else:
            world.get_location(item.readableName).progress_type = LocationProgressType.EXCLUDED

        if item.tier > world.options.starting_tier - 1 and not("settlement" in item.name):

            rule = True_()
            if world.options.progressive_buildings:
                progressiveItemCount = item.tier - (world.options.starting_tier - 1)
                for progBuilding in progBuildings:
                    if item.progressionGroup == progBuilding.name:
                        progressiveItem = progBuilding.readableName
                        rule = rule & Has(progressiveItem, progressiveItemCount)
                        break

            else:
                for building in buildings:
                    if building.readableName == item.readableName and building.tier > world.options.starting_tier - 1:
                        rule = Has(building.readableName)
                        break

            if not world.options.hard_logic:
                if world.options.game_mode == "conquest":
                    rule = rule & Has("Administrative Capacity", max(0, item.tier - 2))

            world.set_rule(world.get_location(item.readableName), rule)

def setTechnologyLocationRules(world: TWW3World, techs):

    specialTechs = [item for key, item in factionItemManager.getSpecial(world, True) if
                    item.type == itemType.tech]
    progTechs = [item for key, item in factionItemManager.getTechs(world.playerFaction.race, True)]
    progTechs += [itemData(*item[:2], *item[3:6], item[6], item[9]) for item in specialTechs if item.progressionGroup is None]

    for item in techs:

        rule = True_()
        if world.options.progressive_technologies:
            for progTech in progTechs:
                if item.progressionGroup == progTech.name:
                    rule = rule & Has(progTech.readableName, item.tier)
                    break
        else:
            if item.tier > 0:
                rule = Has(item.readableName)
        try:
            rule = rule & world.sanityRules.getTechRules(item.readableName)
        except KeyError:
            pass

        try:
            world.set_rule(world.get_location(item.readableName), rule)
        except KeyError:
            world.set_rule(world.get_location(item.readableName), True_())
            world.get_location(item.readableName).progress_type = LocationProgressType.EXCLUDED

def setRitualRules(world: TWW3World, rituals: list):
    rule = True_()
    for item in rituals:
        locName = item.readableName

        for ritual in rituals:
            if ritual.progressionGroup == item.progressionGroup and ritual.tier == 1 and (
                    ritual.tier < item.tier or ritual.readableName == item.readableName) and not ritual.spcLogic:
                rule = rule & Has(ritual.readableName)
        try:
            rule = rule & world.sanityRules.getRitualRules(locName)
        except KeyError:
            pass

        try:
            world.set_rule(world.get_location(item.readableName), rule)
        except KeyError:
            world.set_rule(world.get_location(item.readableName), True_())
            world.get_location(item.readableName).progress_type = LocationProgressType.EXCLUDED

def setBalance(world: TWW3World) -> None:
        worldRegion = world.get_region("Settlements")

        world.item_name_groups.update({"Unlocks": set()})
        #The counter that will determine the maximum number of items that can be prioritised
        counter = 0
        for item in world.multiworld.itempool:
            if item.classification == ItemClassification.progression and item.player == world.player:
                # Check if the item is in progression_table (to prevent strange logic around the progression items)
                if not item.name in [progItem.name for progItem in progressionDict.values()]:
                    world.item_name_groups["Unlocks"].add(item.name)
                    counter += 1

        if world.options.game_mode == "conquest":
            for index, location in enumerate(worldRegion.locations):
                #This increments by 1 every admin_capacity empire size in locations.
                empireSizeInterval = math.floor(index / (world.world.adminCapacity * world.options.checks_per_settlement))
                # This sets the weighting for the item balancing.
                weight = world.options.checks_per_settlement * world.world.adminCapacity * world.options.balance / 100
                requiredUnlockItems = min(empireSizeInterval * weight, counter)
                
                world.set_rule(location, HasGroup("Unlocks", requiredUnlockItems))

        elif world.options.game_mode == "spheres":

            #Number of settlements contained within each diplo range
            settlementsPerDiploRange = [value for key, value in sorted(Counter(world.settlementDiploRange).items())]

            #Number of items to assign to the locations within each diplo range
            itemsPerDiploRange = [int(settlement * world.options.balance / 100) for settlement in settlementsPerDiploRange]

            settlementToDiploRange = [settlement.readableName for settlement in world.settlementManager.shuffledSettlementDict.values()]
            settlementToDiploRange = {settlementToDiploRange[i]: count for i, count in enumerate(world.settlementDiploRange) if count <= world.options.sphere_count}

            for locationName, requiredDiploRange in settlementToDiploRange.items():
                if requiredDiploRange > 0:
                    for i in range(world.options.checks_per_settlement):
                        location = world.get_location(f"{locationName} ({i})")
                        requiredUnlockItems = min(sum(itemsPerDiploRange[:requiredDiploRange]), counter)

                        #add_rule(location, lambda state, count=requiredUnlockItems: state.has_group("Unlocks", world.player, count))
                        world.set_rule(location, HasGroup("Unlocks", requiredUnlockItems))
