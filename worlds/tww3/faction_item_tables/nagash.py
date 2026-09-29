from BaseClasses import ItemClassification as IC
from worlds.tww3.dataStructs import itemType, itemData, specialItemData
# @formatter:off
units: dict[int, itemData] = {}

buildings: dict[int, itemData] = {}

techs: dict[int, itemData] = {}

progUnits: dict[int, itemData] = {}

progBuildings: dict[int, itemData] = {}

progTechs: dict[int, itemData] = {}

special: dict[int, specialItemData] = {}

rituals: dict[int, specialItemData] = {}