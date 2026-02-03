from .item_types import ItemType, ItemData
from BaseClasses import ItemClassification as IC

progressionDict: dict[int, ItemData] = {
   1000: ItemData(IC.progression, 0, "Administrative Capacity", ItemType.progression, "None", None, None),
   1001: ItemData(IC.progression, 0, "Diplomatic Range", ItemType.progression, "None", None, None),
   1002: ItemData(IC.progression, 0, "Orb of Domination", ItemType.goal, "None", None, None)
}
