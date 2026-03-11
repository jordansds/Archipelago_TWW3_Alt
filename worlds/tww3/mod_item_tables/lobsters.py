from BaseClasses import ItemClassification as IC
from worlds.tww3.itemTypes import itemType, itemData, specialItemData

# @formatter:off

units: dict[int, itemData] = {
    114001: itemData(IC.useful, 1, "CN_crab_levy_0", itemType.unit, 1, "Progressive lob_inf", "Lobster Unit: Crab Levy"),
    114002: itemData(IC.useful, 1, "CN_crab_warriors_0", itemType.unit, 1, "Progressive lob_inf", "Lobster Unit: Crab Warriors"),
    114003: itemData(IC.useful, 1, "CN_crab_warriors_1", itemType.unit, 1, "Progressive lob_inf", "Lobster Unit: Crab Warriors (Spears)"),
    114004: itemData(IC.useful, 1, "CN_lobster_warriors_0", itemType.unit, 1, "Progressive lob_inf", "Lobster Unit: Lobster Warriors"),
    114005: itemData(IC.useful, 1, "CN_lobster_warriors_1", itemType.unit, 1, "Progressive lob_inf", "Lobster Unit: Lobster Warriors (Duel Weapons)"),
    114006: itemData(IC.useful, 1, "CN_lobster_warriors_2", itemType.unit, 1, "Progressive lob_inf", "Lobster Unit: Lobster Warriors (Shields)"),
    114007: itemData(IC.useful, 1, "CN_crab_rangers", itemType.unit, 2, "Progressive lob_inf", "Lobster Unit: Crab Rangers"),
    114008: itemData(IC.useful, 1, "wh_main_chs_mon_chaos_spawn", itemType.unit, 2, "Progressive lob_inf", "Lobster Unit: Chaos Spawn"),
    112009: itemData(IC.useful, 1, "CN_monstrous_crabs_0", itemType.unit, 2, "Progressive lob_inf", "Lobster Unit: Hardshell Colossi"),
    112010: itemData(IC.useful, 1, "CN_monstrous_crabs_1", itemType.unit, 3, "Progressive lob_inf", "Lobster Unit: Hardshell Bruisers"),
    114011: itemData(IC.useful, 1, "CN_lobster_champions_0", itemType.unit, 3, "Progressive lob_inf", "Lobster Unit: Lobster Champions"),
    114012: itemData(IC.useful, 1, "CN_lobster_champions_1", itemType.unit, 3, "Progressive lob_inf", "Lobster Unit: Lobster Champions (Spears)"),
    114013: itemData(IC.useful, 1, "CN_lobster_juggernauts", itemType.unit, 4, "Progressive lob_inf", "Lobster Unit: Lobster Juggernauts"),
    114014: itemData(IC.useful, 1, "CN_lobster_hellforged_reaver", itemType.unit, 4, "Progressive lob_inf", "Lobster Unit: Hellforged Reavers"),

    114015: itemData(IC.useful, 1, "CN_crab_levy_1", itemType.unit, 1, "Progressive lob_rng", "Lobster Unit: Crab Levy Slingers"),
    114016: itemData(IC.useful, 1, "CN_crab_bomber", itemType.unit, 1, "Progressive lob_rng", "Lobster Unit: Lobster Bombers"),
    114017: itemData(IC.useful, 1, "CN_crab_gunner", itemType.unit, 1, "Progressive lob_rng", "Lobster Unit: Lobster Gunners"),
    114018: itemData(IC.useful, 1, "CN_crab_bomber_armoured", itemType.unit, 2, "Progressive lob_rng", "Lobster Unit: Lobster Grenadiers"),
    114019: itemData(IC.useful, 1, "CN_crab_warriors_2", itemType.unit, 2, "Progressive lob_rng", "Lobster Unit: Crab Warriors (Javelins)"),
    114020: itemData(IC.useful, 1, "CN_crab_slinger", itemType.unit, 3, "Progressive lob_rng", "Lobster Unit: Lobster Slingers"),
    114021: itemData(IC.useful, 1, "CN_lobster_hellforged_destroyer", itemType.unit, 4, "Progressive lob_rng", "Lobster Unit: Hellforged Destroyers"),

    112022: itemData(IC.useful, 1, "CN_monstrous_crabs_3", itemType.unit, 1, "Progressive lob_art", "Lobster Unit: Hardshell Cannonbacks (Mortars)"),
    112023: itemData(IC.useful, 1, "CN_monstrous_crabs_2", itemType.unit, 1, "Progressive lob_art", "Lobster Unit: Hardshell Cannonbacks"),

    114024: itemData(IC.useful, 1, 'wh3_main_dae_inf_chaos_furies_0', itemType.unit, 1, 'Progressive lob_bst', 'Lobster Unit: Chaos Furies'),
    114025: itemData(IC.useful, 1, 'wh_main_chs_mon_chaos_warhounds_0', itemType.unit, 1, 'Progressive lob_bst', 'Lobster Unit: Chaos Warhounds'),
    114026: itemData(IC.useful, 1, 'wh_main_chs_mon_chaos_warhounds_1', itemType.unit, 1, 'Progressive lob_bst', 'Lobster Unit: Chaos Warhounds (Poison)'),
    114027: itemData(IC.useful, 1, 'wh_dlc06_chs_feral_manticore', itemType.unit, 2, 'Progressive lob_bst', 'Lobster Unit: Chaos Feral Manticore'),

    114028: itemData(IC.useful, 1, 'CN_cha_lobster_hero', itemType.unit, 1, 'Progressive lob_hro', 'Lobster Unit: Lobster Battlemaster'),
}

