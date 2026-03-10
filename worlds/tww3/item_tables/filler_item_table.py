from BaseClasses import ItemClassification as IC

from worlds.tww3.itemTypes import itemType, itemData
fillerWeakDict: dict[int, itemData] = {
    1200: itemData(IC.filler, 0, 'cm:treasury_mod("%s", cm:random_number(2000,1))', itemType.filler_weak, None, "None", "Get-Rich-Slow Scroll"), #Gold
    1201: itemData(IC.filler, 0, "", itemType.filler_weak, None, "None", "Something Happened"), #Random event - not currently included as most don't do anything
    1202: itemData(IC.filler, 0, "set_random_positive_public_order()", itemType.filler_weak, None, "None", "Handful of Order"), #Random amount of positive public order to random region
    1203: itemData(IC.filler, 0, "", itemType.filler_weak, None, "None", "Something Thingy"), #Random item/ancillary
    1204: itemData(IC.filler, 0, "add_random_growth_to_player()", itemType.filler_weak, None, "None", "The GroBro 3000"), #Growth boost to random region
    1205: itemData(IC.filler, 0, "", itemType.filler_strong, None, "None", "Something Shiny") #Random legendary item/ancillary
}

fillerStrongDict: dict[int, itemData] = {
    1300: itemData(IC.filler, 0, "force_settlement_transfer_from_random_enemy_to_player()", itemType.filler_strong, None, "None", "Give me that"), #Gives player random enemy city
    1301: itemData(IC.filler, 0, "force_alliance_with_random_enemy()", itemType.filler_strong, None, "None", "Make Love, Not War"), #Makes random enemy an ally
    1302: itemData(IC.filler, 0, 'cm:treasury_mod("%s", cm:random_number(10000,1000))', itemType.filler_weak, None, "None", "Get-Rich-Quick Scroll"), #Gold
}

trapHarmlessDict: dict[int, itemData] = {
    1400: itemData(IC.trap, 0, "scroll_camera_to_random_region()", itemType.trap_harmless, None, "None", "Look! What's that?"), #Moves map to random position
    1401: itemData(IC.trap, 0, "play_random_movie()", itemType.trap_harmless, None, "None", "Spoiler Alert!") #Plays random movie
}

trapWeakDict: dict[int, itemData] = {
    1500: itemData(IC.trap, 0, "set_random_negative_public_order()", itemType.trap_weak, None, "None", "Handful of Unrest"), #Random amount of negative public order to random region
    1501: itemData(IC.trap, 0, "force_random_weak_rebellion_for_player()", itemType.trap_weak, None, "None", "Unionize This!"), #Weak rebellion
    1502: itemData(IC.trap, 0, "cm:reset_shroud()", itemType.trap_weak, None, "None", "Where is our Map?"), #Resets fog of war
    1503: itemData(IC.trap, 0, 'cm:cai_force_personality_change("All")', itemType.trap_weak, None, "None", "Schizophrenia!"), #Randomise AI personalities
    1504: itemData(IC.trap, 0, "force_alliance_with_random_enemy()", itemType.trap_weak, None, "None", "Make Love, Not War (Trap)"), #Makes random enemy an ally
}

trapStrongDict: dict[int, itemData] = {
    1600: itemData(IC.trap, 0, "force_random_strong_rebellion_for_player()", itemType.trap_strong, None, "None", "Torches and Pitchforks!"), #Strong rebellion
    1601: itemData(IC.trap, 0, "force_settlement_trade_with_random_enemy()", itemType.trap_strong, None, "None", "Let's trade!"), #Swaps random city with random enemy city
    1602: itemData(IC.trap, 0, "force_war_with_random_ally()", itemType.trap_strong, None, "None", "You too, Brutus?") #Ally declares war on player
}