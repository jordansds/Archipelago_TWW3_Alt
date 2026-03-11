from BaseClasses import ItemClassification as IC
from worlds.tww3.itemTypes import itemType, itemData, specialItemData

# @formatter:off

units: dict[int, itemData] = {
    112001: itemData(IC.useful, 1, "CN_crab_levy_0", itemType.unit, 1, "Progressive crb_inf", "Crustacean Unit: Crab Levy"),
    112002: itemData(IC.useful, 1, "CN_crab_warriors_0", itemType.unit, 1, "Progressive crb_inf", "Crustacean Unit: Crab Warriors"),
    112003: itemData(IC.useful, 1, "CN_crab_warriors_1", itemType.unit, 1, "Progressive crb_inf", "Crustacean Unit: Crab Warriors (Spears)"),
    112004: itemData(IC.useful, 1, "CN_crab_rangers", itemType.unit, 2, "Progressive crb_inf", "Crustacean Unit: Crab Rangers"),
    112005: itemData(IC.useful, 1, "CN_crab_monks", itemType.unit, 2, "Progressive crb_inf", "Crustacean Unit: Ironclaw Warrior Monks"),
    112006: itemData(IC.useful, 1, "CN_crab_guard_0", itemType.unit, 3, "Progressive crb_inf", "Crustacean Unit: Crustacean Royal Guard"),
    112007: itemData(IC.useful, 1, "CN_crab_guard_1", itemType.unit, 3, "Progressive crb_inf", "Crustacean Unit: Crustacean Royal Guard (Halberds)"),
    112008: itemData(IC.useful, 1, "CN_monstrous_crabs_0", itemType.unit, 3, "Progressive crb_inf", "Crustacean Unit: Hardshell Colossi"),
    112009: itemData(IC.useful, 1, "CN_monstrous_crabs_1", itemType.unit, 4, "Progressive crb_inf", "Crustacean Unit: Hardshell Bruisers"),
    112010: itemData(IC.useful, 1, "CN_crab_disciples_shell", itemType.unit, 4, "Progressive crb_inf", "Crustacean Unit: Disciples of the Shell"),
    112011: itemData(IC.useful, 1, "CN_crab_disciples_claw", itemType.unit, 4, "Progressive crb_inf", "Crustacean Unit: Disciples of the Claw"),

    112012: itemData(IC.useful, 1, "CN_crab_levy_1", itemType.unit, 1, "Progressive crb_rng", "Crustacean Unit: Crab Levy Slingers"),
    112013: itemData(IC.useful, 1, "CN_crab_warriors_2", itemType.unit, 2, "Progressive crb_rng", "Crustacean Unit: Crab Warriors (Javelins)"),
    112014: itemData(IC.useful, 1, "CN_crab_bomber", itemType.unit, 2, "Progressive crb_rng", "Crustacean Unit: Crustacean Bombers"),
    112015: itemData(IC.useful, 1, "CN_crab_gunner", itemType.unit, 2, "Progressive crb_rng", "Crustacean Unit: Crustacean Gunners"),
    112016: itemData(IC.useful, 1, "CN_crab_slinger", itemType.unit, 3, "Progressive crb_rng", "Crustacean Unit: Crustacean Slingers"),
    112017: itemData(IC.useful, 1, "CN_crab_bomber_armoured", itemType.unit, 3, "Progressive crb_rng", "Crustacean Unit: Crustacean Grenadiers"),

    112018: itemData(IC.useful, 1, "CN_crab_rider", itemType.unit, 1, "Progressive crb_cav", "Crustacean Unit: Spider Crab Riders"),
    112019: itemData(IC.useful, 1, "CN_crab_knight", itemType.unit, 2, "Progressive crb_cav", "Crustacean Unit: Crustacean Knights"),
    112020: itemData(IC.useful, 1, "CN_crab_guard_knight", itemType.unit, 3, "Progressive crb_cav", "Crustacean Unit: Crustacean Royal Knights"),

    112021: itemData(IC.useful, 1, "CN_art_crabcannon", itemType.unit, 1, "Progressive crb_art", "Crustacean Unit: Crabcannons"),
    112022: itemData(IC.useful, 1, "CN_art_shellcracker", itemType.unit, 2, "Progressive crb_art", "Crustacean Unit: Shellcrackers"),
    112023: itemData(IC.useful, 1, "CN_monstrous_crabs_3", itemType.unit, 2, "Progressive crb_art", "Crustacean Unit: Hardshell Cannonbacks (Mortars)"),
    112024: itemData(IC.useful, 1, "CN_monstrous_crabs_2", itemType.unit, 2, "Progressive crb_art", "Crustacean Unit: Hardshell Cannonbacks"),
    112025: itemData(IC.useful, 1, "CN_art_krakencaller", itemType.unit, 3, "Progressive crb_art", "Crustacean Unit: Krakencaller"),

    112026: itemData(IC.useful, 1, "CN_warshrine", itemType.unit, 1, "Progressive crb_veh", "Crustacean Unit: Crustacean Battle Altar"),

    112027: itemData(IC.useful, 1, "CN_scuttlecrabs", itemType.unit, 1, "Progressive crb_bst", "Crustacean Unit: Reef Snappers"),
    112028: itemData(IC.useful, 1, "CN_flying_crabs", itemType.unit, 2, "Progressive crb_bst", "Crustacean Unit: Dragon Shrimps"),
    112029: itemData(IC.useful, 1, "CN_giant_scuttlecrab", itemType.unit, 2, "Progressive crb_bst", "Crustacean Unit: Giant Reef Snapper"),
    112030: itemData(IC.useful, 1, "CN_great_dragon_shrimp", itemType.unit, 3, "Progressive crb_bst", "Crustacean Unit: Giant Dragon Shrimp"),
    112031: itemData(IC.useful, 1, "CN_giant_scuttlecrab_bombs", itemType.unit, 3, "Progressive crb_bst", "Crustacean Unit: Giant Reef Snapper (Battle Platform)"),
    112032: itemData(IC.useful, 1, "CN_giant_crab", itemType.unit, 4, "Progressive crb_bst", "Crustacean Unit: Ancient Leviathan"),

    112033: itemData(IC.useful, 1, "CN_cha_crab_mage_claw", itemType.unit, 1, "Progressive crb_hro", "Crustacean Unit: Crustacean Mage-Priest (Claw)"),
    112034: itemData(IC.useful, 1, "CN_cha_crab_mage_shell", itemType.unit, 1, "Progressive crb_hro", "Crustacean Unit: Crustacean Mage-Priest (Shell)"),
    112035: itemData(IC.useful, 1, "CN_cha_big_crab_champion", itemType.unit, 1, "Progressive crb_hro", "Crustacean Unit: Hardshell Champion"),
    112036: itemData(IC.useful, 1, "CN_cha_crab_guard_captain", itemType.unit, 1, "Progressive crb_hro", "Crustacean Unit: Crustacean Royal Guard Captain"),
    
    112037: itemData(IC.useful, 1, "CN_crab_levy_ror", itemType.unit, 1, "Progressive crb_inf", "Crustacean Unit: Rimeshell Marauders (Crab Levy)"),
    112038: itemData(IC.useful, 1, "CN_crab_monks_ror", itemType.unit, 2, "Progressive crb_inf", "Crustacean Unit: Shadowclaw Assassins (Ironclaw Warrior Monks)"),
    112039: itemData(IC.useful, 1, "CN_crab_rider_ror", itemType.unit, 1, "Progressive crb_cav", "Crustacean Unit: Mirror Moors Outriders (Spider Crab Riders)"),
    112040: itemData(IC.useful, 1, "CN_art_crabcannon_ror", itemType.unit, 1, "Progressive crb_art", "Crustacean Unit: Norseman's Dirge (Crabcannons)"),
    112041: itemData(IC.useful, 1, "CN_crab_disciples_ror", itemType.unit, 4, "Progressive crb_inf", "Crustacean Unit: The Ironclaw Council (Disciples of Claw & Shell)"),
    112042: itemData(IC.useful, 1, "CN_monstrous_crabs_ror", itemType.unit, 3, "Progressive crb_inf", "Crustacean Unit: Black Gulf Gladiators (Hardshell Bruisers)"),
    112043: itemData(IC.useful, 1, "CN_giant_crab_ror", itemType.unit, 4, "Progressive crb_bst", "Crustacean Unit: The Krakenmeister (Ancient Leviathan)"),
    112044: itemData(IC.useful, 1, "CN_crab_gunner_ror", itemType.unit, 1, "Progressive crb_rng", "Crustacean Unit: Pureshell Blunderbacks (Crustacean Gunners)"),
    112045: itemData(IC.useful, 1, "CN_giant_scuttlecrab_ror", itemType.unit, 2, "Progressive crb_bst", "Crustacean Unit: The Raging Guardian (Giant Reef Snapper)"),
}