buildings: dict[int, itemData] = {
    114400: itemData(IC.useful, 1, "cn_lobster_settlement_1", itemType.building, 0, "Progressive lob_settlement_major", "Lobster Building: Lobster Outpost"),
    114401: itemData(IC.useful, 1, "cn_lobster_settlement_2", itemType.building, 1, "Progressive lob_settlement_major", "Lobster Building: Lobster Hold"),
    114402: itemData(IC.useful, 1, "cn_lobster_settlement_3", itemType.building, 2, "Progressive lob_settlement_major", "Lobster Building: Lobster Rampart"),
    114403: itemData(IC.useful, 1, "cn_lobster_settlement_4", itemType.building, 3, "Progressive lob_settlement_major", "Lobster Building: Lobster Keep"),
    114404: itemData(IC.useful, 1, "cn_lobster_settlement_5", itemType.building, 4, "Progressive lob_settlement_major", "Lobster Building: Lobster Fortress"),
    114405: itemData(IC.useful, 1, "cn_lobster_gold_1", itemType.building, 0, "Progressive lob_gold", "Lobster Building: Slave Cage"),
    114406: itemData(IC.useful, 1, "cn_lobster_gold_2", itemType.building, 1, "Progressive lob_gold", "Lobster Building: Slave Pits"),
    114407: itemData(IC.useful, 1, "cn_lobster_gold_3", itemType.building, 2, "Progressive lob_gold", "Lobster Building: Slave Pens"),
    114408: itemData(IC.useful, 1, "cn_lobster_income_1", itemType.building, 0, "Progressive lob_income", "Lobster Building: Overseers"),
    114409: itemData(IC.useful, 1, "cn_lobster_income_2", itemType.building, 1, "Progressive lob_income", "Lobster Building: Malicious Overseers"),
    114410: itemData(IC.useful, 1, "cn_lobster_income_3", itemType.building, 2, "Progressive lob_income", "Lobster Building: Brutish Overseers"),
    114411: itemData(IC.useful, 1, "cn_lobster_income_4", itemType.building, 3, "Progressive lob_income", "Lobster Building: Merciless Overseers"),
    114412: itemData(IC.useful, 1, "cn_lobster_income_5", itemType.building, 4, "Progressive lob_income", "Lobster Building: Hellish Overseers"),
    114413: itemData(IC.useful, 1, "cn_lobster_loot_1", itemType.building, 0, "Progressive lob_loot", "Lobster Building: Ruinous Altar"),
    114414: itemData(IC.useful, 1, "cn_lobster_loot_2", itemType.building, 1, "Progressive lob_loot", "Lobster Building: Ruinous Monument"),
    114415: itemData(IC.useful, 1, "cn_lobster_loot_3", itemType.building, 2, "Progressive lob_loot", "Lobster Building: Ruinous Chapel"),
    114416: itemData(IC.useful, 1, "cn_lobster_lords", itemType.building, 0, "Progressive lob_lords", "Lobster Building: Idol of Destruction"),
    114417: itemData(IC.useful, 1, "cn_lobster_warriors_1", itemType.building, 0, "Progressive lob_warriors", "Lobster Building: Warrior's Assembly"),
    114418: itemData(IC.useful, 1, "cn_lobster_warriors_2", itemType.building, 1, "Progressive lob_warriors", "Lobster Building: Hall of Warriors"),
    114419: itemData(IC.useful, 1, "cn_lobster_warriors_3", itemType.building, 2, "Progressive lob_warriors", "Lobster Building: Hall of Champions"),
    114420: itemData(IC.useful, 1, "cn_lobster_warriors_4", itemType.building, 3, "Progressive lob_warriors", "Lobster Building: The Great Hall"),
    114421: itemData(IC.useful, 1, "cn_lobster_crabs_1", itemType.building, 0, "Progressive lob_crabs", "Lobster Building: Torture Chambers"),
    114422: itemData(IC.useful, 1, "cn_lobster_crabs_2", itemType.building, 1, "Progressive lob_crabs", "Lobster Building: Den of Malice"),
    114423: itemData(IC.useful, 1, "cn_lobster_crabs_3", itemType.building, 2, "Progressive lob_crabs", "Lobster Building: Tower of Despair"),
    114424: itemData(IC.useful, 1, "cn_lobster_monsters_1", itemType.building, 0, "Progressive lob_monsters", "Lobster Building: Corrupted Cavern"),
    114425: itemData(IC.useful, 1, "cn_lobster_monsters_2", itemType.building, 1, "Progressive lob_monsters", "Lobster Building: Chaos Pits"),
    114426: itemData(IC.useful, 1, "cn_lobster_monsters_3", itemType.building, 2, "Progressive lob_monsters", "Lobster Building: Chaotic Bestiary"),
    114427: itemData(IC.useful, 1, "cn_lobster_monsters_4", itemType.building, 3, "Progressive lob_monsters", "Lobster Building: Ruinous Bestiary"),
    114428: itemData(IC.useful, 1, "cn_lobster_missiles_1", itemType.building, 0, "Progressive lob_missiles", "Lobster Building: Forbidden Workshop"),
    114429: itemData(IC.useful, 1, "cn_lobster_missiles_2", itemType.building, 1, "Progressive lob_missiles", "Lobster Building: Dark Foundry"),
    114430: itemData(IC.useful, 1, "cn_lobster_missiles_3", itemType.building, 2, "Progressive lob_missiles", "Lobster Building: Hellforge"),
    114431: itemData(IC.useful, 1, "cn_lobster_missiles_4", itemType.building, 3, "Progressive lob_missiles", "Lobster Building: Infernal Foundry"),
    114432: itemData(IC.useful, 1, "cn_lobster_hardshell_1", itemType.building, 0, "Progressive lob_hardshell", "Lobster Building: Hardshell Mercenary Post"),
    114433: itemData(IC.useful, 1, "cn_lobster_hardshell_2", itemType.building, 1, "Progressive lob_hardshell", "Lobster Building: Hardshell Mercenary Camp"),
    114434: itemData(IC.useful, 1, "cn_lobster_hardshell_3", itemType.building, 2, "Progressive lob_hardshell", "Lobster Building: Hardshell Colosseum"),
    114435: itemData(IC.useful, 1, "cn_lobster_resources_1", itemType.building, 0, "Progressive lob_resources", "Lobster Building: Labour Camp"),
    114436: itemData(IC.useful, 1, "cn_lobster_resources_2", itemType.building, 1, "Progressive lob_resources", "Lobster Building: Grim Labour Camp"),
    114437: itemData(IC.useful, 1, "cn_lobster_resources_3", itemType.building, 2, "Progressive lob_resources", "Lobster Building: Infernal Labour Camp"),
    114438: itemData(IC.useful, 1, "cn_lobster_port_1", itemType.building, 0, "Progressive lob_port", "Lobster Building: Lobster Jetty"),
    114439: itemData(IC.useful, 1, "cn_lobster_port_2", itemType.building, 1, "Progressive lob_port", "Lobster Building: Lobster Port"),
    114440: itemData(IC.useful, 1, "cn_lobster_port_3", itemType.building, 2, "Progressive lob_port", "Lobster Building: Lobster Harbour"),
}

