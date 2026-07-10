from BaseClasses import ItemClassification as IC
from worlds.tww3.dataStructs import itemType, itemData, specialItemData
from worlds.tww3.faction_item_tables import cathay

# @formatter:off
units: dict[int, itemData] = {
    74000: itemData(IC.useful, 1, 'wh3_main_cth_inf_peasant_spearmen_1', itemType.unit, 1, 'Progressive cth_bhashiva_inf', 'Cathay Bhashiva Unit: Peasant Long Spearmen'),
    74041: itemData(IC.useful, 1, 'wh3_dlc24_cth_inf_onyx_crowmen', itemType.unit, 2, 'Progressive cth_bhashiva_inf', 'Cathay Unit: Onyx Crowmen'),
    74001: itemData(IC.useful, 1, 'wh3_main_cth_inf_jade_warriors_0', itemType.unit, 1, 'Progressive cth_bhashiva_inf', 'Cathay Bhashiva Unit: Jade Warriors'),
    74002: itemData(IC.useful, 1, 'wh3_main_cth_inf_jade_warriors_1', itemType.unit, 3, 'Progressive cth_bhashiva_inf', 'Cathay Bhashiva Unit: Jade Warriors (Halberds)'),
    74033: itemData(IC.useful, 1, 'wh3_main_cth_inf_dragon_guard_0', itemType.unit, 4, 'Progressive cth_bhashiva_inf', 'Cathay Bhashiva Unit: Celestial Dragon Guard'),
    74003: itemData(IC.useful, 1, 'wh3_cp1_cth_inf_tiger_warriors_dual_axe', itemType.unit, 2, 'Progressive cth_bhashiva_inf', 'Cathay Bhashiva Unit: Tiger Warriors'),
    74004: itemData(IC.useful, 1, 'wh3_cp1_cth_inf_stalkers_throwing_disc', itemType.unit, 3, 'Progressive cth_bhashiva_inf', 'Cathay Bhashiva Unit: Tiger Warrior Stalkers'),
    74005: itemData(IC.useful, 1, 'wh3_cp1_cth_inf_iron_claw_guandao', itemType.unit, 4, 'Progressive cth_bhashiva_inf', 'Cathay Bhashiva Unit: Iron Claw Tiger Warriors'),

    74006: itemData(IC.useful, 1, 'wh3_main_cth_inf_peasant_archers_0', itemType.unit, 1, 'Progressive cth_bhashiva_rng', 'Cathay Bhashiva Unit: Peasant Archers'),
    74007: itemData(IC.useful, 1, 'wh3_main_cth_inf_jade_warrior_crossbowmen_0', itemType.unit, 1, 'Progressive cth_bhashiva_rng', 'Cathay Bhashiva Unit: Jade Warrior Crossbows'),
    74008: itemData(IC.useful, 1, 'wh3_main_cth_inf_jade_warrior_crossbowmen_1', itemType.unit, 3, 'Progressive cth_bhashiva_rng', 'Cathay Bhashiva Unit: Jade Warrior Crossbows (Shields)'),
    74009: itemData(IC.useful, 1, 'wh3_main_cth_inf_iron_hail_gunners_0', itemType.unit, 2, 'Progressive cth_bhashiva_rng', 'Cathay Bhashiva Unit: Iron Hail Gunners'),
    74034: itemData(IC.useful, 1, 'wh3_main_cth_inf_grenadiers', itemType.unit, 2, 'Progressive cth_bhashiva_rng', 'Cathay Bhashiva Unit: Nan-Gau Grenadiers'),
    74010: itemData(IC.useful, 1, 'wh3_main_cth_inf_crane_gunners_0', itemType.unit, 4, 'Progressive cth_bhashiva_rng', 'Cathay Bhashiva Unit: Crane Gunners'),
    74035: itemData(IC.useful, 1, 'wh3_main_cth_inf_dragon_guard_crossbowmen_0', itemType.unit, 4, 'Progressive cth_bhashiva_rng', 'Cathay Bhashiva Unit: Celestial Dragon Crossbows'),

    74011: itemData(IC.useful, 1, 'wh3_main_cth_cav_peasant_horsemen_0', itemType.unit, 1, 'Progressive cth_bhashiva_cav', 'Cathay Bhashiva Unit: Peasant Horsemen'),
    74012: itemData(IC.useful, 1, 'wh3_main_cth_cav_jade_lancers_0', itemType.unit, 2, 'Progressive cth_bhashiva_cav', 'Cathay Bhashiva Unit: Jade Lancers'),
    74013: itemData(IC.useful, 1, 'wh3_main_cth_cav_jade_longma_riders_0', itemType.unit, 3, 'Progressive cth_bhashiva_cav', 'Cathay Bhashiva Unit: Great Longma Riders'),

    74014: itemData(IC.useful, 1, 'wh3_main_cth_art_grand_cannon_0', itemType.unit, 1, 'Progressive cth_bhashiva_art', 'Cathay Bhashiva Unit: Grand Cannons'),
    74036: itemData(IC.useful, 1, 'wh3_main_cth_art_fire_rain_rocket_battery_0', itemType.unit, 2, 'Progressive cth_art', 'Cathay Bhashiva Unit: Fire Rain Rocket Battery'),

    74037: itemData(IC.useful, 1, 'wh3_dlc24_cth_veh_zhangu_war_drum', itemType.unit, 1, 'Progressive cth_veh', 'Cathay Bhashiva Unit: Zhangu War Drum'),
    74038: itemData(IC.useful, 1, 'wh3_main_cth_veh_war_compass_0', itemType.unit, 2, 'Progressive cth_veh', 'Cathay Bhashiva Unit: Wu Xing War Compass'),
    74015: itemData(IC.useful, 1, 'wh3_main_cth_veh_sky_lantern_0', itemType.unit, 1, 'Progressive cth_bhashiva_veh', 'Cathay Bhashiva Unit: Sky Lantern'),
    74016: itemData(IC.useful, 1, 'wh3_main_cth_veh_sky_junk_0', itemType.unit, 2, 'Progressive cth_bhashiva_veh', 'Cathay Bhashiva Unit: Sky-junk'),

    74039: itemData(IC.useful, 1, 'wh3_dlc24_cth_mon_jet_lion', itemType.unit, 1, 'Progressive cth_bhashiva_bst', 'Cathay Bhashiva Unit: Jet Lion'),
    74040: itemData(IC.useful, 1, 'wh3_dlc24_cth_mon_jade_lion', itemType.unit, 1, 'Progressive cth_bhashiva_bst', 'Cathay Bhashiva Unit: Jade Lion'),
    74017: itemData(IC.useful, 1, 'wh3_dlc24_cth_mon_celestial_lion', itemType.unit, 1, 'Progressive cth_bhashiva_bst', 'Cathay Bhashiva Unit: Celestial Lion'),
    74018: itemData(IC.useful, 1, 'wh3_dlc24_cth_mon_great_moon_bird', itemType.unit, 2, 'Progressive cth_bhashiva_bst', 'Cathay Bhashiva Unit: Great Moon Bird'),
    74019: itemData(IC.useful, 1, 'wh3_main_cth_mon_terracotta_sentinel_0', itemType.unit, 3, 'Progressive cth_bhashiva_bst', 'Cathay Bhashiva Unit: Terracotta Sentinel'),

    74020: itemData(IC.useful, 1, 'wh3_dlc24_cth_cha_gate_master', itemType.unit, 1, 'Progressive cth_bhashiva_hro', 'Cathay Bhashiva Unit: Gate Master'),
    74021: itemData(IC.useful, 1, 'wh3_main_cth_cha_astromancer_0', itemType.unit, 1, 'Progressive cth_bhashiva_hro', 'Cathay Bhashiva Unit: Astromancer'),
    74022: itemData(IC.useful, 1, 'wh3_main_cth_cha_alchemist_0', itemType.unit, 1, 'Progressive cth_bhashiva_hro', 'Cathay Bhashiva Unit: Alchemist'),
    74023: itemData(IC.useful, 1, 'wh3_cp1_cth_cha_clawspeaker_life', itemType.unit, 1, 'Progressive cth_bhashiva_hro', 'Cathay Bhashiva Unit: Clawspeaker (Life)'),
    74024: itemData(IC.useful, 1, 'wh3_cp1_cth_cha_clawspeaker_beasts', itemType.unit, 1, 'Progressive cth_bhashiva_hro', 'Cathay Bhashiva Unit: Clawspeaker (Beasts)'),
    74025: itemData(IC.useful, 1, 'wh3_cp1_cth_cha_clawspeaker_shadows', itemType.unit, 1, 'Progressive cth_bhashiva_hro', 'Cathay Bhashiva Unit: Clawspeaker (Shadows)'),

    74026: itemData(IC.useful, 1, 'wh3_twa10_cth_inf_peasant_archers_ror', itemType.unit, 1, 'Progressive cth_bhashiva_rng', 'Cathay Bhashiva Unit: Bandits of the Silver Road (Peasant Archers)'),
    74027: itemData(IC.useful, 1, 'wh3_twa08_cth_mon_terracotta_sentinel_0_ror', itemType.unit, 3, 'Progressive cth_bhashiva_bst', 'Cathay Bhashiva Unit: The Green Guardian (Terracotta Sentinel)'),
    74028: itemData(IC.useful, 1, 'wh3_twa07_cth_cav_jade_longma_riders_ror_0', itemType.unit, 3, 'Progressive cth_bhashiva_cav', 'Cathay Bhashiva Unit: Righteous Lances of Wei-Jin (Great Longma Riders)'),
    74029: itemData(IC.useful, 1, 'wh3_twa06_cth_inf_dragon_guard_ror_0', itemType.unit, 4, 'Progressive cth_bhashiva_inf', 'Cathay Bhashiva Unit: The Dune Dragons (Celestial Dragon Guard)'),
    74030: itemData(IC.useful, 1, 'wh3_dlc24_cth_inf_dragon_guard_crossbowmen_ror', itemType.unit, 4, 'Progressive cth_bhashiva_rng', 'Cathay Bhashiva Unit: The Grace of Quai Yin (Celestial Dragon Crossbows)'),
    74031: itemData(IC.useful, 1, 'wh3_dlc24_cth_inf_onyx_crowmen_ror', itemType.unit, 2, 'Progressive cth_bhashiva_inf', 'Cathay Bhashiva Unit: Empress Crowmen (Onyx Crowmen)'),
    74032: itemData(IC.useful, 1, 'wh3_dlc24_cth_veh_zhangu_war_drum_ror', itemType.unit, 1, 'Progressive cth_bhashiva_veh', 'Cathay Bhashiva Unit: The Jade War Drum (Zhangu War Drum)')
}

