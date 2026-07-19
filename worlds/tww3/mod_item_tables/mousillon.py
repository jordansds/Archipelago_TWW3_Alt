from BaseClasses import ItemClassification as IC
from worlds.tww3.dataStructs import itemType, itemData, specialItemData

# @formatter:off

units: dict[int, itemData] = {
    102000: itemData(IC.useful, 1, 'mixu_msl_inf_men_at_arms_sword', itemType.unit, 1, 'Progressive msl_inf', 'Mousillon Unit: Men at Arms (Sword)'),
    102001: itemData(IC.useful, 1, 'mixu_msl_inf_men_at_arms_polearms', itemType.unit, 2, 'Progressive msl_inf', 'Mousillon Unit: Men at Arms (Sword)'),
    102002: itemData(IC.useful, 1, 'mixu_msl_inf_grave_guard_sword', itemType.unit, 1, 'Progressive msl_inf', 'Mousillon Unit: Grave Guard'),
    102003: itemData(IC.useful, 1, 'wh3_main_vmp_inf_grave_guard_2', itemType.unit, 2, 'Progressive msl_inf', 'Mousillon Unit: Grave Guard'),
    102004: itemData(IC.useful, 1, 'mixu_msl_inf_grave_guard_great_weapons', itemType.unit, 2, 'Progressive msl_inf', 'Mousillon Unit: Grave Guard (Great Weapons)'),
    102005: itemData(IC.useful, 1, 'mixu_msl_mon_the_grey_men', itemType.unit, 1, 'Progressive msl_inf', 'Mousillon Unit: Grey Men'),
    102006: itemData(IC.useful, 1, 'wh_main_vmp_inf_crypt_ghouls', itemType.unit, 1, 'Progressive msl_inf', 'Mousillon Unit: Crypt Ghouls'),
    102007: itemData(IC.useful, 1, 'wh_main_vmp_inf_cairn_wraiths', itemType.unit, 2, 'Progressive msl_inf', 'Mousillon Unit: Cairn Wraiths'),
    102008: itemData(IC.useful, 1, 'mixu_msl_inf_brigands', itemType.unit, 2, 'Progressive msl_inf', 'Mousillon Unit: Brigands (Polearms)'),

    102009: itemData(IC.useful, 1, 'mixu_msl_inf_bowmen', itemType.unit, 1, 'Progressive msl_rng', 'Mousillon Unit: Bowmen'),
    102010: itemData(IC.useful, 1, 'mixu_msl_inf_bowmen_poison', itemType.unit, 2, 'Progressive msl_rng', 'Mousillon Unit: Bowmen (Poison)'),
    102011: itemData(IC.useful, 1, 'mixu_msl_inf_bowmen_balefire', itemType.unit, 2, 'Progressive msl_rng', 'Mousillon Unit: Bowmen (Balefire)'),

    102012: itemData(IC.useful, 1, 'mixu_msl_inf_mounted_brigands', itemType.unit, 2, 'Progressive msl_cav', 'Mousillon Unit: Mounted Brigands'),
    102013: itemData(IC.useful, 1, 'mixu_msl_cav_black_knights_sword', itemType.unit, 1, 'Progressive msl_cav', 'Mousillon Unit: Black Knights'),
    102014: itemData(IC.useful, 1, 'mixu_msl_cav_black_knights_lance', itemType.unit, 2, 'Progressive msl_cav', 'Mousillon Unit: Black Knights (Lances & Barding)'),
    102015: itemData(IC.useful, 1, 'mixu_msl_cav_black_grail_knights', itemType.unit, 3, 'Progressive msl_cav', 'Mousillon Unit: Black Grail Knights'),
    102016: itemData(IC.useful, 1, 'wh_main_vmp_cav_hexwraiths', itemType.unit, 3, 'Progressive msl_cav', 'Mousillon Unit: Hexwraiths'),
    102017: itemData(IC.useful, 1, 'wh_dlc02_vmp_cav_blood_knights_0', itemType.unit, 4, 'Progressive msl_cav', 'Mousillon Unit: Blood Knights (Lances)'),
    102018: itemData(IC.useful, 1, 'mixu_msl_cav_hellsteed_knights', itemType.unit, 4, 'Progressive msl_cav', 'Mousillon Unit: Hellsteed Knights'),
    102019: itemData(IC.useful, 1, 'wh_dlc07_brt_cav_knights_errant_0', itemType.unit, 2, 'Progressive msl_cav', 'Mousillon Unit: Knights Errant'),
    102020: itemData(IC.useful, 1, 'wh_main_brt_cav_knights_of_the_realm', itemType.unit, 2, 'Progressive msl_cav', 'Mousillon Unit: Knights of the Realm'),
    102021: itemData(IC.useful, 1, 'wh_main_brt_cav_pegasus_knights', itemType.unit, 3, 'Progressive msl_cav', 'Mousillon Unit: Pegasus Knights'),

    102022: itemData(IC.useful, 1, 'mixu_msl_art_trebuchet', itemType.unit, 1, 'Progressive msl_art', 'Mousillon Unit: Bowmen'),
    102023: itemData(IC.useful, 1, 'mixu_msl_art_trebuchet_balefire', itemType.unit, 1, 'Progressive msl_art', 'Mousillon Unit: Bowmen'),

    102024: itemData(IC.useful, 1, 'wh_dlc04_vmp_veh_corpse_cart_0', itemType.unit, 1, 'Progressive msl_veh', 'Mousillon Unit: Corpse Cart'),
    102025: itemData(IC.useful, 1, 'wh_dlc04_vmp_veh_corpse_cart_1', itemType.unit, 2, 'Progressive msl_veh', 'Mousillon Unit: Corpse Cart (Balefire)'),
    102026: itemData(IC.useful, 1, 'wh_dlc04_vmp_veh_corpse_cart_2', itemType.unit, 3, 'Progressive msl_veh', 'Mousillon Unit: Corpse Cart (Unholy Lodestone)'),
    102027: itemData(IC.useful, 1, 'wh_main_vmp_veh_black_coach', itemType.unit, 3, 'Progressive msl_veh', 'Mousillon Unit: Black Coach'),
    102028: itemData(IC.useful, 1, 'wh_dlc04_vmp_veh_mortis_engine_0', itemType.unit, 4, 'Progressive msl_veh', 'Mousillon Unit: Mortis Engine'),

    102029: itemData(IC.useful, 1, 'wh_main_vmp_mon_fell_bats', itemType.unit, 1, 'Progressive msl_bst', 'Mousillon Unit: Fell Bats'),
    102030: itemData(IC.useful, 1, 'wh_main_vmp_mon_dire_wolves', itemType.unit, 1, 'Progressive msl_bst', 'Mousillon Unit: Dire Wolves'),
    102031: itemData(IC.useful, 1, 'wh_main_vmp_mon_crypt_horrors', itemType.unit, 2, 'Progressive msl_bst', 'Mousillon Unit: Crypt Horrors'),
    102032: itemData(IC.useful, 1, 'wh_main_vmp_mon_varghulf', itemType.unit, 2, 'Progressive msl_bst', 'Mousillon Unit: Varghulf'),
    102033: itemData(IC.useful, 1, 'wh2_dlc11_cst_mon_mournguls_0', itemType.unit, 3, 'Progressive msl_bst', 'Mousillon Unit: Mournguls'),
    102034: itemData(IC.useful, 1, 'mixu_msl_mon_giant_snail', itemType.unit, 2, 'Progressive msl_bst', 'Mousillon Unit: Giant Snail'),
    102035: itemData(IC.useful, 1, 'mixu_msl_mon_dracoleech', itemType.unit, 2, 'Progressive msl_bst', 'Mousillon Unit: Rotting Dracoleech'),

    102036: itemData(IC.useful, 1, 'mixu_msl_cha_bretonnian_wight', itemType.unit, 2, 'Progressive msl_hro', 'Mousillon Unit: Wight King'),
    102037: itemData(IC.useful, 1, 'wh_main_vmp_cha_necromancer_0', itemType.unit, 1, 'Progressive msl_hro', 'Mousillon Unit: Necromancer'),
    102038: itemData(IC.useful, 1, 'wh_main_vmp_cha_banshee', itemType.unit, 2, 'Progressive msl_hro', 'Mousillon Unit: Banshee'),
    102039: itemData(IC.useful, 1, 'mixu_msl_cha_damsel_heavens', itemType.unit, 1, 'Progressive msl_hro', 'Mousillon Unit: Damsel (Heavens)'),
    102040: itemData(IC.useful, 1, 'mixu_msl_cha_damsel_beasts', itemType.unit, 1, 'Progressive msl_hro', 'Mousillon Unit: Damsel (Beasts)'),
    102041: itemData(IC.useful, 1, 'mixu_msl_cha_damsel_shadows', itemType.unit, 1, 'Progressive msl_hro', 'Mousillon Unit: Damsel (Shadows)'),
    102042: itemData(IC.useful, 1, 'mixu_msl_cha_damsel_death', itemType.unit, 1, 'Progressive msl_hro', 'Mousillon Unit: Damsel (Death)'),
}

