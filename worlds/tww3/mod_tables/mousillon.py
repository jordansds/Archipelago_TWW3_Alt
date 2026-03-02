from BaseClasses import ItemClassification as IC
from worlds.tww3.item_types import ItemType, ItemData, specialItemData

# @formatter:off

units: dict[int, ItemData] = {
    102000: ItemData(IC.useful, 1, 'mixu_msl_inf_men_at_arms_sword', ItemType.unit, 1, 'Progressive msl_inf', 'Msl Unit: Men at Arms (Sword)'),
    102001: ItemData(IC.useful, 1, 'mixu_msl_inf_men_at_arms_polearms', ItemType.unit, 2, 'Progressive msl_inf', 'Msl Unit: Men at Arms (Sword)'),
    102002: ItemData(IC.useful, 1, 'mixu_msl_inf_grave_guard_sword', ItemType.unit, 1, 'Progressive msl_inf', 'Msl Unit: Grave Guard'),
    102003: ItemData(IC.useful, 1, 'wh3_main_vmp_inf_grave_guard_2', ItemType.unit, 2, 'Progressive msl_inf', 'Msl Unit: Grave Guard'),
    102004: ItemData(IC.useful, 1, 'mixu_msl_inf_grave_guard_great_weapons', ItemType.unit, 2, 'Progressive msl_inf', 'Msl Unit: Grave Guard (Great Weapons)'),
    102005: ItemData(IC.useful, 1, 'mixu_msl_mon_the_grey_men', ItemType.unit, 1, 'Progressive msl_inf', 'Msl Unit: Grey Men'),
    102006: ItemData(IC.useful, 1, 'wh_main_vmp_inf_crypt_ghouls', ItemType.unit, 1, 'Progressive msl_inf', 'Msl Unit: Crypt Ghouls'),
    102007: ItemData(IC.useful, 1, 'wh_main_vmp_inf_cairn_wraiths', ItemType.unit, 2, 'Progressive msl_inf', 'Msl Unit: Cairn Wraiths'),
    102008: ItemData(IC.useful, 1, 'mixu_msl_inf_brigands', ItemType.unit, 2, 'Progressive msl_inf', 'Msl Unit: Brigands (Polearms)'),

    102009: ItemData(IC.useful, 1, 'mixu_msl_inf_bowmen', ItemType.unit, 1, 'Progressive msl_rng', 'Msl Unit: Bowmen'),
    102010: ItemData(IC.useful, 1, 'mixu_msl_inf_bowmen_poison', ItemType.unit, 2, 'Progressive msl_rng', 'Msl Unit: Bowmen (Poison)'),
    102011: ItemData(IC.useful, 1, 'mixu_msl_inf_bowmen_balefire', ItemType.unit, 2, 'Progressive msl_rng', 'Msl Unit: Bowmen (Balefire)'),

    102012: ItemData(IC.useful, 1, 'mixu_msl_inf_mounted_brigands', ItemType.unit, 2, 'Progressive msl_cav', 'Msl Unit: Mounted Brigands'),
    102013: ItemData(IC.useful, 1, 'mixu_msl_cav_black_knights_sword', ItemType.unit, 1, 'Progressive msl_cav', 'Msl Unit: Black Knights'),
    102014: ItemData(IC.useful, 1, 'mixu_msl_cav_black_knights_lance', ItemType.unit, 2, 'Progressive msl_cav', 'Msl Unit: Black Knights (Lances & Barding)'),
    102015: ItemData(IC.useful, 1, 'mixu_msl_cav_black_grail_knights', ItemType.unit, 3, 'Progressive msl_cav', 'Msl Unit: Black Grail Knights'),
    102016: ItemData(IC.useful, 1, 'wh_main_vmp_cav_hexwraiths', ItemType.unit, 3, 'Progressive msl_cav', 'Msl Unit: Hexwraiths'),
    102017: ItemData(IC.useful, 1, 'wh_dlc02_vmp_cav_blood_knights_0', ItemType.unit, 4, 'Progressive msl_cav', 'Msl Unit: Blood Knights (Lances)'),
    102018: ItemData(IC.useful, 1, 'mixu_msl_cav_hellsteed_knights', ItemType.unit, 4, 'Progressive msl_cav', 'Msl Unit: Hellsteed Knights'),
    102019: ItemData(IC.useful, 1, 'wh_dlc07_brt_cav_knights_errant_0', ItemType.unit, 2, 'Progressive msl_cav', 'Msl Unit: Knights Errant'),
    102020: ItemData(IC.useful, 1, 'wh_main_brt_cav_knights_of_the_realm', ItemType.unit, 2, 'Progressive msl_cav', 'Msl Unit: Knights of the Realm'),
    102021: ItemData(IC.useful, 1, 'wh_main_brt_cav_pegasus_knights', ItemType.unit, 3, 'Progressive msl_cav', 'Msl Unit: Pegasus Knights'),

    102022: ItemData(IC.useful, 1, 'mixu_msl_art_trebuchet', ItemType.unit, 1, 'Progressive msl_art', 'Msl Unit: Bowmen'),
    102023: ItemData(IC.useful, 1, 'mixu_msl_art_trebuchet_balefire', ItemType.unit, 1, 'Progressive msl_art', 'Msl Unit: Bowmen'),

    102024: ItemData(IC.useful, 1, 'wh_dlc04_vmp_veh_corpse_cart_0', ItemType.unit, 1, 'Progressive msl_veh', 'Msl Unit: Corpse Cart'),
    102025: ItemData(IC.useful, 1, 'wh_dlc04_vmp_veh_corpse_cart_1', ItemType.unit, 2, 'Progressive msl_veh', 'Msl Unit: Corpse Cart (Balefire)'),
    102026: ItemData(IC.useful, 1, 'wh_dlc04_vmp_veh_corpse_cart_2', ItemType.unit, 3, 'Progressive msl_veh', 'Msl Unit: Corpse Cart (Unholy Lodestone)'),
    102027: ItemData(IC.useful, 1, 'wh_main_vmp_veh_black_coach', ItemType.unit, 3, 'Progressive msl_veh', 'Msl Unit: Black Coach'),
    102028: ItemData(IC.useful, 1, 'wh_dlc04_vmp_veh_mortis_engine_0', ItemType.unit, 4, 'Progressive msl_veh', 'Msl Unit: Mortis Engine'),

    102029: ItemData(IC.useful, 1, 'wh_main_vmp_mon_fell_bats', ItemType.unit, 1, 'Progressive msl_bst', 'Msl Unit: Fell Bats'),
    102030: ItemData(IC.useful, 1, 'wh_main_vmp_mon_dire_wolves', ItemType.unit, 1, 'Progressive msl_bst', 'Msl Unit: Dire Wolves'),
    102031: ItemData(IC.useful, 1, 'wh_main_vmp_mon_crypt_horrors', ItemType.unit, 2, 'Progressive msl_bst', 'Msl Unit: Crypt Horrors'),
    102032: ItemData(IC.useful, 1, 'wh_main_vmp_mon_varghulf', ItemType.unit, 2, 'Progressive msl_bst', 'Msl Unit: Varghulf'),
    102033: ItemData(IC.useful, 1, 'wh2_dlc11_vmp_mon_mournguls_0', ItemType.unit, 3, 'Progressive msl_bst', 'Msl Unit: Mournguls'),
    102034: ItemData(IC.useful, 1, 'mixu_msl_mon_giant_snail', ItemType.unit, 2, 'Progressive msl_bst', 'Msl Unit: Giant Snail'),
    102035: ItemData(IC.useful, 1, 'mixu_msl_mon_dracoleech', ItemType.unit, 2, 'Progressive msl_bst', 'Msl Unit: Rotting Dracoleech'),

    102036: ItemData(IC.useful, 1, 'mixu_msl_cha_bretonnian_wight', ItemType.unit, 2, 'Progressive msl_hro', 'Msl Unit: Wight King'),
    102037: ItemData(IC.useful, 1, 'wh_main_vmp_cha_necromancer_0', ItemType.unit, 1, 'Progressive msl_hro', 'Msl Unit: Necromancer'),
    102038: ItemData(IC.useful, 1, 'wh_main_vmp_cha_banshee', ItemType.unit, 2, 'Progressive msl_hro', 'Msl Unit: Banshee'),
    102039: ItemData(IC.useful, 1, 'mixu_msl_cha_damsel_heavens', ItemType.unit, 1, 'Progressive msl_hro', 'Msl Unit: Damsel (Heavens)'),
    102040: ItemData(IC.useful, 1, 'mixu_msl_cha_damsel_beasts', ItemType.unit, 1, 'Progressive msl_hro', 'Msl Unit: Damsel (Beasts)'),
    102041: ItemData(IC.useful, 1, 'mixu_msl_cha_damsel_shadows', ItemType.unit, 1, 'Progressive msl_hro', 'Msl Unit: Damsel (Shadows)'),
    102042: ItemData(IC.useful, 1, 'mixu_msl_cha_damsel_death', ItemType.unit, 1, 'Progressive msl_hro', 'Msl Unit: Damsel (Death)'),
}

