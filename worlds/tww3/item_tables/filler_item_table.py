from BaseClasses import ItemClassification as IC

from .item_types import ItemType, ItemData
fillerWeakDict: dict[int, ItemData] = {
    1200: ItemData(IC.filler, 0, "Get-Rich-Quick Scroll", ItemType.filler_weak, None, "None", "None"),
    1201: ItemData(IC.filler, 0, "Something Happened", ItemType.filler_weak, None, "None", "None"),
    1202: ItemData(IC.filler, 0, "Handful of Order", ItemType.filler_weak, None, "None", "None"),
    1203: ItemData(IC.filler, 0, "Something Thingy", ItemType.filler_weak, None, "None", "None"),
    1204: ItemData(IC.filler, 0, "The GroBro 3000", ItemType.filler_weak, None, "None", "None")
}

fillerStrongDict: dict[int, ItemData] = {
    1300: ItemData(IC.filler, 0, "Give me that", ItemType.filler_strong, None, "None", "None"),
    1301: ItemData(IC.filler, 0, "Make Love, Not War", ItemType.filler_strong, None, "None", "None"),
    1302: ItemData(IC.filler, 0, "Something Shiny", ItemType.filler_strong, None, "None", "None")
}

trapHarmlessDict: dict[int, ItemData] = {
    1400: ItemData(IC.trap, 0, "Look! What\'s that?", ItemType.trap_harmless, None, "None", "None"),
    1401: ItemData(IC.trap, 0, "Spoiler Alert!", ItemType.trap_harmless, None, "None", "None")
}

trapWeakDict: dict[int, ItemData] = {
    1500: ItemData(IC.trap, 0, "Handful of Unrest", ItemType.trap_weak, None, "None", "None"),
    1501: ItemData(IC.trap, 0, "Unionize This!", ItemType.trap_weak, None, "None", "None"),
    1502: ItemData(IC.trap, 0, "Where is our Map?", ItemType.trap_weak, None, "None", "None"),
    1503: ItemData(IC.trap, 0, "Schizophrenia!", ItemType.trap_weak, None, "None", "None")
}

trapStrongDict: dict[int, ItemData] = {
    1600: ItemData(IC.trap, 0, "Torches and Pitchforks!", ItemType.trap_strong, None, "None", "None"),
    1601: ItemData(IC.trap, 0, "Let's trade!", ItemType.trap_strong, None, "None", "None"),
    1602: ItemData(IC.trap, 0, "You too, Brutus?", ItemType.trap_strong, None, "None", "None")
}