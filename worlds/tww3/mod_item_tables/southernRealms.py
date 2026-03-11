from BaseClasses import ItemClassification as IC
from worlds.tww3.itemTypes import itemType, itemData, specialItemData

# @formatter:off

units: dict[int, itemData] = {
    110000: itemData(IC.useful, 1, "teb_militia_spearmen", itemType.unit, 1, "Progressive teb_inf", "SouthernRealms Unit: Milita Spearmen"),
    110001: itemData(IC.useful, 1, "teb_half_pikes", itemType.unit, 2, "Progressive teb_inf", "SouthernRealms Unit: Half Pikes"),
    110002: itemData(IC.useful, 1, "teb_billmen", itemType.unit, 2, "Progressive teb_inf", "SouthernRealms Unit: Billmen"),
    110003: itemData(IC.useful, 1, "teb_duellists", itemType.unit, 3, "Progressive teb_inf", "SouthernRealms Unit: Duellists"),

    110004: itemData(IC.useful, 1, "teb_xbowmen", itemType.unit, 1, "Progressive teb_rng", "SouthernRealms Unit: Crossbowmen"),
    110005: itemData(IC.useful, 1, "teb_handgunners", itemType.unit, 2, "Progressive teb_rng", "SouthernRealms Unit: Handgunners"),

    110006: itemData(IC.useful, 1, "teb_xbow_cav", itemType.unit, 3, "Progressive teb_cav", "SouthernRealms Unit: Cranequiniers"),

    110007: itemData(IC.useful, 1, "teb_light_cannon", itemType.unit, 1, "Progressive teb_art", "SouthernRealms Unit: Light Cannons"),
    110008: itemData(IC.useful, 1, "wh_main_emp_art_mortar", itemType.unit, 1, "Progressive teb_art", "SouthernRealms Unit: Mortars"),

    110009: itemData(IC.useful, 1, "teb_paymaster", itemType.unit, 1, "Progressive teb_veh", "SouthernRealms Unit: Paymaster Wagon"),
    110010: itemData(IC.useful, 1, "teb_tank", itemType.unit, 2, "Progressive teb_veh", "SouthernRealms Unit: Tortoise Tank"),

    110011: itemData(IC.useful, 1, "teb_golden_lion", itemType.unit, 2, "Progressive teb_bst", "SouthernRealms Unit: Golden Lion"),

    110012: itemData(IC.useful, 1, "teb_merc_captain", itemType.unit, 1, "Progressive teb_hro", "SouthernRealms Unit: Mercenary Captain"),
    110013: itemData(IC.useful, 1, "teb_duellist_hero", itemType.unit, 1, "Progressive teb_hro", "SouthernRealms Unit: Master Duellist"),
    110014: itemData(IC.useful, 1, "teb_priestess", itemType.unit, 1, "Progressive teb_hro", "SouthernRealms Unit: Priestess of Myrmidia"),

    110015: itemData(IC.useful, 1, 'wh3_main_ogr_inf_maneaters_1', itemType.unit, 4, 'Progressive teb_inf', 'SouthernRealms Unit: Maneaters (Ironfists)'),
    110016: itemData(IC.useful, 1, 'wh3_main_ogr_inf_maneaters_3', itemType.unit, 3, 'Progressive teb_rng', 'SouthernRealms Unit: Maneaters (Ogre Pistols)'),

    110017: itemData(IC.useful, 1, 'wh_main_grn_mon_giant', itemType.unit, 2, 'Progressive teb_bst', 'SouthernRealms Unit: Giant'),
    110018: itemData(IC.useful, 1, 'wh3_dlc23_chd_cav_hobgoblin_wolf_raiders_bows', itemType.unit, 3, 'Progressive teb_cav', 'SouthernRealms Unit: Hobgoblin Wolf Raiders (Bows)'),
    110019: itemData(IC.useful, 1, 'wh3_dlc25_dwf_inf_slayer_pirates', itemType.unit, 3, 'Progressive teb_inf', 'SouthernRealms Unit: Slayer Pirates'),
    110020: itemData(IC.useful, 1, 'wh3_main_ksl_cav_gryphon_legion_0', itemType.unit, 4, 'Progressive teb_cav', 'SouthernRealms Unit: Gryphon Legion'),
}

