from BaseClasses import ItemClassification as IC
from item_types import ItemType, ItemData
# @formatter:off
units: dict[int, ItemData] = {}
buildings: dict[int, ItemData] = {}
techs: dict[int, ItemData] = {}

progUnits: dict[int, ItemData] = {}
progBuildings: dict[int, ItemData] = {}
progTechs: dict[int, ItemData] = {}

special: dict[int, ItemData] = {}