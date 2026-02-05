from BaseClasses import ItemClassification as IC
from typing import Dict

from .item_types import ItemType, ItemData

factionItemDict: Dict[int, ItemData] = {
    4000: ItemData(IC.progression, 88, "wh2_dlc09_ritual_crafting_tmb_army_capacity_25", ItemType.effect_faction, None, "None", "None")
}