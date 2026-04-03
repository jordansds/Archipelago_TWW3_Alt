from BaseClasses import ItemClassification as IC
from worlds.tww3.dataStructs import itemType, itemData
from . import warriorsOfChaos

# @formatter:off
units: dict[int, itemData] = warriorsOfChaos.baseUnits
units.update(warriorsOfChaos.khorneUnits)
units.update({
    58000: itemData(IC.useful, 1, 'wh3_dlc26_kho_inf_khorngors', itemType.unit, 3, 'Progressive chs_inf', 'Chaos Unit: Khorngors'),
    58001: itemData(IC.useful, 1, 'wh3_main_kho_inf_bloodletters_1', itemType.unit, 3, 'Progressive chs_inf', 'Chaos Unit: Exalted Bloodletters of Khorne'),
    58002: itemData(IC.useful, 1, 'wh3_dlc26_kho_inf_skullreapers', itemType.unit, 3, 'Progressive chs_inf', 'Chaos Unit: Skullreapers'),
    58003: itemData(IC.useful, 1, 'wh3_dlc26_kho_inf_wrathmongers', itemType.unit, 4, 'Progressive chs_inf', 'Chaos Unit: Wrathmongers'),

    58004: itemData(IC.useful, 1, 'wh3_dlc20_chs_cha_exalted_hero_mkho', itemType.unit, 1, 'Progressive chs_hro', 'Chaos Unit: Exalted Hero of Khorne'),

    58005: itemData(IC.useful, 1, 'wh3_twa06_kho_inf_bloodletters_ror_0', itemType.unit, 3, 'Progressive chs_inf', 'Chaos Unit: Hellforged Host (Exalted Bloodletters of Khorne)'),
    58006: itemData(IC.useful, 1, 'wh_pro04_nor_inf_marauder_berserkers_ror_0', itemType.unit, 1, 'Progressive chs_inf', 'Chaos Unit: Brutes of the Hound (Marauder Berserkers)'),
    58007: itemData(IC.useful, 1, 'wh3_dlc26_kho_inf_wrathmongers_ror', itemType.unit, 4, 'Progressive chs_inf', 'Chaos Unit: Bloodwake Berserkers (Wrathmongers)'),
    58008: itemData(IC.useful, 1, 'wh3_twa07_kho_cav_bloodcrushers_ror_0', itemType.unit, 3, 'Progressive chs_cav', "Chaos Unit: Heralds of Khorne's Fury (Bloodcrushers of Khorne)"),
    58009: itemData(IC.useful, 1, 'wh2_dlc17_bst_mon_ghorgon_ror_0', itemType.unit, 5, 'Progressive chs_bst', 'Chaos Unit: The Bloodbrute Behemoth (Ghorgon)')
})

buildings: dict[int, itemData] = warriorsOfChaos.buildings

