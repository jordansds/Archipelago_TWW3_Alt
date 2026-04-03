from worlds.tww3.dataStructs import itemType, itemData
from BaseClasses import ItemClassification as IC

progressionDict: dict[int, itemData] = {
   1000: itemData(IC.progression, 0, "None", itemType.progression, None, "None", "Administrative Capacity"),
   1001: itemData(IC.progression, 0, "None", itemType.progression, None, "None", "Diplomatic Range"),
   1100: itemData(IC.progression, 0, "None", itemType.goal, None, "None", "Orb of Domination")
}