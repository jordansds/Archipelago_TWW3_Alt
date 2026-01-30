from typing import NamedTuple
from enum import IntEnum
from BaseClasses import ItemClassification


class ItemType(IntEnum):
    tech = 1
    building = 2
    unit = 3
    goal = 4
    filler_weak = 5
    filler_strong = 6
    trap_harmless = 7
    trap_weak = 8
    trap_strong = 9
    progression = 10
    effect_character = 11
    effect_faction = 12
    effect_force = 13
    effect_province = 14
    effect_region = 15
    ancillaries_regular = 16
    ancillaries_legendary = 17
    ritual = 18

class ItemData(NamedTuple):
    classification: ItemClassification
    count: int
    name: str
    type: ItemType
    faction: str
    tier: int
    progressionGroup: str