buildings: dict[int, itemData] = {
    74400: itemData(IC.useful, 1, 'wh3_cp1_cth_bhashiva_settlement_major_1', itemType.building, 0, 'Progressive cth_bhashiva_settlement_major', 'Cathay Bhashiva Building: Hamlet (Major)'),
    74401: itemData(IC.useful, 1, 'wh3_cp1_cth_bhashiva_settlement_major_2', itemType.building, 1, 'Progressive cth_bhashiva_settlement_major', 'Cathay Bhashiva Building: Village (Major)'),
    74402: itemData(IC.useful, 1, 'wh3_cp1_cth_bhashiva_settlement_major_3', itemType.building, 2, 'Progressive cth_bhashiva_settlement_major', 'Cathay Bhashiva Building: Town (Major)'),
    74403: itemData(IC.useful, 1, 'wh3_cp1_cth_bhashiva_settlement_major_4', itemType.building, 3, 'Progressive cth_bhashiva_settlement_major', 'Cathay Bhashiva Building: City (Major)'),
    74404: itemData(IC.useful, 1, 'wh3_cp1_cth_bhashiva_settlement_major_5', itemType.building, 4, 'Progressive cth_bhashiva_settlement_major', 'Cathay Bhashiva Building: Province Capital (Major)'),
    74405: itemData(IC.useful, 1, 'wh3_cp1_cth_bhashiva_settlement_minor_1', itemType.building, 0, 'Progressive cth_bhashiva_settlement_minor', 'Cathay Bhashiva Building: Hamlet (Minor)'),
    74406: itemData(IC.useful, 1, 'wh3_cp1_cth_bhashiva_settlement_minor_2', itemType.building, 1, 'Progressive cth_bhashiva_settlement_minor', 'Cathay Bhashiva Building: Village (Minor)'),
    74407: itemData(IC.useful, 1, 'wh3_cp1_cth_bhashiva_settlement_minor_3', itemType.building, 2, 'Progressive cth_bhashiva_settlement_minor', 'Cathay Bhashiva Building: Town (Minor)'),
    74408: itemData(IC.useful, 1, 'wh3_cp1_cth_den_tigers_1_bhashiva', itemType.building, 0, 'Progressive cth_bhashiva_tigers', 'Cathay Bhashiva Building: Tiger Warrior Den'),
    74409: itemData(IC.useful, 1, 'wh3_cp1_cth_den_tigers_2_bhashiva', itemType.building, 1, 'Progressive cth_bhashiva_tigers', 'Cathay Bhashiva Building: Clawspeaker Shrine'),
    74410: itemData(IC.useful, 1, 'wh3_cp1_cth_den_tigers_3_bhashiva', itemType.building, 2, 'Progressive cth_bhashiva_tigers', 'Cathay Bhashiva Building: Iron Claw Barracks'),

    74411: itemData(IC.useful, 1, 'wh3_cp1_cth_armoury_tigers_0', itemType.building, 0, 'Progressive cth_bhashiva_armoury', 'Cathay Bhashiva Building: Jade Muster'),
    74412: itemData(IC.useful, 1, 'wh3_cp1_cth_armoury_tigers_1', itemType.building, 1, 'Progressive cth_bhashiva_armoury', 'Cathay Bhashiva Building: Warden Arsenal'),
    74413: itemData(IC.useful, 1, 'wh3_cp1_cth_armoury_tigers_2', itemType.building, 2, 'Progressive cth_bhashiva_armoury', 'Cathay Bhashiva Building: Dragon Armoury'),

    74414: itemData(IC.useful, 1, 'wh3_cp1_cth_gunpowder_tigers_1', itemType.building, 0, 'Progressive cth_bhashiva_gunpowder', 'Cathay Bhashiva Building: Powderhouse'),
    74415: itemData(IC.useful, 1, 'wh3_cp1_cth_gunpowder_tigers_2', itemType.building, 1, 'Progressive cth_bhashiva_gunpowder', 'Cathay Bhashiva Building: Cannon Foundry'),
    74416: itemData(IC.useful, 1, 'wh3_cp1_cth_gunpowder_tigers_3', itemType.building, 2, 'Progressive cth_bhashiva_gunpowder', 'Cathay Bhashiva Building: Crane Gun Hall'),

    74417: itemData(IC.useful, 1, 'wh3_cp1_cth_living_forge_tigers_1', itemType.building, 0, 'Progressive cth_bhashiva_forge', 'Cathay Bhashiva Building: Star-Forged Eyrie'),
    74418: itemData(IC.useful, 1, 'wh3_cp1_cth_living_forge_tigers_2', itemType.building, 1, 'Progressive cth_bhashiva_forge', 'Cathay Bhashiva Building: Heavenwing Roost'),
    74419: itemData(IC.useful, 1, 'wh3_cp1_cth_living_forge_tigers_3', itemType.building, 2, 'Progressive cth_bhashiva_forge', 'Cathay Bhashiva Building: Celestial Crucible'),

    74420: itemData(IC.useful, 1, 'wh3_cp1_cth_alchemist_tigers_1', itemType.building, 0, 'Progressive cth_bhashiva_alchemist', 'Cathay Bhashiva Building: Fuming Atelier'),
    74421: itemData(IC.useful, 1, 'wh3_cp1_cth_alchemist_tigers_2', itemType.building, 1, 'Progressive cth_bhashiva_alchemist', 'Cathay Bhashiva Building: Cloudwork Hall'),
    74422: itemData(IC.useful, 1, 'wh3_cp1_cth_alchemist_tigers_3', itemType.building, 2, 'Progressive cth_bhashiva_alchemist', 'Cathay Bhashiva Building: Smog-Bound Spire'),

    74423: itemData(IC.useful, 1, 'wh3_cp1_cth_defence_yang_tigers_1', itemType.building, 0, 'Progressive cth_bhashiva_defence_yang', 'Cathay Bhashiva Building: Ramparts'),
    74424: itemData(IC.useful, 1, 'wh3_cp1_cth_defence_yang_tigers_2', itemType.building, 1, 'Progressive cth_bhashiva_defence_yang', 'Cathay Bhashiva Building: Cannon Emplacements'),
    74425: itemData(IC.useful, 1, 'wh3_cp1_cth_defence_yang_tigers_3', itemType.building, 2, 'Progressive cth_bhashiva_defence_yang', 'Cathay Bhashiva Building: Artillery Batteries'),

    74426: itemData(IC.useful, 1, 'wh3_cp1_cth_defence_yin_tigers_1', itemType.building, 0, 'Progressive cth_bhashiva_defence_yin', 'Cathay Bhashiva Building: Archer Platforms'),
    74427: itemData(IC.useful, 1, 'wh3_cp1_cth_defence_yin_tigers_2', itemType.building, 1, 'Progressive cth_bhashiva_defence_yin', 'Cathay Bhashiva Building: Archer Towers'),
    74428: itemData(IC.useful, 1, 'wh3_cp1_cth_defence_yin_tigers_3', itemType.building, 2, 'Progressive cth_bhashiva_defence_yin', 'Cathay Bhashiva Building: Sky Lantern Roosts'),

    74429: itemData(IC.useful, 1, 'wh3_cp1_cth_foreign_slot_discovery_tigers_1', itemType.building, 0, 'Progressive cth_bhashiva_foreign_slot_discovery', 'Cathay Bhashiva Building: Sky Lantern Lookouts'),
    74430: itemData(IC.useful, 1, 'wh3_cp1_cth_foreign_slot_discovery_tigers_2', itemType.building, 1, 'Progressive cth_bhashiva_foreign_slot_discovery', 'Cathay Bhashiva Building: Sky Lantern Scouts'),
    74431: itemData(IC.useful, 1, 'wh3_cp1_cth_foreign_slot_discovery_tigers_3', itemType.building, 2, 'Progressive cth_bhashiva_foreign_slot_discovery', 'Cathay Bhashiva Building: Dragon Sentries'),

    74432: itemData(IC.useful, 1, 'wh3_cp1_cth_walls_minor_tigers_1', itemType.building, 0, 'Progressive cth_bhashiva_walls_minor', 'Cathay Bhashiva Building: Stockades'),
    74433: itemData(IC.useful, 1, 'wh3_cp1_cth_walls_minor_tigers_2', itemType.building, 1, 'Progressive cth_bhashiva_walls_minor', 'Cathay Bhashiva Building: Pagodan Walls'),

    74434: itemData(IC.useful, 1, 'wh3_cp1_cth_peasants_tigers_1', itemType.building, 0, 'Progressive cth_bhashiva_peasants', 'Cathay Bhashiva Building: Peasant Huts'),
    74435: itemData(IC.useful, 1, 'wh3_cp1_cth_peasants_tigers_2', itemType.building, 1, 'Progressive cth_bhashiva_peasants', 'Cathay Bhashiva Building: Peasant Stables'),

    74436: itemData(IC.useful, 1, 'wh3_cp1_cth_tiger_court_kamau_1', itemType.building, 0, 'Progressive cth_bhashiva_kamau', "Cathay Bhashiva Building: Kamau’s Pillar"),
    74437: itemData(IC.useful, 1, 'wh3_cp1_cth_tiger_court_kamau_yang_2', itemType.building, 1, 'Progressive cth_bhashiva_kamau', "Cathay Bhashiva Building: Hunter’s Pillar"),
    74438: itemData(IC.useful, 1, 'wh3_cp1_cth_tiger_court_kamau_yin_2', itemType.building, 1, 'Progressive cth_bhashiva_kamau', "Cathay Bhashiva Building: Leader’s Pillar"),
    74439: itemData(IC.useful, 1, 'wh3_cp1_cth_tiger_court_kamau_yang_3', itemType.building, 2, 'Progressive cth_bhashiva_kamau', "Cathay Bhashiva Building: Hunter’s Altar"),
    74440: itemData(IC.useful, 1, 'wh3_cp1_cth_tiger_court_kamau_yin_3', itemType.building, 2, 'Progressive cth_bhashiva_kamau', "Cathay Bhashiva Building: Leader’s Altar"),

    74441: itemData(IC.useful, 1, 'wh3_cp1_cth_tiger_court_white_tiger_1', itemType.building, 0, 'Progressive cth_bhashiva_white_tiger', "Cathay Bhashiva Building: White Tiger Pillar"),
    74442: itemData(IC.useful, 1, 'wh3_cp1_cth_tiger_court_white_tiger_yang_2', itemType.building, 1, 'Progressive cth_bhashiva_white_tiger', "Cathay Bhashiva Building: White Tiger Standard"),
    74443: itemData(IC.useful, 1, 'wh3_cp1_cth_tiger_court_white_tiger_yin_2', itemType.building, 1, 'Progressive cth_bhashiva_white_tiger', "Cathay Bhashiva Building: White Tiger Shrine"),
    74444: itemData(IC.useful, 1, 'wh3_cp1_cth_tiger_court_white_tiger_yang_3', itemType.building, 2, 'Progressive cth_bhashiva_white_tiger', "Cathay Bhashiva Building: White Tiger Warbanner"),
    74445: itemData(IC.useful, 1, 'wh3_cp1_cth_tiger_court_white_tiger_yin_3', itemType.building, 2, 'Progressive cth_bhashiva_white_tiger', "Cathay Bhashiva Building: White Tiger Omen"),

    74446: itemData(IC.useful, 1, 'wh3_cp1_cth_tiger_court_thousand_gods_1', itemType.building, 0, 'Progressive cth_bhashiva_indish', "Cathay Bhashiva Building: Indish Pillar"),
    74447: itemData(IC.useful, 1, 'wh3_cp1_cth_tiger_court_thousand_gods_yang_2', itemType.building, 1, 'Progressive cth_bhashiva_indish', "Cathay Bhashiva Building: Indish Shrine"),
    74448: itemData(IC.useful, 1, 'wh3_cp1_cth_tiger_court_thousand_gods_yin_2', itemType.building, 1, 'Progressive cth_bhashiva_indish', "Cathay Bhashiva Building: Fortune’s Offerings"),
    74449: itemData(IC.useful, 1, 'wh3_cp1_cth_tiger_court_thousand_gods_yang_3', itemType.building, 2, 'Progressive cth_bhashiva_indish', "Cathay Bhashiva Building: Indish Altar"),
    74450: itemData(IC.useful, 1, 'wh3_cp1_cth_tiger_court_thousand_gods_yin_3', itemType.building, 2, 'Progressive cth_bhashiva_indish', "Cathay Bhashiva Building: Wisdom’s Bounty"),
    
    74451: itemData(IC.useful, 1, 'wh3_main_cth_port_1', itemType.building, 0, 'Progressive cth_bhashiva_port', 'Cathay Bhashiva Building: Dock'),
    74452: itemData(IC.useful, 1, 'wh3_main_cth_port_2', itemType.building, 1, 'Progressive cth_bhashiva_port', 'Cathay Bhashiva Building: River Port'),
    74453: itemData(IC.useful, 1, 'wh3_main_cth_port_3', itemType.building, 2, 'Progressive cth_bhashiva_port', 'Cathay Bhashiva Building: Sea Port'),
    74454: itemData(IC.useful, 1, 'wh3_main_cth_resource_animals_1', itemType.building, 0, 'Progressive cth_bhashiva_resource_animals', 'Cathay Bhashiva Building: Exotic Animal Tamer'),
    74455: itemData(IC.useful, 1, 'wh3_main_cth_resource_animals_2', itemType.building, 1, 'Progressive cth_bhashiva_resource_animals', 'Cathay Bhashiva Building: Exotic Animal Pen'),
    74456: itemData(IC.useful, 1, 'wh3_main_cth_resource_animals_3', itemType.building, 2, 'Progressive cth_bhashiva_resource_animals', 'Cathay Bhashiva Building: Exotic Animal Market'),
    74457: itemData(IC.useful, 1, 'wh3_main_cth_resource_dyes_1', itemType.building, 0, 'Progressive cth_bhashiva_resource_dyes', 'Cathay Bhashiva Building: Cinnabar Mining Pit'),
    74458: itemData(IC.useful, 1, 'wh3_main_cth_resource_dyes_2', itemType.building, 1, 'Progressive cth_bhashiva_resource_dyes', 'Cathay Bhashiva Building: Cinnabar Mine'),
    74459: itemData(IC.useful, 1, 'wh3_main_cth_resource_dyes_3', itemType.building, 2, 'Progressive cth_bhashiva_resource_dyes', 'Cathay Bhashiva Building: Dyemaker'),
    74460: itemData(IC.useful, 1, 'wh3_main_cth_resource_furs_1', itemType.building, 0, 'Progressive cth_bhashiva_resource_furs', 'Cathay Bhashiva Building: Hunting Camp'),
    74461: itemData(IC.useful, 1, 'wh3_main_cth_resource_furs_2', itemType.building, 1, 'Progressive cth_bhashiva_resource_furs', 'Cathay Bhashiva Building: Hunting Lodge'),
    74462: itemData(IC.useful, 1, 'wh3_main_cth_resource_furs_3', itemType.building, 2, 'Progressive cth_bhashiva_resource_furs', 'Cathay Bhashiva Building: Tannery'),
    74463: itemData(IC.useful, 1, 'wh3_main_cth_resource_gems_1', itemType.building, 0, 'Progressive cth_bhashiva_resource_gems', 'Cathay Bhashiva Building: Gem Mineshaft'),
    74464: itemData(IC.useful, 1, 'wh3_main_cth_resource_gems_2', itemType.building, 1, 'Progressive cth_bhashiva_resource_gems', 'Cathay Bhashiva Building: Gem Mine'),
    74465: itemData(IC.useful, 1, 'wh3_main_cth_resource_gems_3', itemType.building, 2, 'Progressive cth_bhashiva_resource_gems', "Cathay Bhashiva Building: Gemcutter's Workshop"),
    74466: itemData(IC.useful, 1, 'wh3_main_cth_resource_gold_1', itemType.building, 0, 'Progressive cth_bhashiva_resource_gold', 'Cathay Bhashiva Building: Gold Mining Pit'),
    74467: itemData(IC.useful, 1, 'wh3_main_cth_resource_gold_2', itemType.building, 1, 'Progressive cth_bhashiva_resource_gold', 'Cathay Bhashiva Building: Gold Mine'),
    74468: itemData(IC.useful, 1, 'wh3_main_cth_resource_gold_3', itemType.building, 2, 'Progressive cth_bhashiva_resource_gold', 'Cathay Bhashiva Building: Gold Smelter'),
    74469: itemData(IC.useful, 1, 'wh3_main_cth_resource_iron_1', itemType.building, 0, 'Progressive cth_bhashiva_resource_iron', 'Cathay Bhashiva Building: Iron Mining Pit'),
    74470: itemData(IC.useful, 1, 'wh3_main_cth_resource_iron_2', itemType.building, 1, 'Progressive cth_bhashiva_resource_iron', 'Cathay Bhashiva Building: Iron Mines'),
    74471: itemData(IC.useful, 1, 'wh3_main_cth_resource_iron_3', itemType.building, 2, 'Progressive cth_bhashiva_resource_iron', 'Cathay Bhashiva Building: Iron Smelter'),
    74472: itemData(IC.useful, 1, 'wh3_main_cth_resource_ivory_1', itemType.building, 0, 'Progressive cth_bhashiva_resource_ivory', 'Cathay Bhashiva Building: Animal Store'),
    74473: itemData(IC.useful, 1, 'wh3_main_cth_resource_ivory_2', itemType.building, 1, 'Progressive cth_bhashiva_resource_ivory', 'Cathay Bhashiva Building: Tusk Market'),
    74474: itemData(IC.useful, 1, 'wh3_main_cth_resource_ivory_3', itemType.building, 2, 'Progressive cth_bhashiva_resource_ivory', 'Cathay Bhashiva Building: Tusk Compound'),
    74475: itemData(IC.useful, 1, 'wh3_main_cth_resource_marble_1', itemType.building, 0, 'Progressive cth_bhashiva_resource_marble', 'Cathay Bhashiva Building: Sawyer'),
    74476: itemData(IC.useful, 1, 'wh3_main_cth_resource_marble_2', itemType.building, 1, 'Progressive cth_bhashiva_resource_marble', 'Cathay Bhashiva Building: Marble Quarry'),
    74477: itemData(IC.useful, 1, 'wh3_main_cth_resource_marble_3', itemType.building, 2, 'Progressive cth_bhashiva_resource_marble', "Cathay Bhashiva Building: Stone Mason's Workshop"),
    74478: itemData(IC.useful, 1, 'wh3_main_cth_resource_medicine_1', itemType.building, 0, 'Progressive cth_bhashiva_resource_medicine', "Cathay Bhashiva Building: Herb Gatherer's Camp"),
    74479: itemData(IC.useful, 1, 'wh3_main_cth_resource_medicine_2', itemType.building, 1, 'Progressive cth_bhashiva_resource_medicine', 'Cathay Bhashiva Building: Exotic Hothouse'),
    74480: itemData(IC.useful, 1, 'wh3_main_cth_resource_medicine_3', itemType.building, 2, 'Progressive cth_bhashiva_resource_medicine', 'Cathay Bhashiva Building: Alchemy Workshop'),
    74481: itemData(IC.useful, 1, 'wh3_main_cth_resource_obsidian_1', itemType.building, 0, 'Progressive cth_bhashiva_resource_obsidian', 'Cathay Bhashiva Building: Obsidian Quarry'),
    74582: itemData(IC.useful, 1, 'wh3_main_cth_resource_obsidian_2', itemType.building, 1, 'Progressive cth_bhashiva_resource_obsidian', 'Cathay Bhashiva Building: Obsidian Trinket Maker'),
    74583: itemData(IC.useful, 1, 'wh3_main_cth_resource_obsidian_3', itemType.building, 2, 'Progressive cth_bhashiva_resource_obsidian', 'Cathay Bhashiva Building: Obsidian Amulet Carver'),
    74584: itemData(IC.useful, 1, 'wh3_main_cth_resource_pasture_1', itemType.building, 0, 'Progressive cth_bhashiva_resource_pasture', 'Cathay Bhashiva Building: Grazing Pastures'),
    74585: itemData(IC.useful, 1, 'wh3_main_cth_resource_pasture_2', itemType.building, 1, 'Progressive cth_bhashiva_resource_pasture', 'Cathay Bhashiva Building: Livestock Pens'),
    74586: itemData(IC.useful, 1, 'wh3_main_cth_resource_pasture_3', itemType.building, 2, 'Progressive cth_bhashiva_resource_pasture', 'Cathay Bhashiva Building: Cattle Ranch'),
    74587: itemData(IC.useful, 1, 'wh3_main_cth_resource_pottery_1', itemType.building, 0, 'Progressive cth_bhashiva_resource_pottery', 'Cathay Bhashiva Building: Clay Pit'),
    74588: itemData(IC.useful, 1, 'wh3_main_cth_resource_pottery_2', itemType.building, 1, 'Progressive cth_bhashiva_resource_pottery', 'Cathay Bhashiva Building: Pottery Maker'),
    74589: itemData(IC.useful, 1, 'wh3_main_cth_resource_pottery_3', itemType.building, 2, 'Progressive cth_bhashiva_resource_pottery', 'Cathay Bhashiva Building: Kilns'),
    74590: itemData(IC.useful, 1, 'wh3_main_cth_resource_salt_1', itemType.building, 0, 'Progressive cth_bhashiva_resource_salt', 'Cathay Bhashiva Building: Brine Mining Pans'),
    74591: itemData(IC.useful, 1, 'wh3_main_cth_resource_salt_2', itemType.building, 1, 'Progressive cth_bhashiva_resource_salt', 'Cathay Bhashiva Building: Brine Mining Basin'),
    74592: itemData(IC.useful, 1, 'wh3_main_cth_resource_salt_3', itemType.building, 2, 'Progressive cth_bhashiva_resource_salt', 'Cathay Bhashiva Building: Saltworks'),
    74593: itemData(IC.useful, 1, 'wh3_main_cth_resource_spices_1', itemType.building, 0, 'Progressive cth_bhashiva_resource_spices', 'Cathay Bhashiva Building: Spice Market'),
    74594: itemData(IC.useful, 1, 'wh3_main_cth_resource_spices_2', itemType.building, 1, 'Progressive cth_bhashiva_resource_spices', 'Cathay Bhashiva Building: Spice Trading Post'),
    74595: itemData(IC.useful, 1, 'wh3_main_cth_resource_spices_3', itemType.building, 2, 'Progressive cth_bhashiva_resource_spices', 'Cathay Bhashiva Building: Eastern Bazaar'),
    74596: itemData(IC.useful, 1, 'wh3_main_cth_resource_wine_1', itemType.building, 0, 'Progressive cth_bhashiva_resource_wine', 'Cathay Bhashiva Building: Orchards'),
    74597: itemData(IC.useful, 1, 'wh3_main_cth_resource_wine_2', itemType.building, 1, 'Progressive cth_bhashiva_resource_wine', 'Cathay Bhashiva Building: Vineyard'),
    74598: itemData(IC.useful, 1, 'wh3_main_cth_resource_wine_3', itemType.building, 2, 'Progressive cth_bhashiva_resource_wine', 'Cathay Bhashiva Building: Vintner'),
    74599: itemData(IC.useful, 1, 'wh3_main_cth_resource_wood_1', itemType.building, 0, 'Progressive cth_bhashiva_resource_wood', "Cathay Bhashiva Building: Woodman's Hut"),
    74600: itemData(IC.useful, 1, 'wh3_main_cth_resource_wood_2', itemType.building, 1, 'Progressive cth_bhashiva_resource_wood', 'Cathay Bhashiva Building: Timber Mill'),
    74601: itemData(IC.useful, 1, 'wh3_main_cth_resource_wood_3', itemType.building, 2, 'Progressive cth_bhashiva_resource_wood', 'Cathay Bhashiva Building: Lumberyard'),
}