techs: dict[int, itemData] = {
    114800: itemData(IC.useful, 1, "cn_lobster_tech_main_1", itemType.tech, 1, "Progressive tech_lob_main", "Lobster Tech: Ruinous Initiation"),
    114801: itemData(IC.useful, 1, "cn_lobster_tech_main_1_1", itemType.tech, 2, "Progressive tech_lob_main", "Lobster Tech: Sharpened Axes"),
    114802: itemData(IC.useful, 1, "cn_lobster_tech_main_1_2", itemType.tech, 2, "Progressive tech_lob_main", "Lobster Tech: Tempered Steel"),
    114803: itemData(IC.useful, 1, "cn_lobster_tech_main_1_3", itemType.tech, 2, "Progressive tech_lob_main", "Lobster Tech: Profane Claws"),
    114804: itemData(IC.useful, 1, "cn_lobster_tech_main_1_4", itemType.tech, 2, "Progressive tech_lob_main", "Lobster Tech: Driven by Fear"),
    114805: itemData(IC.useful, 1, "cn_lobster_tech_main_1_5", itemType.tech, 2, "Progressive tech_lob_main", "Lobster Tech: Heretical Loyalty"),
    114806: itemData(IC.useful, 1, "cn_lobster_tech_main_2", itemType.tech, 2, "Progressive tech_lob_main", "Lobster Tech: Ruinous Dominion"),
    114807: itemData(IC.useful, 1, "cn_lobster_tech_main_2_1", itemType.tech, 3, "Progressive tech_lob_main", "Lobster Tech: Urge to Kill"),
    114808: itemData(IC.useful, 1, "cn_lobster_tech_main_2_2", itemType.tech, 3, "Progressive tech_lob_main", "Lobster Tech: World Eaters"),
    114809: itemData(IC.useful, 1, "cn_lobster_tech_main_2_3", itemType.tech, 3, "Progressive tech_lob_main", "Lobster Tech: Goaded Fury"),
    114810: itemData(IC.useful, 1, "cn_lobster_tech_main_2_4", itemType.tech, 3, "Progressive tech_lob_main", "Lobster Tech: Chaotic Mutations"),
    114811: itemData(IC.useful, 1, "cn_lobster_tech_main_2_5", itemType.tech, 3, "Progressive tech_lob_main", "Lobster Tech: Cursed Armaments"),
    114812: itemData(IC.useful, 1, "cn_lobster_tech_main_3", itemType.tech, 3, "Progressive tech_lob_main", "Lobster Tech: Ruinous Ascension"),
    114813: itemData(IC.useful, 1, "cn_lobster_tech_main_3_1", itemType.tech, 4, "Progressive tech_lob_main", "Lobster Tech: Resolute Advance"),
    114814: itemData(IC.useful, 1, "cn_lobster_tech_main_3_2", itemType.tech, 4, "Progressive tech_lob_main", "Lobster Tech: Iron Will"),
    114815: itemData(IC.useful, 1, "cn_lobster_tech_main_3_3", itemType.tech, 4, "Progressive tech_lob_main", "Lobster Tech: Mindless Rage"),
    114816: itemData(IC.useful, 1, "cn_lobster_tech_main_3_4", itemType.tech, 4, "Progressive tech_lob_main", "Lobster Tech: Infernal Munitions"),
    114817: itemData(IC.useful, 1, "cn_lobster_tech_main_3_5", itemType.tech, 4, "Progressive tech_lob_main", "Lobster Tech: Higher Standards"),
    114818: itemData(IC.useful, 1, "cn_lobster_tech_main_4", itemType.tech, 4, "Progressive tech_lob_main", "Lobster Tech: Ruinous Mastery"),
    114819: itemData(IC.useful, 1, "cn_lobster_tech_main_4_1", itemType.tech, 5, "Progressive tech_lob_main", "Lobster Tech: Deadly Proficiency"),
    114820: itemData(IC.useful, 1, "cn_lobster_tech_main_4_2", itemType.tech, 5, "Progressive tech_lob_main", "Lobster Tech: Dark Blessings"),
    114821: itemData(IC.useful, 1, "cn_lobster_tech_main_4_3", itemType.tech, 5, "Progressive tech_lob_main", "Lobster Tech: Bestial Charge"),
    114822: itemData(IC.useful, 1, "cn_lobster_tech_main_4_4", itemType.tech, 5, "Progressive tech_lob_main", "Lobster Tech: Paragons of Chaos"),
    114823: itemData(IC.useful, 1, "cn_lobster_tech_main_4_5", itemType.tech, 5, "Progressive tech_lob_main", "Lobster Tech: Fall to Chaos"),

    114824: itemData(IC.useful, 1, "cn_lobster_tech_offerings_0", itemType.tech, 1, "Progressive tech_lob_offerings", "Lobster Tech: Ruinous Offerings"),
    114825: itemData(IC.useful, 1, "cn_lobster_tech_offerings_1", itemType.tech, 1, "Progressive tech_lob_offerings", "Lobster Tech: Offerings to Khorne"),
    114826: itemData(IC.useful, 1, "cn_lobster_tech_offerings_2", itemType.tech, 1, "Progressive tech_lob_offerings", "Lobster Tech: Offerings to Nurgle"),
    114827: itemData(IC.useful, 1, "cn_lobster_tech_offerings_3", itemType.tech, 1, "Progressive tech_lob_offerings", "Lobster Tech: Offerings to the Great Horned Rat"),
    114828: itemData(IC.useful, 1, "cn_lobster_tech_offerings_4", itemType.tech, 1, "Progressive tech_lob_offerings", "Lobster Tech: Offerings to Tzeentch"),
    114829: itemData(IC.useful, 1, "cn_lobster_tech_offerings_5", itemType.tech, 1, "Progressive tech_lob_offerings", "Lobster Tech: Offerings to Slaanesh"),
    114830: itemData(IC.useful, 1, "cn_lobster_tech_offerings_6", itemType.tech, 1, "Progressive tech_lob_offerings", "Lobster Tech: Offerings to Hashut"),

    114831: itemData(IC.useful, 1, "cn_lobster_tech_economy_0", itemType.tech, 1, "Progressive tech_lob_economy", "Lobster Tech: Dark Authority"),
    114832: itemData(IC.useful, 1, "cn_lobster_tech_economy_1_1", itemType.tech, 2, "Progressive tech_lob_economy", "Lobster Tech: Raiding Parties"),
    114833: itemData(IC.useful, 1, "cn_lobster_tech_economy_1_2", itemType.tech, 3, "Progressive tech_lob_economy", "Lobster Tech: Loot mules"),
    114834: itemData(IC.useful, 1, "cn_lobster_tech_economy_1_3", itemType.tech, 4, "Progressive tech_lob_economy", "Lobster Tech: Call to Ruin"),
    114835: itemData(IC.useful, 1, "cn_lobster_tech_economy_2_1", itemType.tech, 2, "Progressive tech_lob_economy", "Lobster Tech: Whipmasters"),
    114836: itemData(IC.useful, 1, "cn_lobster_tech_economy_2_2", itemType.tech, 3, "Progressive tech_lob_economy", "Lobster Tech: Forbidden Knowledge"),
    114837: itemData(IC.useful, 1, "cn_lobster_tech_economy_2_3", itemType.tech, 4, "Progressive tech_lob_economy", "Lobster Tech: Supply Chain"),
    114838: itemData(IC.useful, 1, "cn_lobster_tech_economy_3_1", itemType.tech, 2, "Progressive tech_lob_economy", "Lobster Tech: Ruinous Monuments"),
    114839: itemData(IC.useful, 1, "cn_lobster_tech_economy_3_2", itemType.tech, 3, "Progressive tech_lob_economy", "Lobster Tech: Unholy Rituals"),
    114840: itemData(IC.useful, 1, "cn_lobster_tech_economy_3_3", itemType.tech, 4, "Progressive tech_lob_economy", "Lobster Tech: Sustained by Carnage"),
}