buildings: dict[int, itemData] = {
    110400: itemData(IC.useful, 1, "wh_main_teb_port_1", itemType.building, 0, "Progressive teb_port", "SouthernRealms Building: Mercantile Docks"),
    110401: itemData(IC.useful, 1, "wh_main_teb_port_2", itemType.building, 1, "Progressive teb_port", "SouthernRealms Building: Mercantile Harbour"),
    110402: itemData(IC.useful, 1, "wh_main_teb_port_3", itemType.building, 2, "Progressive teb_port", "SouthernRealms Building: Mercantile Port"),

    110403: itemData(IC.useful, 1, "teb_mil_city_1", itemType.building, 0, "Progressive teb_barracks", "SouthernRealms Building: Militia Posts"),
    110404: itemData(IC.useful, 1, "teb_mil_city_2", itemType.building, 1, "Progressive teb_barracks", "SouthernRealms Building: Training Fields"),
    110405: itemData(IC.useful, 1, "teb_mil_city_3", itemType.building, 2, "Progressive teb_barracks", "SouthernRealms Building: City Barracks"),

    110406: itemData(IC.useful, 1, "teb_mil_mercs_1", itemType.building, 0, "Progressive teb_mercs", "SouthernRealms Building: Company Posts"),
    110407: itemData(IC.useful, 1, "teb_mil_mercs_2", itemType.building, 1, "Progressive teb_mercs", "SouthernRealms Building: Mercenary Hub"),
    110408: itemData(IC.useful, 1, "teb_mil_mercs_3", itemType.building, 2, "Progressive teb_mercs", "SouthernRealms Building: Retinue Hall"),

    110409: itemData(IC.useful, 1, "teb_mil_cannons_1", itemType.building, 0, "Progressive teb_artillery", "SouthernRealms Building: Artillery Foundry"),
    110410: itemData(IC.useful, 1, "teb_mil_cannons_2", itemType.building, 1, "Progressive teb_artillery", "SouthernRealms Building: Siege Workshop"),

    110411: itemData(IC.useful, 1, "teb_smith_1", itemType.building, 0, "Progressive teb_smith", "SouthernRealms Building: Smithies"),
    110412: itemData(IC.useful, 1, "teb_smith_2", itemType.building, 1, "Progressive teb_smith", "SouthernRealms Building: Arms Market"),

    110413: itemData(IC.useful, 1, "teb_worship_myrmidia_1", itemType.building, 0, "Progressive teb_worship_myrmidia", "SouthernRealms Building: Myrmidian Figurine"),
    110414: itemData(IC.useful, 1, "teb_worship_myrmidia_2", itemType.building, 1, "Progressive teb_worship_myrmidia", "SouthernRealms Building: Myrmidian Alcove"),
    110415: itemData(IC.useful, 1, "teb_worship_myrmidia_3", itemType.building, 2, "Progressive teb_worship_myrmidia", "SouthernRealms Building: Myrmidian Temple"),
    110416: itemData(IC.useful, 1, "teb_worship_myrmidia_4", itemType.building, 3, "Progressive teb_worship_myrmidia", "SouthernRealms Building: Myrmidian Academy"),
    110417: itemData(IC.useful, 1, "teb_worship_myrmidia_5", itemType.building, 4, "Progressive teb_worship_myrmidia", "SouthernRealms Building: Myrmidian Fortress"),

    110418: itemData(IC.useful, 1, "teb_worship_shallya_1", itemType.building, 0, "Progressive teb_worship_shallya", "SouthernRealms Building: Shallyan Figurine"),
    110419: itemData(IC.useful, 1, "teb_worship_shallya_2", itemType.building, 1, "Progressive teb_worship_shallya", "SouthernRealms Building: Shallyan Alcove"),
    110420: itemData(IC.useful, 1, "teb_worship_shallya_3", itemType.building, 2, "Progressive teb_worship_shallya", "SouthernRealms Building: Shallyan Temple"),
    110421: itemData(IC.useful, 1, "teb_worship_shallya_4", itemType.building, 3, "Progressive teb_worship_shallya", "SouthernRealms Building: Shallyan Hospital"),
    110422: itemData(IC.useful, 1, "teb_worship_shallya_5", itemType.building, 4, "Progressive teb_worship_shallya", "SouthernRealms Building: Shallyan Abbey"),

    110423: itemData(IC.useful, 1, "teb_mil_badmercs_1", itemType.building, 0, "Progressive teb_badmercs", "SouthernRealms Building: Mercenary Haven"),
    110424: itemData(IC.useful, 1, "teb_mil_badmercs_2", itemType.building, 1, "Progressive teb_badmercs", "SouthernRealms Building: Scum and Villainy"),
    110425: itemData(IC.useful, 1, "teb_mil_badmercs_3", itemType.building, 2, "Progressive teb_badmercs", "SouthernRealms Building: Reign of Terror"),

    110426: itemData(IC.useful, 1, "teb_garrison_big_1", itemType.building, 0, "Progressive teb_walls", "SouthernRealms Building: Gatehouse"),
    110427: itemData(IC.useful, 1, "teb_garrison_big_2", itemType.building, 1, "Progressive teb_walls", "SouthernRealms Building: Basic Walls"),
    110428: itemData(IC.useful, 1, "teb_garrison_big_3", itemType.building, 2, "Progressive teb_walls", "SouthernRealms Building: Tall Walls"),
    110429: itemData(IC.useful, 1, "teb_garrison_big_4", itemType.building, 3, "Progressive teb_walls", "SouthernRealms Building: Reinforced Walls"),
    110430: itemData(IC.useful, 1, "teb_garrison_big_5", itemType.building, 4, "Progressive teb_walls", "SouthernRealms Building: Star Fort"),

    110431: itemData(IC.useful, 1, "wh2_main_foreign_slot_discovery_emp_1", itemType.building, 0, "Progressive teb_foreign_slot_discovery", "SouthernRealms Building: Night Watch"),
    110432: itemData(IC.useful, 1, "wh2_main_foreign_slot_discovery_emp_2", itemType.building, 1, "Progressive teb_foreign_slot_discovery", "SouthernRealms Building: Armoured Watchers"),
    110433: itemData(IC.useful, 1, "wh2_main_foreign_slot_discovery_emp_3", itemType.building, 2, "Progressive teb_foreign_slot_discovery", "SouthernRealms Building: Elite Watchers"),

    110434: itemData(IC.useful, 1, "teb_garrison_small_1", itemType.building, 0, "Progressive teb_garrison", "SouthernRealms Building: Guard Post"),
    110435: itemData(IC.useful, 1, "teb_garrison_small_2", itemType.building, 1, "Progressive teb_garrison", "SouthernRealms Building: Guard House"),
    110436: itemData(IC.useful, 1, "teb_garrison_small_3", itemType.building, 2, "Progressive teb_garrison", "SouthernRealms Building: City Watch"),

    110437: itemData(IC.useful, 1, "teb_eco_farm_1", itemType.building, 0, "Progressive teb_farm", "SouthernRealms Building: Fields"),
    110438: itemData(IC.useful, 1, "teb_eco_farm_2", itemType.building, 1, "Progressive teb_farm", "SouthernRealms Building: Farm"),
    110439: itemData(IC.useful, 1, "teb_eco_farm_3", itemType.building, 2, "Progressive teb_farm", "SouthernRealms Building: Landed Estate"),
    110440: itemData(IC.useful, 1, "teb_eco_farm_4", itemType.building, 3, "Progressive teb_farm", "SouthernRealms Building: Flourishing Estates"),
    110441: itemData(IC.useful, 1, "teb_eco_farm_5", itemType.building, 4, "Progressive teb_farm", "SouthernRealms Building: Cooperative Latifundia"),

    110442: itemData(IC.useful, 1, "teb_eco_cloth_1", itemType.building, 0, "Progressive teb_industry", "SouthernRealms Building: Weaving House"),
    110443: itemData(IC.useful, 1, "teb_eco_cloth_2", itemType.building, 1, "Progressive teb_industry", "SouthernRealms Building: Clothier"),
    110444: itemData(IC.useful, 1, "teb_eco_cloth_3", itemType.building, 2, "Progressive teb_industry", "SouthernRealms Building: Tailors' Guild"),
    110445: itemData(IC.useful, 1, "teb_eco_cloth_4", itemType.building, 3, "Progressive teb_industry", "SouthernRealms Building: Clothing Industry"),
    110446: itemData(IC.useful, 1, "teb_eco_cloth_5", itemType.building, 4, "Progressive teb_industry", "SouthernRealms Building: Provincial Monopoly"),

    110447: itemData(IC.useful, 1, "teb_eco_order_1", itemType.building, 0, "Progressive teb_wine", "SouthernRealms Building: Orchards"),
    110448: itemData(IC.useful, 1, "teb_eco_order_2", itemType.building, 1, "Progressive teb_wine", "SouthernRealms Building: Vineyard"),
    110449: itemData(IC.useful, 1, "teb_eco_order_3", itemType.building, 2, "Progressive teb_wine", "SouthernRealms Building: Winery"),
    110450: itemData(IC.useful, 1, "teb_eco_order_4", itemType.building, 3, "Progressive teb_wine", "SouthernRealms Building: Winemakers' Guild"),
    110451: itemData(IC.useful, 1, "teb_eco_order_5", itemType.building, 4, "Progressive teb_wine", "SouthernRealms Building: Winery Monopoly"),

    110452: itemData(IC.useful, 1, "teb_eco_stocks_1", itemType.building, 0, "Progressive teb_trade", "SouthernRealms Building: Trading Depot"),
    110453: itemData(IC.useful, 1, "teb_eco_stocks_2", itemType.building, 1, "Progressive teb_trade", "SouthernRealms Building: Trading Stockpile"),
    110454: itemData(IC.useful, 1, "teb_eco_stocks_3", itemType.building, 2, "Progressive teb_trade", "SouthernRealms Building: Trading Node"),
    110455: itemData(IC.useful, 1, "teb_eco_stocks_4", itemType.building, 3, "Progressive teb_trade", "SouthernRealms Building: Mercantile Stocks"),
    110456: itemData(IC.useful, 1, "teb_eco_stocks_5", itemType.building, 4, "Progressive teb_trade", "SouthernRealms Building: Futures"),

    110457: itemData(IC.useful, 1, "wh2_main_emp_roads_1", itemType.building, 0, "Progressive teb_roads", "SouthernRealms Building: Paved Roads"),
    110458: itemData(IC.useful, 1, "wh2_main_emp_roads_2", itemType.building, 1, "Progressive teb_roads", "SouthernRealms Building: Toll Gates"),

    110459: itemData(IC.useful, 1, 'wh_main_emp_settlement_major_1', itemType.building, 0, 'Progressive teb_settlement_major', 'SouthernRealms Building: Hamlet (Major)'),
    110460: itemData(IC.useful, 1, 'wh_main_emp_settlement_major_2', itemType.building, 1, 'Progressive teb_settlement_major', 'SouthernRealms Building: Village (Major)'),
    110461: itemData(IC.useful, 1, 'wh_main_emp_settlement_major_3', itemType.building, 2, 'Progressive teb_settlement_major', 'SouthernRealms Building: Town (Major)'),
    110462: itemData(IC.useful, 1, 'wh_main_emp_settlement_major_4', itemType.building, 3, 'Progressive teb_settlement_major', 'SouthernRealms Building: City (Major)'),
    110463: itemData(IC.useful, 1, 'wh_main_emp_settlement_major_5', itemType.building, 4, 'Progressive teb_settlement_major', 'SouthernRealms Building: City-State (Major)'),
    110464: itemData(IC.useful, 1, 'wh_main_emp_settlement_minor_1', itemType.building, 0, 'Progressive teb_settlement_minor', 'SouthernRealms Building: Hamlet (Minor)'),
    110465: itemData(IC.useful, 1, 'wh_main_emp_settlement_minor_2', itemType.building, 1, 'Progressive teb_settlement_minor', 'SouthernRealms Building: Village (Minor)'),
    110466: itemData(IC.useful, 1, 'wh_main_emp_settlement_minor_3', itemType.building, 2, 'Progressive teb_settlement_minor', 'SouthernRealms Building: Town (Minor)'),

    110467: itemData(IC.useful, 1, "teb_resource_iron_1", itemType.building, 0, "Progressive teb_resource_iron", "SouthernRealms Building: Steelworks"),
    110468: itemData(IC.useful, 1, "teb_resource_iron_2", itemType.building, 1, "Progressive teb_resource_iron", "SouthernRealms Building: Armourer's Guild"),

    110469: itemData(IC.useful, 1, "wh_main_brt_resource_salt_1", itemType.building, 0, "Progressive teb_resource_salt", "SouthernRealms Building: Brine Mining Pit"),
    110470: itemData(IC.useful, 1, "wh_main_brt_resource_salt_2", itemType.building, 1, "Progressive teb_resource_salt", "SouthernRealms Building: Brine Mine"),
    110471: itemData(IC.useful, 1, "wh_main_brt_resource_salt_3", itemType.building, 2, "Progressive teb_resource_salt", "SouthernRealms Building: Saltworks"),

    110472: itemData(IC.useful, 1, "teb_resource_animals_1", itemType.building, 0, "Progressive teb_resource_animals", "SouthernRealms Building: Exotic Animal Tamer"),
    110473: itemData(IC.useful, 1, "teb_resource_animals_2", itemType.building, 1, "Progressive teb_resource_animals", "SouthernRealms Building: Exotic Animal Pen"),
    110474: itemData(IC.useful, 1, "teb_resource_animals_3", itemType.building, 2, "Progressive teb_resource_animals", "SouthernRealms Building: Exotic Animal Market"),

    110475: itemData(IC.useful, 1, "teb_resource_gold_1", itemType.building, 0, "Progressive teb_resource_gold", "SouthernRealms Building: Gold Mining Pit"),
    110476: itemData(IC.useful, 1, "teb_resource_gold_2", itemType.building, 1, "Progressive teb_resource_gold", "SouthernRealms Building: Gold Mine"),
    110477: itemData(IC.useful, 1, "teb_resource_gold_3", itemType.building, 2, "Progressive teb_resource_gold", "SouthernRealms Building: Gold Smelter"),

    110478: itemData(IC.useful, 1, "teb_resource_pastures_1", itemType.building, 0, "Progressive teb_resource_pastures", "SouthernRealms Building: Grazing Pastures"),
    110479: itemData(IC.useful, 1, "teb_resource_pastures_2", itemType.building, 1, "Progressive teb_resource_pastures", "SouthernRealms Building: Livestock Pens"),
    110480: itemData(IC.useful, 1, "teb_resource_pastures_3", itemType.building, 2, "Progressive teb_resource_pastures", "SouthernRealms Building: Cattle Ranch"),

    110481: itemData(IC.useful, 1, "teb_resource_timber_1", itemType.building, 0, "Progressive teb_resource_timber", "SouthernRealms Building: Woodman's Hut"),
    110482: itemData(IC.useful, 1, "teb_resource_timber_2", itemType.building, 1, "Progressive teb_resource_timber", "SouthernRealms Building: Timber Mill"),
    110483: itemData(IC.useful, 1, "teb_resource_timber_3", itemType.building, 2, "Progressive teb_resource_timber", "SouthernRealms Building: Lumberyard"),

    #110516

    110517: itemData(IC.useful, 1, "teb_camp_main_1", itemType.building, 0, "Progressive teb_camp_main", "SouthernRealms Camp: Improvised Shacks"),
    110518: itemData(IC.useful, 1, "teb_camp_main_2", itemType.building, 1, "Progressive teb_camp_main", "SouthernRealms Camp: Small Mercenary Camp"),
    110519: itemData(IC.useful, 1, "teb_camp_main_3", itemType.building, 2, "Progressive teb_camp_main", "SouthernRealms Camp: Encampment"),
    110520: itemData(IC.useful, 1, "teb_camp_main_4", itemType.building, 3, "Progressive teb_camp_main", "SouthernRealms Camp: Organized Encampment"),
    110521: itemData(IC.useful, 1, "teb_camp_main_5", itemType.building, 4, "Progressive teb_camp_main", "SouthernRealms Camp: Mercenary Stronghold"),

    110522: itemData(IC.useful, 1, "teb_camp_inf_1", itemType.building, 0, "Progressive teb_camp_infantry", "SouthernRealms Camp: Half-Companies"),
    110523: itemData(IC.useful, 1, "teb_camp_inf_2", itemType.building, 1, "Progressive teb_camp_infantry", "SouthernRealms Camp: Companies"),
    110524: itemData(IC.useful, 1, "teb_camp_inf_3", itemType.building, 2, "Progressive teb_camp_infantry", "SouthernRealms Camp: Regiments"),
    110525: itemData(IC.useful, 1, "teb_camp_inf_4", itemType.building, 3, "Progressive teb_camp_infantry", "SouthernRealms Camp: Infantry Hosts"),

    110526: itemData(IC.useful, 1, "teb_camp_missile_1", itemType.building, 0, "Progressive teb_camp_ranged", "SouthernRealms Camp: Missile Range"),
    110527: itemData(IC.useful, 1, "teb_camp_missile_2", itemType.building, 1, "Progressive teb_camp_ranged", "SouthernRealms Camp: Marksmen Recruitment"),
    110528: itemData(IC.useful, 1, "teb_camp_missile_3", itemType.building, 2, "Progressive teb_camp_ranged", "SouthernRealms Camp: Masters' Lodge"),

    110529: itemData(IC.useful, 1, "teb_camp_cavalry_1", itemType.building, 0, "Progressive teb_camp_cavalry", "SouthernRealms Camp: Horse Pen"),
    110530: itemData(IC.useful, 1, "teb_camp_cavalry_2", itemType.building, 1, "Progressive teb_camp_cavalry", "SouthernRealms Camp: Stables"),
    110531: itemData(IC.useful, 1, "teb_camp_cavalry_3", itemType.building, 2, "Progressive teb_camp_cavalry", "SouthernRealms Camp: Horse Keeper's Ranch"),

    110532: itemData(IC.useful, 1, "teb_camp_artillery_1", itemType.building, 0, "Progressive teb_camp_artillery", "SouthernRealms Camp: Repair Shop"),
    110533: itemData(IC.useful, 1, "teb_camp_artillery_2", itemType.building, 1, "Progressive teb_camp_artillery", "SouthernRealms Camp: Improvised Forge"),

    110534: itemData(IC.useful, 1, "teb_camp_recr_1", itemType.building, 0, "Progressive teb_camp_recruitment", "SouthernRealms Camp: Room for More"),
    110535: itemData(IC.useful, 1, "teb_camp_recr_2", itemType.building, 1, "Progressive teb_camp_recruitment", "SouthernRealms Camp: Recruiter's Tent"),
    110536: itemData(IC.useful, 1, "teb_camp_recr_3", itemType.building, 2, "Progressive teb_camp_recruitment", "SouthernRealms Camp: Recruiter's Hut"),
    110537: itemData(IC.useful, 1, "teb_camp_recr_4", itemType.building, 3, "Progressive teb_camp_recruitment", "SouthernRealms Camp: Recruiter's Shack"),
    110538: itemData(IC.useful, 1, "teb_camp_recr_5", itemType.building, 4, "Progressive teb_camp_recruitment", "SouthernRealms Camp: Recruiter's Log House"),

    110539: itemData(IC.useful, 1, "teb_camp_upk_1", itemType.building, 0, "Progressive teb_camp_upkeep", "SouthernRealms Camp: Paymaster's Desk"),
    110540: itemData(IC.useful, 1, "teb_camp_upk_2", itemType.building, 1, "Progressive teb_camp_upkeep", "SouthernRealms Camp: Paymaster's Hut"),
    110541: itemData(IC.useful, 1, "teb_camp_upk_3", itemType.building, 2, "Progressive teb_camp_upkeep", "SouthernRealms Camp: Paymaster's Safe House"),
    110542: itemData(IC.useful, 1, "teb_camp_upk_4", itemType.building, 3, "Progressive teb_camp_upkeep", "SouthernRealms Camp: Paymaster's Tavern"),
    110543: itemData(IC.useful, 1, "teb_camp_upk_5", itemType.building, 4, "Progressive teb_camp_upkeep", "SouthernRealms Camp: Paymaster's Complex"),

    110544: itemData(IC.useful, 1, "teb_camp_foreign_1", itemType.building, 0, "Progressive teb_camp_foreign", "SouthernRealms Camp: Foreign Mercs"),
    110545: itemData(IC.useful, 1, "teb_camp_foreign_2", itemType.building, 1, "Progressive teb_camp_foreign", "SouthernRealms Camp: More Expensive Foreign Mercs"),

    110546: itemData(IC.useful, 1, "teb_camp_replenish_1", itemType.building, 0, "Progressive teb_camp_replenishment", "SouthernRealms Camp: First Aid"),
    110547: itemData(IC.useful, 1, "teb_camp_replenish_2", itemType.building, 1, "Progressive teb_camp_replenishment", "SouthernRealms Camp: Medic's Tent"),
    110548: itemData(IC.useful, 1, "teb_camp_replenish_3", itemType.building, 2, "Progressive teb_camp_replenishment", "SouthernRealms Camp: Infirmary"),
    110549: itemData(IC.useful, 1, "teb_camp_replenish_4", itemType.building, 3, "Progressive teb_camp_replenishment", "SouthernRealms Camp: Medical Team"),
    110550: itemData(IC.useful, 1, "teb_camp_replenish_5", itemType.building, 4, "Progressive teb_camp_replenishment", "SouthernRealms Camp: Field Hospital"),

    110551: itemData(IC.useful, 1, "teb_camp_growth_1", itemType.building, 0, "Progressive teb_camp_growth", "SouthernRealms Camp: Supplies"),
    110552: itemData(IC.useful, 1, "teb_camp_growth_2", itemType.building, 1, "Progressive teb_camp_growth", "SouthernRealms Camp: More Supplies"),
    110553: itemData(IC.useful, 1, "teb_camp_growth_3", itemType.building, 2, "Progressive teb_camp_growth", "SouthernRealms Camp: Even More Supplies"),
    110554: itemData(IC.useful, 1, "teb_camp_growth_4", itemType.building, 3, "Progressive teb_camp_growth", "SouthernRealms Camp: Amazingly More Supplies"),
    110555: itemData(IC.useful, 1, "teb_camp_growth_5", itemType.building, 4, "Progressive teb_camp_growth", "SouthernRealms Camp: Surprisingly, Stockpiles"),

    110556: itemData(IC.useful, 1, "teb_camp_port", itemType.building, 0, "Progressive teb_camp_region", "SouthernRealms Camp: Port Intermediaries"),
    110557: itemData(IC.useful, 1, "teb_camp_mountain", itemType.building, 0, "Progressive teb_camp_region", "SouthernRealms Camp: Mountain Guides"),
    110558: itemData(IC.useful, 1, "teb_camp_jungle", itemType.building, 0, "Progressive teb_camp_region", "SouthernRealms Camp: Jungle Guides"),
    110559: itemData(IC.useful, 1, "teb_camp_scavenge", itemType.building, 0, "Progressive teb_camp_region", "SouthernRealms Camp: Organized Scavenging"),
}
"""
103419: itemData(IC.useful, 1, 'Progressive teb_resource_gemstones', itemType.building, 3, '', 'Progressive SouthernRealms Building: Gemstones'),
103420: itemData(IC.useful, 1, 'Progressive teb_resource_medicine', itemType.building, 3, '', 'Progressive SouthernRealms Building: Medicine'),
103421: itemData(IC.useful, 1, 'Progressive teb_resource_obsidian', itemType.building, 3, '', 'Progressive SouthernRealms Building: Obsidian'),
103422: itemData(IC.useful, 1, 'Progressive teb_resource_spices', itemType.building, 3, '', 'Progressive SouthernRealms Building: Spices'),
103423: itemData(IC.useful, 1, 'Progressive teb_resource_ivory', itemType.building, 3, '', 'Progressive SouthernRealms Building: Ivory'),
103424: itemData(IC.useful, 1, 'Progressive teb_resource_dyes', itemType.building, 3, '', "Progressive SouthernRealms Building: Dyes"),
103425: itemData(IC.useful, 1, 'Progressive teb_resource_furs', itemType.building, 3, '', "Progressive SouthernRealms Building: Furs"),
103427: itemData(IC.useful, 1, 'Progressive teb_resource_iron', itemType.building, 3, '', 'Progressive SouthernRealms Building: Iron'),
103428: itemData(IC.useful, 1, 'Progressive teb_resource_marble', itemType.building, 3, '', "Progressive SouthernRealms Building: Marble"),
103430: itemData(IC.useful, 1, 'Progressive teb_resource_pottery', itemType.building, 3, '', 'Progressive SouthernRealms Building: Pottery'),
103433: itemData(IC.useful, 1, 'Progressive teb_resource_wine', itemType.building, 3, '', 'Progressive SouthernRealms Building: Wine'),
"""

