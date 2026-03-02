from BaseClasses import ItemClassification as IC
from worlds.tww3.item_types import ItemType, ItemData
from . import warriorsOfChaos

# @formatter:off
units: dict[int, ItemData] = warriorsOfChaos.baseUnits
units.update(warriorsOfChaos.khorneUnits)
units.update({
    58000: ItemData(IC.useful, 1, 'wh3_dlc26_kho_inf_khorngors', ItemType.unit, 3, 'Progressive chs_inf', 'Chs Unit: Khorngors'),
    58001: ItemData(IC.useful, 1, 'wh3_main_kho_inf_bloodletters_1', ItemType.unit, 3, 'Progressive chs_inf', 'Chs Unit: Exalted Bloodletters of Khorne'),
    58002: ItemData(IC.useful, 1, 'wh3_dlc26_kho_inf_skullreapers', ItemType.unit, 3, 'Progressive chs_inf', 'Chs Unit: Skullreapers'),
    58003: ItemData(IC.useful, 1, 'wh3_dlc26_kho_inf_wrathmongers', ItemType.unit, 4, 'Progressive chs_inf', 'Chs Unit: Wrathmongers'),

    58004: ItemData(IC.useful, 1, 'wh3_dlc20_chs_cha_exalted_hero_mkho', ItemType.unit, 1, 'Progressive chs_hro', 'Chs Unit: Exalted Hero of Khorne'),

    58005: ItemData(IC.useful, 1, 'wh3_twa06_kho_inf_bloodletters_ror_0', ItemType.unit, 3, 'Progressive chs_inf', 'Chs Unit: Hellforged Host (Exalted Bloodletters of Khorne)'),
    58006: ItemData(IC.useful, 1, 'wh_pro04_nor_inf_marauder_berserkers_ror_0', ItemType.unit, 1, 'Progressive chs_inf', 'Chs Unit: Brutes of the Hound (Marauder Berserkers)'),
    58007: ItemData(IC.useful, 1, 'wh3_dlc26_kho_inf_wrathmongers_ror', ItemType.unit, 4, 'Progressive chs_inf', 'Chs Unit: Bloodwake Berserkers (Wrathmongers)'),
    58008: ItemData(IC.useful, 1, 'wh3_twa07_kho_cav_bloodcrushers_ror_0', ItemType.unit, 3, 'Progressive chs_cav', "Chs Unit: Heralds of Khorne's Fury (Bloodcrushers of Khorne)"),
    58009: ItemData(IC.useful, 1, 'wh2_dlc17_bst_mon_ghorgon_ror_0', ItemType.unit, 5, 'Progressive chs_bst', 'Chs Unit: The Bloodbrute Behemoth (Ghorgon)')
})

buildings: dict[int, ItemData] = warriorsOfChaos.buildings

