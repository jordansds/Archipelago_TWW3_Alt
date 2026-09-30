from BaseClasses import ItemClassification as IC
from worlds.tww3.dataStructs import itemType, itemData, specialItemData
# @formatter:off

#74000
units: dict[int, itemData] = {
    74000: itemData(IC.useful, 1, 'wh_main_vmp_inf_zombie', itemType.unit, 1, 'Progressive nag_inf', 'Nagash Unit: Zombies'),
    74001: itemData(IC.useful, 1, 'wh_main_vmp_inf_skeleton_warriors_1', itemType.unit, 1, 'Progressive nag_inf', 'Nagash Unit: Skeleton Spearmen'),
    74002: itemData(IC.useful, 1, 'wh_main_vmp_inf_skeleton_warriors_0', itemType.unit, 1, 'Progressive nag_inf', 'Nagash Unit: Skeleton Warriors'),
    74003: itemData(IC.useful, 1, 'wh_main_vmp_inf_crypt_ghouls', itemType.unit, 1, 'Progressive nag_inf', 'Nagash Unit: Crypt Ghouls'),
    74004: itemData(IC.useful, 1, 'wh2_dlc09_tmb_inf_skeleton_warriors_0', itemType.unit, 1, 'Progressive nag_inf', 'Nagash Unit: Skeleton Warriors'),
    74005: itemData(IC.useful, 1, 'wh2_dlc09_tmb_inf_skeleton_spearmen_0', itemType.unit, 1, 'Progressive nag_inf', 'Nagash Unit: Skeleton Spearmen'),
    74006: itemData(IC.useful, 1, 'wh2_dlc09_tmb_inf_nehekhara_warriors_0', itemType.unit, 1, 'Progressive nag_inf', 'Nagash Unit: Nehekharan Warriors'),
    74007: itemData(IC.useful, 1, 'wh2_dlc11_cst_inf_zombie_deckhands_mob_0', itemType.unit, 1, 'Progressive nag_inf', 'Nagash Unit: Zombie Pirate Deckhand Mob'),
    74008: itemData(IC.useful, 1, 'wh2_dlc11_cst_inf_zombie_deckhands_mob_1', itemType.unit, 1, 'Progressive nag_inf', 'Nagash Unit: Zombie Pirate Deckhand Mob (Polearms)'),
    74009: itemData(IC.useful, 1, 'wh_main_vmp_inf_grave_guard_0', itemType.unit, 2, 'Progressive nag_inf', 'Nagash Unit: Grave Guard'),
    74010: itemData(IC.useful, 1, 'wh2_dlc09_tmb_inf_tomb_guard_0', itemType.unit, 2, 'Progressive nag_inf', 'Nagash Unit: Tomb Guard'),
    74011: itemData(IC.useful, 1, 'wh2_dlc09_tmb_mon_ushabti_0', itemType.unit, 2, 'Progressive nag_inf', 'Nagash Unit: Ushabti'),
    74012: itemData(IC.useful, 1, 'wh3_main_vmp_inf_grave_guard_2', itemType.unit, 3, 'Progressive nag_inf', 'Nagash Unit: Grave Guard (Halberds)'),
    74013: itemData(IC.useful, 1, 'wh_main_vmp_inf_grave_guard_1', itemType.unit, 3, 'Progressive nag_inf', 'Nagash Unit: Grave Guard (Great Weapons)'),
    74014: itemData(IC.useful, 1, 'wh_main_vmp_inf_cairn_wraiths', itemType.unit, 3, 'Progressive nag_inf', 'Nagash Unit: Cairn Wraiths'),
    74015: itemData(IC.useful, 1, 'wh2_dlc09_tmb_inf_tomb_guard_1', itemType.unit, 3, 'Progressive nag_inf', 'Nagash Unit: Tomb Guard (Halberds)'),
    74016: itemData(IC.useful, 1, 'wh2_dlc11_cst_inf_syreens', itemType.unit, 3, 'Progressive nag_inf', 'Nagash Unit: Syreens'),
    74017: itemData(IC.useful, 1, 'wh2_dlc11_cst_inf_depth_guard_0', itemType.unit, 4, 'Progressive nag_inf', 'Nagash Unit: Depth Guard'),
    74018: itemData(IC.useful, 1, 'wh2_dlc11_cst_inf_depth_guard_1', itemType.unit, 4, 'Progressive nag_inf', 'Nagash Unit: Depth Guard (Polearms)'),
    74019: itemData(IC.useful, 1, 'wh3_dlc29_vmp_inf_lahmian_handmaidens_death', itemType.unit, 5, 'Progressive nag_inf', 'Nagash Unit: Lahmian Handmaidens (Death)'),
    74020: itemData(IC.useful, 1, 'wh3_dlc29_vmp_inf_lahmian_handmaidens_shadow', itemType.unit, 5, 'Progressive nag_inf', 'Nagash Unit: Lahmian Handmaidens (Shadows)'),

    74021: itemData(IC.useful, 1, 'wh2_dlc09_tmb_inf_skeleton_archers_0', itemType.unit, 1, 'Progressive nag_rng', 'Nagash Unit: Skeleton Archers'),
    74022: itemData(IC.useful, 1, 'wh2_dlc11_cst_inf_zombie_gunnery_mob_0', itemType.unit, 1, 'Progressive nag_rng', 'Nagash Unit: Zombie Pirate Gunnery Mob'),
    74023: itemData(IC.useful, 1, 'wh2_dlc11_cst_inf_zombie_gunnery_mob_3', itemType.unit, 1, 'Progressive nag_rng', 'Nagash Unit: Zombie Pirate Gunnery Mob (Bombers)'),
    74024: itemData(IC.useful, 1, 'wh2_dlc09_tmb_mon_ushabti_1', itemType.unit, 2, 'Progressive nag_rng', 'Nagash Unit: Ushabti (Great Bows)'),
    74025: itemData(IC.useful, 1, 'wh2_dlc11_cst_inf_zombie_gunnery_mob_1', itemType.unit, 2, 'Progressive nag_rng', 'Nagash Unit: Zombie Pirate Gunnery Mob (Handgunners)'),
    74026: itemData(IC.useful, 1, 'wh2_dlc11_cst_inf_zombie_gunnery_mob_2', itemType.unit, 2, 'Progressive nag_rng', 'Nagash Unit: Zombie Pirate Gunnery Mob (Hand Cannons)'),
    74027: itemData(IC.useful, 1, 'wh2_dlc11_cst_inf_deck_gunners_0', itemType.unit, 3, 'Progressive nag_rng', 'Nagash Unit: Deck Gunners'),
    74028: itemData(IC.useful, 1, 'wh2_dlc11_cst_mon_rotting_prometheans_gunnery_mob_0', itemType.unit, 4, 'Progressive nag_rng', 'Nagash Unit: Rotting Prometheans (Gunnery Mob)'),

    74029: itemData(IC.useful, 1, 'wh2_dlc09_tmb_cav_skeleton_horsemen_0', itemType.unit, 1, 'Progressive nag_cav', 'Nagash Unit: Skeleton Horsemen'),
    74030: itemData(IC.useful, 1, 'wh2_dlc09_tmb_cav_skeleton_horsemen_archers_0', itemType.unit, 1, 'Progressive nag_cav', 'Nagash Unit: Skeleton Horse Archers'),
    74031: itemData(IC.useful, 1, 'wh2_dlc11_cst_cav_deck_droppers_0', itemType.unit, 1, 'Progressive nag_cav', 'Nagash Unit: Deck Droppers'),
    74032: itemData(IC.useful, 1, 'wh2_dlc09_tmb_cav_nehekhara_horsemen_0', itemType.unit, 2, 'Progressive nag_cav', 'Nagash Unit: Nehekharan Horsemen'),
    74033: itemData(IC.useful, 1, 'wh2_dlc11_cst_cav_deck_droppers_1', itemType.unit, 2, 'Progressive nag_cav', 'Nagash Unit: Deck Droppers (Bombers)'),
    74034: itemData(IC.useful, 1, 'wh_main_vmp_cav_black_knights_0', itemType.unit, 3, 'Progressive nag_cav', 'Nagash Unit: Black Knights'),
    74035: itemData(IC.useful, 1, 'wh_main_vmp_cav_black_knights_3', itemType.unit, 3, 'Progressive nag_cav', 'Nagash Unit: Black Knights (Lances & Barding)'),
    74036: itemData(IC.useful, 1, 'wh2_dlc09_tmb_mon_sepulchral_stalkers_0', itemType.unit, 3, 'Progressive nag_cav', 'Nagash Unit: Sepulchral Stalkers'),
    74037: itemData(IC.useful, 1, 'wh2_dlc11_cst_cav_deck_droppers_2', itemType.unit, 3, 'Progressive nag_cav', 'Nagash Unit: Deck Droppers (Handgunners)'),
    74038: itemData(IC.useful, 1, 'wh_main_vmp_cav_hexwraiths', itemType.unit, 4, 'Progressive nag_cav', 'Nagash Unit: Hexwraiths'),
    74039: itemData(IC.useful, 1, 'wh2_dlc09_tmb_cav_necropolis_knights_0', itemType.unit, 4, 'Progressive nag_cav', 'Nagash Unit: Necropolis Knights'),
    74040: itemData(IC.useful, 1, 'wh2_dlc09_tmb_cav_necropolis_knights_1', itemType.unit, 4, 'Progressive nag_cav', 'Nagash Unit: Necropolis Knights (Halberds)'),
    74041: itemData(IC.useful, 1, 'wh3_main_vmp_blood_knights_sword_shield', itemType.unit, 5, 'Progressive nag_cav', 'Nagash Unit: Blood Knights'),
    74042: itemData(IC.useful, 1, 'wh_dlc02_vmp_cav_blood_knights_0', itemType.unit, 5, 'Progressive nag_cav', 'Nagash Unit: Blood Knights (Lances)'),

    74043: itemData(IC.useful, 1, 'wh2_dlc11_cst_art_mortar', itemType.unit, 1, 'Progressive nag_art', 'Nagash Unit: Mortars'),
    74044: itemData(IC.useful, 1, 'wh2_dlc11_cst_art_carronade', itemType.unit, 1, 'Progressive nag_art', 'Nagash Unit: Carronades'),
    74045: itemData(IC.useful, 1, 'wh2_dlc09_tmb_art_screaming_skull_catapult_0', itemType.unit, 2, 'Progressive nag_art', 'Nagash Unit: Screaming Skull Catapults'),
    74046: itemData(IC.useful, 1, 'wh2_dlc09_tmb_art_casket_of_souls_0', itemType.unit, 2, 'Progressive nag_art', 'Nagash Unit: Casket of Souls'),
    74047: itemData(IC.useful, 1, 'wh2_pro06_tmb_mon_bone_giant_0', itemType.unit, 3, 'Progressive nag_art', 'Nagash Unit: Bone Giant'),
    
    74048: itemData(IC.useful, 1, 'wh_dlc04_vmp_veh_corpse_cart_0', itemType.unit, 1, 'Progressive nag_veh', 'Nagash Unit: Corpse Cart'),
    74049: itemData(IC.useful, 1, 'wh_dlc04_vmp_veh_corpse_cart_1', itemType.unit, 2, 'Progressive nag_veh', 'Nagash Unit: Corpse Cart (Balefire)'),
    74050: itemData(IC.useful, 1, 'wh2_dlc09_tmb_veh_skeleton_chariot_0', itemType.unit, 2, 'Progressive nag_veh', 'Nagash Unit: Skeleton Chariots'),
    74051: itemData(IC.useful, 1, 'wh2_dlc09_tmb_veh_skeleton_archer_chariot_0', itemType.unit, 2, 'Progressive nag_veh', 'Nagash Unit: Skeleton Archer Chariots'),
    74052: itemData(IC.useful, 1, 'wh_dlc04_vmp_veh_corpse_cart_2', itemType.unit, 3, 'Progressive nag_veh', 'Nagash Unit: Corpse Cart (Unholy Lodestone)'),
    74053: itemData(IC.useful, 1, 'wh_main_vmp_veh_black_coach', itemType.unit, 3, 'Progressive nag_veh', 'Nagash Unit: Black Coach'),
    74054: itemData(IC.useful, 1, 'wh_dlc04_vmp_veh_mortis_engine_0', itemType.unit, 4, 'Progressive nag_veh', 'Nagash Unit: Mortis Engine'),

    74055: itemData(IC.useful, 1, 'wh_main_vmp_mon_fell_bats', itemType.unit, 1, 'Progressive nag_bst', 'Nagash Unit: Fell Bats'),
    74056: itemData(IC.useful, 1, 'wh_main_vmp_mon_dire_wolves', itemType.unit, 1, 'Progressive nag_bst', 'Nagash Unit: Dire Wolves'),
    74057: itemData(IC.useful, 1, 'wh2_dlc09_tmb_mon_carrion_0', itemType.unit, 1, 'Progressive nag_bst', 'Nagash Unit: Carrion'),
    74058: itemData(IC.useful, 1, 'wh2_dlc11_cst_mon_bloated_corpse_0', itemType.unit, 1, 'Progressive nag_bst', 'Nagash Unit: Bloated Corpse'),
    74059: itemData(IC.useful, 1, 'wh_main_vmp_mon_crypt_horrors', itemType.unit, 2, 'Progressive nag_bst', 'Nagash Unit: Crypt Horrors'),
    74060: itemData(IC.useful, 1, 'wh2_dlc11_cst_mon_mournguls_0', itemType.unit, 2, 'Progressive nag_bst', 'Nagash Unit: Mournguls'),
    74061: itemData(IC.useful, 1, 'wh2_dlc09_tmb_mon_tomb_scorpion_0', itemType.unit, 2, 'Progressive nag_bst', 'Nagash Unit: Tomb Scorpion'),
    74062: itemData(IC.useful, 1, 'wh2_dlc11_cst_mon_animated_hulks_0', itemType.unit, 2, 'Progressive nag_bst', 'Nagash Unit: Animated Hulks'),
    74063: itemData(IC.useful, 1, 'wh2_dlc11_cst_mon_rotting_prometheans_0', itemType.unit, 2, 'Progressive nag_bst', 'Nagash Unit: Rotting Prometheans'),
    74064: itemData(IC.useful, 1, 'wh_main_vmp_mon_vargheists', itemType.unit, 3, 'Progressive nag_bst', 'Nagash Unit: Vargheists'),
    74065: itemData(IC.useful, 1, 'wh_main_vmp_mon_varghulf', itemType.unit, 3, 'Progressive nag_bst', 'Nagash Unit: Varghulf'),
    74066: itemData(IC.useful, 1, 'wh2_dlc09_tmb_mon_khemrian_warsphinx_0', itemType.unit, 4, 'Progressive tmb_bst', 'Nagash Unit: Warsphinx'),
    74067: itemData(IC.useful, 1, 'wh_main_vmp_mon_terrorgheist', itemType.unit, 5, 'Progressive nag_bst', 'Nagash Unit: Terrorgheist'),
    74068: itemData(IC.useful, 1, 'wh2_dlc09_tmb_mon_necrosphinx_0', itemType.unit, 5, 'Progressive nag_bst', 'Nagash Unit: Necrosphinx'),
    74069: itemData(IC.useful, 1, 'wh2_dlc09_tmb_mon_heirotitan_0', itemType.unit, 5, 'Progressive nag_bst', 'Nagash Unit: Hierotitan'),
    74070: itemData(IC.useful, 1, 'wh3_dlc29_tmb_mon_khemric_titan', itemType.unit, 5, 'Progressive nag_bst', 'Nagash Unit: Khemric Titan'),
    74071: itemData(IC.useful, 1, 'wh2_dlc11_cst_mon_rotting_leviathan_0', itemType.unit, 5, 'Progressive nag_bst', 'Nagash Unit: Rotting Leviathan'),
    74072: itemData(IC.useful, 1, 'wh2_dlc11_cst_mon_necrofex_colossus_0', itemType.unit, 5, 'Progressive nag_bst', 'Nagash Unit: Necrofex Colossus'),

    #52049: itemData(IC.useful, 1, 'wh_dlc04_vmp_veh_claw_of_nagash_0', itemType.unit, 4, 'Progressive nag_veh', 'Nagash Unit: The Claw of Nagash (Mortis Engine)'),
    #52050: itemData(IC.useful, 1, 'wh_dlc04_vmp_mon_direpack_0', itemType.unit, 1, 'Progressive nag_inf', 'Nagash Unit: The Direpack (Dire Wolves)'),
    #52051: itemData(IC.useful, 1, 'wh_dlc04_vmp_mon_devils_swartzhafen_0', itemType.unit, 3, 'Progressive nag_inf', 'Nagash Unit: The Devils of Swartzhafen (Vargheists)'),
    #52052: itemData(IC.useful, 1, 'wh_dlc04_vmp_inf_tithe_0', itemType.unit, 1, 'Progressive nag_inf', 'Nagash Unit: The Tithe (Zombies)'),
    #52053: itemData(IC.useful, 1, 'wh_dlc04_vmp_inf_sternsmen_0', itemType.unit, 2, 'Progressive nag_inf', 'Nagash Unit: The Sternsmen (Grave Guard)'),
    #52054: itemData(IC.useful, 1, 'wh_dlc04_vmp_inf_konigstein_stalkers_0', itemType.unit, 1, 'Progressive nag_inf', 'Nagash Unit: The Konigstein Stalkers (Skeleton Warriors)'),
    #52055: itemData(IC.useful, 1, 'wh_dlc04_vmp_inf_feasters_in_the_dusk_0', itemType.unit, 1, 'Progressive nag_inf', 'Nagash Unit: The Feasters in the Dusk (Crypt Ghouls)'),
    #52056: itemData(IC.useful, 1, 'wh_dlc04_vmp_cav_vereks_reavers_0', itemType.unit, 2, 'Progressive nag_cav', "Nagash Unit: Verek's Reavers (Black Knights - Lances & Barding)"),
    #52057: itemData(IC.useful, 1, 'wh_dlc04_vmp_cav_chillgheists_0', itemType.unit, 2, 'Progressive nag_cav', 'Nagash Unit: The Chillgheists (Hexwraiths)'),

    #50031: itemData(IC.useful, 1, 'wh2_dlc11_cst_inf_depth_guard_ror_0', itemType.unit, 4, 'Progressive nag_inf', 'Nagash Unit: The Bloody Reaver Deck Guard (Depth Guard)'),
    #50032: itemData(IC.useful, 1, 'wh2_dlc11_cst_inf_deck_gunners_ror_0', itemType.unit, 4, 'Progressive nag_rng', 'Nagash Unit: Shadewraith Gunners (Deck Gunners)'),
    #50033: itemData(IC.useful, 1, 'wh2_dlc11_cst_inf_zombie_deckhands_mob_ror_0', itemType.unit, 1, 'Progressive nag_inf', 'Nagash Unit: The Tide of Skjold (Zombie Pirate Deckhand Mob)'),
    #50034: itemData(IC.useful, 1, 'wh2_dlc11_cst_inf_zombie_gunnery_mob_ror_0', itemType.unit, 2, 'Progressive nag_rng', 'Nagash Unit: The Black Spot (Zombie Pirate Gunnery Mob - Handgunners)'),
    #50035: itemData(IC.useful, 1, 'wh2_dlc11_cst_mon_mournguls_ror_0', itemType.unit, 3, 'Progressive nag_inf', 'Nagash Unit: Night Terrors (Mournguls)'),
    #50036: itemData(IC.useful, 1, 'wh2_dlc11_cst_mon_necrofex_colossus_ror_0', itemType.unit, 5, 'Progressive nag_bst', 'Nagash Unit: Gallows Giant (Necrofex Colossus)'),
    #50037: itemData(IC.useful, 1, 'wh2_dlc11_cst_mon_rotting_prometheans_gunnery_mob_ror', itemType.unit, 4, 'Progressive nag_bst', "Nagash Unit: The Lamprey's Revenge (Rotting Promethean Gunnery Mob)"),
    #50038: itemData(IC.useful, 1, 'wh2_dlc11_cst_cav_deck_droppers_ror_0', itemType.unit, 2, 'Progressive nag_cav', 'Nagash Unit: Salt Lord Scuttlers (Deck Droppers - Bombers)')

    #46029: itemData(IC.useful, 1, 'wh2_dlc09_tmb_mon_carrion_ror', itemType.unit, 1, 'Progressive nag_bst', 'Nagash Unit: The Flock of Djaf (Carrion)'),
    #46030: itemData(IC.useful, 1, 'wh2_dlc09_tmb_mon_ushabti_ror', itemType.unit, 2, 'Progressive nag_rng', 'Nagash Unit: Chosen of the Gods (Ushabti - Great Bows)'),
    #46031: itemData(IC.useful, 1, 'wh2_dlc09_tmb_mon_sepulchral_stalkers_ror', itemType.unit, 3, 'Progressive nag_cav', 'Nagash Unit: Eyes of the Desert (Sepulchral Stalkers)'),
    #46032: itemData(IC.useful, 1, 'wh2_dlc09_tmb_mon_necrosphinx_ror', itemType.unit, 3, 'Progressive nag_bst', 'Nagash Unit: The Sphinx of Usekph (Necrosphinx)'),
    #46033: itemData(IC.useful, 1, 'wh2_dlc09_tmb_inf_tomb_guard_ror', itemType.unit, 2, 'Progressive nag_inf', 'Nagash Unit: The Khepra Guard (Tomb Guard)'),
    #46034: itemData(IC.useful, 1, 'wh2_dlc09_tmb_inf_skeleton_spearmen_ror', itemType.unit, 1, 'Progressive nag_inf', "Nagash Unit: King Nekhesh's Scorpion Legion (Skeleton Spearmen)"),
    #46035: itemData(IC.useful, 1, 'wh2_dlc09_tmb_inf_skeleton_archers_ror', itemType.unit, 1, 'Progressive nag_rng', 'Nagash Unit: Blessed Legion of Phakth (Skeleton Archers)'),
    #46036: itemData(IC.useful, 1, 'wh2_dlc09_tmb_inf_nehekhara_warriors_ror', itemType.unit, 1, 'Progressive nag_inf', "Nagash Unit: Usirian's Legion of the Netherworld (Nehekharan Warriors)"),
    #46037: itemData(IC.useful, 1, 'wh2_dlc09_tmb_cav_nehekhara_horsemen_ror', itemType.unit, 2, 'Progressive nag_cav', 'Nagash Unit: Storm Riders of Khsar (Nehekharan Horsemen)'),
    #46038: itemData(IC.useful, 1, 'wh2_dlc09_tmb_cav_necropolis_knights_ror', itemType.unit, 3, 'Progressive nag_cav', 'Nagash Unit: Venom Knights of Asaph (Necropolis Knights)')
    #46037: itemData(IC.useful, 1, 'wh3_dlc29_tmb_mon_khemric_titan_ror', itemType.unit, 3, 'Progressive tmb_bst', 'Nagash Unit: Icon of Usirian (Khemric Titan)'),
}

buildings: dict[int, itemData] = {}

#Hahaha, no.
techs: dict[int, itemData] = {}

progUnits: dict[int, itemData] = {
    47200: itemData(IC.useful, 5, "Progressive tmb_inf", itemType.unit, 5, None, "Progressive Nagash Unit: Infantry"),
    47201: itemData(IC.useful, 4, "Progressive tmb_rng", itemType.unit, 4, None, "Progressive Nagash Unit: Ranged"),
    47202: itemData(IC.useful, 5, "Progressive tmb_cav", itemType.unit, 5, None, "Progressive Nagash Unit: Cavalry"),
    47203: itemData(IC.useful, 3, "Progressive tmb_art", itemType.unit, 3, None, "Progressive Nagash Unit: Artillery"),
    47204: itemData(IC.useful, 4, "Progressive tmb_veh", itemType.unit, 4, None, "Progressive Nagash Unit: Chariot"),
    47205: itemData(IC.useful, 5, "Progressive tmb_bst", itemType.unit, 5, None, "Progressive Nagash Unit: Beast"),
}

progBuildings: dict[int, itemData] = {}

#Hahaha, no.
progTechs: dict[int, itemData] = {}

special: dict[int, specialItemData] = {}

rituals: dict[int, specialItemData] = {}