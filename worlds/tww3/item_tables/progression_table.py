from .item_types import ItemType, ItemData
from BaseClasses import ItemClassification as IC

progression_table: dict[int, ItemData] = {
   1000: ItemData(IC.progression, 0, "Administrative Capacity", ItemType.progression, "None", None, None)
}