buildings: dict[int, itemData] = {
    112400: itemData(IC.useful, 1, "cn_settlement_minor_1", itemType.building, 0, "Progressive crb_settlement_minor", "Crustacean Building: Crustacean Village (Minor)"),
    112401: itemData(IC.useful, 1, "cn_settlement_minor_2", itemType.building, 1, "Progressive crb_settlement_minor", "Crustacean Building: Crustacean Hollows (Minor)"),
    112402: itemData(IC.useful, 1, "cn_settlement_minor_3", itemType.building, 2, "Progressive crb_settlement_minor", "Crustacean Building: Crustacean Burrows (Minor)"),
    112403: itemData(IC.useful, 1, "cn_settlement_major_1", itemType.building, 0, "Progressive crb_settlement_major", "Crustacean Building: Crustacean Burrows (Major)"),
    112404: itemData(IC.useful, 1, "cn_settlement_major_2", itemType.building, 1, "Progressive crb_settlement_major", "Crustacean Building: Crustacean Hollows (Major)"),
    112405: itemData(IC.useful, 1, "cn_settlement_major_3", itemType.building, 2, "Progressive crb_settlement_major", "Crustacean Building: Crustacean Village (Major)"),
    112406: itemData(IC.useful, 1, "cn_settlement_major_4", itemType.building, 3, "Progressive crb_settlement_major", "Crustacean Building: Crustacean Colony (Major)"),
    112407: itemData(IC.useful, 1, "cn_settlement_major_5", itemType.building, 4, "Progressive crb_settlement_major", "Crustacean Building: Crab City (Major)"),
    112408: itemData(IC.useful, 1, "cn_defense_major_1", itemType.building, 0, "Progressive crb_garrison_major", "Crustacean Building: Crustacean Watch Tower"),
    112409: itemData(IC.useful, 1, "cn_defense_major_2", itemType.building, 1, "Progressive crb_garrison_major", "Crustacean Building: Crustacean Guard Tower"),
    112410: itemData(IC.useful, 1, "cn_defense_major_3", itemType.building, 2, "Progressive crb_garrison_major", "Crustacean Building: Crustacean Garrison"),
    112411: itemData(IC.useful, 1, "cn_defense_minor_1", itemType.building, 0, "Progressive crb_garrison_minor", "Crustacean Building: Crustacean Town Watch"),
    112412: itemData(IC.useful, 1, "cn_defense_minor_2", itemType.building, 1, "Progressive crb_garrison_minor", "Crustacean Building: Crustacean City Watch"),

    112413: itemData(IC.useful, 1, "cn_growth_1", itemType.building, 0, "Progressive crb_farms", "Crustacean Building: Kelp Farm"),
    112414: itemData(IC.useful, 1, "cn_growth_2", itemType.building, 1, "Progressive crb_farms", "Crustacean Building: Kelp Ranch"),
    112415: itemData(IC.useful, 1, "cn_growth_3", itemType.building, 2, "Progressive crb_farms", "Crustacean Building: Kelp Plantation"),

    112416: itemData(IC.useful, 1, "cn_money_1", itemType.building, 0, "Progressive crb_industry", "Crustacean Building: Crabtissans Hut"),
    112417: itemData(IC.useful, 1, "cn_money_2", itemType.building, 1, "Progressive crb_industry", "Crustacean Building: Crabtissans Workshop"),
    112418: itemData(IC.useful, 1, "cn_money_3", itemType.building, 2, "Progressive crb_industry", "Crustacean Building: Crabtissans Guild"),

    112419: itemData(IC.useful, 1, "cn_order_1", itemType.building, 0, "Progressive crb_order", "Crustacean Building: Coral Bed"),
    112420: itemData(IC.useful, 1, "cn_order_2", itemType.building, 1, "Progressive crb_order", "Crustacean Building: Coral Reef"),
    112421: itemData(IC.useful, 1, "cn_order_3", itemType.building, 2, "Progressive crb_order", "Crustacean Building: Coral Garden"),

    112422: itemData(IC.useful, 1, "cn_port_1", itemType.building, 0, "Progressive crb_port", "Crustacean Building: Crustacean Wharf"),
    112423: itemData(IC.useful, 1, "cn_port_2", itemType.building, 1, "Progressive crb_port", "Crustacean Building: Crustacean Port"),
    112424: itemData(IC.useful, 1, "cn_port_3", itemType.building, 2, "Progressive crb_port", "Crustacean Building: Crustacean Harbour"),

    112425: itemData(IC.useful, 1, "cn_beast_barracks_1", itemType.building, 0, "Progressive crb_beast_barracks", "Crustacean Building: Crustacean Beast Pens"),
    112426: itemData(IC.useful, 1, "cn_beast_barracks_2", itemType.building, 1, "Progressive crb_beast_barracks", "Crustacean Building: Crustacean Menagerie"),

    112427: itemData(IC.useful, 1, "cn_warrior_barracks_1", itemType.building, 0, "Progressive crb_warrior_barracks", "Crustacean Building: Mustering Fields"),
    112428: itemData(IC.useful, 1, "cn_warrior_barracks_2", itemType.building, 1, "Progressive crb_warrior_barracks", "Crustacean Building: Mustering Hall"),
    112429: itemData(IC.useful, 1, "cn_warrior_barracks_3", itemType.building, 2, "Progressive crb_warrior_barracks", "Crustacean Building: Crustacean Barracks"),

    112430: itemData(IC.useful, 1, "cn_royal_barracks_1", itemType.building, 0, "Progressive crb_royal_barracks", "Crustacean Building: Royal Guard Outpost"),
    112431: itemData(IC.useful, 1, "cn_royal_barracks_2", itemType.building, 1, "Progressive crb_royal_barracks", "Crustacean Building: Royal Guard Barracks"),
    112432: itemData(IC.useful, 1, "cn_royal_barracks_3", itemType.building, 2, "Progressive crb_royal_barracks", "Crustacean Building: Royal Guard Keep"),

    112433: itemData(IC.useful, 1, "cn_foreign_slot_discovery_1", itemType.building, 0, "Progressive crb_foreign_slot_discovery", "Crustacean Building: Crabby Patrols"),
    112434: itemData(IC.useful, 1, "cn_foreign_slot_discovery_2", itemType.building, 1, "Progressive crb_foreign_slot_discovery", "Crustacean Building: Crabby Watchmen"),
    112435: itemData(IC.useful, 1, "cn_foreign_slot_discovery_3", itemType.building, 2, "Progressive crb_foreign_slot_discovery", "Crustacean Building: Crabby Sentinels"),

    112436: itemData(IC.useful, 1, "cn_shells_1", itemType.building, 0, "Progressive crb_shells", "Crustacean Building: Shell Storage"),
    112437: itemData(IC.useful, 1, "cn_shells_2", itemType.building, 1, "Progressive crb_shells", "Crustacean Building: Shell Emporium"),
    112438: itemData(IC.useful, 1, "cn_shells_3", itemType.building, 2, "Progressive crb_shells", "Crustacean Building: Royal Shell Vault"),

    112439: itemData(IC.useful, 1, "cn_gunpowder_barracks_1", itemType.building, 0, "Progressive crb_gunpowder_barracks", "Crustacean Building: Crustacean Powdermaker"),
    112440: itemData(IC.useful, 1, "cn_gunpowder_barracks_2", itemType.building, 1, "Progressive crb_gunpowder_barracks", "Crustacean Building: Crustacean Gunsmith"),
    112441: itemData(IC.useful, 1, "cn_gunpowder_barracks_3", itemType.building, 2, "Progressive crb_gunpowder_barracks", "Crustacean Building: Crustacean Arsenal"),

    112442: itemData(IC.useful, 1, "cn_monster_barracks_1", itemType.building, 0, "Progressive crb_monster_barracks", "Crustacean Building: Hardshell Pits"),
    112443: itemData(IC.useful, 1, "cn_monster_barracks_2", itemType.building, 1, "Progressive crb_monster_barracks", "Crustacean Building: Hardshell Colosseum"),
    112444: itemData(IC.useful, 1, "cn_monster_barracks_3", itemType.building, 2, "Progressive crb_monster_barracks", "Crustacean Building: Hardshell Undercity"),

    112445: itemData(IC.useful, 1, "cn_cult_barracks_1", itemType.building, 0, "Progressive crb_cult_barracks", "Crustacean Building: Crustacean Shrine"),
    112446: itemData(IC.useful, 1, "cn_cult_barracks_2", itemType.building, 1, "Progressive crb_cult_barracks", "Crustacean Building: Crustacean Monument"),
    112447: itemData(IC.useful, 1, "cn_cult_barracks_3", itemType.building, 2, "Progressive crb_cult_barracks", "Crustacean Building: Crustacean Monastery"),
    112448: itemData(IC.useful, 1, "cn_cult_barracks_4", itemType.building, 3, "Progressive crb_cult_barracks", "Crustacean Building: Crustacean Temple"),

    112449: itemData(IC.useful, 1, "cn_forge_1", itemType.building, 0, "Progressive crb_forge", "Crustacean Building: Crustacean Smith"),
    112450: itemData(IC.useful, 1, "cn_forge_2", itemType.building, 1, "Progressive crb_forge", "Crustacean Building: Crustacean Forge"),

    112451: itemData(IC.useful, 1, "cn_research_1", itemType.building, 0, "Progressive crb_research", "Crustacean Building: Tidestone"),

    112452: itemData(IC.useful, 1, "cn_resource_animals_1", itemType.building, 0, "Progressive crb_resource_animals", "Crustacean Building: Exotic Beast Cages"),
    112453: itemData(IC.useful, 1, "cn_resource_animals_2", itemType.building, 1, "Progressive crb_resource_animals", "Crustacean Building: Exotic Beast Enclosure"),
    112454: itemData(IC.useful, 1, "cn_resource_animals_3", itemType.building, 2, "Progressive crb_resource_animals", "Crustacean Building: Exotic Beast Stables"),

    112455: itemData(IC.useful, 1, "cn_resource_dyes_1", itemType.building, 0, "Progressive crb_resource_dyes", "Crustacean Building: Dye Camp"),
    112456: itemData(IC.useful, 1, "cn_resource_dyes_2", itemType.building, 1, "Progressive crb_resource_dyes", "Crustacean Building: Dye Workshop"),
    112457: itemData(IC.useful, 1, "cn_resource_dyes_3", itemType.building, 2, "Progressive crb_resource_dyes", "Crustacean Building: Dye Emporium"),

    112458: itemData(IC.useful, 1, "cn_resource_furs_1", itemType.building, 0, "Progressive crb_resource_furs", "Crustacean Building: Fur Camp"),
    112459: itemData(IC.useful, 1, "cn_resource_furs_2", itemType.building, 1, "Progressive crb_resource_furs", "Crustacean Building: Fur Workshop"),
    112460: itemData(IC.useful, 1, "cn_resource_furs_3", itemType.building, 2, "Progressive crb_resource_furs", "Crustacean Building: Fur Emporium"),

    112461: itemData(IC.useful, 1, "cn_resource_gems_1", itemType.building, 0, "Progressive crb_resource_gems", "Crustacean Building: Gemstone Camp"),
    112462: itemData(IC.useful, 1, "cn_resource_gems_2", itemType.building, 1, "Progressive crb_resource_gems", "Crustacean Building: Gemstone Workshop"),
    112463: itemData(IC.useful, 1, "cn_resource_gems_3", itemType.building, 2, "Progressive crb_resource_gems", "Crustacean Building: Gemstone Emporium"),

    112464: itemData(IC.useful, 1, "cn_resource_gold_1", itemType.building, 0, "Progressive crb_resource_gold", "Crustacean Building: Gold Camp"),
    112465: itemData(IC.useful, 1, "cn_resource_gold_2", itemType.building, 1, "Progressive crb_resource_gold", "Crustacean Building: Gold Workshop"),
    112466: itemData(IC.useful, 1, "cn_resource_gold_3", itemType.building, 2, "Progressive crb_resource_gold", "Crustacean Building: Gold Emporium"),

    112467: itemData(IC.useful, 1, "cn_resource_iron_1", itemType.building, 0, "Progressive crb_resource_iron", "Crustacean Building: Iron Camp"),
    112468: itemData(IC.useful, 1, "cn_resource_iron_2", itemType.building, 1, "Progressive crb_resource_iron", "Crustacean Building: Iron Workshop"),
    112469: itemData(IC.useful, 1, "cn_resource_iron_3", itemType.building, 2, "Progressive crb_resource_iron", "Crustacean Building: Iron Emporium"),

    112470: itemData(IC.useful, 1, "cn_resource_ivory_1", itemType.building, 0, "Progressive crb_resource_ivory", "Crustacean Building: Ivory Camp"),
    112471: itemData(IC.useful, 1, "cn_resource_ivory_2", itemType.building, 1, "Progressive crb_resource_ivory", "Crustacean Building: Ivory Workshop"),
    112472: itemData(IC.useful, 1, "cn_resource_ivory_3", itemType.building, 2, "Progressive crb_resource_ivory", "Crustacean Building: Ivory Emporium"),

    112473: itemData(IC.useful, 1, "cn_resource_marble_1", itemType.building, 0, "Progressive crb_resource_marble", "Crustacean Building: Marble Camp"),
    112474: itemData(IC.useful, 1, "cn_resource_marble_2", itemType.building, 1, "Progressive crb_resource_marble", "Crustacean Building: Marble Workshop"),
    112475: itemData(IC.useful, 1, "cn_resource_marble_3", itemType.building, 2, "Progressive crb_resource_marble", "Crustacean Building: Marble Emporium"),

    112476: itemData(IC.useful, 1, "cn_resource_medicine_1", itemType.building, 0, "Progressive crb_resource_medicine", "Crustacean Building: Medicine Camp"),
    112477: itemData(IC.useful, 1, "cn_resource_medicine_2", itemType.building, 1, "Progressive crb_resource_medicine", "Crustacean Building: Medicine Workshop"),
    112478: itemData(IC.useful, 1, "cn_resource_medicine_3", itemType.building, 2, "Progressive crb_resource_medicine", "Crustacean Building: Medicine Emporium"),

    112479: itemData(IC.useful, 1, "cn_resource_obsidian_1", itemType.building, 0, "Progressive crb_resource_obsidian", "Crustacean Building: Obsidian Camp"),
    112480: itemData(IC.useful, 1, "cn_resource_obsidian_2", itemType.building, 1, "Progressive crb_resource_obsidian", "Crustacean Building: Obsidian Workshop"),
    112481: itemData(IC.useful, 1, "cn_resource_obsidian_3", itemType.building, 2, "Progressive crb_resource_obsidian", "Crustacean Building: Obsidian Emporium"),

    112482: itemData(IC.useful, 1, "cn_resource_pasture_1", itemType.building, 0, "Progressive crb_resource_pasture", "Crustacean Building: Spider Crab Pastures"),
    112483: itemData(IC.useful, 1, "cn_resource_pasture_2", itemType.building, 1, "Progressive crb_resource_pasture", "Crustacean Building: Spider Crab Ranch"),
    112484: itemData(IC.useful, 1, "cn_resource_pasture_3", itemType.building, 2, "Progressive crb_resource_pasture", "Crustacean Building: Spider Crab Stables"),

    112485: itemData(IC.useful, 1, "cn_resource_pottery_1", itemType.building, 0, "Progressive crb_resource_pottery", "Crustacean Building: Pottery Camp"),
    112486: itemData(IC.useful, 1, "cn_resource_pottery_2", itemType.building, 1, "Progressive crb_resource_pottery", "Crustacean Building: Pottery Workshop"),
    112487: itemData(IC.useful, 1, "cn_resource_pottery_3", itemType.building, 2, "Progressive crb_resource_pottery", "Crustacean Building: Pottery Emporium"),

    112488: itemData(IC.useful, 1, "cn_resource_salt_1", itemType.building, 0, "Progressive crb_resource_salt", "Crustacean Building: Salt Water Well"),
    112489: itemData(IC.useful, 1, "cn_resource_salt_2", itemType.building, 1, "Progressive crb_resource_salt", "Crustacean Building: Salt Water Brewery"),
    112490: itemData(IC.useful, 1, "cn_resource_salt_3", itemType.building, 2, "Progressive crb_resource_salt", "Crustacean Building: Salt Water Distillery"),

    112491: itemData(IC.useful, 1, "cn_resource_spices_1", itemType.building, 0, "Progressive crb_resource_spices", "Crustacean Building: Spice Camp"),
    112492: itemData(IC.useful, 1, "cn_resource_spices_2", itemType.building, 1, "Progressive crb_resource_spices", "Crustacean Building: Spice Workshop"),
    112493: itemData(IC.useful, 1, "cn_resource_spices_3", itemType.building, 2, "Progressive crb_resource_spices", "Crustacean Building: Spice Emporium"),

    112494: itemData(IC.useful, 1, "cn_resource_wine_1", itemType.building, 0, "Progressive crb_resource_wine", "Crustacean Building: Wine Camp"),
    112495: itemData(IC.useful, 1, "cn_resource_wine_2", itemType.building, 1, "Progressive crb_resource_wine", "Crustacean Building: Wine Workshop"),
    112496: itemData(IC.useful, 1, "cn_resource_wine_3", itemType.building, 2, "Progressive crb_resource_wine", "Crustacean Building: Wine Emporium"),

    112497: itemData(IC.useful, 1, "cn_resource_wood_1", itemType.building, 0, "Progressive crb_resource_wood", "Crustacean Building: Lumber Camp"),
    112498: itemData(IC.useful, 1, "cn_resource_wood_2", itemType.building, 1, "Progressive crb_resource_wood", "Crustacean Building: Lumber Workshop"),
    112499: itemData(IC.useful, 1, "cn_resource_wood_3", itemType.building, 2, "Progressive crb_resource_wood", "Crustacean Building: Lumber Emporium"),
}