techs: dict[int, itemData] = cathay.techs
techs.update({
    74800: itemData(IC.useful, 1, 'wh3_cp1_tech_cth_59_bhashiva', itemType.tech, 5, 'Progressive tech_cth_provinces', "Cathay Tech: Clawspeaker's Meditation"),
    74801: itemData(IC.useful, 1, 'wh3_cp1_tech_cth_19_bhashiva', itemType.tech, 4, 'Progressive tech_cth_provinces', 'Cathay Tech: Harmonic Discipline (Bhashiva)'),
    74802: itemData(IC.useful, 1, 'wh3_main_tech_cth_71', itemType.tech, 6, 'Progressive tech_cth_provinces', "Cathay Tech: Honed Senses"),
    74803: itemData(IC.useful, 1, 'wh3_main_tech_cth_72', itemType.tech, 6, 'Progressive tech_cth_provinces', "Cathay Tech: Tiger's Call")
})

progUnits: dict[int, itemData] = {
    75200: itemData(IC.useful, 4, "Progressive cth_bhashiva_inf", itemType.unit, 4, "", "Progressive Cathay Bhashiva Unit: Infantry"),
    75201: itemData(IC.useful, 4, "Progressive cth_bhashiva_rng", itemType.unit, 4, "", "Progressive Cathay Bhashiva Unit: Ranged"),
    75202: itemData(IC.useful, 3, "Progressive cth_bhashiva_cav", itemType.unit, 3, "", "Progressive Cathay Bhashiva Unit: Cavalry"),
    75203: itemData(IC.useful, 1, "Progressive cth_bhashiva_art", itemType.unit, 1, "", "Progressive Cathay Bhashiva Unit: Artillery"),
    75204: itemData(IC.useful, 2, "Progressive cth_bhashiva_veh", itemType.unit, 2, "", "Progressive Cathay Bhashiva Unit: War Machine"),
    75205: itemData(IC.useful, 3, "Progressive cth_bhashiva_bst", itemType.unit, 3, "", "Progressive Cathay Bhashiva Unit: Beast"),
    75206: itemData(IC.useful, 1, "Progressive cth_bhashiva_hro", itemType.unit, 1, "", "Progressive Cathay Bhashiva Unit: Hero")
}