buildings: dict[int, itemData] = {
    102400: itemData(IC.useful, 1, 'mixu_msl_cemetary_1', itemType.building, 0, 'Progressive msl_cemetery', 'Mousillon Building: Barrow'),
    102401: itemData(IC.useful, 1, 'mixu_msl_cemetary_2', itemType.building, 1, 'Progressive msl_cemetery', 'Mousillon Building: Mausoleum'),
    102402: itemData(IC.useful, 1, 'mixu_msl_barracks_1', itemType.building, 0, 'Progressive msl_barracks', 'Mousillon Building: Training Field'),
    102403: itemData(IC.useful, 1, 'mixu_msl_barracks_2', itemType.building, 1, 'Progressive msl_barracks', 'Mousillon Building: Rally Field'),
    102404: itemData(IC.useful, 1, 'mixu_msl_swamp_land_1', itemType.building, 0, 'Progressive msl_swamp', 'Mousillon Building: Cursed Bog'),
    102405: itemData(IC.useful, 1, 'mixu_msl_swamp_land_2', itemType.building, 1, 'Progressive msl_swamp', 'Mousillon Building: Sacred Swamp'),
    102406: itemData(IC.useful, 1, 'mixu_msl_binding_circle_1', itemType.building, 0, 'Progressive msl_binding', 'Mousillon Building: Defiled Cairn'),
    102407: itemData(IC.useful, 1, 'mixu_msl_binding_circle_2', itemType.building, 1, 'Progressive msl_binding', 'Mousillon Building: Binding Circle'),
    102408: itemData(IC.useful, 1, 'mixu_msl_binding_circle_3', itemType.building, 2, 'Progressive msl_binding', 'Mousillon Building: Lodestone of Darkness'),
    102409: itemData(IC.useful, 1, 'mixu_msl_carpenter_1', itemType.building, 0, 'Progressive msl_carpenter', "Mousillon Building: Carpenter's Workshop"),
    102410: itemData(IC.useful, 1, 'mixu_msl_carpenter_2', itemType.building, 1, 'Progressive msl_carpenter', 'Mousillon Building: Siege Workshop'),
    102411: itemData(IC.useful, 1, 'mixu_msl_wraiths_1', itemType.building, 0, 'Progressive msl_wraiths', 'Mousillon Building: Spirit Well'),
    102412: itemData(IC.useful, 1, 'mixu_msl_wraiths_2', itemType.building, 1, 'Progressive msl_wraiths', 'Mousillon Building: Font of Nightmares'),
    102413: itemData(IC.useful, 1, 'mixu_msl_wraiths_3', itemType.building, 2, 'Progressive msl_wraiths', 'Mousillon Building: Forbidden Library'),
    102414: itemData(IC.useful, 1, 'mixu_msl_vampires_1', itemType.building, 0, 'Progressive msl_vampires', 'Mousillon Building: Vampire Crypts'),
    102415: itemData(IC.useful, 1, 'mixu_msl_vampires_2', itemType.building, 1, 'Progressive msl_vampires', "Mousillon Building: Vampire's Keep"),

    102416: itemData(IC.useful, 1, 'mixu_msl_walls_1', itemType.building, 0, 'Progressive msl_walls', 'Mousillon Building: Basic Walls'),
    102417: itemData(IC.useful, 1, 'mixu_msl_walls_2', itemType.building, 1, 'Progressive msl_walls', 'Mousillon Building: Tall Walls'),
    102418: itemData(IC.useful, 1, 'mixu_msl_walls_3', itemType.building, 2, 'Progressive msl_walls', 'Mousillon Building: Reinforced Walls'),
    102419: itemData(IC.useful, 1, 'wh2_main_vmp_raisedead', itemType.building, 0, 'Progressive msl_battlefield', 'Mousillon Building: Awakened Battlefield'),
    102420: itemData(IC.useful, 1, 'wh2_main_foreign_slot_discovery_vmp_1', itemType.building, 0, 'Progressive msl_foreign_slot_discovery', 'Mousillon Building: Crypt Keepers'),
    102421: itemData(IC.useful, 1, 'wh2_main_foreign_slot_discovery_vmp_2', itemType.building, 1, 'Progressive msl_foreign_slot_discovery', 'Mousillon Building: Undercroft Sentries'),
    102422: itemData(IC.useful, 1, 'wh2_main_foreign_slot_discovery_vmp_3', itemType.building, 2, 'Progressive msl_foreign_slot_discovery', 'Mousillon Building: Grave Guardians'),
    102423: itemData(IC.useful, 1, 'mixu_msl_garrison_1', itemType.building, 0, 'Progressive msl_garrison', 'Mousillon Building: Guard House'),
    102424: itemData(IC.useful, 1, 'mixu_msl_garrison_2', itemType.building, 1, 'Progressive msl_garrison', 'Mousillon Building: City Watch'),

    102425: itemData(IC.useful, 1, 'mixu_msl_swampaire_camp_1', itemType.building, 0, 'Progressive msl_swampaire', 'Mousillon Building: Snail Hunting Grounds'),
    102426: itemData(IC.useful, 1, 'mixu_msl_swampaire_camp_2', itemType.building, 1, 'Progressive msl_swampaire', 'Mousillon Building: Swampaire Camp'),
    102427: itemData(IC.useful, 1, 'mixu_msl_swampaire_camp_3', itemType.building, 2, 'Progressive msl_swampaire', 'Mousillon Building: Swampaire Lodge'),
    102428: itemData(IC.useful, 1, 'wh_main_vmp_ossuary_1', itemType.building, 0, 'Progressive msl_ossuary', 'Mousillon Building: Charnel Pit'),
    102429: itemData(IC.useful, 1, 'wh_main_vmp_ossuary_2', itemType.building, 1, 'Progressive msl_ossuary', 'Mousillon Building: Lychyard'),
    102430: itemData(IC.useful, 1, 'wh_main_vmp_ossuary_3', itemType.building, 2, 'Progressive msl_ossuary', 'Mousillon Building: Ossuary'),
    102431: itemData(IC.useful, 1, 'mixu_msl_farm_1', itemType.building, 0, 'Progressive msl_farm', 'Mousillon Building: Fields'),
    102432: itemData(IC.useful, 1, 'mixu_msl_farm_2', itemType.building, 1, 'Progressive msl_farm', 'Mousillon Building: Farm'),
    102433: itemData(IC.useful, 1, 'mixu_msl_farm_3', itemType.building, 2, 'Progressive msl_farm', 'Mousillon Building: Landed Estate'),
    102434: itemData(IC.useful, 1, 'mixu_msl_balefire_1', itemType.building, 0, 'Progressive msl_balefire', 'Mousillon Building: Balefire Brazier'),
    102435: itemData(IC.useful, 1, 'mixu_msl_balefire_2', itemType.building, 1, 'Progressive msl_balefire', 'Mousillon Building: Balefire Hearth'),
    102436: itemData(IC.useful, 1, 'mixu_msl_balefire_3', itemType.building, 2, 'Progressive msl_balefire', 'Mousillon Building: Witch House'),
    102437: itemData(IC.useful, 1, 'mixu_msl_tavern_1', itemType.building, 0, 'Progressive msl_tavern', 'Mousillon Building: Tap Room'),
    102438: itemData(IC.useful, 1, 'mixu_msl_tavern_2', itemType.building, 1, 'Progressive msl_tavern', 'Mousillon Building: Shady Tavern'),
    102439: itemData(IC.useful, 1, 'mixu_msl_tavern_3', itemType.building, 2, 'Progressive msl_tavern', 'Mousillon Building: Coaching Inn'),
    102440: itemData(IC.useful, 1, 'mixu_msl_auction_house_1', itemType.building, 0, 'Progressive msl_auction', 'Mousillon Building: Dark Alleyway Fence'),
    102441: itemData(IC.useful, 1, 'mixu_msl_auction_house_2', itemType.building, 1, 'Progressive msl_auction', 'Mousillon Building: Auction House'),
    102442: itemData(IC.useful, 1, 'mixu_msl_port_1', itemType.building, 0, 'Progressive msl_port', 'Mousillon Building: Crumbling Wharf'),
    102443: itemData(IC.useful, 1, 'mixu_msl_port_2', itemType.building, 1, 'Progressive msl_port', 'Mousillon Building: Murky Harbour'),
    102444: itemData(IC.useful, 1, 'mixu_msl_port_3', itemType.building, 2, 'Progressive msl_port', 'Mousillon Building: Dark Port'),

    102445: itemData(IC.useful, 1, 'mixu_msl_resource_animals_1', itemType.building, 0, 'Progressive msl_resource_animals', 'Mousillon Building: Exotic Animal Tamer'),
    102446: itemData(IC.useful, 1, 'mixu_msl_resource_animals_2', itemType.building, 1, 'Progressive msl_resource_animals', 'Mousillon Building: Exotic Animal Pen'),
    102447: itemData(IC.useful, 1, 'mixu_msl_resource_animals_3', itemType.building, 2, 'Progressive msl_resource_animals', 'Mousillon Building: Exotic Animal Market'),
    102448: itemData(IC.useful, 1, 'mixu_msl_resource_gemstones_1', itemType.building, 0, 'Progressive msl_resource_gemstones', 'Mousillon Building: Cursed Gemstone Mineshaft'),
    102449: itemData(IC.useful, 1, 'mixu_msl_resource_gemstones_2', itemType.building, 1, 'Progressive msl_resource_gemstones', 'Mousillon Building: Hexed Gemstone Pit'),
    102450: itemData(IC.useful, 1, 'mixu_msl_resource_gemstones_3', itemType.building, 2, 'Progressive msl_resource_gemstones', 'Mousillon Building: Haunted Gemstone Mine'),
    102451: itemData(IC.useful, 1, 'mixu_msl_resource_medicine_1', itemType.building, 0, 'Progressive msl_resource_medicine', "Mousillon Building: Herb Gatherer's Camp"),
    102452: itemData(IC.useful, 1, 'mixu_msl_resource_medicine_2', itemType.building, 1, 'Progressive msl_resource_medicine', 'Mousillon Building: Exotic Hothouse'),
    102453: itemData(IC.useful, 1, 'mixu_msl_resource_medicine_3', itemType.building, 2, 'Progressive msl_resource_medicine', 'Mousillon Building: Alchemy Workshop'),
    102454: itemData(IC.useful, 1, 'mixu_msl_resource_obsidian_1', itemType.building, 0, 'Progressive msl_resource_obsidian', 'Mousillon Building: Obsidian Quarry'),
    102455: itemData(IC.useful, 1, 'mixu_msl_resource_obsidian_2', itemType.building, 1, 'Progressive msl_resource_obsidian', 'Mousillon Building: Obsidian Trinket Maker'),
    102456: itemData(IC.useful, 1, 'mixu_msl_resource_obsidian_3', itemType.building, 2, 'Progressive msl_resource_obsidian', 'Mousillon Building: Obsidian Amulet Carver'),
    102457: itemData(IC.useful, 1, 'mixu_msl_resource_spices_1', itemType.building, 0, 'Progressive msl_resource_spices', 'Mousillon Building: Spice Market'),
    102458: itemData(IC.useful, 1, 'mixu_msl_resource_spices_2', itemType.building, 1, 'Progressive msl_resource_spices', 'Mousillon Building: Spice Trading Post'),
    102459: itemData(IC.useful, 1, 'mixu_msl_resource_spices_3', itemType.building, 2, 'Progressive msl_resource_spices', 'Mousillon Building: Eastern Bazaar'),
    102460: itemData(IC.useful, 1, 'mixu_msl_resource_ivory_1', itemType.building, 0, 'Progressive msl_resource_ivory', 'Mousillon Building: Animal Store'),
    102461: itemData(IC.useful, 1, 'mixu_msl_resource_ivory_2', itemType.building, 1, 'Progressive msl_resource_ivory', 'Mousillon Building: Tusk Market'),
    102462: itemData(IC.useful, 1, 'mixu_msl_resource_ivory_3', itemType.building, 2, 'Progressive msl_resource_ivory', 'Mousillon Building: Tusk Compound'),
    102463: itemData(IC.useful, 1, 'mixu_msl_resource_dyes_1', itemType.building, 0, 'Progressive msl_resource_dyes', 'Mousillon Building: Red Pit'),
    102464: itemData(IC.useful, 1, 'mixu_msl_resource_dyes_2', itemType.building, 1, 'Progressive msl_resource_dyes', 'Mousillon Building: Blood Mines'),
    102465: itemData(IC.useful, 1, 'mixu_msl_resource_dyes_3', itemType.building, 2, 'Progressive msl_resource_dyes', "Mousillon Building: Pigment Grinder's Shop"),
    102466: itemData(IC.useful, 1, 'mixu_msl_resource_furs_1', itemType.building, 0, 'Progressive msl_resource_furs', 'Mousillon Building: Hunting Grounds'),
    102467: itemData(IC.useful, 1, 'mixu_msl_resource_furs_2', itemType.building, 1, 'Progressive msl_resource_furs', 'Mousillon Building: Poaching Camp'),
    102468: itemData(IC.useful, 1, 'mixu_msl_resource_furs_3', itemType.building, 2, 'Progressive msl_resource_furs', "Mousillon Building: Flayer's Lair"),
    102469: itemData(IC.useful, 1, 'mixu_msl_resource_gold_1', itemType.building, 0, 'Progressive msl_resource_gold', 'Mousillon Building: Tarnished Gold Shaft'),
    102470: itemData(IC.useful, 1, 'mixu_msl_resource_gold_2', itemType.building, 1, 'Progressive msl_resource_gold', 'Mousillon Building: Tarnished Gold Mine'),
    102471: itemData(IC.useful, 1, 'mixu_msl_resource_gold_3', itemType.building, 2, 'Progressive msl_resource_gold', 'Mousillon Building: Balefire Gold Smeltery'),
    102472: itemData(IC.useful, 1, 'mixu_msl_resource_iron_1', itemType.building, 0, 'Progressive msl_resource_iron', 'Mousillon Building: Iron Mining Pit'),
    102473: itemData(IC.useful, 1, 'mixu_msl_resource_iron_2', itemType.building, 1, 'Progressive msl_resource_iron', 'Mousillon Building: Iron Mine'),
    102474: itemData(IC.useful, 1, 'mixu_msl_resource_iron_3', itemType.building, 2, 'Progressive msl_resource_iron', 'Mousillon Building: Iron Smelter'),
    102475: itemData(IC.useful, 1, 'mixu_msl_resource_marble_1', itemType.building, 0, 'Progressive msl_resource_marble', "Mousillon Building: Brimstone Cutter's Workshop"),
    102476: itemData(IC.useful, 1, 'mixu_msl_resource_marble_2', itemType.building, 1, 'Progressive msl_resource_marble', "Mousillon Building: Tombstone Maker's Atelier"),
    102477: itemData(IC.useful, 1, 'mixu_msl_resource_marble_3', itemType.building, 2, 'Progressive msl_resource_marble', "Mousillon Building: Gargoyle Sculptor's Garret"),
    102478: itemData(IC.useful, 1, 'mixu_msl_resource_pastures_1', itemType.building, 0, 'Progressive msl_resource_pastures', 'Mousillon Building: Grazing Pastures'),
    102479: itemData(IC.useful, 1, 'mixu_msl_resource_pastures_2', itemType.building, 1, 'Progressive msl_resource_pastures', 'Mousillon Building: Livestock Pens'),
    102480: itemData(IC.useful, 1, 'mixu_msl_resource_pastures_3', itemType.building, 2, 'Progressive msl_resource_pastures', 'Mousillon Building: Cattle Ranch'),
    102481: itemData(IC.useful, 1, 'mixu_msl_resource_pottery_1', itemType.building, 0, 'Progressive msl_resource_pottery', 'Mousillon Building: Flooded Clay Pit'),
    102482: itemData(IC.useful, 1, 'mixu_msl_resource_pottery_2', itemType.building, 1, 'Progressive msl_resource_pottery', "Mousillon Building: Urn Maker's Pottery"),
    102483: itemData(IC.useful, 1, 'mixu_msl_resource_pottery_3', itemType.building, 2, 'Progressive msl_resource_pottery', 'Mousillon Building: Screeching Kilns'),
    102484: itemData(IC.useful, 1, 'mixu_msl_resource_salt_1', itemType.building, 0, 'Progressive msl_resource_salt', 'Mousillon Building: Brackish Pond'),
    102485: itemData(IC.useful, 1, 'mixu_msl_resource_salt_2', itemType.building, 1, 'Progressive msl_resource_salt', 'Mousillon Building: Salt Marsh'),
    102486: itemData(IC.useful, 1, 'mixu_msl_resource_salt_3', itemType.building, 2, 'Progressive msl_resource_salt', 'Mousillon Building: Desolate Salt Pans'),
    102487: itemData(IC.useful, 1, 'mixu_msl_resource_timber_1', itemType.building, 0, 'Progressive msl_resource_timber', "Mousillon Building: Woodman's Hut"),
    102488: itemData(IC.useful, 1, 'mixu_msl_resource_timber_2', itemType.building, 1, 'Progressive msl_resource_timber', 'Mousillon Building: Timber Mill'),
    102489: itemData(IC.useful, 1, 'mixu_msl_resource_timber_3', itemType.building, 2, 'Progressive msl_resource_timber', 'Mousillon Building: Lumberyard'),
    102490: itemData(IC.useful, 1, 'mixu_msl_resource_wine_1', itemType.building, 0, 'Progressive msl_resource_wine', 'Mousillon Building: Tangled Vine Patch'),
    102491: itemData(IC.useful, 1, 'mixu_msl_resource_wine_2', itemType.building, 1, 'Progressive msl_resource_wine', 'Mousillon Building: Thorny Orchard'),
    102492: itemData(IC.useful, 1, 'mixu_msl_resource_wine_3', itemType.building, 2, 'Progressive msl_resource_wine', 'Mousillon Building: Animated Winepress'),

    #102493: ItemData(IC.useful, 1, 'mixu_msl_settlement_major_1', ItemType.building, 0, 'Progressive msl_settlement_major', 'Mousillon Building: Crumbling Hamlet'),
    102494: itemData(IC.useful, 1, 'mixu_msl_settlement_major_2', itemType.building, 0, 'Progressive msl_settlement_major', 'Mousillon Building: Corrupted Village'),
    102495: itemData(IC.useful, 1, 'mixu_msl_settlement_major_3', itemType.building, 1, 'Progressive msl_settlement_major', 'Mousillon Building: Shady Township'),
    102496: itemData(IC.useful, 1, 'mixu_msl_settlement_major_4', itemType.building, 2, 'Progressive msl_settlement_major', 'Mousillon Building: Accursed City'),
    102497: itemData(IC.useful, 1, 'mixu_msl_settlement_major_5', itemType.building, 3, 'Progressive msl_settlement_major', 'Mousillon Building: Dark Castle'),
    #102498: ItemData(IC.useful, 1, 'mixu_msl_settlement_minor_1', ItemType.building, 0, 'Progressive msl_settlement_minor', 'Mousillon Building: Crumbling Hamlet'),
    102499: itemData(IC.useful, 1, 'mixu_msl_settlement_minor_2', itemType.building, 0, 'Progressive msl_settlement_minor', 'Mousillon Building: Corrupted Village'),
    102500: itemData(IC.useful, 1, 'mixu_msl_settlement_minor_3', itemType.building, 1, 'Progressive msl_settlement_minor', 'Mousillon Building: Shady Township'),
}
"""
mixu_special_settlement_altdorf_1_msl
mixu_special_settlement_altdorf_2_msl
mixu_special_settlement_altdorf_3_msl
mixu_special_settlement_altdorf_4_msl
mixu_special_settlement_altdorf_5_msl
mixu_special_settlement_castle_drakenhof_1_msl
mixu_special_settlement_castle_drakenhof_2_msl
mixu_special_settlement_castle_drakenhof_3_msl
mixu_special_settlement_castle_drakenhof_4_msl
mixu_special_settlement_castle_drakenhof_5_msl
mixu_special_settlement_couronne_1_msl
mixu_special_settlement_couronne_2_msl
mixu_special_settlement_couronne_3_msl
mixu_special_settlement_couronne_4_msl
mixu_special_settlement_couronne_5_msl
mixu_special_settlement_mousillon_1_msl
mixu_special_settlement_mousillon_2_msl
mixu_special_settlement_mousillon_3_msl
"""

