from typing import NamedTuple
from enum import IntEnum
from BaseClasses import ItemClassification

class itemType(IntEnum):
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

class itemData(NamedTuple):
    classification: ItemClassification
    count: int
    name: str
    type: itemType
    tier: int
    progressionGroup: str
    readableName: str

class specialItemData(NamedTuple):
    classification: ItemClassification
    count: int
    faction: str
    name: str
    type: itemType
    tier: int
    progressionGroup: str
    forceEarly: bool
    isProgressiveItem: bool
    readableName: str

class modItemData(NamedTuple):
    classification: ItemClassification
    count: int
    race: str
    faction: str
    name: str
    type: itemType
    tier: int
    progressionGroup: str
    readableName: str

class factionData(NamedTuple):
    name: str
    isPlayable: bool
    hasHome: bool
    race: str
    readableName: str
    isHorde: bool

class settlementData(NamedTuple):
    name: str
    type: str
    x: int
    y: int
    faction: str
    climate: str
    readableName: str


#Progression items: 1000
#Goal items: 1100
#Filler items: 1200, 1300, 1400, 1500, 1600
#Ancillaries: 2000, 2500


