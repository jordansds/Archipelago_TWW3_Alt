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
    world.set_rule(location, Has("Key", 9))

    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)

def setKeyRule(world: TWW3World, locations, i):
    for location in locations:
        world.set_rule(location, Has("Key", i-1))


def setGenericLocationRule(world: TWW3World, location, i: int, maxCheck: int):
    world.set_rule(location, Has("Key", (i+1) * 8 // maxCheck))

def setBuildingLocationRules(world: TWW3World, buildings):

    specialBuildings = [item for key, item in factionItemManager.getSpecial(world, True) if
                        item.type == itemType.building]
    progBuildings = [item for key, item in factionItemManager.getBuildings(world.playerFaction.race, True)]
    progBuildings += [itemData(*item[:2], *item[3:6], item[6], item[9]) for item in specialBuildings if item.progressionGroup is None]

    for item in buildings:
        if ("resource" in item.name or "port" in item.name or "allied" in item.name
                or "settlement" in item.progressionGroup or "horde_main" in item.progressionGroup):
            world.get_location(item.readableName).progress_type = LocationProgressType.EXCLUDED

        if item.tier > world.options.starting_tier - 1 and not("settlement" in item.name or "settlement" in item.progressionGroup):

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
                itemCount = item.tier if item.tier <= 3 else item.tier + 2

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
    for item in rituals:
        rule = True_()
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

        world.item_name_groups.update({"Unlocks": set()})
        #The counter that will determine the maximum number of items that can be prioritised
        counter = 0
        for item in world.multiworld.itempool:
            if item.classification == ItemClassification.progression and item.player == world.player:
                # Check if the item is in progression_table (to prevent strange logic around the progression items)
                if not item.name in [progItem.readableName for progItem in progressionDict.values()]:
                    world.item_name_groups["Unlocks"].add(item.name)
                    counter += 1

        for index, location in enumerate(world.get_region("Keys").locations):
            # Should have access to all items by the 9th key
            requiredItems = len(world.item_name_groups["Unlocks"]) * min(1, (index // 6) / 8)
            if requiredItems > 0:
                world.set_rule(location, HasGroup("Unlocks", requiredItems) | Has("Glitch Logic"))

        if requiredItems > 0:
            location = world.get_location("Victory")
            world.set_rule(location, HasGroup("Unlocks", requiredItems) | Has("Glitch Logic"))