techs: dict[int, itemData] = {
    102800: itemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_cursed_land', itemType.tech, 1, 'Progressive tech_msl_undead', 'Mousillon Tech: Cursed Land'),
    102801: itemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_raise_newly_dead', itemType.tech, 2, 'Progressive tech_msl_undead', 'Mousillon Tech: Raise Newly Dead'),
    102802: itemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_defiler_of_the_ancient_barrows', itemType.tech, 2, 'Progressive tech_msl_undead', 'Mousillon Tech: Defiler of the Ancient Dragon'),
    102803: itemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_rotten_gift', itemType.tech, 2, 'Progressive tech_msl_undead', 'Mousillon Tech: Rotten Gift'),
    102804: itemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_bonds_of_flesh', itemType.tech, 2, 'Progressive tech_msl_undead', 'Mousillon Tech: Bonds of Flesh'),
    102805: itemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_dread_animator', itemType.tech, 2, 'Progressive tech_msl_undead', 'Mousillon Tech: Dread Animator'),
    102806: itemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_spirit_shackles', itemType.tech, 2, 'Progressive tech_msl_undead', 'Mousillon Tech: Spirit Shackles'),
    102807: itemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_unearth_cursed_blades', itemType.tech, 2, 'Progressive tech_msl_undead', 'Mousillon Tech: Unearth Cursed Blades'),
    102808: itemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_cannibalistic_rituals', itemType.tech, 2, 'Progressive tech_msl_undead', 'Mousillon Tech: Cannibalistic Rituals'),
    102809: itemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_enshrine_ancient_lords', itemType.tech, 2, 'Progressive tech_msl_undead', 'Mousillon Tech: Enshrine Ancient Lords'),
    102810: itemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_infuse_the_tireless_hordes', itemType.tech, 2, 'Progressive tech_msl_undead', 'Mousillon Tech: Infuse the Tireless Hordes'),
    102811: itemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_soulbinder', itemType.tech, 2, 'Progressive tech_msl_undead', 'Mousillon Tech: Soulbinder'),
    102812: itemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_nightmarish_reaping', itemType.tech, 2, 'Progressive tech_msl_undead', 'Mousillon Tech: Nightmarish Reaping'),

    102813: itemData(IC.useful, 1, 'mixu_msl_mallobaude_living_rally_the_peasants', itemType.tech, 1, 'Progressive tech_msl_living', 'Mousillon Tech: Rally the Peasants'),
    102814: itemData(IC.useful, 1, 'mixu_msl_mallobaude_living_disgraced_and_damned', itemType.tech, 2, 'Progressive tech_msl_living', 'Mousillon Tech: Disgraced and Damned'),
    102815: itemData(IC.useful, 1, 'mixu_msl_mallobaude_living_embrace_the_darkness', itemType.tech, 2, 'Progressive tech_msl_living', 'Mousillon Tech: Embrace the Darkness'),
    102816: itemData(IC.useful, 1, 'mixu_msl_mallobaude_living_steel_furnaces', itemType.tech, 2, 'Progressive tech_msl_living', 'Mousillon Tech: Steel Furnaces'),
    102817: itemData(IC.useful, 1, 'mixu_msl_mallobaude_living_master_swordsmiths', itemType.tech, 2, 'Progressive tech_msl_living', 'Mousillon Tech: Master Swordsmiths'),
    102818: itemData(IC.useful, 1, 'mixu_msl_mallobaude_living_professional_fletchers', itemType.tech, 2, 'Progressive tech_msl_living', 'Mousillon Tech: Professional Fletchers'),
    102819: itemData(IC.useful, 1, 'mixu_msl_mallobaude_living_siege_engineering', itemType.tech, 2, 'Progressive tech_msl_living', 'Mousillon Tech: Siege Engineering'),
    102820: itemData(IC.useful, 1, 'mixu_msl_mallobaude_living_serve_in_life_or_in_death', itemType.tech, 2, 'Progressive tech_msl_living', 'Mousillon Tech: Serve in Life or in Death'),
    102821: itemData(IC.useful, 1, 'mixu_msl_mallobaude_living_charity', itemType.tech, 2, 'Progressive tech_msl_living', 'Mousillon Tech: Charity'),
    102822: itemData(IC.useful, 1, 'mixu_msl_mallobaude_living_registered_draft', itemType.tech, 2, 'Progressive tech_msl_living', 'Mousillon Tech: Registered Draft'),
    102823: itemData(IC.useful, 1, 'mixu_msl_mallobaude_living_bigger_shovels', itemType.tech, 2, 'Progressive tech_msl_living', 'Mousillon Tech: Bigger Shovels'),
    102824: itemData(IC.useful, 1, 'mixu_msl_mallobaude_living_subsidised_tools', itemType.tech, 2, 'Progressive tech_msl_living', 'Mousillon Tech: Subsidised Tools'),
    102825: itemData(IC.useful, 1, 'mixu_msl_mallobaude_living_improved_construction', itemType.tech, 2, 'Progressive tech_msl_living', 'Mousillon Tech: Improved Construction'),

    102826: itemData(IC.useful, 1, 'mixu_msl_mallobaude_cavalry_regular_tournaments', itemType.tech, 1, 'Progressive tech_msl_knights', 'Mousillon Tech: Regular Tournaments'),
    102827: itemData(IC.useful, 1, 'mixu_msl_mallobaude_cavalry_dark_deeds', itemType.tech, 1, 'Progressive tech_msl_knights', 'Mousillon Tech: Dark Deeds'),
    102828: itemData(IC.useful, 1, 'mixu_msl_mallobaude_cavalry_unholy_strength', itemType.tech, 1, 'Progressive tech_msl_knights', 'Mousillon Tech: Unholy Strength'),

    102829: itemData(IC.useful, 1, 'mixu_msl_mallobaude_swamps_horrors_of_the_bog', itemType.tech, 1, 'Progressive tech_msl_swamp', 'Mousillon Tech: Horrors of the Bog'),
    102830: itemData(IC.useful, 1, 'mixu_msl_mallobaude_swamps_swampaire_training', itemType.tech, 1, 'Progressive tech_msl_swamp', 'Mousillon Tech: Swampaire Training'),
    102831: itemData(IC.useful, 1, 'mixu_msl_mallobaude_swamps_support_the_frogwives', itemType.tech, 1, 'Progressive tech_msl_swamp', 'Mousillon Tech: Support the Frogwives'),

    102832: itemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_nobels_of_mousillon', itemType.tech, 1, 'Progressive tech_msl_nobility', 'Mousillon Tech: Nobles of Mousillon'),
    102833: itemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_blood_is_power', itemType.tech, 2, 'Progressive tech_msl_nobility', 'Mousillon Tech: Blood is Power'),
    102834: itemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_hexensnacht_sacrifices', itemType.tech, 2, 'Progressive tech_msl_nobility', 'Mousillon Tech: Hexensnacht Sacrifices'),
    102835: itemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_blasphemous_disciples', itemType.tech, 2, 'Progressive tech_msl_nobility', 'Mousillon Tech: Blasphemous Disciples'),
    102836: itemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_spread_vampire_covens', itemType.tech, 2, 'Progressive tech_msl_nobility', 'Mousillon Tech: Spread Vampire Covens'),
    102837: itemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_turning_knights_of_the_realm', itemType.tech, 2, 'Progressive tech_msl_nobility', 'Mousillon Tech: Turning Knights of the Realm'),
    102838: itemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_delusions_of_grandeur', itemType.tech, 2, 'Progressive tech_msl_nobility', 'Mousillon Tech: Delusions of Grandeur'),
    102839: itemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_puppet_master', itemType.tech, 2, 'Progressive tech_msl_nobility', 'Mousillon Tech: Puppet Master'),
    102840: itemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_infiltrate_noble_houses', itemType.tech, 2, 'Progressive tech_msl_nobility', 'Mousillon Tech: Infiltrate Noble Houses'),
    102841: itemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_baleful_rituals', itemType.tech, 2, 'Progressive tech_msl_nobility', 'Mousillon Tech: Baleful Rituals'),
    102842: itemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_vampiric_revivification', itemType.tech, 2, 'Progressive tech_msl_nobility', 'Mousillon Tech: Vampiric Revivification'),
    102843: itemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_traditions_of_hospitality', itemType.tech, 2, 'Progressive tech_msl_nobility', 'Mousillon Tech: Traditions of Hospitality'),
    102844: itemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_code_of_conduct', itemType.tech, 2, 'Progressive tech_msl_nobility', 'Mousillon Tech: Code of Conduct'),
}

