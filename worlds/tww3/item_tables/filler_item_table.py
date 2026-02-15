from BaseClasses import ItemClassification as IC

from ..faction_tables.item_types import ItemType, ItemData
fillerWeakDict: dict[int, ItemData] = {
    1200: ItemData(IC.filler, 0, 'cm:treasury_mod("%s", cm:random_number(10000,1))', ItemType.filler_weak, None, "None", "Get-Rich-Quick Scroll"), #Gold
    1201: ItemData(IC.filler, 0, "", ItemType.filler_weak, None, "None", "Something Happened"), #Random event - not currently included as most don't do anything
    1202: ItemData(IC.filler, 0, "set_random_positive_public_order()", ItemType.filler_weak, None, "None", "Handful of Order"), #Random amount of positive public order to random region
    1203: ItemData(IC.filler, 0, "", ItemType.filler_weak, None, "None", "Something Thingy"), #Random item/ancillary
    1204: ItemData(IC.filler, 0, "add_random_growth_to_player()", ItemType.filler_weak, None, "None", "The GroBro 3000") #Growth boost to random region
}

fillerStrongDict: dict[int, ItemData] = {
    1300: ItemData(IC.filler, 0, "force_settlement_transfer_from_random_enemy_to_player()", ItemType.filler_strong, None, "None", "Give me that"), #Gives player random enemy city
    1301: ItemData(IC.filler, 0, "", ItemType.filler_strong, None, "None", "Make Love, Not War"), #Makes random enemy an ally
    1302: ItemData(IC.filler, 0, "force_alliance_with_random_enemy()", ItemType.filler_strong, None, "None", "Something Shiny") #Random legendary item/ancillary
}

trapHarmlessDict: dict[int, ItemData] = {
    1400: ItemData(IC.trap, 0, "scroll_camera_to_random_region()", ItemType.trap_harmless, None, "None", "Look! What's that?"), #Moves map to random position
    1401: ItemData(IC.trap, 0, "play_random_movie()", ItemType.trap_harmless, None, "None", "Spoiler Alert!") #Plays random movie
}

trapWeakDict: dict[int, ItemData] = {
    1500: ItemData(IC.trap, 0, "set_random_negative_public_order()", ItemType.trap_weak, None, "None", "Handful of Unrest"), #Random amount of negative public order to random region
    1501: ItemData(IC.trap, 0, "force_random_weak_rebellion_for_player()", ItemType.trap_weak, None, "None", "Unionize This!"), #Weak rebellion
    1502: ItemData(IC.trap, 0, "cm:reset_shroud()", ItemType.trap_weak, None, "None", "Where is our Map?"), #Resets fog of war
    1503: ItemData(IC.trap, 0, 'cm:cai_force_personality_change("All")', ItemType.trap_weak, None, "None", "Schizophrenia!"), #Randomise AI personalities
    1504: ItemData(IC.trap, 0, "force_alliance_with_random_enemy()", ItemType.trap_weak, None, "None", "Make Love, Not War (Trap)"), #Makes random enemy an ally
}

trapStrongDict: dict[int, ItemData] = {
    1600: ItemData(IC.trap, 0, "force_random_strong_rebellion_for_player()", ItemType.trap_strong, None, "None", "Torches and Pitchforks!"), #Strong rebellion
    1601: ItemData(IC.trap, 0, "force_settlement_trade_with_random_enemy()", ItemType.trap_strong, None, "None", "Let's trade!"), #Swaps random city with random enemy city
    1602: ItemData(IC.trap, 0, "force_war_with_random_ally()", ItemType.trap_strong, None, "None", "You too, Brutus?") #Ally declares war on player
}