techs: dict[int, itemData] = {
    112800: itemData(IC.useful, 1, "cn_tech_0_growth", itemType.building, 1, "Progressive tech_crb_head", "Crustacean Tech: Future of Crabkind"),
    112801: itemData(IC.useful, 1, "cn_tech_head_1", itemType.building, 2, "Progressive tech_crb_head", "Crustacean Tech: Martial Claw"),

    112802: itemData(IC.useful, 1, "cn_tech_left_claw_0", itemType.building, 1, "Progressive tech_crb_left_claw", "Crustacean Tech: Military Training"),
    112803: itemData(IC.useful, 1, "cn_tech_left_claw_1", itemType.building, 2, "Progressive tech_crb_left_claw", "Crustacean Tech: Bullet Workshops"),
    112804: itemData(IC.useful, 1, "cn_tech_left_claw_1b", itemType.building, 2, "Progressive tech_crb_left_claw", "Crustacean Tech: Improved Throwing Technique"),
    112805: itemData(IC.useful, 1, "cn_tech_left_claw_2", itemType.building, 3, "Progressive tech_crb_left_claw", "Crustacean Tech: Defensive Formation"),
    112806: itemData(IC.useful, 1, "cn_tech_left_claw_3b", itemType.building, 4, "Progressive tech_crb_left_claw", "Crustacean Tech: Marching Drills"),
    112807: itemData(IC.useful, 1, "cn_tech_left_claw_3", itemType.building, 4, "Progressive tech_crb_left_claw", "Crustacean Tech: Sneaky Scuttlers"),
    112808: itemData(IC.useful, 1, "cn_tech_left_claw_3c", itemType.building, 5, "Progressive tech_crb_left_claw", "Crustacean Tech: Heavy Munitions"),
    112809: itemData(IC.useful, 1, "cn_tech_left_claw_4", itemType.building, 5, "Progressive tech_crb_left_claw", "Crustacean Tech: Weapon Maintenance"),
    112810: itemData(IC.useful, 1, "cn_tech_left_claw_5", itemType.building, 5, "Progressive tech_crb_left_claw", "Crustacean Tech: Military Stockpiles"),
    112811: itemData(IC.useful, 1, "cn_tech_left_claw_6", itemType.building, 5, "Progressive tech_crb_left_claw", "Crustacean Tech: Finest Armaments"),
    112812: itemData(IC.useful, 1, "cn_tech_left_claw_6b", itemType.building, 6, "Progressive tech_crb_left_claw", "Crustacean Tech: Specialist Training"),
    112813: itemData(IC.useful, 1, "cn_tech_left_claw_7", itemType.building, 6, "Progressive tech_crb_left_claw", "Crustacean Tech: Royal Traditions"),
    112814: itemData(IC.useful, 1, "cn_tech_left_claw_7b", itemType.building, 6, "Progressive tech_crb_left_claw", "Crustacean Tech: Officers Academy"),
    112815: itemData(IC.useful, 1, "cn_tech_left_claw_8", itemType.building, 7, "Progressive tech_crb_left_claw", "Crustacean Tech: Release the Kraken"),
    112816: itemData(IC.useful, 1, "cn_tech_left_claw_9", itemType.building, 8, "Progressive tech_crb_left_claw", "Crustacean Tech: Crustacean Dominion"),

    112817: itemData(IC.useful, 1, "cn_tech_right_claw_0", itemType.building, 1, "Progressive tech_crb_right_claw", "Crustacean Tech: Reinforced Clubs"),
    112818: itemData(IC.useful, 1, "cn_tech_right_claw_1", itemType.building, 2, "Progressive tech_crb_right_claw", "Crustacean Tech: Padded Saddles"),
    112819: itemData(IC.useful, 1, "cn_tech_right_claw_1b", itemType.building, 2, "Progressive tech_crb_right_claw", "Crustacean Tech: Free-range Training"),
    112820: itemData(IC.useful, 1, "cn_tech_right_claw_2", itemType.building, 3, "Progressive tech_crb_right_claw", "Crustacean Tech: Ironclaw Teachings"),
    112821: itemData(IC.useful, 1, "cn_tech_right_claw_3b", itemType.building, 4, "Progressive tech_crb_right_claw", "Crustacean Tech: Bigger Casting Molds"),
    112822: itemData(IC.useful, 1, "cn_tech_right_claw_3", itemType.building, 4, "Progressive tech_crb_right_claw", "Crustacean Tech: Selective Breeding"),
    112823: itemData(IC.useful, 1, "cn_tech_right_claw_3c", itemType.building, 5, "Progressive tech_crb_right_claw", "Crustacean Tech: Natural Selection"),
    112824: itemData(IC.useful, 1, "cn_tech_right_claw_4", itemType.building, 5, "Progressive tech_crb_right_claw", "Crustacean Tech: Ancestral Resilience"),
    112825: itemData(IC.useful, 1, "cn_tech_right_claw_5", itemType.building, 5, "Progressive tech_crb_right_claw", "Crustacean Tech: Unstoppable Onslaught"),
    112826: itemData(IC.useful, 1, "cn_tech_right_claw_6", itemType.building, 5, "Progressive tech_crb_right_claw", "Crustacean Tech: Elite Training Regimens"),
    112827: itemData(IC.useful, 1, "cn_tech_right_claw_6b", itemType.building, 6, "Progressive tech_crb_right_claw", "Crustacean Tech: Mighty Champions"),
    112828: itemData(IC.useful, 1, "cn_tech_right_claw_7", itemType.building, 6, "Progressive tech_crb_right_claw", "Crustacean Tech: Transcribe Ancient Texts"),
    112829: itemData(IC.useful, 1, "cn_tech_right_claw_7b", itemType.building, 6, "Progressive tech_crb_right_claw", "Crustacean Tech: Hardshell Elites"),
    112830: itemData(IC.useful, 1, "cn_tech_right_claw_8", itemType.building, 7, "Progressive tech_crb_right_claw", "Crustacean Tech: Awakening of the Elders"),
    112831: itemData(IC.useful, 1, "cn_tech_right_claw_9", itemType.building, 8, "Progressive tech_crb_right_claw", "Crustacean Tech: Crustacean Supremacy"),

    112832: itemData(IC.useful, 1, "cn_tech_left_leg_0", itemType.building, 1, "Progressive tech_crb_left_leg", "Crustacean Tech: Cast Expansion"),
    112833: itemData(IC.useful, 1, "cn_tech_left_leg_1", itemType.building, 2, "Progressive tech_crb_left_leg", "Crustacean Tech: Long Term Planning"),
    112834: itemData(IC.useful, 1, "cn_tech_left_leg_2", itemType.building, 2, "Progressive tech_crb_left_leg", "Crustacean Tech: Coastline Development"),
    112835: itemData(IC.useful, 1, "cn_tech_left_leg_3", itemType.building, 2, "Progressive tech_crb_left_leg", "Crustacean Tech: Crusty Tax Reforms"),
    112836: itemData(IC.useful, 1, "cn_tech_left_leg_4", itemType.building, 2, "Progressive tech_crb_left_leg", "Crustacean Tech: Kelp Farming Techniques"),

    112837: itemData(IC.useful, 1, "cn_tech_right_leg_0", itemType.building, 1, "Progressive tech_crb_right_leg", "Crustacean Tech: Crab King's Tithes"),
    112838: itemData(IC.useful, 1, "cn_tech_right_leg_1", itemType.building, 2, "Progressive tech_crb_right_leg", "Crustacean Tech: Clawkin Solidarity"),
    112839: itemData(IC.useful, 1, "cn_tech_right_leg_2", itemType.building, 2, "Progressive tech_crb_right_leg", "Crustacean Tech: Inspect Foreign Visitors"),
    112840: itemData(IC.useful, 1, "cn_tech_right_leg_3", itemType.building, 2, "Progressive tech_crb_right_leg", "Crustacean Tech: Coral Healing Serum"),
    112841: itemData(IC.useful, 1, "cn_tech_right_leg_4", itemType.building, 2, "Progressive tech_crb_right_leg", "Crustacean Tech: Crustworthy Allies"),
}

