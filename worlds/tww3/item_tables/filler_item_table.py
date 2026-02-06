from BaseClasses import ItemClassification as IC

from .item_types import ItemType, ItemData
fillerWeakDict: dict[int, ItemData] = {
    1200: ItemData(IC.filler, 0, "", ItemType.filler_weak, None, "None", "Get-Rich-Quick Scroll"),
    1201: ItemData(IC.filler, 0, "", ItemType.filler_weak, None, "None", "Something Happened"),
    1202: ItemData(IC.filler, 0, "", ItemType.filler_weak, None, "None", "Handful of Order"),
    1203: ItemData(IC.filler, 0, "", ItemType.filler_weak, None, "None", "Something Thingy"),
    1204: ItemData(IC.filler, 0, "", ItemType.filler_weak, None, "None", "The GroBro 3000")
}

fillerStrongDict: dict[int, ItemData] = {
    1300: ItemData(IC.filler, 0, "", ItemType.filler_strong, None, "None", "Give me that"),
    1301: ItemData(IC.filler, 0, "", ItemType.filler_strong, None, "None", "Make Love, Not War"),
    1302: ItemData(IC.filler, 0, "", ItemType.filler_strong, None, "None", "Something Shiny")
}

trapHarmlessDict: dict[int, ItemData] = {
    1400: ItemData(IC.trap, 0, "", ItemType.trap_harmless, None, "None", "Look! What's that?"),
    1401: ItemData(IC.trap, 0, "", ItemType.trap_harmless, None, "None", "Spoiler Alert!")
}

trapWeakDict: dict[int, ItemData] = {
    1500: ItemData(IC.trap, 0, "", ItemType.trap_weak, None, "None", "Handful of Unrest"),
    1501: ItemData(IC.trap, 0, "", ItemType.trap_weak, None, "None", "Unionize This!"),
    1502: ItemData(IC.trap, 0, "", ItemType.trap_weak, None, "None", "Where is our Map?"),
    1503: ItemData(IC.trap, 0, "", ItemType.trap_weak, None, "None", "Schizophrenia!")
}

trapStrongDict: dict[int, ItemData] = {
    1600: ItemData(IC.trap, 0, "", ItemType.trap_strong, None, "None", "Torches and Pitchforks!"),
    1601: ItemData(IC.trap, 0, "", ItemType.trap_strong, None, "None", "Let's trade!"),
    1602: ItemData(IC.trap, 0, "", ItemType.trap_strong, None, "None", "You too, Brutus?")
}