progUnits: dict[int, itemData] = {
    115200: itemData(IC.useful, 1, "Progressive lob_inf", itemType.unit, 4, None, "Progressive Lobster Unit: Infantry"),
    115201: itemData(IC.useful, 1, "Progressive lob_rng", itemType.unit, 4, None, "Progressive Lobster Unit: Ranged"),
    115203: itemData(IC.useful, 1, "Progressive lob_art", itemType.unit, 1, None, "Progressive Lobster Unit: Artillery"),
    115205: itemData(IC.useful, 1, "Progressive lob_bst", itemType.unit, 2, None, "Progressive Lobster Unit: Beast"),
    115206: itemData(IC.useful, 1, "Progressive lob_hro", itemType.unit, 1, None, "Progressive Lobster Unit: Hero"),
}

progBuildings: dict[int, itemData] = {
    115300: itemData(IC.useful, 1, "cn_lobster_settlement_5", itemType.building, 4, "Progressive lob_settlement_major", "Lobster Building: Lobster Fortress"),
    115301: itemData(IC.useful, 1, "cn_lobster_gold_3", itemType.building, 2, "Progressive lob_gold", "Lobster Building: Slave Pens"),
    115302: itemData(IC.useful, 1, "cn_lobster_income_5", itemType.building, 4, "Progressive lob_income", "Lobster Building: Hellish Overseers"),
    115303: itemData(IC.useful, 1, "cn_lobster_loot_3", itemType.building, 2, "Progressive lob_loot", "Lobster Building: Ruinous Chapel"),
    115304: itemData(IC.useful, 1, "cn_lobster_lords", itemType.building, 0, "Progressive lob_lords", "Lobster Building: Idol of Destruction"),
    115305: itemData(IC.useful, 1, "cn_lobster_warriors_4", itemType.building, 3, "Progressive lob_warriors", "Lobster Building: The Great Hall"),
    115306: itemData(IC.useful, 1, "cn_lobster_crabs_3", itemType.building, 2, "Progressive lob_crabs", "Lobster Building: Tower of Despair"),
    115307: itemData(IC.useful, 1, "cn_lobster_monsters_4", itemType.building, 3, "Progressive lob_monsters", "Lobster Building: Ruinous Bestiary"),
    115308: itemData(IC.useful, 1, "cn_lobster_missiles_4", itemType.building, 3, "Progressive lob_missiles", "Lobster Building: Infernal Foundry"),
    115309: itemData(IC.useful, 1, "cn_lobster_hardshell_3", itemType.building, 2, "Progressive lob_hardshell", "Lobster Building: Hardshell Colosseum"),
    115310: itemData(IC.useful, 1, "cn_lobster_resources_3", itemType.building, 2, "Progressive lob_resources", "Lobster Building: Infernal Labour Camp"),
    115311: itemData(IC.useful, 1, "cn_lobster_port_3", itemType.building, 2, "Progressive lob_port", "Lobster Building: Lobster Harbour"),
}

progTechs: dict[int, itemData] = {
    115400: itemData(IC.useful, 1, "Progressive tech_lob_main", itemType.tech, 5, None, "Lobster Tech: Ruinous Initiation"),
    114401: itemData(IC.useful, 1, "Progressive tech_lob_offerings", itemType.tech, 1, None, "Lobster Tech: Ruinous Initiation"),
    114402: itemData(IC.useful, 1, "Progressive tech_lob_economy", itemType.tech, 4, None, "Lobster Tech: Ruinous Initiation"),
}

special: dict[int, specialItemData] = {

}