techs: dict[int, ItemData] = {
    58800: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_marks_khorne', ItemType.tech, 1, 'Progressive tech_chs_kho_khorne', 'Chs Tech: Searing Branding Iron'),
    58801: ItemData(IC.useful, 1, 'wh3_dlc20_chs_kho_shared_gift_upgrade_authority', ItemType.tech, 2, 'Progressive tech_chs_kho_khorne', 'Chs Tech: Sacrificial Altar'),
    58802: ItemData(IC.useful, 1, 'wh3_dlc20_chs_kho_shared_gift_upgrade_corruption', ItemType.tech, 3, 'Progressive tech_chs_kho_khorne', 'Chs Tech: Bloodied Blade'),
    58803: ItemData(IC.useful, 1, 'wh3_dlc20_chs_kho_valkia_buildings', ItemType.tech, 4, 'Progressive tech_chs_kho_khorne', 'Chs Tech: Builder of Glory'),
    58804: ItemData(IC.useful, 1, 'wh3_dlc20_chs_kho_valkia_gift_slot_1', ItemType.tech, 5, 'Progressive tech_chs_kho_khorne', 'Chs Tech: Blood for the Blood God'),
    58805: ItemData(IC.useful, 1, 'wh3_dlc20_chs_kho_valkia_heroes_lords', ItemType.tech, 6, 'Progressive tech_chs_kho_khorne', "Chs Tech: Insidious Selection"),
    58806: ItemData(IC.useful, 1, 'wh3_dlc20_chs_kho_shared_gift_upgrade_diplomacy', ItemType.tech, 6, 'Progressive tech_chs_kho_khorne', 'Chs Tech: Gorestained Robes'),
    58807: ItemData(IC.useful, 1, 'wh3_dlc20_chs_kho_valkia_xp', ItemType.tech, 7, 'Progressive tech_chs_kho_khorne', 'Chs Tech: Savage Strategy'),
    58808: ItemData(IC.useful, 1, 'wh3_dlc20_chs_kho_valkia_military_1', ItemType.tech, 3, 'Progressive tech_chs_kho_khorne', 'Chs Tech: Mortal Brutality'),
    58809: ItemData(IC.useful, 1, 'wh3_dlc20_chs_kho_valkia_movement', ItemType.tech, 4, 'Progressive tech_chs_kho_khorne', 'Chs Tech: Scarred Wings'),
    58810: ItemData(IC.useful, 1, 'wh3_dlc20_chs_kho_valkia_gift_slot_2', ItemType.tech, 5, 'Progressive tech_chs_kho_khorne', 'Chs Tech: Skulls for the Skull Throne'),
    58811: ItemData(IC.useful, 1, 'wh3_dlc20_chs_kho_valkia_weapons', ItemType.tech, 6, 'Progressive tech_chs_kho_khorne', 'Chs Tech: Honed Blades'),
    58812: ItemData(IC.useful, 1, 'wh3_dlc20_chs_kho_shared_gift_upgrade_summons', ItemType.tech, 6, 'Progressive tech_chs_kho_khorne', 'Chs Tech: Bloody Summons'),
    58813: ItemData(IC.useful, 1, 'wh3_dlc20_chs_kho_valkia_military_2', ItemType.tech, 7, 'Progressive tech_chs_kho_khorne', 'Chs Tech: Vengeful Warriors'),
    58814: ItemData(IC.useful, 1, 'wh3_dlc20_chs_kho_valkia_gift_slot_3', ItemType.tech, 8, 'Progressive tech_chs_kho_khorne', 'Chs Tech: Sword-Maiden'),
    58815: ItemData(IC.useful, 1, 'wh3_dlc20_chs_kho_valkia_ultimate', ItemType.tech, 9, 'Progressive tech_chs_kho_khorne', 'Chs Tech: War Horn'),

    58816: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_marauders', ItemType.tech, 1, 'Progressive tech_chs_kho_undivided', 'Chs Tech: Scrutiny of the Dark Gods'),
    58817: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_chariots', ItemType.tech, 2, 'Progressive tech_chs_kho_undivided', 'Chs Tech: Charioteer'),
    58818: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_mutants', ItemType.tech, 3, 'Progressive tech_chs_kho_undivided', 'Chs Tech: A Thousand Twisted Blessings'),
    58819: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_chosen', ItemType.tech, 3, 'Progressive tech_chs_kho_undivided', 'Chs Tech: Rite of Ascension'),
    58820: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_diplomacy', ItemType.tech, 4, 'Progressive tech_chs_kho_undivided', 'Chs Tech: Dark Diplomacy'),
    58821: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_movement', ItemType.tech, 4, 'Progressive tech_chs_kho_undivided', 'Chs Tech: Infernal March'),
    58822: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_gift_slot_1', ItemType.tech, 5, 'Progressive tech_chs_kho_undivided', 'Chs Tech: Daemonic Pact'),
    58823: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_knights', ItemType.tech, 5, 'Progressive tech_chs_kho_undivided', 'Chs Tech: Profane Weaponry'),
    58824: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_daemonic_mounts', ItemType.tech, 6, 'Progressive tech_chs_kho_undivided', 'Chs Tech: Daemon Mounts'),
    58825: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_corruption', ItemType.tech, 5, 'Progressive tech_chs_kho_undivided', 'Chs Tech: Malignant Totems'),
    58826: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_vassals', ItemType.tech, 6, 'Progressive tech_chs_kho_undivided', 'Chs Tech: Slaves to Darkness'),
    58827: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_beasts', ItemType.tech, 6, 'Progressive tech_chs_kho_undivided', 'Chs Tech: Unchained Beasts'),
    58828: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_building', ItemType.tech, 6, 'Progressive tech_chs_kho_undivided', 'Chs Tech: Erection of Ruinous Monuments'),
    58829: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_upgrades', ItemType.tech, 6, 'Progressive tech_chs_kho_undivided', 'Chs Tech: Inscribed Chaos Armour'),
    58830: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_souls', ItemType.tech, 6, 'Progressive tech_chs_kho_undivided', 'Chs Tech: Culling of the Weak'),
    58831: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_monsters', ItemType.tech, 7, 'Progressive tech_chs_kho_undivided', 'Chs Tech: Giant Manacles'),
    58832: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_gift_slot_2', ItemType.tech, 8, 'Progressive tech_chs_kho_undivided', 'Chs Tech: Gaze of the Dark Gods'),
}

progUnits: dict[int, ItemData] = warriorsOfChaos.progUnits

progBuildings: dict[int, ItemData] = warriorsOfChaos.progBuildings

progTechs: dict[int, ItemData] = {
    59400: ItemData(IC.useful, 9, "Progressive tech_chs_kho_undivided", ItemType.tech, 8, None, "Progressive Chs Tech: Undivided"),
    59401: ItemData(IC.useful, 9, "Progressive tech_chs_kho_khorne", ItemType.tech, 9, None, "Progressive Chs Tech: Khorne"),
}

special: dict[int, ItemData] = {

}