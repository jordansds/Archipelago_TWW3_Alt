from BaseClasses import ItemClassification as IC
from worlds.tww3.item_types import ItemType, modItemData
# @formatter:off

units: dict[int, modItemData] = {
    100000: modItemData(IC.useful, 1, 'beastmen', '', 'dec_bestigor_dual_axe', ItemType.unit, 3, 'Progressive bst_inf', 'Bst Unit: Bestigor Herd (Dual Axes)'),
    100001: modItemData(IC.useful, 1, 'beastmen', '', 'dec_gor_great_axe', ItemType.unit, 2, 'Progressive bst_inf', 'Bst Unit: Gor Herd (Great Weapons)'),
    100002: modItemData(IC.useful, 1, 'beastmen', '', 'dec_gouge_horns', ItemType.unit, 3, 'Progressive bst_inf', 'Bst Unit: Gouge-horns'),

    100003: modItemData(IC.useful, 1, 'chaosDwarfs', '', 'deco_chd_acolytes', ItemType.unit, 4, 'Progressive chd_inf', 'Chd Unit: Acolytes of Hashut'),
    100004: modItemData(IC.useful, 1, 'chaosDwarfs', '', 'deco_chd_zealots', ItemType.unit, 3, 'Progressive chd_inf', 'Chd Unit: Zealot Berzerkers'),
    100005: modItemData(IC.useful, 1, 'chaosDwarfs', '', 'deco_chd_ogre_slaves', ItemType.unit, 2, 'Progressive chd_inf', 'Chd Unit: Ogre Labourers'),
    100006: modItemData(IC.useful, 1, 'chaosDwarfs', '', 'deco_chd_naphtha', ItemType.unit, 3, 'Progressive chd_inf', 'Chd Unit: Infernal Guard (Naphtha Bombs)'),
    100007: modItemData(IC.useful, 1, 'chaosDwarfs', '', 'deco_chd_lava_trolls', ItemType.unit, 2, 'Progressive chd_inf', 'Chd Unit: Lava Trolls'),
    100008: modItemData(IC.useful, 1, 'chaosDwarfs', '', 'deco_chd_ravagers', ItemType.unit, 1, 'Progressive chd_cav', 'Chd Unit: Hobhound Ravagers'),
    100009: modItemData(IC.useful, 1, 'chaosDwarfs', '', 'deco_chd_quarrellers', ItemType.unit, 2, 'Progressive chd_rng', 'Chd Unit: Chaos Dwarf Quarrellers'),
    100010: modItemData(IC.useful, 1, 'chaosDwarfs', '', 'deco_chd_annihilators', ItemType.unit, 3, 'Progressive chd_rng', 'Chd Unit: Annihilators'),
    100011: modItemData(IC.useful, 1, 'chaosDwarfs', '', 'deco_chd_siege_giant', ItemType.unit, 3, 'Progressive chd_bst', 'Chd Unit: Siege Giant'),
    100012: modItemData(IC.useful, 1, 'chaosDwarfs', '', 'deco_chd_gnoblar_slaves', ItemType.unit, 2, 'Progressive chd_rng', 'Chd Unit: Gnoblar Labourers'),

    100013: modItemData(IC.useful, 1, 'darkElves', '', 'land_units_onscreen_name_dec_magma_dragon', ItemType.unit, 3, 'Progressive def_bst', 'Def Unit: Magma Dragon'),
    100014: modItemData(IC.useful, 1, 'darkElves', '', 'land_units_onscreen_name_dec_tower_masters', ItemType.unit, 4, 'Progressive def_inf', 'Def Unit: Tower Masters'),
    100015: modItemData(IC.useful, 1, 'darkElves', '', 'land_units_onscreen_name_dec_lords_oblivion', ItemType.unit, 4, 'Progressive def_cav', 'Def Unit: Lords of Oblivion'),
    100016: modItemData(IC.useful, 1, 'darkElves', '', 'land_units_onscreen_name_dec_hunters_anath_raema', ItemType.unit, 2, 'Progressive def_rng', 'Def Unit: Hunters of Anath Raema'),

    100017: modItemData(IC.useful, 1, 'dwarfs', '', 'land_units_onscreen_name_deco_bugman_thrower', ItemType.unit, 2, 'Progressive dwf_art', "Dwf Unit: Bugman's Thrower"),
    100018: modItemData(IC.useful, 1, 'dwarfs', '', 'land_units_onscreen_name_deco_irondrakes_drakefire', ItemType.unit, 1, 'Progressive dwf_rng', 'Dwf Unit: Irondrakes (Drakefire Pistols)'),
    100019: modItemData(IC.useful, 1, 'dwarfs', '', 'land_units_onscreen_name_deco_hammerers_dual', ItemType.unit, 3, 'Progressive dwf_inf', 'Dwf Unit: Hammerers (Dual Weapons)'),
    100020: modItemData(IC.useful, 1, 'dwarfs', '', 'land_units_onscreen_name_deco_old_guard', ItemType.unit, 3, 'Progressive dwf_inf', 'Dwf Unit: Old Guard'),
    100021: modItemData(IC.useful, 1, 'dwarfs', '', 'land_units_onscreen_name_deco_prospectors', ItemType.unit, 2, 'Progressive dwf_inf', 'Dwf Unit: Prospectors'),

    100022: modItemData(IC.useful, 1, 'empire', '', 'deco_shielded_halberdiers', ItemType.unit, 3, 'Progressive emp_inf', 'Emp Unit: Halberdiers (Shields)'),
    100023: modItemData(IC.useful, 1, 'empire', '', 'deco_roadwardens', ItemType.unit, 2, 'Progressive emp_cav', 'Emp Unit: Roadwardens'),
    100024: modItemData(IC.useful, 1, 'empire', '', 'deco_knights_lynx', ItemType.unit, 3, 'Progressive emp_cav', 'Emp Unit: Knights of the Black Lynx'),
    100025: modItemData(IC.useful, 1, 'empire', '', 'deco_ironsides', ItemType.unit, 3, 'Progressive emp_rng', 'Emp Unit: Nuln Ironsides (Repeater Rifles)'),
    100026: modItemData(IC.useful, 1, 'empire', '', 'deco_doom_prophets', ItemType.unit, 2, 'Progressive emp_inf', 'Emp Unit: Prophets of Doom'),

    100027: modItemData(IC.useful, 1, 'greenskins', '', 'deco_forest_goblin_archers', ItemType.unit, 2, 'Progressive grn_rng', 'Grn Unit: Forest Goblins (Bows)'),
    100028: modItemData(IC.useful, 1, 'greenskins', '', 'deco_night_goblin_spears', ItemType.unit, 3, 'Progressive grn_inf', 'Grn Unit: Night Goblins (Spears)'),
    100029: modItemData(IC.useful, 1, 'greenskins', '', 'deco_forest_goblin_swords', ItemType.unit, 2, 'Progressive grn_inf', 'Grn Unit: Forest Goblins'),
    100030: modItemData(IC.useful, 1, 'greenskins', '', 'deco_forest_goblin_spears', ItemType.unit, 2, 'Progressive grn_inf', 'Grn Unit: Forest Goblins (Spears)'),
    100031: modItemData(IC.useful, 1, 'greenskins', '', 'deco_snotlings', ItemType.unit, 1, 'Progressive grn_inf', 'Grn Unit: Snotlings'),
    100032: modItemData(IC.useful, 1, 'greenskins', '', 'deco_hill_goblins', ItemType.unit, 3, 'Progressive grn_inf', 'Grn Unit: Hill Goblins'),
    100033: modItemData(IC.useful, 1, 'greenskins', '', 'deco_armored_colossal_squig', ItemType.unit, 4, 'Progressive grn_inf', 'Grn Unit: Armored Colossal Squig'),
    100034: modItemData(IC.useful, 1, 'greenskins', '', 'str_urgat_wolf_chariot', ItemType.unit, 3, 'Progressive grn_veh', 'Grn Unit: Goblin Triple Wolf Chariots'),
    100035: modItemData(IC.useful, 1, 'greenskins', '', 'grn_poop', ItemType.unit, 2, 'Progressive grn_cav', 'Grn Unit: Snotroom Riders'),
    100036: modItemData(IC.useful, 1, 'greenskins', '', 'deco_savage_orc_spears', ItemType.unit, 1, 'Progressive grn_inf', 'Grn Unit: Savage Orcs (Spears)'),
    100037: modItemData(IC.useful, 1, 'greenskins', '', 'deco_savage_big_uns_gw', ItemType.unit, 3, 'Progressive grn_inf', "Grn Unit: Savage Orc Big 'Uns (Great Weapons)"),
    100038: modItemData(IC.useful, 1, 'greenskins', '', 'deco_black_orc_dual', ItemType.unit, 3, 'Progressive grn_inf', 'Grn Unit: Black Orcs (Dual Weapons)'),
    100039: modItemData(IC.useful, 1, 'greenskins', '', 'deco_savage_giant', ItemType.unit, 3, 'Progressive grn_bst', 'Grn Unit: Savage Giant'),
    100040: modItemData(IC.useful, 1, 'greenskins', '', 'deco_big_uns_shields', ItemType.unit, 2, 'Progressive grn_inf', "Grn Unit: Orc Big 'Uns (Shields)"),

    100041: modItemData(IC.useful, 1, 'highElves', '', 'deco_griffon_knights', ItemType.unit, 3, 'Progressive hef_cav', 'Hef Unit: Griffon Knights'),
    100042: modItemData(IC.useful, 1, 'highElves', '', 'deco_high_helms', ItemType.unit, 2, 'Progressive hef_cav', 'Hef Unit: High Helms'),
    100043: modItemData(IC.useful, 1, 'highElves', '', 'deco_bladelords', ItemType.unit, 4, 'Progressive hef_inf', 'Hef Unit: Bladelords'),
    100044: modItemData(IC.useful, 1, 'highElves', '', 'deco_skywardens', ItemType.unit, 2, 'Progressive hef_cav', 'Hef Unit: Skywardens of Yvresse'),
    100045: modItemData(IC.useful, 1, 'highElves', '', 'deco_avelorn_maidens', ItemType.unit, 2, 'Progressive hef_inf', 'Hef Unit: Maidens of Avelorn'),

    100046: modItemData(IC.useful, 1, 'norsca', '', 'deco_nor_pit', ItemType.unit, 1, 'Progressive nor_inf', 'Nor Unit: Pit Fighters'),
    100047: modItemData(IC.useful, 1, 'norsca', '', 'deco_nor_reavers', ItemType.unit, 2, 'Progressive nor_inf', 'Nor Unit: Reavers'),
    100048: modItemData(IC.useful, 1, 'norsca', '', 'deco_nor_huskarls', ItemType.unit, 4, 'Progressive nor_inf', 'Nor Unit: Huskarls'),
    100049: modItemData(IC.useful, 1, 'norsca', '', 'deco_nor_bondsmen', ItemType.unit, 1, 'Progressive nor_rng', 'Nor Unit: Bondsmen'),
    100050: modItemData(IC.useful, 1, 'norsca', '', 'deco_nor_maidens', ItemType.unit, 2, 'Progressive nor_inf', 'Nor Unit: Shield Maidens'),
    100051: modItemData(IC.useful, 1, 'norsca', '', 'deco_nor_hydra', ItemType.unit, 5, 'Progressive nor_bst', 'Nor Unit: Frost Hydra'),
    100052: modItemData(IC.useful, 1, 'norsca', '', 'deco_nor_wolf', ItemType.unit, 2, 'Progressive nor_bst', "Nor Unit: Mortkin's Fang (Norscan Ice Wolf)"),
    100053: modItemData(IC.useful, 1, 'norsca', '', 'deco_nor_valkyrie', ItemType.unit, 4, 'Progressive nor_bst', 'Nor Unit: Valkyrie'),

    100054: modItemData(IC.useful, 1, 'ogreKingdoms', '', 'dec_ogre_bulls_gw', ItemType.unit, 2, 'Progressive ogr_inf', 'Ogr Unit: Ogre Bulls (Great Weapons) '),
    100055: modItemData(IC.useful, 1, 'ogreKingdoms', '', 'dec_giantbreakers', ItemType.unit, 4, 'Progressive ogr_inf', 'Ogr Unit: Giantbreakers'),
    100056: modItemData(IC.useful, 1, 'ogreKingdoms', '', 'dec_rhinox_bull', ItemType.unit, 2, 'Progressive ogr_bst', 'Ogr Unit: Rhinox Bull'),

    100057: modItemData(IC.useful, 1, 'vampireCounts', '', 'dec_spirit_host', ItemType.unit, 2, 'Progressive vmp_inf', 'Vmp Unit: Spirit Hosts'),
    100058: modItemData(IC.useful, 1, 'vampireCounts', '', 'dec_reapers', ItemType.unit, 1, 'Progressive vmp_inf', 'Vmp Unit: Skeleton Reapers'),
    100059: modItemData(IC.useful, 1, 'vampireCounts', '', 'dec_lahmian', ItemType.unit, 2, 'Progressive vmp_inf', 'Vmp Unit: Lahmian Handmaidens'),
    100060: modItemData(IC.useful, 1, 'vampireCounts', '', 'dec_hell_knights', ItemType.unit, 2, 'Progressive vmp_cav', 'Vmp Unit: Hell Knights'),
    100061: modItemData(IC.useful, 1, 'vampireCounts', '', 'dec_kastellans', ItemType.unit, 3, 'Progressive vmp_cav', 'Vmp Unit: Blood Knight Kastellans'),

    100062: modItemData(IC.useful, 1, 'woodElves', '', 'deco_meadow_chariots', ItemType.unit, 2, 'Progressive wef_cav', 'Wef Unit: Meadow Chariots'),
    100063: modItemData(IC.useful, 1, 'woodElves', '', 'deco_glade_knights', ItemType.unit, 3, 'Progressive wef_cav', 'Wef Unit: Glade Knights'),
    100064: modItemData(IC.useful, 1, 'woodElves', '', 'deco_wind_riders', ItemType.unit, 2, 'Progressive wef_cav', 'Wef Unit: Wind Hunters'),
    100065: modItemData(IC.useful, 1, 'woodElves', '', 'deco_handmaidens_torothal', ItemType.unit, 2, 'Progressive wef_inf', 'Wef Unit: Handmaidens of Torothal'),
    100066: modItemData(IC.useful, 1, 'woodElves', '', 'deco_wildwood_wardens', ItemType.unit, 3, 'Progressive wef_inf', 'Wef Unit: Wildwood Wardens'),
    100067: modItemData(IC.useful, 1, 'woodElves', 'wh2_dlc16_wef_drycha', 'deco_dryads_willow_malicious', ItemType.unit, 3, 'Progressive wef_inf', 'Wef Unit: Malevolent Dryads (Willow Aspect)'),
    100068: modItemData(IC.useful, 1, 'woodElves', 'wh_dlc05_wef_wood_elves', 'deco_dryads_willow', ItemType.unit, 3, 'Progressive wef_inf', 'Wef Unit: Dryads (Willow Aspect)'),
    100069: modItemData(IC.useful, 1, 'woodElves', 'wh_dlc05_wef_argwylon', 'deco_dryads_willow', ItemType.unit, 3, 'Progressive wef_inf', 'Wef Unit: Dryads (Willow Aspect)'),
    100070: modItemData(IC.useful, 1, 'woodElves', 'wh2_dlc16_wef_sisters_of_twilight', 'deco_dryads_willow', ItemType.unit, 3, 'Progressive wef_inf', 'Wef Unit: Dryads (Willow Aspect)'),
}

dicts = [units]