progUnits: dict[int, itemData] = {
    103200: itemData(IC.useful, 2, "Progressive msl_inf", itemType.unit, 2, "", "Progressive Mousillon Unit: Infantry"),
    103201: itemData(IC.useful, 2, "Progressive msl_rng", itemType.unit, 2, "", "Progressive Mousillon Unit: Ranged"),
    103202: itemData(IC.useful, 3, "Progressive msl_cav", itemType.unit, 3, "", "Progressive Mousillon Unit: Cavalry"),
    103203: itemData(IC.useful, 1, "Progressive msl_art", itemType.unit, 1, "", "Progressive Mousillon Unit: Artillery"),
    103204: itemData(IC.useful, 4, "Progressive msl_veh", itemType.unit, 4, "", "Progressive Mousillon Unit: Chariot"),
    103205: itemData(IC.useful, 2, "Progressive msl_bst", itemType.unit, 2, "", "Progressive Mousillon Unit: Beast"),
    103206: itemData(IC.useful, 2, "Progressive msl_hro", itemType.unit, 2, "", "Progressive Mousillon Unit: Hero")
}

progBuildings: dict[int, itemData] = {
    103400: itemData(IC.useful, 2, 'Progressive msl_cemetery', itemType.building, 2, '', 'Progressive Mousillon Building: Cemetery'),
    103401: itemData(IC.useful, 2, 'Progressive msl_barracks', itemType.building, 2, '', 'Progressive Mousillon Building: Barracks'),
    103402: itemData(IC.useful, 2, 'Progressive msl_swamp', itemType.building, 2, '', 'Progressive Mousillon Building: Swamp'),
    103403: itemData(IC.useful, 3, 'Progressive msl_binding', itemType.building, 3, '', 'Progressive Mousillon Building: Binding'),
    103404: itemData(IC.useful, 2, 'Progressive msl_carpenter', itemType.building, 2, '', 'Progressive Mousillon Building: Carpenter'),
    103405: itemData(IC.useful, 3, 'Progressive msl_wraiths', itemType.building, 3, '', 'Progressive Mousillon Building: Wraiths'),
    103406: itemData(IC.useful, 2, 'Progressive msl_vampires', itemType.building, 2, '', "Progressive Mousillon Building: Vampires"),

    103407: itemData(IC.useful, 3, 'Progressive msl_walls', itemType.building, 3, '', 'Progressive Mousillon Building: Walls'),
    103408: itemData(IC.useful, 1, 'Progressive msl_battlefield', itemType.building, 1, '', 'Progressive Mousillon Building: Awakened Battlefield'),
    103409: itemData(IC.useful, 3, 'Progressive msl_foreign_slot_discovery', itemType.building, 3, '', 'Progressive Mousillon Building: Protection'),
    103410: itemData(IC.useful, 2, 'Progressive msl_garrison', itemType.building, 2, '', 'Progressive Mousillon Building: Garrison'),

    103411: itemData(IC.useful, 3, 'Progressive msl_swampaire', itemType.building, 3, '', 'Progressive Mousillon Building: Swampaire'),
    103412: itemData(IC.useful, 3, 'Progressive msl_ossuary', itemType.building, 3, '', 'Progressive Mousillon Building: Ossuary'),
    103413: itemData(IC.useful, 3, 'Progressive msl_farm', itemType.building, 3, '', 'Progressive Mousillon Building: Farms'),
    103414: itemData(IC.useful, 3, 'Progressive msl_balefire', itemType.building, 3, '', 'Progressive Mousillon Building: Witches'),
    103415: itemData(IC.useful, 3, 'Progressive msl_tavern', itemType.building, 3, '', 'Progressive Mousillon Building: Tavern'),
    103416: itemData(IC.useful, 2, 'Progressive msl_auction', itemType.building, 2, '', 'Progressive Mousillon Building: Trade'),
    103417: itemData(IC.useful, 3, 'Progressive msl_port', itemType.building, 3, '', 'Progressive Mousillon Building: Port'),

    103418: itemData(IC.useful, 3, 'Progressive msl_resource_animals', itemType.building, 3, '', 'Progressive Mousillon Building: Animals'),
    103419: itemData(IC.useful, 3, 'Progressive msl_resource_gemstones', itemType.building, 3, '', 'Progressive Mousillon Building: Gemstones'),
    103420: itemData(IC.useful, 3, 'Progressive msl_resource_medicine', itemType.building, 3, '', 'Progressive Mousillon Building: Medicine'),
    103421: itemData(IC.useful, 3, 'Progressive msl_resource_obsidian', itemType.building, 3, '', 'Progressive Mousillon Building: Obsidian'),
    103422: itemData(IC.useful, 3, 'Progressive msl_resource_spices', itemType.building, 3, '', 'Progressive Mousillon Building: Spices'),
    103423: itemData(IC.useful, 3, 'Progressive msl_resource_ivory', itemType.building, 3, '', 'Progressive Mousillon Building: Ivory'),
    103424: itemData(IC.useful, 3, 'Progressive msl_resource_dyes', itemType.building, 3, '', "Progressive Mousillon Building: Dyes"),
    103425: itemData(IC.useful, 3, 'Progressive msl_resource_furs', itemType.building, 3, '', "Progressive Mousillon Building: Furs"),
    103426: itemData(IC.useful, 3, 'Progressive msl_resource_gold', itemType.building, 3, '', 'Progressive Mousillon Building: Gold'),
    103427: itemData(IC.useful, 3, 'Progressive msl_resource_iron', itemType.building, 3, '', 'Progressive Mousillon Building: Iron'),
    103428: itemData(IC.useful, 3, 'Progressive msl_resource_marble', itemType.building, 3, '', "Progressive Mousillon Building: Marble"),
    103429: itemData(IC.useful, 3, 'Progressive msl_resource_pastures', itemType.building, 3, '', 'Progressive Mousillon Building: Pastures'),
    103430: itemData(IC.useful, 3, 'Progressive msl_resource_pottery', itemType.building, 3, '', 'Progressive Mousillon Building: Pottery'),
    103431: itemData(IC.useful, 3, 'Progressive msl_resource_salt', itemType.building, 3, '', 'Progressive Mousillon Building: Salt'),
    103432: itemData(IC.useful, 3, 'Progressive msl_resource_timber', itemType.building, 3, '', 'Progressive Mousillon Building: Timber'),
    103433: itemData(IC.useful, 3, 'Progressive msl_resource_wine', itemType.building, 3, '', 'Progressive Mousillon Building: Wine'),

    103434: itemData(IC.useful, 4, 'Progressive msl_settlement_major', itemType.building, 4, '', 'Vmp Building: Settlement Major'),
    103535: itemData(IC.useful, 2, 'Progressive msl_settlement_minor', itemType.building, 2, '', 'Vmp Building: Settlement Minor'),
}

