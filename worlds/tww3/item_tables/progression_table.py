from .item_types import ItemType, ItemData
from BaseClasses import ItemClassification as IC

progressionDict: dict[int, ItemData] = {
   1000: ItemData(IC.progression, 0, "None", ItemType.progression, None, "None", "Administrative Capacity"),
   1001: ItemData(IC.progression, 0, "None", ItemType.progression, None, "None", "Diplomatic Range"),
   1100: ItemData(IC.progression, 0, "None", ItemType.goal, None, "None", "Orb of Domination")
}