techs: dict[int, itemData] = {
    110800: itemData(IC.useful, 1, "teb_tank_1", itemType.tech, 1, "Progressive tech_teb_doodles", "SouthernRealms Tech: Doodles of Mass Destruction"),
    110801: itemData(IC.useful, 1, "teb_tank_2", itemType.tech, 2, "Progressive tech_teb_doodles", "SouthernRealms Tech: Cranking it Up"),
    110802: itemData(IC.useful, 1, "teb_tank_3", itemType.tech, 3, "Progressive tech_teb_doodles", "SouthernRealms Tech: The Saucer"),
    110803: itemData(IC.useful, 1, "teb_crossbow_rocket", itemType.tech, 2, "Progressive tech_teb_doodles", "SouthernRealms Tech: Weaponized Fireworks"),

    110804: itemData(IC.useful, 1, "teb_tech_exped_vets", itemType.tech, 1, "Progressive tech_teb_upper", "SouthernRealms Tech: Expeditionary Veterans"),
    110805: itemData(IC.useful, 1, "teb_tech_recr_vets", itemType.tech, 1, "Progressive tech_teb_upper", "SouthernRealms Tech: Recruit the Veterans"),
    110806: itemData(IC.useful, 1, "teb_tech_immune_psy", itemType.tech, 1, "Progressive tech_teb_upper", "SouthernRealms Tech: Unfazed Survivors"),
    110807: itemData(IC.useful, 1, "teb_tech_mercs", itemType.tech, 1, "Progressive tech_teb_upper", "SouthernRealms Tech: Mercenary Hosts"),
    110808: itemData(IC.useful, 1, "teb_tech_recr_vets_sub", itemType.tech, 2, "Progressive tech_teb_upper", "SouthernRealms Tech: Men with No Names"),
    110809: itemData(IC.useful, 1, "teb_tech_exped_vets_sub", itemType.tech, 2, "Progressive tech_teb_upper", "SouthernRealms Tech: Militia Reforms"),

    110810: itemData(IC.useful, 1, "teb_tech_steel", itemType.tech, 1, "Progressive tech_teb_middle", "SouthernRealms Tech: Local Steel"),
    110811: itemData(IC.useful, 1, "teb_tech_classical", itemType.tech, 1, "Progressive tech_teb_middle", "SouthernRealms Tech: Classical Military Studies"),
    110812: itemData(IC.useful, 1, "teb_tech_tactics", itemType.tech, 1, "Progressive tech_teb_middle", "SouthernRealms Tech: Tactical Superiority"),
    110813: itemData(IC.useful, 1, "teb_tech_leaders", itemType.tech, 1, "Progressive tech_teb_middle", "SouthernRealms Tech: Self-made Leaders"),

    110815: itemData(IC.useful, 1, "teb_tech_trade", itemType.tech, 1, "Progressive tech_teb_lower", "SouthernRealms Tech: Flourishing Southern Trade"),
    110816: itemData(IC.useful, 1, "teb_tech_lucrezia", itemType.tech, 1, "Progressive tech_teb_lower", "SouthernRealms Tech: Lucrezzian Diplomacy"),
    110817: itemData(IC.useful, 1, "teb_tech_myrmidia", itemType.tech, 1, "Progressive tech_teb_lower", "SouthernRealms Tech: Greater Rites of Myrmidia"),
    110818: itemData(IC.useful, 1, "teb_tech_trade_sub_lions", itemType.tech, 1, "Progressive tech_teb_lower", "SouthernRealms Tech: Tribute to the Lions"),
}