progTechs: dict[int, itemData] = {
    103500: itemData(IC.useful, 2, "Progressive tech_msl_undead", itemType.tech, 2, "", "Progressive Mousillon Tech: Living Dead"),
    103501: itemData(IC.useful, 2, "Progressive tech_msl_living", itemType.tech, 2, "", "Progressive Mousillon Tech: Peasantry"),
    103502: itemData(IC.useful, 1, "Progressive tech_msl_knights", itemType.tech, 1, "", "Progressive Mousillon Tech: Knights of the Realm"),
    103503: itemData(IC.useful, 1, "Progressive tech_msl_swamp", itemType.tech, 1, "", "Progressive Mousillon Tech: Swamp Land"),
    103504: itemData(IC.useful, 2, "Progressive tech_msl_nobility", itemType.tech, 2, "", "Progressive Mousillon Tech: Nobility"),
}

special: dict[int, specialItemData] = {
    103600: specialItemData(IC.useful, 1, 'mixer_msl_cult_of_the_bloody_grail', "mixu_msl_ror_cantankerous_bellends", itemType.unit, 1, 'Progressive msl_inf', False, False, 'Mousillon Unit: Cantankerous Bellends (Men-at-Arms)'),
    103601: specialItemData(IC.useful, 1, 'mixer_msl_cult_of_the_bloody_grail', "mixu_msl_ror_knights_of_bougar", itemType.unit, 2, 'Progressive msl_cav', False, False, 'Mousillon Unit: Knights of Bougars'),
    103602: specialItemData(IC.useful, 1, 'mixer_msl_cult_of_the_bloody_grail', "mixu_msl_ror_the_rose_lances", itemType.unit, 1, 'Progressive msl_cav', False, False, 'Mousillon Unit: The Rose Lances (Black Knights)'),
    103603: specialItemData(IC.useful, 1, 'mixer_msl_cult_of_the_bloody_grail', "mixu_msl_ror_ghosts_of_grismerie", itemType.unit, 1, 'Progressive msl_inf', False, False, 'Mousillon Unit: Ghosts of Grismerie (Grey Men)'),
    103604: specialItemData(IC.useful, 1, 'mixer_msl_cult_of_the_bloody_grail', "mixu_msl_ror_barons_men", itemType.unit, 1, 'Progressive msl_inf', False, False, "Mousillon Unit: Baron's Men (Crypt Ghouls)"),
}

rituals: dict[int, specialItemData] = {
    103700: specialItemData(IC.useful, 1, "mixer_msl_cult_of_the_bloody_grail", "mixu_msl_black_grail_ritual_vassalise", itemType.ritual, 1, "progressive msl_ritual", True, False, "Mousillon Ritual: Black Grail Vassalise"),
    103701: specialItemData(IC.useful, 1, "mixer_msl_cult_of_the_bloody_grail", "mixu_msl_black_grail_ritual_apply_corruption", itemType.ritual, 1, "progressive msl_ritual", True, False, "Mousillon Ritual: Black Grail Apply Corruption"),
    103702: specialItemData(IC.useful, 1, "mixer_msl_cult_of_the_bloody_grail", "mixu_msl_black_grail_ritual_reveal_shroud", itemType.ritual, 1, "progressive msl_ritual", True, False, "Mousillon Ritual: Black Grail Reveal Shroud"),
}
