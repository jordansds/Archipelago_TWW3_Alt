from BaseClasses import ItemClassification as IC

from worlds.tww3.itemTypes import itemType, itemData
fillerDict: dict[int, itemData] = {
    1200: itemData(IC.filler, 0, 'cm:treasury_mod("%s", cm:random_number(2000,1))', itemType.filler, None, "None", "Buff: Get-Rich-Slow Scroll"), #Gold
    #1201: itemData(IC.filler, 0, "", itemType.filler, None, "None", "Something Happened"), #Random event - not currently included as most don't do anything
    1202: itemData(IC.filler, 0, "set_random_positive_public_order()", itemType.filler, None, "None", "Buff: Handful of Order"), #Random amount of positive public order to random region
    1203: itemData(IC.filler, 0, "", itemType.filler, None, "None", "Something Thingy"), #Random item/ancillary
    1204: itemData(IC.filler, 0, "add_random_growth_to_player()", itemType.filler, None, "None", "Buff: The GroBro 3000"), #Growth boost to random region
    1205: itemData(IC.filler, 0, "", itemType.filler, None, "None", "Something Shiny"), #Random legendary item/ancillary
    1206: itemData(IC.filler, 0, "force_settlement_transfer_from_random_enemy_to_player()", itemType.filler, None, "None", "Buff: Give me that"), #Gives player random enemy city
    1207: itemData(IC.filler, 0, "force_alliance_with_random_enemy()", itemType.filler, None, "None", "Buff: Make Love, Not War"), #Makes random enemy an ally
    1208: itemData(IC.filler, 0, 'cm:treasury_mod("%s", cm:random_number(10000,1000))', itemType.filler, None, "None", "Buff: Get-Rich-Quick Scroll"), #Gold
}

fillerStrongDict: dict[int, itemData] = {

}

#trapHarmlessDict: dict[int, itemData] = {
#    1400: itemData(IC.trap, 0, "scroll_camera_to_random_region()", itemType.trap_harmless, None, "None", "Look! What's that?"), #Moves map to random position
#    1401: itemData(IC.trap, 0, "play_random_movie()", itemType.trap_harmless, None, "None", "Spoiler Alert!") #Plays random movie
#}

trapDict: dict[int, itemData] = {
    1500: itemData(IC.trap, 0, "set_random_negative_public_order()", itemType.trap, None, "None", "Trap: Handful of Unrest"), #Random amount of negative public order to random region
    1501: itemData(IC.trap, 0, "force_random_weak_rebellion_for_player()", itemType.trap, None, "None", "Trap: Unionize This!"), #Weak rebellion
    1502: itemData(IC.trap, 0, "cm:reset_shroud()", itemType.trap, None, "None", "Trap: Where is our Map?"), #Resets fog of war
    1503: itemData(IC.trap, 0, 'cm:cai_force_personality_change("All")', itemType.trap, None, "None", "Trap: Schizophrenia!"), #Randomise AI personalities
    1504: itemData(IC.trap, 0, "force_alliance_with_random_enemy()", itemType.trap, None, "None", "Trap: Make Love, Not War (Trap)"), #Makes random enemy an ally
    #1505: itemData(IC.trap, 0, "force_random_strong_rebellion_for_player()", itemType.trap, None, "None", "Trap: Torches and Pitchforks!"), #Strong rebellion
    #1506: itemData(IC.trap, 0, "force_settlement_trade_with_random_enemy()", itemType.trap, None, "None", "Trap: Let's trade!"), #Swaps random city with random enemy city
    #1507: itemData(IC.trap, 0, "force_war_with_random_ally()", itemType.trap, None, "None", "Trap: You too, Brutus?"), #Ally declares war on player
    #1508: itemData(IC.trap, 0, "teleport_lord_to_random_region()", itemType.trap, None, "None", "Trap: We're Going on a Trip") #Teleports the player's leader to a random city
    1509: itemData(IC.trap, 0, "force_war_with_random_faction()", itemType.trap, None, "None", "Trap: En Garde!"), #Random faction declares war on player
}

trapStrongDict: dict[int, itemData] = {
}