progUnits: dict[int, itemData] = {
    111200: itemData(IC.useful, 1, "Progressive teb_inf", itemType.unit, 4, None, "Progressive SouthernRealms Unit: Infantry"),
    111201: itemData(IC.useful, 1, "Progressive teb_rng", itemType.unit, 3, None, "Progressive SouthernRealms Unit: Ranged"),
    111202: itemData(IC.useful, 1, "Progressive teb_cav", itemType.unit, 4, None, "Progressive SouthernRealms Unit: Cavalry"),
    111203: itemData(IC.useful, 1, "Progressive teb_art", itemType.unit, 1, None, "Progressive SouthernRealms Unit: Artillery"),
    111204: itemData(IC.useful, 1, "Progressive teb_veh", itemType.unit, 2, None, "Progressive SouthernRealms Unit: Vehicle"),
    111205: itemData(IC.useful, 1, "Progressive teb_bst", itemType.unit, 1, None, "Progressive SouthernRealms Unit: Beast"),
    111206: itemData(IC.useful, 1, "Progressive teb_hro", itemType.unit, 1, None, "Progressive SouthernRealms Unit: Hero"),
}

progBuildings: dict[int, itemData] = {
    111300: itemData(IC.useful, 1, "Progressive teb_port", itemType.building, 3, None, "Progressive SouthernRealms Building: Port"),
    110301: itemData(IC.useful, 1, "Progressive teb_port", itemType.building, 3, None, "Progressive SouthernRealms Building: Barracks"),
    110408: itemData(IC.useful, 1, "Progressive teb_mercs", itemType.building, 3, None, "Progressive SouthernRealms Building: Mercenaries"),
    110410: itemData(IC.useful, 1, "Progressive teb_artillery", itemType.building, 2, None, "Progressive SouthernRealms Building: Artillery"),
    110412: itemData(IC.useful, 1, "Progressive teb_smith", itemType.building, 2, None, "Progressive SouthernRealms Building: Smithy"),
    110417: itemData(IC.useful, 1, "Progressive teb_worship_myrmidia", itemType.building, 5, None, "Progressive SouthernRealms Building: Cult of Myrmidia"),
    110422: itemData(IC.useful, 1, "Progressive teb_worship_shallya", itemType.building, 5, None, "Progressive SouthernRealms Building: Cult of Shallya"),
    110425: itemData(IC.useful, 1, "Progressive teb_badmercs", itemType.building, 3, None, "Progressive SouthernRealms Building: Mercenary Warfare"),
    110430: itemData(IC.useful, 1, "Progressive teb_walls", itemType.building, 5, None, "Progressive SouthernRealms Building: Walls"),
    110433: itemData(IC.useful, 1, "Progressive teb_foreign_slot_discovery", itemType.building, 3, None, "Progressive SouthernRealms Building: Protection"),
    110436: itemData(IC.useful, 1, "Progressive teb_garrison", itemType.building, 3, None, "Progressive SouthernRealms Building: Garrison"),
    110441: itemData(IC.useful, 1, "Progressive teb_farm", itemType.building, 5, None, "Progressive SouthernRealms Building: Farms"),
    110446: itemData(IC.useful, 1, "Progressive teb_industry", itemType.building, 5, None, "Progressive SouthernRealms Building: Industry"),
    110451: itemData(IC.useful, 1, "Progressive teb_wine", itemType.building, 5, None, "Progressive SouthernRealms Building: Order"),
    110456: itemData(IC.useful, 1, "Progressive teb_trade", itemType.building, 5, None, "Progressive SouthernRealms Building: Trade"),
    110458: itemData(IC.useful, 1, "Progressive teb_roads", itemType.building, 2, None, "Progressive SouthernRealms Building: Roads"),
    110463: itemData(IC.useful, 1, 'Progressive teb_settlement_major', itemType.building, 5, None, 'Progressive SouthernRealms Building: Settlement Major'),
    110466: itemData(IC.useful, 1, 'Progressive teb_settlement_minor', itemType.building, 3, None, 'Progressive SouthernRealms Building: Settlement Minor'),
    110468: itemData(IC.useful, 1, "Progressive teb_resource_iron", itemType.building, 3, None, "Progressive SouthernRealms Building: Armourer's Guild"),
    110471: itemData(IC.useful, 1, "Progressive teb_resource_salt", itemType.building, 3, None, "Progressive SouthernRealms Building: Saltworks"),
    110474: itemData(IC.useful, 1, "Progressive teb_resource_animals", itemType.building, 3, None, "Progressive SouthernRealms Building: Exotic Animal Market"),
    110477: itemData(IC.useful, 1, "Progressive teb_resource_gold", itemType.building, 3, None, "Progressive SouthernRealms Building: Gold Smelter"),
    110480: itemData(IC.useful, 1, "Progressive teb_resource_pastures", itemType.building, 3, None, "Progressive SouthernRealms Building: Cattle Ranch"),
    110483: itemData(IC.useful, 1, "Progressive teb_resource_timber", itemType.building, 3, None, "Progressive SouthernRealms Building: Lumberyard"),
}