techs: dict[int, itemData] = {
    58800: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_marks_khorne', itemType.tech, 1, 'Progressive tech_chs_kho_khorne', 'Chaos Khorne Tech: Searing Branding Iron'),
    58801: itemData(IC.useful, 1, 'wh3_dlc20_chs_kho_shared_gift_upgrade_authority', itemType.tech, 2, 'Progressive tech_chs_kho_khorne', 'Chaos Khorne Tech: Sacrificial Altar'),
    58802: itemData(IC.useful, 1, 'wh3_dlc20_chs_kho_shared_gift_upgrade_corruption', itemType.tech, 3, 'Progressive tech_chs_kho_khorne', 'Chaos Khorne Tech: Bloodied Blade'),
    58803: itemData(IC.useful, 1, 'wh3_dlc20_chs_kho_valkia_buildings', itemType.tech, 4, 'Progressive tech_chs_kho_khorne', 'Chaos Khorne Tech: Builder of Glory'),
    58804: itemData(IC.useful, 1, 'wh3_dlc20_chs_kho_valkia_gift_slot_1', itemType.tech, 5, 'Progressive tech_chs_kho_khorne', 'Chaos Khorne Tech: Blood for the Blood God'),
    58805: itemData(IC.useful, 1, 'wh3_dlc20_chs_kho_valkia_heroes_lords', itemType.tech, 6, 'Progressive tech_chs_kho_khorne', "Chaos Khorne Tech: Insidious Selection"),
    58806: itemData(IC.useful, 1, 'wh3_dlc20_chs_kho_shared_gift_upgrade_diplomacy', itemType.tech, 6, 'Progressive tech_chs_kho_khorne', 'Chaos Khorne Tech: Gorestained Robes'),
    58807: itemData(IC.useful, 1, 'wh3_dlc20_chs_kho_valkia_xp', itemType.tech, 7, 'Progressive tech_chs_kho_khorne', 'Chaos Khorne Tech: Savage Strategy'),
    58808: itemData(IC.useful, 1, 'wh3_dlc20_chs_kho_valkia_military_1', itemType.tech, 3, 'Progressive tech_chs_kho_khorne', 'Chaos Khorne Tech: Mortal Brutality'),
    58809: itemData(IC.useful, 1, 'wh3_dlc20_chs_kho_valkia_movement', itemType.tech, 4, 'Progressive tech_chs_kho_khorne', 'Chaos Khorne Tech: Scarred Wings'),
    58810: itemData(IC.useful, 1, 'wh3_dlc20_chs_kho_valkia_gift_slot_2', itemType.tech, 5, 'Progressive tech_chs_kho_khorne', 'Chaos Khorne Tech: Skulls for the Skull Throne'),
    58811: itemData(IC.useful, 1, 'wh3_dlc20_chs_kho_valkia_weapons', itemType.tech, 6, 'Progressive tech_chs_kho_khorne', 'Chaos Khorne Tech: Honed Blades'),
    58812: itemData(IC.useful, 1, 'wh3_dlc20_chs_kho_shared_gift_upgrade_summons', itemType.tech, 6, 'Progressive tech_chs_kho_khorne', 'Chaos Khorne Tech: Bloody Summons'),
    58813: itemData(IC.useful, 1, 'wh3_dlc20_chs_kho_valkia_military_2', itemType.tech, 7, 'Progressive tech_chs_kho_khorne', 'Chaos Khorne Tech: Vengeful Warriors'),
    58814: itemData(IC.useful, 1, 'wh3_dlc20_chs_kho_valkia_gift_slot_3', itemType.tech, 8, 'Progressive tech_chs_kho_khorne', 'Chaos Khorne Tech: Sword-Maiden'),
    58815: itemData(IC.useful, 1, 'wh3_dlc20_chs_kho_valkia_ultimate', itemType.tech, 9, 'Progressive tech_chs_kho_khorne', 'Chaos Khorne Tech: War Horn'),

    58816: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_marauders', itemType.tech, 1, 'Progressive tech_chs_kho_undivided', 'Chaos Khorne Tech: Scrutiny of the Dark Gods'),
    58817: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_chariots', itemType.tech, 2, 'Progressive tech_chs_kho_undivided', 'Chaos Khorne Tech: Charioteer'),
    58818: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_mutants', itemType.tech, 3, 'Progressive tech_chs_kho_undivided', 'Chaos Khorne Tech: A Thousand Twisted Blessings'),
    58819: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_chosen', itemType.tech, 3, 'Progressive tech_chs_kho_undivided', 'Chaos Khorne Tech: Rite of Ascension'),
    58820: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_diplomacy', itemType.tech, 4, 'Progressive tech_chs_kho_undivided', 'Chaos Khorne Tech: Dark Diplomacy'),
    58821: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_movement', itemType.tech, 4, 'Progressive tech_chs_kho_undivided', 'Chaos Khorne Tech: Infernal March'),
    58822: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_gift_slot_1', itemType.tech, 5, 'Progressive tech_chs_kho_undivided', 'Chaos Khorne Tech: Daemonic Pact'),
    58823: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_knights', itemType.tech, 5, 'Progressive tech_chs_kho_undivided', 'Chaos Khorne Tech: Profane Weaponry'),
    58824: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_daemonic_mounts', itemType.tech, 6, 'Progressive tech_chs_kho_undivided', 'Chaos Khorne Tech: Daemon Mounts'),
    58825: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_corruption', itemType.tech, 5, 'Progressive tech_chs_kho_undivided', 'Chaos Khorne Tech: Malignant Totems'),
    58826: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_vassals', itemType.tech, 6, 'Progressive tech_chs_kho_undivided', 'Chaos Khorne Tech: Slaves to Darkness'),
    58827: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_beasts', itemType.tech, 6, 'Progressive tech_chs_kho_undivided', 'Chaos Khorne Tech: Unchained Beasts'),
    58828: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_building', itemType.tech, 6, 'Progressive tech_chs_kho_undivided', 'Chaos Khorne Tech: Erection of Ruinous Monuments'),
    58829: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_upgrades', itemType.tech, 6, 'Progressive tech_chs_kho_undivided', 'Chaos Khorne Tech: Inscribed Chaos Armour'),
    58830: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_souls', itemType.tech, 6, 'Progressive tech_chs_kho_undivided', 'Chaos Khorne Tech: Culling of the Weak'),
    58831: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_monsters', itemType.tech, 7, 'Progressive tech_chs_kho_undivided', 'Chaos Khorne Tech: Giant Manacles'),
    58832: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_gift_slot_2', itemType.tech, 8, 'Progressive tech_chs_kho_undivided', 'Chaos Khorne Tech: Gaze of the Dark Gods'),
}

progUnits: dict[int, itemData] = warriorsOfChaos.progUnits

progBuildings: dict[int, itemData] = warriorsOfChaos.progBuildings

progTechs: dict[int, itemData] = {
    59400: itemData(IC.useful, 9, "Progressive tech_chs_kho_undivided", itemType.tech, 8, None, "Progressive Chaos Khorne Tech: Undivided"),
    59401: itemData(IC.useful, 9, "Progressive tech_chs_kho_khorne", itemType.tech, 9, None, "Progressive Chaos Khorne Tech: Khorne"),
}

special: dict[int, itemData] = {

}