buildings: dict[int, ItemData] = {
    102400: ItemData(IC.useful, 1, 'mixu_msl_cemetary_1', ItemType.building, 0, 'Progressive msl_cemetery', 'Msl Building: Barrow'),
    102401: ItemData(IC.useful, 1, 'mixu_msl_cemetary_2', ItemType.building, 1, 'Progressive msl_cemetery', 'Msl Building: Mausoleum'),
    102402: ItemData(IC.useful, 1, 'mixu_msl_barracks_1', ItemType.building, 0, 'Progressive msl_barracks', 'Msl Building: Training Field'),
    102403: ItemData(IC.useful, 1, 'mixu_msl_barracks_2', ItemType.building, 1, 'Progressive msl_barracks', 'Msl Building: Rally Field'),
    102404: ItemData(IC.useful, 1, 'mixu_msl_swamp_land_1', ItemType.building, 0, 'Progressive msl_swamp', 'Msl Building: Cursed Bog'),
    102405: ItemData(IC.useful, 1, 'mixu_msl_swamp_land_2', ItemType.building, 1, 'Progressive msl_swamp', 'Msl Building: Sacred Swamp'),
    102406: ItemData(IC.useful, 1, 'mixu_msl_binding_circle_1', ItemType.building, 0, 'Progressive msl_binding', 'Msl Building: Defiled Cairn'),
    102407: ItemData(IC.useful, 1, 'mixu_msl_binding_circle_2', ItemType.building, 1, 'Progressive msl_binding', 'Msl Building: Binding Circle'),
    102408: ItemData(IC.useful, 1, 'mixu_msl_binding_circle_3', ItemType.building, 2, 'Progressive msl_binding', 'Msl Building: Lodestone of Darkness'),
    102409: ItemData(IC.useful, 1, 'mixu_msl_carpenter_1', ItemType.building, 0, 'Progressive msl_carpenter', "Msl Building: Carpenter's Workshop"),
    102410: ItemData(IC.useful, 1, 'mixu_msl_carpenter_2', ItemType.building, 1, 'Progressive msl_carpenter', 'Msl Building: Siege Workshop'),
    102411: ItemData(IC.useful, 1, 'mixu_msl_wraiths_1', ItemType.building, 0, 'Progressive msl_wraiths', 'Msl Building: Spirit Well'),
    102412: ItemData(IC.useful, 1, 'mixu_msl_wraiths_2', ItemType.building, 1, 'Progressive msl_wraiths', 'Msl Building: Font of Nightmares'),
    102413: ItemData(IC.useful, 1, 'mixu_msl_wraiths_3', ItemType.building, 2, 'Progressive msl_wraiths', 'Msl Building: Forbidden Library'),
    102414: ItemData(IC.useful, 1, 'mixu_msl_vampires_1', ItemType.building, 0, 'Progressive msl_vampires', 'Msl Building: Vampire Crypts'),
    102415: ItemData(IC.useful, 1, 'mixu_msl_vampires_2', ItemType.building, 1, 'Progressive msl_vampires', "Msl Building: Vampire's Keep"),

    102416: ItemData(IC.useful, 1, 'mixu_msl_walls_1', ItemType.building, 0, 'Progressive msl_walls', 'Msl Building: Basic Walls'),
    102417: ItemData(IC.useful, 1, 'mixu_msl_walls_2', ItemType.building, 1, 'Progressive msl_walls', 'Msl Building: Tall Walls'),
    102418: ItemData(IC.useful, 1, 'mixu_msl_walls_3', ItemType.building, 2, 'Progressive msl_walls', 'Msl Building: Reinforced Walls'),
    102419: ItemData(IC.useful, 1, 'mixu_msl_awakened_battlefield', ItemType.building, 0, 'Progressive msl_battlefield', 'Msl Building: Awakened Battlefield'),
    102420: ItemData(IC.useful, 1, 'wh2_main_foreign_slot_discovery_vmp_1', ItemType.building, 0, 'Progressive msl_foreign_slot_discovery', 'Msl Building: Crypt Keepers'),
    102421: ItemData(IC.useful, 1, 'wh2_main_foreign_slot_discovery_vmp_2', ItemType.building, 1, 'Progressive msl_foreign_slot_discovery', 'Msl Building: Undercroft Sentries'),
    102422: ItemData(IC.useful, 1, 'wh2_main_foreign_slot_discovery_vmp_3', ItemType.building, 2, 'Progressive msl_foreign_slot_discovery', 'Msl Building: Grave Guardians'),
    102423: ItemData(IC.useful, 1, 'mixu_msl_garrison_1', ItemType.building, 0, 'Progressive msl_garrison', 'Msl Building: Guard House'),
    102424: ItemData(IC.useful, 1, 'mixu_msl_garrison_2', ItemType.building, 1, 'Progressive msl_garrison', 'Msl Building: City Watch'),

    102425: ItemData(IC.useful, 1, 'mixu_msl_swampaire_camp_1', ItemType.building, 0, 'Progressive msl_swampaire', 'Msl Building: Snail Hunting Grounds'),
    102426: ItemData(IC.useful, 1, 'mixu_msl_swampaire_camp_2', ItemType.building, 1, 'Progressive msl_swampaire', 'Msl Building: Swampaire Camp'),
    102427: ItemData(IC.useful, 1, 'mixu_msl_swampaire_camp_3', ItemType.building, 2, 'Progressive msl_swampaire', 'Msl Building: Swampaire Lodge'),
    102428: ItemData(IC.useful, 1, 'wh_main_vmp_ossuary_1', ItemType.building, 0, 'Progressive msl_ossuary', 'Msl Building: Charnel Pit'),
    102429: ItemData(IC.useful, 1, 'wh_main_vmp_ossuary_2', ItemType.building, 1, 'Progressive msl_ossuary', 'Msl Building: Lychyard'),
    102430: ItemData(IC.useful, 1, 'wh_main_vmp_ossuary_3', ItemType.building, 2, 'Progressive msl_ossuary', 'Msl Building: Ossuary'),
    102431: ItemData(IC.useful, 1, 'mixu_msl_farm_1', ItemType.building, 0, 'Progressive msl_farm', 'Msl Building: Fields'),
    102432: ItemData(IC.useful, 1, 'mixu_msl_farm_2', ItemType.building, 1, 'Progressive msl_farm', 'Msl Building: Farm'),
    102433: ItemData(IC.useful, 1, 'mixu_msl_farm_3', ItemType.building, 2, 'Progressive msl_farm', 'Msl Building: Landed Estate'),
    102434: ItemData(IC.useful, 1, 'mixu_msl_balefire_1', ItemType.building, 0, 'Progressive msl_balefire', 'Msl Building: Balefire Brazier'),
    102435: ItemData(IC.useful, 1, 'mixu_msl_balefire_2', ItemType.building, 1, 'Progressive msl_balefire', 'Msl Building: Balefire Hearth'),
    102436: ItemData(IC.useful, 1, 'mixu_msl_balefire_3', ItemType.building, 2, 'Progressive msl_balefire', 'Msl Building: Witch House'),
    102437: ItemData(IC.useful, 1, 'mixu_msl_tavern_1', ItemType.building, 0, 'Progressive msl_tavern', 'Msl Building: Tap Room'),
    102438: ItemData(IC.useful, 1, 'mixu_msl_tavern_2', ItemType.building, 1, 'Progressive msl_tavern', 'Msl Building: Shady Tavern'),
    102439: ItemData(IC.useful, 1, 'mixu_msl_tavern_3', ItemType.building, 2, 'Progressive msl_tavern', 'Msl Building: Coaching Inn'),
    102440: ItemData(IC.useful, 1, 'mixu_msl_auction_house_1', ItemType.building, 0, 'Progressive msl_auction', 'Msl Building: Dark Alleyway Fence'),
    102441: ItemData(IC.useful, 1, 'mixu_msl_auction_house_2', ItemType.building, 1, 'Progressive msl_auction', 'Msl Building: Auction House'),
    102442: ItemData(IC.useful, 1, 'mixu_msl_port_1', ItemType.building, 0, 'Progressive msl_port', 'Msl Building: Crumbling Wharf'),
    102443: ItemData(IC.useful, 1, 'mixu_msl_port_2', ItemType.building, 1, 'Progressive msl_port', 'Msl Building: Murky Harbour'),
    102444: ItemData(IC.useful, 1, 'mixu_msl_port_3', ItemType.building, 2, 'Progressive msl_port', 'Msl Building: Dark Port'),

    102445: ItemData(IC.useful, 1, 'mixu_msl_resource_animals_1', ItemType.building, 0, 'Progressive msl_resource_animals', 'Msl Building: Exotic Animal Tamer'),
    102446: ItemData(IC.useful, 1, 'mixu_msl_resource_animals_2', ItemType.building, 1, 'Progressive msl_resource_animals', 'Msl Building: Exotic Animal Pen'),
    102447: ItemData(IC.useful, 1, 'mixu_msl_resource_animals_3', ItemType.building, 2, 'Progressive msl_resource_animals', 'Msl Building: Exotic Animal Market'),
    102448: ItemData(IC.useful, 1, 'mixu_msl_resource_gemstones_1', ItemType.building, 0, 'Progressive msl_resource_gemstones', 'Msl Building: Cursed Gemstone Mineshaft'),
    102449: ItemData(IC.useful, 1, 'mixu_msl_resource_gemstones_2', ItemType.building, 1, 'Progressive msl_resource_gemstones', 'Msl Building: Hexed Gemstone Pit'),
    102450: ItemData(IC.useful, 1, 'mixu_msl_resource_gemstones_3', ItemType.building, 2, 'Progressive msl_resource_gemstones', 'Msl Building: Haunted Gemstone Mine'),
    102451: ItemData(IC.useful, 1, 'mixu_msl_resource_medicine_1', ItemType.building, 0, 'Progressive msl_resource_medicine', "Msl Building: Herb Gatherer's Camp"),
    102452: ItemData(IC.useful, 1, 'mixu_msl_resource_medicine_2', ItemType.building, 1, 'Progressive msl_resource_medicine', 'Msl Building: Exotic Hothouse'),
    102453: ItemData(IC.useful, 1, 'mixu_msl_resource_medicine_3', ItemType.building, 2, 'Progressive msl_resource_medicine', 'Msl Building: Alchemy Workshop'),
    102454: ItemData(IC.useful, 1, 'mixu_msl_resource_obsidian_1', ItemType.building, 0, 'Progressive msl_resource_obsidian', 'Msl Building: Obsidian Quarry'),
    102455: ItemData(IC.useful, 1, 'mixu_msl_resource_obsidian_2', ItemType.building, 1, 'Progressive msl_resource_obsidian', 'Msl Building: Obsidian Trinket Maker'),
    102456: ItemData(IC.useful, 1, 'mixu_msl_resource_obsidian_3', ItemType.building, 2, 'Progressive msl_resource_obsidian', 'Msl Building: Obsidian Amulet Carver'),
    102457: ItemData(IC.useful, 1, 'mixu_msl_resource_spices_1', ItemType.building, 0, 'Progressive msl_resource_spices', 'Msl Building: Spice Market'),
    102458: ItemData(IC.useful, 1, 'mixu_msl_resource_spices_2', ItemType.building, 1, 'Progressive msl_resource_spices', 'Msl Building: Spice Trading Post'),
    102459: ItemData(IC.useful, 1, 'mixu_msl_resource_spices_3', ItemType.building, 2, 'Progressive msl_resource_spices', 'Msl Building: Eastern Bazaar'),
    102460: ItemData(IC.useful, 1, 'mixu_msl_resource_ivory_1', ItemType.building, 0, 'Progressive msl_resource_ivory', 'Msl Building: Animal Store'),
    102461: ItemData(IC.useful, 1, 'mixu_msl_resource_ivory_2', ItemType.building, 1, 'Progressive msl_resource_ivory', 'Msl Building: Tusk Market'),
    102462: ItemData(IC.useful, 1, 'mixu_msl_resource_ivory_3', ItemType.building, 2, 'Progressive msl_resource_ivory', 'Msl Building: Tusk Compound'),
    102463: ItemData(IC.useful, 1, 'mixu_msl_resource_dyes_1', ItemType.building, 0, 'Progressive msl_resource_dyes', 'Msl Building: Red Pit'),
    102464: ItemData(IC.useful, 1, 'mixu_msl_resource_dyes_2', ItemType.building, 1, 'Progressive msl_resource_dyes', 'Msl Building: Blood Mines'),
    102465: ItemData(IC.useful, 1, 'mixu_msl_resource_dyes_3', ItemType.building, 2, 'Progressive msl_resource_dyes', "Msl Building: Pigment Grinder's Shop"),
    102466: ItemData(IC.useful, 1, 'mixu_msl_resource_furs_1', ItemType.building, 0, 'Progressive msl_resource_furs', 'Msl Building: Hunting Grounds'),
    102467: ItemData(IC.useful, 1, 'mixu_msl_resource_furs_2', ItemType.building, 1, 'Progressive msl_resource_furs', 'Msl Building: Poaching Camp'),
    102468: ItemData(IC.useful, 1, 'mixu_msl_resource_furs_3', ItemType.building, 2, 'Progressive msl_resource_furs', "Msl Building: Flayer's Lair"),
    102469: ItemData(IC.useful, 1, 'mixu_msl_resource_gold_1', ItemType.building, 0, 'Progressive msl_resource_gold', 'Msl Building: Tarnished Gold Shaft'),
    102470: ItemData(IC.useful, 1, 'mixu_msl_resource_gold_2', ItemType.building, 1, 'Progressive msl_resource_gold', 'Msl Building: Tarnished Gold Mine'),
    102471: ItemData(IC.useful, 1, 'mixu_msl_resource_gold_3', ItemType.building, 2, 'Progressive msl_resource_gold', 'Msl Building: Balefire Gold Smeltery'),
    102472: ItemData(IC.useful, 1, 'mixu_msl_resource_iron_1', ItemType.building, 0, 'Progressive msl_resource_iron', 'Msl Building: Iron Mining Pit'),
    102473: ItemData(IC.useful, 1, 'mixu_msl_resource_iron_2', ItemType.building, 1, 'Progressive msl_resource_iron', 'Msl Building: Iron Mine'),
    102474: ItemData(IC.useful, 1, 'mixu_msl_resource_iron_3', ItemType.building, 2, 'Progressive msl_resource_iron', 'Msl Building: Iron Smelter'),
    102475: ItemData(IC.useful, 1, 'mixu_msl_resource_marble_1', ItemType.building, 0, 'Progressive msl_resource_marble', "Msl Building: Brimstone Cutter's Workshop"),
    102476: ItemData(IC.useful, 1, 'mixu_msl_resource_marble_2', ItemType.building, 1, 'Progressive msl_resource_marble', "Msl Building: Tombstone Maker's Atelier"),
    102477: ItemData(IC.useful, 1, 'mixu_msl_resource_marble_3', ItemType.building, 2, 'Progressive msl_resource_marble', "Msl Building: Gargoyle Sculptor's Garret"),
    102478: ItemData(IC.useful, 1, 'mixu_msl_resource_pastures_1', ItemType.building, 0, 'Progressive msl_resource_pastures', 'Msl Building: Grazing Pastures'),
    102479: ItemData(IC.useful, 1, 'mixu_msl_resource_pastures_2', ItemType.building, 1, 'Progressive msl_resource_pastures', 'Msl Building: Livestock Pens'),
    102480: ItemData(IC.useful, 1, 'mixu_msl_resource_pastures_3', ItemType.building, 2, 'Progressive msl_resource_pastures', 'Msl Building: Cattle Ranch'),
    102481: ItemData(IC.useful, 1, 'mixu_msl_resource_pottery_1', ItemType.building, 0, 'Progressive msl_resource_pottery', 'Msl Building: Flooded Clay Pit'),
    102482: ItemData(IC.useful, 1, 'mixu_msl_resource_pottery_2', ItemType.building, 1, 'Progressive msl_resource_pottery', "Msl Building: Urn Maker's Pottery"),
    102483: ItemData(IC.useful, 1, 'mixu_msl_resource_pottery_3', ItemType.building, 2, 'Progressive msl_resource_pottery', 'Msl Building: Screeching Kilns'),
    102484: ItemData(IC.useful, 1, 'mixu_msl_resource_salt_1', ItemType.building, 0, 'Progressive msl_resource_salt', 'Msl Building: Brackish Pond'),
    102485: ItemData(IC.useful, 1, 'mixu_msl_resource_salt_2', ItemType.building, 1, 'Progressive msl_resource_salt', 'Msl Building: Salt Marsh'),
    102486: ItemData(IC.useful, 1, 'mixu_msl_resource_salt_3', ItemType.building, 2, 'Progressive msl_resource_salt', 'Msl Building: Desolate Salt Pans'),
    102487: ItemData(IC.useful, 1, 'mixu_msl_resource_timber_1', ItemType.building, 0, 'Progressive msl_resource_timber', "Msl Building: Woodman's Hut"),
    102488: ItemData(IC.useful, 1, 'mixu_msl_resource_timber_2', ItemType.building, 1, 'Progressive msl_resource_timber', 'Msl Building: Timber Mill'),
    102489: ItemData(IC.useful, 1, 'mixu_msl_resource_timber_3', ItemType.building, 2, 'Progressive msl_resource_timber', 'Msl Building: Lumberyard'),
    102490: ItemData(IC.useful, 1, 'mixu_msl_resource_wine_1', ItemType.building, 0, 'Progressive msl_resource_wine', 'Msl Building: Tangled Vine Patch'),
    102491: ItemData(IC.useful, 1, 'mixu_msl_resource_wine_2', ItemType.building, 1, 'Progressive msl_resource_wine', 'Msl Building: Thorny Orchard'),
    102492: ItemData(IC.useful, 1, 'mixu_msl_resource_wine_3', ItemType.building, 2, 'Progressive msl_resource_wine', 'Msl Building: Animated Winepress'),

    102493: ItemData(IC.useful, 1, 'mixu_msl_settlement_major_1', ItemType.building, 0, 'Progressive msl_settlement_major', 'Msl Building: Crumbling Hamlet'),
    102494: ItemData(IC.useful, 1, 'mixu_msl_settlement_major_2', ItemType.building, 1, 'Progressive msl_settlement_major', 'Msl Building: Corrupted Village'),
    102495: ItemData(IC.useful, 1, 'mixu_msl_settlement_major_3', ItemType.building, 2, 'Progressive msl_settlement_major', 'Msl Building: Shady Township'),
    102496: ItemData(IC.useful, 1, 'mixu_msl_settlement_major_4', ItemType.building, 3, 'Progressive msl_settlement_major', 'Msl Building: Accursed City'),
    102497: ItemData(IC.useful, 1, 'mixu_msl_settlement_major_5', ItemType.building, 4, 'Progressive msl_settlement_major', 'Msl Building: Dark Castle'),
    102498: ItemData(IC.useful, 1, 'mixu_msl_settlement_minor_1', ItemType.building, 0, 'Progressive msl_settlement_minor', 'Msl Building: Crumbling Hamlet'),
    102499: ItemData(IC.useful, 1, 'mixu_msl_settlement_minor_2', ItemType.building, 1, 'Progressive msl_settlement_minor', 'Msl Building: Corrupted Village'),
    102500: ItemData(IC.useful, 1, 'mixu_msl_settlement_minor_3', ItemType.building, 2, 'Progressive msl_settlement_minor', 'Msl Building: Shady Township'),
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

techs: dict[int, ItemData] = {
    102800: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_cursed_land', ItemType.tech, 1, 'Progressive tech_msl_undead', 'Msl Tech: Cursed Land'),
    102801: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_raise_newly_dead', ItemType.tech, 2, 'Progressive tech_msl_undead', 'Msl Tech: Raise Newly Dead'),
    102802: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_defiler_of_the_ancient_barrows', ItemType.tech, 2, 'Progressive tech_msl_undead', 'Msl Tech: Defiler of the Ancient Dragon'),
    102803: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_rotten_gift', ItemType.tech, 2, 'Progressive tech_msl_undead', 'Msl Tech: Rotten Gift'),
    102804: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_bonds_of_flesh', ItemType.tech, 2, 'Progressive tech_msl_undead', 'Msl Tech: Bonds of Flesh'),
    102805: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_dread_animator', ItemType.tech, 2, 'Progressive tech_msl_undead', 'Msl Tech: Dread Animator'),
    102806: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_spirit_shackles', ItemType.tech, 2, 'Progressive tech_msl_undead', 'Msl Tech: Spirit Shackles'),
    102807: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_unearth_cursed_blades', ItemType.tech, 2, 'Progressive tech_msl_undead', 'Msl Tech: Unearth Cursed Blades'),
    102808: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_cannibalistic_rituals', ItemType.tech, 2, 'Progressive tech_msl_undead', 'Msl Tech: Cannibalistic Rituals'),
    102809: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_enshrine_ancient_lords', ItemType.tech, 2, 'Progressive tech_msl_undead', 'Msl Tech: Enshrine Ancient Lords'),
    102810: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_infuse_the_tireless_hordes', ItemType.tech, 2, 'Progressive tech_msl_undead', 'Msl Tech: Infuse the Tireless Hordes'),
    102811: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_soulbinder', ItemType.tech, 2, 'Progressive tech_msl_undead', 'Msl Tech: Soulbinder'),
    102812: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_nightmarish_reaping', ItemType.tech, 2, 'Progressive tech_msl_undead', 'Msl Tech: Nightmarish Reaping'),

    102813: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_living_rally_the_peasants', ItemType.tech, 1, 'Progressive tech_msl_living', 'Msl Tech: Rally the Peasants'),
    102814: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_living_disgraced_and_damned', ItemType.tech, 2, 'Progressive tech_msl_living', 'Msl Tech: Disgraced and Damned'),
    102815: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_living_embrace_the_darkness', ItemType.tech, 2, 'Progressive tech_msl_living', 'Msl Tech: Embrace the Darkness'),
    102816: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_living_steel_furnaces', ItemType.tech, 2, 'Progressive tech_msl_living', 'Msl Tech: Steel Furnaces'),
    102817: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_living_master_swordsmiths', ItemType.tech, 2, 'Progressive tech_msl_living', 'Msl Tech: Master Swordsmiths'),
    102818: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_living_professional_fletchers', ItemType.tech, 2, 'Progressive tech_msl_living', 'Msl Tech: Professional Fletchers'),
    102819: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_living_siege_engineering', ItemType.tech, 2, 'Progressive tech_msl_living', 'Msl Tech: Siege Engineering'),
    102820: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_living_serve_in_life_or_in_death', ItemType.tech, 2, 'Progressive tech_msl_living', 'Msl Tech: Serve in Life or in Death'),
    102821: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_living_charity', ItemType.tech, 2, 'Progressive tech_msl_living', 'Msl Tech: Charity'),
    102822: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_living_registered_draft', ItemType.tech, 2, 'Progressive tech_msl_living', 'Msl Tech: Registered Draft'),
    102823: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_living_bigger_shovels', ItemType.tech, 2, 'Progressive tech_msl_living', 'Msl Tech: Bigger Shovels'),
    102824: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_living_subsidised_tools', ItemType.tech, 2, 'Progressive tech_msl_living', 'Msl Tech: Subsidised Tools'),
    102825: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_living_improved_construction', ItemType.tech, 2, 'Progressive tech_msl_living', 'Msl Tech: Improved Construction'),

    102826: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_cavalry_regular_tournaments', ItemType.tech, 1, 'Progressive tech_msl_knights', 'Msl Tech: Regular Tournaments'),
    102827: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_cavalry_dark_deeds', ItemType.tech, 1, 'Progressive tech_msl_knights', 'Msl Tech: Dark Deeds'),
    102828: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_cavalry_unholy_strength', ItemType.tech, 1, 'Progressive tech_msl_knights', 'Msl Tech: Unholy Strength'),

    102829: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_swamps_horrors_of_the_bog', ItemType.tech, 1, 'Progressive tech_msl_swamp', 'Msl Tech: Horrors of the Bog'),
    102830: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_swamps_swampaire_training', ItemType.tech, 1, 'Progressive tech_msl_swamp', 'Msl Tech: Swampaire Training'),
    102831: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_swamps_support_the_frogwives', ItemType.tech, 1, 'Progressive tech_msl_swamp', 'Msl Tech: Support the Frogwives'),

    102832: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_nobels_of_mousillon', ItemType.tech, 1, 'Progressive tech_msl_nobility', 'Msl Tech: Nobles of Mousillon'),
    102833: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_blood_is_power', ItemType.tech, 2, 'Progressive tech_msl_nobility', 'Msl Tech: Blood is Power'),
    102834: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_hexensnacht_sacrifices', ItemType.tech, 2, 'Progressive tech_msl_nobility', 'Msl Tech: Hexensnacht Sacrifices'),
    102835: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_blasphemous_disciples', ItemType.tech, 2, 'Progressive tech_msl_nobility', 'Msl Tech: Blasphemous Disciples'),
    102836: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_spread_vampire_covens', ItemType.tech, 2, 'Progressive tech_msl_nobility', 'Msl Tech: Spread Vampire Covens'),
    102837: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_turning_knights_of_the_realm', ItemType.tech, 2, 'Progressive tech_msl_nobility', 'Msl Tech: Turning Knights of the Realm'),
    102838: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_delusions_of_grandeur', ItemType.tech, 2, 'Progressive tech_msl_nobility', 'Msl Tech: Delusions of Grandeur'),
    102839: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_puppet_master', ItemType.tech, 2, 'Progressive tech_msl_nobility', 'Msl Tech: Puppet Master'),
    102840: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_infiltrate_noble_houses', ItemType.tech, 2, 'Progressive tech_msl_nobility', 'Msl Tech: Infiltrate Noble Houses'),
    102841: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_baleful_rituals', ItemType.tech, 2, 'Progressive tech_msl_nobility', 'Msl Tech: Baleful Rituals'),
    102842: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_vampiric_revivification', ItemType.tech, 2, 'Progressive tech_msl_nobility', 'Msl Tech: Vampiric Revivification'),
    102843: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_traditions_of_hospitality', ItemType.tech, 2, 'Progressive tech_msl_nobility', 'Msl Tech: Traditions of Hospitality'),
    102844: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_code_of_conduct', ItemType.tech, 2, 'Progressive tech_msl_nobility', 'Msl Tech: Code of Conduct'),
}

progUnits: dict[int, ItemData] = {
    103200: ItemData(IC.useful, 2, "Progressive msl_inf", ItemType.unit, 2, "", "Progressive Msl Unit: Infantry"),
    103201: ItemData(IC.useful, 2, "Progressive msl_rng", ItemType.unit, 2, "", "Progressive Msl Unit: Ranged"),
    103202: ItemData(IC.useful, 3, "Progressive msl_cav", ItemType.unit, 3, "", "Progressive Msl Unit: Cavalry"),
    103203: ItemData(IC.useful, 1, "Progressive msl_art", ItemType.unit, 1, "", "Progressive Msl Unit: Artillery"),
    103204: ItemData(IC.useful, 4, "Progressive msl_veh", ItemType.unit, 4, "", "Progressive Msl Unit: Chariot"),
    103205: ItemData(IC.useful, 2, "Progressive msl_bst", ItemType.unit, 2, "", "Progressive Msl Unit: Beast"),
    103206: ItemData(IC.useful, 2, "Progressive msl_hro", ItemType.unit, 2, "", "Progressive Msl Unit: Hero")
}

progBuildings: dict[int, ItemData] = {
    103400: ItemData(IC.useful, 1, 'Progressive msl_cemetery', ItemType.building, 2, '', 'Progressive Msl Building: Cemetery'),
    103401: ItemData(IC.useful, 1, 'Progressive msl_barracks', ItemType.building, 2, '', 'Progressive Msl Building: Barracks'),
    103402: ItemData(IC.useful, 1, 'Progressive msl_swamp', ItemType.building, 2, '', 'Progressive Msl Building: Swamp'),
    103403: ItemData(IC.useful, 1, 'Progressive msl_binding', ItemType.building, 3, '', 'Progressive Msl Building: Binding'),
    103404: ItemData(IC.useful, 1, 'Progressive msl_carpenter', ItemType.building, 2, '', 'Progressive Msl Building: Carpenter'),
    103405: ItemData(IC.useful, 1, 'Progressive msl_wraiths', ItemType.building, 3, '', 'Progressive Msl Building: Wraiths'),
    103406: ItemData(IC.useful, 1, 'Progressive msl_vampires', ItemType.building, 2, '', "Progressive Msl Building: Vampires"),

    103407: ItemData(IC.useful, 1, 'Progressive msl_walls', ItemType.building, 3, '', 'Progressive Msl Building: Walls'),
    103408: ItemData(IC.useful, 1, 'Progressive msl_battlefield', ItemType.building, 1, '', 'Progressive Msl Building: Awakened Battlefield'),
    103409: ItemData(IC.useful, 1, 'Progressive msl_foreign_slot_discovery', ItemType.building, 3, '', 'Progressive Msl Building: Protection'),
    103410: ItemData(IC.useful, 1, 'Progressive msl_garrison', ItemType.building, 2, '', 'Progressive Msl Building: Garrison'),

    103411: ItemData(IC.useful, 1, 'Progressive msl_swampaire', ItemType.building, 3, '', 'Progressive Msl Building: Swampaire'),
    103412: ItemData(IC.useful, 1, 'Progressive msl_ossuary', ItemType.building, 3, '', 'Progressive Msl Building: Ossuary'),
    103413: ItemData(IC.useful, 1, 'Progressive msl_farm', ItemType.building, 3, '', 'Progressive Msl Building: Farms'),
    103414: ItemData(IC.useful, 1, 'Progressive msl_balefire', ItemType.building, 3, '', 'Progressive Msl Building: Witches'),
    103415: ItemData(IC.useful, 1, 'Progressive msl_tavern', ItemType.building, 3, '', 'Progressive Msl Building: Tavern'),
    103416: ItemData(IC.useful, 1, 'Progressive msl_auction', ItemType.building, 2, '', 'Progressive Msl Building: Trade'),
    103417: ItemData(IC.useful, 1, 'Progressive msl_port', ItemType.building, 3, '', 'Progressive Msl Building: Port'),

    103418: ItemData(IC.useful, 1, 'Progressive msl_resource_animals', ItemType.building, 3, '', 'Progressive Msl Building: Animals'),
    103419: ItemData(IC.useful, 1, 'Progressive msl_resource_gemstones', ItemType.building, 3, '', 'Progressive Msl Building: Gemstones'),
    103420: ItemData(IC.useful, 1, 'Progressive msl_resource_medicine', ItemType.building, 3, '', 'Progressive Msl Building: Medicine'),
    103421: ItemData(IC.useful, 1, 'Progressive msl_resource_obsidian', ItemType.building, 3, '', 'Progressive Msl Building: Obsidian'),
    103422: ItemData(IC.useful, 1, 'Progressive msl_resource_spices', ItemType.building, 3, '', 'Progressive Msl Building: Spices'),
    103423: ItemData(IC.useful, 1, 'Progressive msl_resource_ivory', ItemType.building, 3, '', 'Progressive Msl Building: Ivory'),
    103424: ItemData(IC.useful, 1, 'Progressive msl_resource_dyes', ItemType.building, 3, '', "Progressive Msl Building: Dyes"),
    103425: ItemData(IC.useful, 1, 'Progressive msl_resource_furs', ItemType.building, 3, '', "Progressive Msl Building: Furs"),
    103426: ItemData(IC.useful, 1, 'Progressive msl_resource_gold', ItemType.building, 3, '', 'Progressive Msl Building: Gold'),
    103427: ItemData(IC.useful, 1, 'Progressive msl_resource_iron', ItemType.building, 3, '', 'Progressive Msl Building: Iron'),
    103428: ItemData(IC.useful, 1, 'Progressive msl_resource_marble', ItemType.building, 3, '', "Progressive Msl Building: Marble"),
    103429: ItemData(IC.useful, 1, 'Progressive msl_resource_pastures', ItemType.building, 3, '', 'Progressive Msl Building: Pastures'),
    103430: ItemData(IC.useful, 1, 'Progressive msl_resource_pottery', ItemType.building, 3, '', 'Progressive Msl Building: Pottery'),
    103431: ItemData(IC.useful, 1, 'Progressive msl_resource_salt', ItemType.building, 3, '', 'Progressive Msl Building: Salt'),
    103432: ItemData(IC.useful, 1, 'Progressive msl_resource_timber', ItemType.building, 3, '', 'Progressive Msl Building: Timber'),
    103433: ItemData(IC.useful, 1, 'Progressive msl_resource_wine', ItemType.building, 3, '', 'Progressive Msl Building: Wine'),

    103434: ItemData(IC.useful, 1, 'Progressive msl_settlement_major', ItemType.building, 5, '', 'Vmp Building: Settlement Major'),
    103535: ItemData(IC.useful, 1, 'Progressive msl_settlement_minor', ItemType.building, 3, '', 'Vmp Building: Settlement Minor'),
}

progTechs: dict[int, ItemData] = {
    103400: ItemData(IC.useful, 2, "Progressive tech_msl_undead", ItemType.tech, 2, "", "Progressive Msl Tech: Living Dead"),
    103401: ItemData(IC.useful, 2, "Progressive tech_msl_living", ItemType.tech, 2, "", "Progressive Msl Tech: Peasantry"),
    103402: ItemData(IC.useful, 2, "Progressive tech_msl_knights", ItemType.tech, 1, "", "Progressive Msl Tech: Knights of the Realm"),
    103403: ItemData(IC.useful, 2, "Progressive tech_msl_swamp", ItemType.tech, 1, "", "Progressive Msl Tech: Swamp Land"),
    103404: ItemData(IC.useful, 2, "Progressive tech_msl_nobility", ItemType.tech, 2, "", "Progressive Msl Tech: Nobility"),
}

special: dict[int, specialItemData] = {
    103500: specialItemData(IC.useful, 1, 'mixer_msl_cult_of_the_bloody_grail', "mixu_msl_ror_cantankerous_bellends", ItemType.unit, 1, 'Progressive msl_inf', False, False, 'Msl Unit: Cantankerous Bellends (Men-at-Arms)'),
    103501: specialItemData(IC.useful, 1, 'mixer_msl_cult_of_the_bloody_grail', "mixu_msl_ror_knights_of_bougar", ItemType.unit, 2, 'Progressive msl_cav', False, False, 'Msl Unit: Knights of Bougars'),
    103502: specialItemData(IC.useful, 1, 'mixer_msl_cult_of_the_bloody_grail', "mixu_msl_ror_the_rose_lances", ItemType.unit, 1, 'Progressive msl_cav', False, False, 'Msl Unit: The Rose Lances (Black Knights)'),
    103503: specialItemData(IC.useful, 1, 'mixer_msl_cult_of_the_bloody_grail', "mixu_msl_ror_ghosts_of_grismerie", ItemType.unit, 1, 'Progressive msl_inf', False, False, 'Msl Unit: Ghosts of Grismerie (Grey Men)'),
    103504: specialItemData(IC.useful, 1, 'mixer_msl_cult_of_the_bloody_grail', "mixu_msl_ror_barons_men", ItemType.unit, 1, 'Progressive msl_inf', False, False, "Msl Unit: Baron's Men (Crypt Ghouls)"),
}