progTechs: dict[int, itemData] = {
    111400: itemData(IC.useful, 1, "Progressive tech_teb_upper", itemType.tech, 2, None, "Progressive SouthernRealms Tech: Upper Tree"),
    111401: itemData(IC.useful, 1, "Progressive tech_teb_middle", itemType.tech, 2, None, "Progressive SouthernRealms Tech: Middle Tree"),
    111402: itemData(IC.useful, 1, "Progressive tech_teb_lower", itemType.tech, 2, None, "Progressive SouthernRealms Tech: Lower Tree"),
}

special: dict[int, specialItemData] = {
    111500: specialItemData(IC.useful, 1, "mixer_teb_border_princes", "teb_kotrs", itemType.unit, 2, "Progressive teb_cav", False, False, "SouthernRealms Unit: Knights of the Righteous Spear"),
    111501: specialItemData(IC.useful, 1, "mixer_teb_border_princes", "teb_sisters", itemType.unit, 4, "Progressive teb_inf", False, False, "SouthernRealms Unit: Sisters of Fury"),
    111502: specialItemData(IC.useful, 1, "mixer_teb_border_princes", "teb_shieldbearers", itemType.unit, 4, "Progressive teb_inf", False, False, "SouthernRealms Unit: Shieldbearers"),
    111503: specialItemData(IC.useful, 1, "mixer_teb_border_princes", "teb_swash", itemType.unit, 2, "Progressive teb_rng", False, False, "SouthernRealms Unit: Swashbucklers"),
    111504: specialItemData(IC.useful, 1, "mixer_teb_border_princes", "teb_light_scouts", itemType.unit, 1, "Progressive teb_cav", False, False, "SouthernRealms Unit: Light Scouts"),
    111505: specialItemData(IC.useful, 1, "mixer_teb_border_princes", "teb_enforcers", itemType.unit, 2, "Progressive teb_cav", False, False, "SouthernRealms Unit: Enforcers"),
    111506: specialItemData(IC.useful, 1, "mixer_teb_border_princes", "teb_militia_archers", itemType.unit, 1, "Progressive teb_rng", False, False, "SouthernRealms Unit: Militia Archers"),
    111507: specialItemData(IC.useful, 1, "mixer_teb_border_princes", "teb_freelance_knights", itemType.unit, 2, "Progressive teb_cav", False, False, "SouthernRealms Unit: Freelance Knights"),
    111508: specialItemData(IC.useful, 1, "mixer_teb_border_princes", "teb_militia_knights", itemType.unit, 2, "Progressive teb_cav", False, False, "SouthernRealms Unit: Carlsson Militia"),
    111509: specialItemData(IC.useful, 1, "mixer_teb_border_princes", "teb_border_rangers", itemType.unit, 1, "Progressive teb_rng", False, False, "SouthernRealms Unit: Border Rangers"),
    111510: specialItemData(IC.useful, 1, "mixer_teb_border_princes", "teb_guard_kossars", itemType.unit, 3, "Progressive teb_rng", False, False, "SouthernRealms Unit: Uvetovsk Kossars"),
    111511: specialItemData(IC.useful, 1, "mixer_teb_border_princes", "wh_dlc06_dwf_inf_rangers_0", itemType.unit, 2, "Progressive teb_rng", False, False, "SouthernRealms Unit: Rangers"),
    111512: specialItemData(IC.useful, 1, "mixer_teb_gashnag", "teb_kotrs", itemType.unit, 2, "Progressive teb_cav", False, False, "SouthernRealms Unit: Knights of the Righteous Spear"),
    111513: specialItemData(IC.useful, 1, "mixer_teb_gashnag", "teb_sisters", itemType.unit, 4, "Progressive teb_inf", False, False, "SouthernRealms Unit: Sisters of Fury"),
    111514: specialItemData(IC.useful, 1, "mixer_teb_gashnag", "teb_shieldbearers", itemType.unit, 4, "Progressive teb_inf", False, False, "SouthernRealms Unit: Shieldbearers"),
    111515: specialItemData(IC.useful, 1, "mixer_teb_gashnag", "teb_swash", itemType.unit, 2, "Progressive teb_rng", False, False, "SouthernRealms Unit: Swashbucklers"),
    111516: specialItemData(IC.useful, 1, "mixer_teb_gashnag", "teb_light_scouts", itemType.unit, 1, "Progressive teb_cav", False, False, "SouthernRealms Unit: Light Scouts"),
    111517: specialItemData(IC.useful, 1, "mixer_teb_gashnag", "teb_enforcers", itemType.unit, 2, "Progressive teb_cav", False, False, "SouthernRealms Unit: Enforcers"),
    111518: specialItemData(IC.useful, 1, "mixer_teb_gashnag", "teb_militia_archers", itemType.unit, 1, "Progressive teb_rng", False, False, "SouthernRealms Unit: Militia Archers"),
    111519: specialItemData(IC.useful, 1, "mixer_teb_gashnag", "teb_freelance_knights", itemType.unit, 2, "Progressive teb_cav", False, False, "SouthernRealms Unit: Freelance Knights"),
    111520: specialItemData(IC.useful, 1, "mixer_teb_gashnag", "teb_militia_knights", itemType.unit, 2, "Progressive teb_cav", False, False, "SouthernRealms Unit: Carlsson Militia"),
    111521: specialItemData(IC.useful, 1, "mixer_teb_gashnag", "teb_border_rangers", itemType.unit, 1, "Progressive teb_rng", False, False, "SouthernRealms Unit: Border Rangers"),
    111522: specialItemData(IC.useful, 1, "mixer_teb_gashnag", "teb_guard_kossars", itemType.unit, 3, "Progressive teb_rng", False, False, "SouthernRealms Unit: Uvetovsk Kossars"),
    111523: specialItemData(IC.useful, 1, "mixer_teb_gashnag", "wh_dlc06_dwf_inf_rangers_0", itemType.unit, 2, "Progressive teb_rng", False, False, "SouthernRealms Unit: Rangers"),

    111524: specialItemData(IC.useful, 1, "cr_teb_miragliano", "teb_pikemen", itemType.unit, 2, "Progressive teb_inf", False, False, "SouthernRealms Unit: Pikemen"),
    111525: specialItemData(IC.useful, 1, "cr_teb_miragliano", "teb_republican_guard", itemType.unit, 3, "Progressive teb_inf", False, False, "SouthernRealms Unit: Republican Guard"),
    111526: specialItemData(IC.useful, 1, "cr_teb_miragliano", "teb_montante_greatswords", itemType.unit, 4, "Progressive teb_inf", False, False, "SouthernRealms Unit: Montante Swordsmen"),
    111527: specialItemData(IC.useful, 1, "cr_teb_miragliano", "teb_pavisiers", itemType.unit, 2, "Progressive teb_rng", False, False, "SouthernRealms Unit: Pavise Crossbowmen"),
    111528: specialItemData(IC.useful, 1, "cr_teb_miragliano", "teb_broken_lances", itemType.unit, 2, "Progressive teb_cav", False, False, "SouthernRealms Unit: Broken Lances"),
    111529: specialItemData(IC.useful, 1, "cr_teb_miragliano", "teb_noble_retinue", itemType.unit, 3, "Progressive teb_cav", False, False, "SouthernRealms Unit: Noble Retinue"),
    111530: specialItemData(IC.useful, 1, "cr_teb_miragliano", "teb_carabiniers", itemType.unit, 3, "Progressive teb_cav", False, False, "SouthernRealms Unit: Carabiniers"),
    111531: specialItemData(IC.useful, 1, "cr_teb_miragliano", "teb_encarmine", itemType.unit, 3, "Progressive teb_cav", False, False, "SouthernRealms Unit: Knights Encarmine"),
    111532: specialItemData(IC.useful, 1, "cr_teb_miragliano", "teb_kotrs", itemType.unit, 2, "Progressive teb_cav", False, False, "SouthernRealms Unit: Knights of the Righteous Spear"),
    111533: specialItemData(IC.useful, 1, "cr_teb_miragliano", "teb_sisters", itemType.unit, 4, "Progressive teb_inf", False, False, "SouthernRealms Unit: Sisters of Fury"),
    111534: specialItemData(IC.useful, 1, "cr_teb_miragliano", "teb_galloper", itemType.unit, 1, "Progressive teb_art", False, False, "SouthernRealms Unit: Galloper Guns"),

    111535: specialItemData(IC.useful, 1, "mixer_teb_estalia", "teb_pikemen", itemType.unit, 2, "Progressive teb_inf", False, False, "SouthernRealms Unit: Pikemen"),
    111536: specialItemData(IC.useful, 1, "mixer_teb_estalia", "teb_bwatch", itemType.unit, 3, "Progressive teb_inf", False, False, "SouthernRealms Unit: Black Watch"),
    111537: specialItemData(IC.useful, 1, "mixer_teb_estalia", "teb_montante_greatswords", itemType.unit, 4, "Progressive teb_inf", False, False, "SouthernRealms Unit: Montante Swordsmen"),
    111538: specialItemData(IC.useful, 1, "mixer_teb_estalia", "teb_conqui_adventurers", itemType.unit, 2, "Progressive teb_inf", False, False, "SouthernRealms Unit: Adventurers"),
    111539: specialItemData(IC.useful, 1, "mixer_teb_estalia", "teb_irrana", itemType.unit, 2, "Progressive teb_rng", False, False, "SouthernRealms Unit: Irranan Hillmen"),
    111540: specialItemData(IC.useful, 1, "mixer_teb_estalia", "teb_conqui_royal_guard", itemType.unit, 3, "Progressive teb_rng", False, False, "SouthernRealms Unit: Royal Guard"),
    111541: specialItemData(IC.useful, 1, "mixer_teb_estalia", "teb_conqui_lancers", itemType.unit, 1, "Progressive teb_cav", False, False, "SouthernRealms Unit: Lancers"),
    111542: specialItemData(IC.useful, 1, "mixer_teb_estalia", "teb_conqui_riders", itemType.unit, 2, "Progressive teb_cav", False, False, "SouthernRealms Unit: Riders"),
    111543: specialItemData(IC.useful, 1, "mixer_teb_estalia", "teb_noble_retinue", itemType.unit, 3, "Progressive teb_cav", False, False, "SouthernRealms Unit: Noble Retinue"),
    111544: specialItemData(IC.useful, 1, "mixer_teb_estalia", "teb_kotrs", itemType.unit, 2, "Progressive teb_cav", False, False, "SouthernRealms Unit: Knights of the Righteous Spear"),
    111545: specialItemData(IC.useful, 1, "mixer_teb_estalia", "teb_sisters", itemType.unit, 4, "Progressive teb_inf", False, False, "SouthernRealms Unit: Sisters of Fury"),

    111546: specialItemData(IC.useful, 1, "mixer_teb_bilbali", "teb_pikemen", itemType.unit, 2, "Progressive teb_inf", False, False, "SouthernRealms Unit: Pikemen"),
    111547: specialItemData(IC.useful, 1, "mixer_teb_bilbali", "teb_bwatch", itemType.unit, 3, "Progressive teb_inf", False, False, "SouthernRealms Unit: Black Watch"),
    111548: specialItemData(IC.useful, 1, "mixer_teb_bilbali", "teb_montante_greatswords", itemType.unit, 4, "Progressive teb_inf", False, False, "SouthernRealms Unit: Montante Swordsmen"),
    111549: specialItemData(IC.useful, 1, "mixer_teb_bilbali", "teb_conqui_adventurers", itemType.unit, 2, "Progressive teb_inf", False, False, "SouthernRealms Unit: Adventurers"),
    111550: specialItemData(IC.useful, 1, "mixer_teb_bilbali", "teb_irrana", itemType.unit, 2, "Progressive teb_rng", False, False, "SouthernRealms Unit: Irranan Hillmen"),
    111551: specialItemData(IC.useful, 1, "mixer_teb_bilbali", "teb_conqui_royal_guard", itemType.unit, 3, "Progressive teb_rng", False, False, "SouthernRealms Unit: Royal Guard"),
    111552: specialItemData(IC.useful, 1, "mixer_teb_bilbali", "teb_conqui_lancers", itemType.unit, 1, "Progressive teb_cav", False, False, "SouthernRealms Unit: Lancers"),
    111553: specialItemData(IC.useful, 1, "mixer_teb_bilbali", "teb_conqui_riders", itemType.unit, 2, "Progressive teb_cav", False, False, "SouthernRealms Unit: Riders"),
    111554: specialItemData(IC.useful, 1, "mixer_teb_bilbali", "teb_noble_retinue", itemType.unit, 3, "Progressive teb_cav", False, False, "SouthernRealms Unit: Noble Retinue"),
    111555: specialItemData(IC.useful, 1, "mixer_teb_bilbali", "teb_kotrs", itemType.unit, 2, "Progressive teb_cav", False, False, "SouthernRealms Unit: Knights of the Righteous Spear"),
    111556: specialItemData(IC.useful, 1, "mixer_teb_bilbali", "teb_sisters", itemType.unit, 4, "Progressive teb_inf", False, False, "SouthernRealms Unit: Sisters of Fury"),

    111557: specialItemData(IC.useful, 1, "mixer_teb_catrazza", "teb_pikemen", itemType.unit, 2, "Progressive teb_inf", False, False, "SouthernRealms Unit: Pikemen"),
    111558: specialItemData(IC.useful, 1, "mixer_teb_catrazza", "teb_republican_guard", itemType.unit, 3, "Progressive teb_inf", False, False, "SouthernRealms Unit: Republican Guard"),
    111559: specialItemData(IC.useful, 1, "mixer_teb_catrazza", "teb_montante_greatswords", itemType.unit, 4, "Progressive teb_inf", False, False, "SouthernRealms Unit: Montante Swordsmen"),
    111560: specialItemData(IC.useful, 1, "mixer_teb_catrazza", "teb_pavisiers", itemType.unit, 2, "Progressive teb_rng", False, False, "SouthernRealms Unit: Pavise Crossbowmen"),
    111561: specialItemData(IC.useful, 1, "mixer_teb_catrazza", "teb_broken_lances", itemType.unit, 2, "Progressive teb_cav", False, False, "SouthernRealms Unit: Broken Lances"),
    111562: specialItemData(IC.useful, 1, "mixer_teb_catrazza", "teb_noble_retinue", itemType.unit, 3, "Progressive teb_cav", False, False, "SouthernRealms Unit: Noble Retinue"),
    111563: specialItemData(IC.useful, 1, "mixer_teb_catrazza", "teb_carabiniers", itemType.unit, 3, "Progressive teb_cav", False, False, "SouthernRealms Unit: Carabiniers"),
    111564: specialItemData(IC.useful, 1, "mixer_teb_catrazza", "teb_encarmine", itemType.unit, 3, "Progressive teb_cav", False, False, "SouthernRealms Unit: Knights Encarmine"),
    111565: specialItemData(IC.useful, 1, "mixer_teb_catrazza", "teb_kotrs", itemType.unit, 2, "Progressive teb_cav", False, False, "SouthernRealms Unit: Knights of the Righteous Spear"),
    111566: specialItemData(IC.useful, 1, "mixer_teb_catrazza", "teb_sisters", itemType.unit, 4, "Progressive teb_inf", False, False, "SouthernRealms Unit: Sisters of Fury"),
    111567: specialItemData(IC.useful, 1, "mixer_teb_catrazza", "teb_galloper", itemType.unit, 1, "Progressive teb_art", False, False, "SouthernRealms Unit: Galloper Guns"),

    111568: specialItemData(IC.useful, 1, "mixer_teb_colombo", "teb_conqui_adventurers", itemType.unit, 2, "Progressive teb_inf", False, False, "SouthernRealms Unit: Adventurers"),
    111569: specialItemData(IC.useful, 1, "mixer_teb_colombo", "teb_pikemen", itemType.unit, 2, "Progressive teb_inf", False, False, "SouthernRealms Unit: Pikemen"),
    111570: specialItemData(IC.useful, 1, "mixer_teb_colombo", "teb_montante_greatswords", itemType.unit, 4, "Progressive teb_inf", False, False, "SouthernRealms Unit: Montante Swordsmen"),
    111571: specialItemData(IC.useful, 1, "mixer_teb_new_world_colonies", "teb_swash", itemType.unit, 2, "Progressive teb_rng", False, False, "SouthernRealms Unit: Swashbucklers"),
    111572: specialItemData(IC.useful, 1, "mixer_teb_colombo", "teb_pavisiers", itemType.unit, 2, "Progressive teb_rng", False, False, "SouthernRealms Unit: Pavise Crossbowmen"),
    111573: specialItemData(IC.useful, 1, "mixer_teb_colombo", "teb_noble_retinue", itemType.unit, 3, "Progressive teb_cav", False, False, "SouthernRealms Unit: Noble Retinue"),
    111574: specialItemData(IC.useful, 1, "mixer_teb_colombo", "teb_conqui_lancers", itemType.unit, 1, "Progressive teb_cav", False, False, "SouthernRealms Unit: Lancers"),
    111575: specialItemData(IC.useful, 1, "mixer_teb_colombo", "teb_conqui_riders", itemType.unit, 2, "Progressive teb_cav", False, False, "SouthernRealms Unit: Riders"),
    111576: specialItemData(IC.useful, 1, "mixer_teb_colombo", "teb_galloper", itemType.unit, 1, "Progressive teb_art", False, False, "SouthernRealms Unit: Galloper Guns"),

    111579: specialItemData(IC.useful, 1, "mixer_teb_new_world_colonies", "teb_conqui_adventurers", itemType.unit, 2, "Progressive teb_inf", False, False, "SouthernRealms Unit: Adventurers"),
    111580: specialItemData(IC.useful, 1, "mixer_teb_new_world_colonies", "teb_pikemen", itemType.unit, 2, "Progressive teb_inf", False, False, "SouthernRealms Unit: Pikemen"),
    111581: specialItemData(IC.useful, 1, "mixer_teb_new_world_colonies", "teb_montante_greatswords", itemType.unit, 4, "Progressive teb_inf", False, False, "SouthernRealms Unit: Montante Swordsmen"),
    111582: specialItemData(IC.useful, 1, "mixer_teb_new_world_colonies", "teb_swash", itemType.unit, 2, "Progressive teb_rng", False, False, "SouthernRealms Unit: Swashbucklers"),
    111583: specialItemData(IC.useful, 1, "mixer_teb_new_world_colonies", "teb_pavisiers", itemType.unit, 2, "Progressive teb_rng", False, False, "SouthernRealms Unit: Pavise Crossbowmen"),
    111584: specialItemData(IC.useful, 1, "mixer_teb_new_world_colonies", "teb_noble_retinue", itemType.unit, 3, "Progressive teb_cav", False, False, "SouthernRealms Unit: Noble Retinue"),
    111585: specialItemData(IC.useful, 1, "mixer_teb_new_world_colonies", "teb_conqui_lancers", itemType.unit, 1, "Progressive teb_cav", False, False, "SouthernRealms Unit: Lancers"),
    111586: specialItemData(IC.useful, 1, "mixer_teb_new_world_colonies", "teb_conqui_riders", itemType.unit, 2, "Progressive teb_cav", False, False, "SouthernRealms Unit: Riders"),
    111587: specialItemData(IC.useful, 1, "mixer_teb_new_world_colonies", "teb_galloper", itemType.unit, 1, "Progressive teb_art", False, False, "SouthernRealms Unit: Galloper Guns"),

    111589: specialItemData(IC.useful, 1, "mixer_teb_border_princes", "teb_mil_rangers_1", itemType.building, 0, "Progressive teb_rangers", False, False, "SouthernRealms Building: Enforcers Camp"),
    111590: specialItemData(IC.useful, 1, "mixer_teb_border_princes", "teb_mil_rangers_2", itemType.building, 1, "Progressive teb_rangers", False, False, "SouthernRealms Building: Rangers Camp"),
    111591: specialItemData(IC.useful, 1, "mixer_teb_border_princes", "Progressive teb_rangers", itemType.building, 2, None, False, False, "Progressive SouthernRealms Building: Rangers"),
    111592: specialItemData(IC.useful, 1, "mixer_teb_gashnag", "teb_mil_rangers_1", itemType.building, 0, "Progressive teb_rangers", False, False, "SouthernRealms Building: Enforcers Camp"),
    111593: specialItemData(IC.useful, 1, "mixer_teb_gashnag", "teb_mil_rangers_2", itemType.building, 1, "Progressive teb_rangers", False, False, "SouthernRealms Building: Rangers Camp"),
    111594: specialItemData(IC.useful, 1, "mixer_teb_gashnag", "Progressive teb_rangers", itemType.building, 2, None, False, False, "Progressive SouthernRealms Building: Rangers"),

    111595: specialItemData(IC.useful, 1, "mixer_teb_border_princes", "teb_tech_borderlands", itemType.building, 2, "Progressive tech_teb_upper", False, False, "SouthernRealms Tech: Defiant Borderlands"),
    111596: specialItemData(IC.useful, 1, "mixer_teb_border_princes", "teb_tech_unsung", itemType.building, 2, "Progressive tech_teb_middle", False, False, "SouthernRealms Tech: Unsung Heroes"),
    111597: specialItemData(IC.useful, 1, "mixer_teb_border_princes", "teb_tech_classical_sub_BP", itemType.building, 2, "Progressive tech_teb_middle", False, False, "SouthernRealms Tech: Phalanxes"),
    111598: specialItemData(IC.useful, 1, "mixer_teb_border_princes", "teb_tech_dorf", itemType.building, 1, "Progressive tech_teb_lower", False, False, "SouthernRealms Tech: Dwarfen Allies"),
    111599: specialItemData(IC.useful, 1, "mixer_teb_border_princes", "teb_tech_myrmidia_sub_BP", itemType.building, 1, "Progressive tech_teb_lower", False, False, "SouthernRealms Tech: Importing the Orders"),
    111600: specialItemData(IC.useful, 1, "mixer_teb_border_princes", "teb_tech_rebuild", itemType.building, 2, "Progressive tech_teb_lower", False, False, "SouthernRealms Tech: Frontier No More"),

    111601: specialItemData(IC.useful, 1, "mixer_teb_estalia", "teb_tech_mercs_sub_estalia", itemType.building, 2, "Progressive tech_teb_upper", False, False, "SouthernRealms Tech: Irregulars"),
    111602: specialItemData(IC.useful, 1, "mixer_teb_estalia", "teb_tech_tercio", itemType.building, 2, "Progressive tech_teb_upper", False, False, "SouthernRealms Tech: Expeditionary Tercios"),
    111603: specialItemData(IC.useful, 1, "mixer_teb_estalia", "teb_tech_conquistadores", itemType.building, 2, "Progressive tech_teb_middle", False, False, "SouthernRealms Tech: Conquistador Lords"),
    111604: specialItemData(IC.useful, 1, "mixer_teb_estalia", "teb_tech_dorf", itemType.building, 1, "Progressive tech_teb_lower", False, False, "SouthernRealms Tech: Dwarfen Allies"),
    111605: specialItemData(IC.useful, 1, "mixer_teb_estalia", "teb_tech_inquisition", itemType.building, 2, "Progressive tech_teb_lower", False, False, "SouthernRealms Tech: Grand Estalian Inquisition"),

    111606: specialItemData(IC.useful, 1, "cr_teb_miragliano", "teb_tech_tilean", itemType.building, 2, "Progressive tech_teb_upper", False, False, "SouthernRealms Tech: Tilean Renown"),
    111607: specialItemData(IC.useful, 1, "cr_teb_miragliano", "teb_tech_supremacy", itemType.building, 2, "Progressive tech_teb_middle", False, False, "SouthernRealms Tech: Tilean Supremacy"),
    111608: specialItemData(IC.useful, 1, "cr_teb_miragliano", "teb_tech_dorf", itemType.building, 1, "Progressive tech_teb_lower", False, False, "SouthernRealms Tech: Dwarfen Allies"),
    111609: specialItemData(IC.useful, 1, "cr_teb_miragliano", "teb_tech_empire", itemType.building, 2, "Progressive tech_teb_lower", False, False, "SouthernRealms Tech: Dreams of Empire"),

    111610: specialItemData(IC.useful, 1, "mixer_teb_bilbali", "teb_tech_mercs_sub_estalia", itemType.building, 2, "Progressive tech_teb_upper", False, False, "SouthernRealms Tech: Irregulars"),
    111611: specialItemData(IC.useful, 1, "mixer_teb_bilbali", "teb_tech_tercio", itemType.building, 2, "Progressive tech_teb_upper", False, False, "SouthernRealms Tech: Expeditionary Tercios"),
    111612: specialItemData(IC.useful, 1, "mixer_teb_bilbali", "teb_tech_conquistadores", itemType.building, 2, "Progressive tech_teb_middle", False, False, "SouthernRealms Tech: Conquistador Lords"),
    111613: specialItemData(IC.useful, 1, "mixer_teb_bilbali", "teb_tech_dorf", itemType.building, 1, "Progressive tech_teb_lower", False, False, "SouthernRealms Tech: Dwarfen Allies"),
    111614: specialItemData(IC.useful, 1, "mixer_teb_bilbali", "teb_tech_inquisition", itemType.building, 2, "Progressive tech_teb_lower", False, False, "SouthernRealms Tech: Grand Estalian Inquisition"),

    111617: specialItemData(IC.useful, 1, "mixer_teb_catrazza", "teb_tech_tilean", itemType.building, 2, "Progressive tech_teb_upper", False, False, "SouthernRealms Tech: Tilean Renown"),
    111618: specialItemData(IC.useful, 1, "mixer_teb_catrazza", "teb_tech_supremacy", itemType.building, 2, "Progressive tech_teb_middle", False, False, "SouthernRealms Tech: Tilean Supremacy"),
    111619: specialItemData(IC.useful, 1, "mixer_teb_catrazza", "teb_tech_dorf", itemType.building, 1, "Progressive tech_teb_lower", False, False, "SouthernRealms Tech: Dwarfen Allies"),
    111620: specialItemData(IC.useful, 1, "mixer_teb_catrazza", "teb_tech_empire", itemType.building, 2, "Progressive tech_teb_lower", False, False, "SouthernRealms Tech: Dreams of Empire"),

    111621: specialItemData(IC.useful, 1, "mixer_teb_colombo", "teb_tech_bestofworst", itemType.building, 2, "Progressive tech_teb_upper", False, False, "SouthernRealms Tech: The Best of the Worst"),
    111622: specialItemData(IC.useful, 1, "mixer_teb_colombo", "teb_tech_conquistadores_col", itemType.building, 2, "Progressive tech_teb_middle", False, False, "SouthernRealms Tech: Fear the Reaver"),
    111623: specialItemData(IC.useful, 1, "mixer_teb_colombo", "teb_tech_oldones", itemType.building, 1, "Progressive tech_teb_lower", False, False, "SouthernRealms Tech: Legacy of the Old Ones"),
    111624: specialItemData(IC.useful, 1, "mixer_teb_colombo", "teb_tech_bravenewworld", itemType.building, 2, "Progressive tech_teb_lower", False, False, "SouthernRealms Tech: Brave New World"),
    111625: specialItemData(IC.useful, 1, "mixer_teb_colombo", "teb_tech_ROR_outland", itemType.building, 1, "Progressive tech_teb_renown", False, False, "SouthernRealms Tech: Renown: The Outlanders"),
    111626: specialItemData(IC.useful, 1, "mixer_teb_colombo", "teb_tech_ROR_pro", itemType.building, 1, "Progressive tech_teb_renown", False, False, "SouthernRealms Tech: Renown: The Professionals"),
    111627: specialItemData(IC.useful, 1, "mixer_teb_colombo", "teb_tech_ROR_brass", itemType.building, 1, "Progressive tech_teb_renown", False, False, "SouthernRealms Tech: Renown: The Brass of Tilea"),
    111628: specialItemData(IC.useful, 1, "mixer_teb_colombo", "Progressive tech_teb_renown", itemType.building, 1, None, False, False, "Progressive SouthernRealms Tech: Renown: Renown"),

    111629: specialItemData(IC.useful, 1, "mixer_teb_new_world_colonies", "teb_tech_bestofworst", itemType.building, 2, "Progressive tech_teb_upper", False, False, "SouthernRealms Tech: The Best of the Worst"),
    111630: specialItemData(IC.useful, 1, "mixer_teb_new_world_colonies", "teb_tech_conquistadores_col", itemType.building, 2, "Progressive tech_teb_middle", False, False, "SouthernRealms Tech: Fear the Reaver"),
    111631: specialItemData(IC.useful, 1, "mixer_teb_new_world_colonies", "teb_tech_oldones", itemType.building, 1, "Progressive tech_teb_lower", False, False, "SouthernRealms Tech: Legacy of the Old Ones"),
    111632: specialItemData(IC.useful, 1, "mixer_teb_new_world_colonies", "teb_tech_bravenewworld", itemType.building, 2, "Progressive tech_teb_lower", False, False, "SouthernRealms Tech: Brave New World"),
    111633: specialItemData(IC.useful, 1, "mixer_teb_new_world_colonies", "teb_tech_ROR_outland", itemType.building, 1, "Progressive tech_teb_renown", False, False, "SouthernRealms Tech: Renown: The Outlanders"),
    111634: specialItemData(IC.useful, 1, "mixer_teb_new_world_colonies", "teb_tech_ROR_pro", itemType.building, 1, "Progressive tech_teb_renown", False, False, "SouthernRealms Tech: Renown: The Professionals"),
    111635: specialItemData(IC.useful, 1, "mixer_teb_new_world_colonies", "teb_tech_ROR_brass", itemType.building, 1, "Progressive tech_teb_renown", False, False, "SouthernRealms Tech: Renown: The Brass of Tilea"),
    111636: specialItemData(IC.useful, 1, "mixer_teb_new_world_colonies", "Progressive tech_teb_renown", itemType.building, 1, None, False, False, "Progressive SouthernRealms Tech: Renown: Renown"),
}
"""
teb_sartosan_pirates
teb_galloper_limbered
"""