progUnits: dict[int, itemData] = {
    113200: itemData(IC.useful, 4, "Progressive crb_inf", itemType.unit, 4, None, "Progressive Crustacean Unit: Infantry"),
    113201: itemData(IC.useful, 3, "Progressive crb_rng", itemType.unit, 3, None, "Progressive Crustacean Unit: Ranged"),
    113202: itemData(IC.useful, 3, "Progressive crb_cav", itemType.unit, 3, None, "Progressive Crustacean Unit: Cavalry"),
    113203: itemData(IC.useful, 3, "Progressive crb_art", itemType.unit, 3, None, "Progressive Crustacean Unit: Artillery"),
    113204: itemData(IC.useful, 1, "Progressive crb_veh", itemType.unit, 1, None, "Progressive Crustacean Unit: Vehicle"),
    113205: itemData(IC.useful, 4, "Progressive crb_bst", itemType.unit, 4, None, "Progressive Crustacean Unit: Beast"),
    113206: itemData(IC.useful, 1, "Progressive crb_hro", itemType.unit, 1, None, "Progressive Crustacean Unit: Hero"),
}

progBuildings: dict[int, itemData] = {
    113300: itemData(IC.useful, 3, "Progressive crb_settlement_minor", itemType.building, 3, None, "Crustacean Building: Settlement Minor"),
    113301: itemData(IC.useful, 5, "Progressive crb_settlement_major", itemType.building, 5, None, "Crustacean Building: Settlement Major"),
    113302: itemData(IC.useful, 3, "Progressive crb_garrison_major", itemType.building, 3, None, "Crustacean Building: Garrison Major"),
    113303: itemData(IC.useful, 2, "Progressive crb_garrison_minor", itemType.building, 2, None, "Crustacean Building: Garrison Minor"),
    113304: itemData(IC.useful, 3, "Progressive crb_farms", itemType.building, 3, None, "Crustacean Building: Farms"),
    113305: itemData(IC.useful, 3, "Progressive crb_industry", itemType.building, 3, None, "Crustacean Building: Industry"),
    113306: itemData(IC.useful, 3, "Progressive crb_order", itemType.building, 3, None, "Crustacean Building: Infrastructure"),
    113307: itemData(IC.useful, 3, "Progressive crb_port", itemType.building, 3, None, "Crustacean Building: Port"),
    113308: itemData(IC.useful, 2, "Progressive crb_beast_barracks", itemType.building, 2, None, "Crustacean Building: Beast Pens"),
    113309: itemData(IC.useful, 3, "Progressive crb_warrior_barracks", itemType.building, 3, None, "Crustacean Building: Barracks"),
    113310: itemData(IC.useful, 3, "Progressive crb_royal_barracks", itemType.building, 3, None, "Crustacean Building: Royal Barracks"),
    113311: itemData(IC.useful, 3, "Progressive crb_foreign_slot_discovery", itemType.building, 3, None, "Crustacean Building: Protection"),
    113312: itemData(IC.useful, 3, "Progressive crb_shells", itemType.building, 3, None, "Crustacean Building: Management"),
    113313: itemData(IC.useful, 3, "Progressive crb_gunpowder_barracks", itemType.building, 3, None, "Crustacean Building: Gunnery"),
    113314: itemData(IC.useful, 3, "Progressive crb_monster_barracks", itemType.building, 3, None, "Crustacean Building: Hardshell Colosseum"),
    113315: itemData(IC.useful, 4, "Progressive crb_cult_barracks", itemType.building, 4, None, "Crustacean Building: Worship"),
    113316: itemData(IC.useful, 2, "Progressive crb_forge", itemType.building, 2, None, "Crustacean Building: Forge"),
    113317: itemData(IC.useful, 1, "Progressive crb_research", itemType.building, 1, None, "Crustacean Building: Tidestone"),
    113318: itemData(IC.useful, 3, "Progressive crb_resource_animals", itemType.building, 3, None, "Crustacean Building: Animals"),
    113319: itemData(IC.useful, 3, "Progressive crb_resource_dyes", itemType.building, 3, None, "Crustacean Building: Dyes"),
    113320: itemData(IC.useful, 3, "Progressive crb_resource_furs", itemType.building, 3, None, "Crustacean Building: Furs"),
    113321: itemData(IC.useful, 3, "Progressive crb_resource_gems", itemType.building, 3, None, "Crustacean Building: Gemstones"),
    113322: itemData(IC.useful, 3, "Progressive crb_resource_gold", itemType.building, 3, None, "Crustacean Building: Gold"),
    113323: itemData(IC.useful, 3, "Progressive crb_resource_iron", itemType.building, 3, None, "Crustacean Building: Iron"),
    113324: itemData(IC.useful, 3, "Progressive crb_resource_ivory", itemType.building, 3, None, "Crustacean Building: Ivory"),
    113325: itemData(IC.useful, 3, "Progressive crb_resource_marble", itemType.building, 3, None, "Crustacean Building: Marble"),
    113326: itemData(IC.useful, 3, "Progressive crb_resource_medicine", itemType.building, 3, None, "Crustacean Building: Medicine"),
    113327: itemData(IC.useful, 3, "Progressive crb_resource_obsidian", itemType.building, 3, None, "Crustacean Building: Obsidian"),
    113328: itemData(IC.useful, 3, "Progressive crb_resource_pasture", itemType.building, 3, None, "Crustacean Building: Pastures"),
    113329: itemData(IC.useful, 3, "Progressive crb_resource_pottery", itemType.building, 3, None, "Crustacean Building: Pottery"),
    113330: itemData(IC.useful, 3, "Progressive crb_resource_salt", itemType.building, 3, None, "Crustacean Building: Salt"),
    113331: itemData(IC.useful, 3, "Progressive crb_resource_spices", itemType.building, 3, None, "Crustacean Building: Spices"),
    113332: itemData(IC.useful, 3, "Progressive crb_resource_wine", itemType.building, 3, None, "Crustacean Building: Wine"),
    113333: itemData(IC.useful, 3, "Progressive crb_resource_wood", itemType.building, 3, None, "Crustacean Building: Lumber"),
}

