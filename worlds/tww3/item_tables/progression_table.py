from worlds.tww3.dataStructs import itemType, itemData
from BaseClasses import ItemClassification as IC

progressionDict: dict[int, itemData] = {
   1000: itemData(IC.progression, 0, "Key", itemType.progression, None, None, "Key"),
   1001: itemData(IC.progression, 0, "Map", itemType.progression, None, None, "Map"),
}