"""
wh2_dlc11_special_settlement_galleons_graveyard_other
wh2_dlc12_special_bordeleaux_manann_shrine
wh2_dlc14_special_copher_port
wh2_dlc14_special_dragon_isle_port
wh2_dlc14_special_pigbarter_human
wh2_main_EMPIRE_roads
wh2_main_HUMAN_resource_gemstones
wh2_main_emp_defence_norsca
wh2_main_emp_resource_medicine
wh2_main_emp_resource_obsidian
wh2_main_emp_resource_spices
wh2_main_foreign_slot_discovery_emp
wh2_main_special_altdorf_imperial_palace
wh2_main_special_chamber_of_visions
wh2_main_special_clar_karond_lairs_other
wh2_main_special_fortress_gate_eagle_untainted
wh2_main_special_fortress_gate_griffon_untainted
wh2_main_special_fortress_gate_phoenix_untainted
wh2_main_special_fortress_gate_unicorn_untainted
wh2_main_special_ghrond_convent_of_sorcery_emp
wh2_main_special_glittering_tower
wh2_main_special_golden_tower_of_the_gods_other
wh2_main_special_hag_graef_mines
wh2_main_special_hexoatl_stellar_pyramids_other
wh2_main_special_itza_emerald_pools
wh2_main_special_lothern_port_other
wh2_main_special_quintex
wh2_main_special_salzenmund_laurelorn_human
wh2_main_special_settlement_sartosa_emp
wh2_main_special_shrine_of_asuryan_other
wh2_main_special_shrine_of_khaine_other
wh2_main_special_tower_of_hoeth_emp
wh2_main_special_ziggurat_of_dawn_beacon
wh2_main_wef_oak_of_ages_occupied
wh2_twa03_special_ogham_stones
wh3_main_emp_resource_ivory
wh3_main_special_settlement_bastion_other
wh3_main_special_settlement_fort_other
wh3_main_special_standing_stones
wh3_main_special_the_great_desert_other
wh_main_EMPIRE_settlement_major
wh_main_EMPIRE_settlement_minor
wh_main_HUMAN_resource_dyes
wh_main_HUMAN_resource_furs
wh_main_HUMAN_resource_marble
wh_main_HUMAN_resource_pottery
wh_main_HUMAN_resource_salt
wh_main_HUMAN_resource_wine
wh_main_TEB_port
wh_main_bretonnia_legendary_bordeleaux
wh_main_sch_special_moot_cauldron
wh_main_special_blazing_sun_chapterhouse
wh_main_special_bokha_palace
wh_main_special_bordeleaux_vineyards
wh_main_special_college_of_magic
wh_main_special_erengrad_port
wh_main_special_great_temple_of_ulric
wh_main_special_knights_panther_chapterhouse
wh_main_special_marienburg_port
wh_main_special_nuln_gunnery_school
wh_main_special_settlement_altdorf
wh_main_special_settlement_castle_drakenhof_empire
wh_main_special_settlement_couronne_empire
wh_main_special_settlement_miragliano
wh_main_special_tournament_grounds
wh_main_special_ubersreik_inn
teb_mercs
teb_art
teb_homeland
teb_ritual_exploit
teb_ritual_trade
teb_tylos
teb_miragliano_channels
teb_smith
teb_lothern_good
teb_lothern_bad
wh2_main_special_pyramid_of_nagash_other
wh2_main_special_peg_street_pawnshop
wh2_main_special_smithys_tavern
teb_luccini_acropolis
teb_tobaro_deep
teb_terraform_jungle
teb_terraform_mountain
teb_resource_iron
teb_mil_city
teb_mil_mercs
teb_mil_rangers
teb_mil_cannons
teb_eco_cloth
teb_eco_farm
teb_eco_order
teb_worship_shallya
teb_worship_shallya_couronne
teb_worship_myrmidia
teb_worship_myrmidia_magritta
teb_mil_badmercs
teb_eco_stocks
teb_resource_animals
teb_resource_gold
teb_resource_pastures
teb_resource_timber
teb_garrison_big
teb_garrison_small
teb_tylos_settlement
teb_tylos_settlement
teb_allied_outpost
teb_morgheim_gashnag
teb_morgheim_gashnag_bad
wh3_main_special_the_great_embassy
wh3_dlc23_special_fortress_of_dawn_dawns_harbour
wh3_dlc23_special_great_temple_of_hashut_other
wh3_dlc24_special_fu_chow_port
wh3_dlc24_special_celestial_palace_other
cr_special_nerja_catacombs
cr_special_heideck_ancient_battle_site
teb_luccini_acropolis_major
teb_montecastello_special
teb_norsca_exploit_furs
teb_norsca_exploit_obsi
cr_special_roc_outpost
cr_special_kraka_ravnvake_port
cr_special_rocket_test_site
cr_special_vaults_of_plenty_granary
teb_special_sentinels
teb_pavona_lucy
teb_special_windmills_lupio
"""