progTechs: dict[int, itemData] = {
    113401: itemData(IC.useful, 2, "Progressive tech_crb_head", itemType.building, 2, None, "Progressive Crustacean Tech: Martial Claw"),
    113416: itemData(IC.useful, 8, "Progressive tech_crb_left_claw", itemType.building, 8, None, "Progressive Crustacean Tech: Crustacean Dominion"),
    113431: itemData(IC.useful, 8, "Progressive tech_crb_right_claw", itemType.building, 8, None, "Progressive Crustacean Tech: Crustacean Supremacy"),
    113436: itemData(IC.useful, 2, "Progressive tech_crb_left_leg", itemType.building, 2, None, "Progressive Crustacean Tech: Kelp Farming Techniques"),
    113441: itemData(IC.useful, 2, "Progressive tech_crb_right_leg", itemType.building, 2, None, "Progressive Crustacean Tech: Crustworthy Allies"),
}

special: dict[int, specialItemData] = {
    113500: specialItemData(IC.useful, 1, "mixer_cn_nuja", "CN_crab_knight_special_gw", itemType.unit, 1, "Progressive crb_cav", False, False, "Crustacean Unit: Knights of the Raging Claw"),
    113501: specialItemData(IC.useful, 1, "mixer_cn_nuja", "CN_crab_knight_special_jav", itemType.unit, 1, "Progressive crb_cav", False, False, "Crustacean Unit: Knights of the Weeping Shell"),
    113502: specialItemData(IC.useful, 1, "mixer_cn_nuja", "CN_crab_knight_special_pearl", itemType.unit, 1, "Progressive crb_cav", False, False, "Crustacean Unit: Knights of the Argent Pearl"),
    113503: specialItemData(IC.useful, 1, "mixer_cn_nuja", "CN_crab_knight_special_shrimp", itemType.unit, 1, "Progressive crb_cav", False, False, "Crustacean Unit: Knights of the Valiant Prawn"),

    113504: specialItemData(IC.useful, 1, "mixer_cn_warlord", "CN_tidelord_warriors", itemType.unit, 2, "Progressive crb_inf", False, False, "Crustacean Unit: Tideguard Warriors"),
    113505: specialItemData(IC.useful, 1, "mixer_cn_warlord", "CN_tidelord_slingers", itemType.unit, 2, "Progressive crb_rng", False, False, "Crustacean Unit: Tideguard Slingers"),
    113506: specialItemData(IC.useful, 1, "mixer_cn_warlord", "CN_tidelord_knights", itemType.unit, 2, "Progressive crb_cav", False, False, "Crustacean Unit: Tideguard Knights"),

    113507: specialItemData(IC.useful, 1, "mixer_cn_hunter", "cn_hunter_tech_1", itemType.tech, 2, "Progressive tech_crb_hunter", False, False, "Crustacean Tech: Greater Good"),
    113508: specialItemData(IC.useful, 1, "mixer_cn_hunter", "cn_hunter_tech_2", itemType.tech, 2, "Progressive tech_crb_hunter", False, False, "Crustacean Tech: Full Mobilisation"),
    113509: specialItemData(IC.useful, 1, "mixer_cn_hunter", "cn_hunter_tech_3", itemType.tech, 2, "Progressive tech_crb_hunter", False, False, "Crustacean Tech: Loot Wagons"),
    113510: specialItemData(IC.useful, 1, "mixer_cn_hunter", "cn_hunter_tech_4", itemType.tech, 2, "Progressive tech_crb_hunter", False, False, "Crustacean Tech: One with the Land"),
    113511: specialItemData(IC.useful, 2, "mixer_cn_hunter", "Progressive tech_crb_hunter", itemType.tech, 2, None, False, False, "Progressive Crustacean Tech: Assembly"),

    113512: specialItemData(IC.useful, 1, "mixer_cn_hunter", "cn_hunter_ranger_outpost", itemType.building, 0, "Progressive crb_outpost", False, False, "Crustacean Building: Ranger Outpost"),
    113513: specialItemData(IC.useful, 1, "mixer_cn_hunter", "Progressive crb_outpost", itemType.building, 1, None, False, False, "Progressive Crustacean Building: Outpost"),

    113514: specialItemData(IC.useful, 1, "mixer_cn_nuja", "cn_knights_pearl_1", itemType.building, 0, "Progressive crb_knights", False, False, "Crustacean Building: Argent Pearl Chapterhouse"),
    113515: specialItemData(IC.useful, 1, "mixer_cn_nuja", "cn_knights_pearl_2", itemType.building, 1, "Progressive crb_knights", False, False, "Crustacean Building: Argent Pearl Keep"),
    113516: specialItemData(IC.useful, 1, "mixer_cn_nuja", "cn_knights_shrimp_1", itemType.building, 0, "Progressive crb_knights", False, False, "Crustacean Building: Valiant Prawn Chapterhouse"),
    113517: specialItemData(IC.useful, 1, "mixer_cn_nuja", "cn_knights_shrimp_2", itemType.building, 1, "Progressive crb_knights", False, False, "Crustacean Building: Valiant Prawn Keep"),
    113518: specialItemData(IC.useful, 1, "mixer_cn_nuja", "cn_knights_gw_1", itemType.building, 0, "Progressive crb_knights", False, False, "Crustacean Building: Raging Claw Chapterhouse"),
    113519: specialItemData(IC.useful, 1, "mixer_cn_nuja", "cn_knights_gw_2", itemType.building, 1, "Progressive crb_knights", False, False, "Crustacean Building: Raging Claw Keep"),
    113520: specialItemData(IC.useful, 1, "mixer_cn_nuja", "cn_knights_jav_1", itemType.building, 0, "Progressive crb_knights", False, False, "Crustacean Building: Weeping Shell Chapterhouse"),
    113521: specialItemData(IC.useful, 1, "mixer_cn_nuja", "cn_knights_jav_2", itemType.building, 1, "Progressive crb_knights", False, False, "Crustacean Building: Weeping Shell Keep"),
    113522: specialItemData(IC.useful, 2, "mixer_cn_nuja", "Progressive crb_knights", itemType.building, 2, None, False, False, "Progressive Crustacean Building: Knights"),

    113523: specialItemData(IC.useful, 1, "mixer_cn_reefspeaker", "cn_reefspeaker_chain_1", itemType.building, 0, "Progressive crb_reef", False, False, "Crustacean Building: Great Reef Sanctuary"),
    113524: specialItemData(IC.useful, 1, "mixer_cn_reefspeaker", "cn_reefspeaker_chain_2", itemType.building, 1, "Progressive crb_reef", False, False, "Crustacean Building: Thriving Great Reef Sanctuary"),
    113525: specialItemData(IC.useful, 2, "mixer_cn_reefspeaker", "Progressive crb_reef", itemType.building, 2, None, False, False, "Progressive Crustacean Building: Reef"),

    113526: specialItemData(IC.useful, 1, "mixer_cn_ancient", "cn_ancient_sanctuary_base", itemType.building, 0, "Progressive crb_sanctuary", False, False, "Crustacean Sanctuary: Ancient Sanctuary"),
    113527: specialItemData(IC.useful, 1, "mixer_cn_ancient", "cn_ancient_sanctuary_attack_1", itemType.building, 1, "Progressive crb_sanctuary", False, False, "Crustacean Sanctuary: Attack"),
    113528: specialItemData(IC.useful, 1, "mixer_cn_ancient", "cn_ancient_sanctuary_attack_2", itemType.building, 2, "Progressive crb_sanctuary", False, False, "Crustacean Sanctuary: Greater Attack"),
    113529: specialItemData(IC.useful, 1, "mixer_cn_ancient", "cn_ancient_sanctuary_attack_3", itemType.building, 3, "Progressive crb_sanctuary", False, False, "Crustacean Sanctuary: Grand Attack"),
    113530: specialItemData(IC.useful, 1, "mixer_cn_ancient", "cn_ancient_sanctuary_defence_1", itemType.building, 1, "Progressive crb_sanctuary", False, False, "Crustacean Sanctuary: Defence"),
    113531: specialItemData(IC.useful, 1, "mixer_cn_ancient", "cn_ancient_sanctuary_defence_2", itemType.building, 2, "Progressive crb_sanctuary", False, False, "Crustacean Sanctuary: Greater Defence"),
    113532: specialItemData(IC.useful, 1, "mixer_cn_ancient", "cn_ancient_sanctuary_defence_3", itemType.building, 3, "Progressive crb_sanctuary", False, False, "Crustacean Sanctuary: Grand Defence"),
    113533: specialItemData(IC.useful, 1, "mixer_cn_ancient", "cn_ancient_sanctuary_shells_1", itemType.building, 1, "Progressive crb_sanctuary", False, False, "Crustacean Sanctuary: Shells"),
    113534: specialItemData(IC.useful, 1, "mixer_cn_ancient", "cn_ancient_sanctuary_shells_2", itemType.building, 2, "Progressive crb_sanctuary", False, False, "Crustacean Sanctuary: Greater Shells"),
    113535: specialItemData(IC.useful, 1, "mixer_cn_ancient", "cn_ancient_sanctuary_shells_3", itemType.building, 3, "Progressive crb_sanctuary", False, False, "Crustacean Sanctuary: Grand Shells"),
    113536: specialItemData(IC.useful, 1, "mixer_cn_ancient", "cn_ancient_sanctuary_gold_1", itemType.building, 1, "Progressive crb_sanctuary", False, False, "Crustacean Sanctuary: Income"),
    113537: specialItemData(IC.useful, 1, "mixer_cn_ancient", "cn_ancient_sanctuary_gold_2", itemType.building, 2, "Progressive crb_sanctuary", False, False, "Crustacean Sanctuary: Greater Income"),
    113538: specialItemData(IC.useful, 1, "mixer_cn_ancient", "cn_ancient_sanctuary_gold_3", itemType.building, 3, "Progressive crb_sanctuary", False, False, "Crustacean Sanctuary: Grand Income"),
    113539: specialItemData(IC.useful, 1, "mixer_cn_ancient", "cn_ancient_sanctuary_ranged_1", itemType.building, 1, "Progressive crb_sanctuary", False, False, "Crustacean Sanctuary: Ranged"),
    113540: specialItemData(IC.useful, 1, "mixer_cn_ancient", "cn_ancient_sanctuary_ranged_2", itemType.building, 2, "Progressive crb_sanctuary", False, False, "Crustacean Sanctuary: Greater Ranged"),
    113541: specialItemData(IC.useful, 1, "mixer_cn_ancient", "cn_ancient_sanctuary_ranged_3", itemType.building, 3, "Progressive crb_sanctuary", False, False, "Crustacean Sanctuary: Grand Ranged"),
    113542: specialItemData(IC.useful, 4, "mixer_cn_ancient", "Progressive crb_sanctuary", itemType.building, 4, None, False, False, "Progressive Crustacean Sanctuary: Sanctuary"),

    113543: specialItemData(IC.useful, 1, "mixer_cn_ancient", "cn_sanctuary_addon_research", itemType.building, 0, "Progressive crb_sanctuary_extra", False, False, "Crustacean Sanctuary: Sanctuary Road"),
    113544: specialItemData(IC.useful, 1, "mixer_cn_ancient", "cn_sanctuary_addon_shells", itemType.building, 0, "Progressive crb_sanctuary_extra", False, False, "Crustacean Sanctuary: Sanctuary Vault"),
    113545: specialItemData(IC.useful, 1, "mixer_cn_ancient", "cn_sanctuary_addon_garrison", itemType.building, 0, "Progressive crb_sanctuary_extra", False, False, "Crustacean Sanctuary: Sanctuary Guard"),
    113546: specialItemData(IC.useful, 1, "mixer_cn_ancient", "Progressive crb_sanctuary_extra", itemType.building, 1, None, False, False, "Progressive Crustacean Building: Sanctuary Addon"),
}