progBuildings: dict[int, itemData] = {
    75300: itemData(IC.useful, 5, 'Progressive cth_bhashiva_settlement_major', itemType.building, 5, None, 'Progressive Cathay Bhashiva Building: Settlement Major'),
    75301: itemData(IC.useful, 3, 'Progressive cth_bhashiva_settlement_minor', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: Settlement Minor'),

    75302: itemData(IC.useful, 3, 'Progressive cth_bhashiva_tigers', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: Tiger Den'),
    75303: itemData(IC.useful, 3, 'Progressive cth_bhashiva_armoury', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: Jade Armoury'),
    75304: itemData(IC.useful, 3, 'Progressive cth_bhashiva_gunpowder', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: Gunpowder Wuku'),
    75305: itemData(IC.useful, 3, 'Progressive cth_bhashiva_forge', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: Celestial Forge'),
    75306: itemData(IC.useful, 3, 'Progressive cth_bhashiva_alchemist', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: Alchemist Foundry'),

    75307: itemData(IC.useful, 3, 'Progressive cth_bhashiva_defence_yang', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: '),
    75308: itemData(IC.useful, 3, 'Progressive cth_bhashiva_defence_yin', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: '),
    75309: itemData(IC.useful, 3, 'Progressive cth_bhashiva_foreign_slot_discovery', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: Foreign Slot Discovery'),
    75310: itemData(IC.useful, 2, 'Progressive cth_bhashiva_walls_minor', itemType.building, 2, None, 'Progressive Cathay Bhashiva Building: Garrison'),
    75311: itemData(IC.useful, 2, 'Progressive cth_bhashiva_peasants', itemType.building, 2, None, 'Progressive Cathay Bhashiva Building: Villagers'),

    75312: itemData(IC.useful, 3, 'Progressive cth_bhashiva_kamau', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: Teachings of Kamau'),
    75313: itemData(IC.useful, 3, 'Progressive cth_bhashiva_white_tiger', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: Prophecy of the White Tiger'),
    75314: itemData(IC.useful, 3, 'Progressive cth_bhashiva_indish', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: Way of the Thousand Gods'),

    75315: itemData(IC.useful, 3, 'Progressive cth_bhashiva_port', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: Port'),
    75316: itemData(IC.useful, 3, 'Progressive cth_bhashiva_resource_animals', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: Animals'),
    75317: itemData(IC.useful, 3, 'Progressive cth_bhashiva_resource_dyes', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: Dyes'),
    75318: itemData(IC.useful, 3, 'Progressive cth_bhashiva_resource_furs', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: Furs'),
    75319: itemData(IC.useful, 3, 'Progressive cth_bhashiva_resource_gems', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: Gems'),
    75320: itemData(IC.useful, 3, 'Progressive cth_bhashiva_resource_gold', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: Gold'),
    75321: itemData(IC.useful, 3, 'Progressive cth_bhashiva_resource_iron', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: Iron'),
    75322: itemData(IC.useful, 3, 'Progressive cth_bhashiva_resource_ivory', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: Ivory'),
    75323: itemData(IC.useful, 3, 'Progressive cth_bhashiva_resource_marble', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: Marble'),
    75324: itemData(IC.useful, 3, 'Progressive cth_bhashiva_resource_medicine', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: Medicine'),
    75325: itemData(IC.useful, 3, 'Progressive cth_bhashiva_resource_obsidian', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: Obsidian'),
    75326: itemData(IC.useful, 3, 'Progressive cth_bhashiva_resource_pasture', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: Pasture'),
    75327: itemData(IC.useful, 3, 'Progressive cth_bhashiva_resource_pottery', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: Pottery'),
    75328: itemData(IC.useful, 3, 'Progressive cth_bhashiva_resource_salt', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: Salt'),
    75329: itemData(IC.useful, 3, 'Progressive cth_bhashiva_resource_spices', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: Spices'),
    75330: itemData(IC.useful, 3, 'Progressive cth_bhashiva_resource_wine', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: Wine'),
    75331: itemData(IC.useful, 3, 'Progressive cth_bhashiva_resource_wood', itemType.building, 3, None, 'Progressive Cathay Bhashiva Building: Wood'),
}

progTechs: dict[int, itemData] = cathay.progTechs

special: dict[int, specialItemData]  = {}

rituals: dict[int, specialItemData] = {}