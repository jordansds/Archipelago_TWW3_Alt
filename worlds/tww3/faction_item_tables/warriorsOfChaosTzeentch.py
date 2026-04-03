from BaseClasses import ItemClassification as IC
from worlds.tww3.dataStructs import itemType, itemData
from . import warriorsOfChaos

# @formatter:off
units: dict[int, itemData] = warriorsOfChaos.baseUnits
units.update(warriorsOfChaos.tzeentchUnits)
units.update({
    64000: itemData(IC.useful, 1, 'wh3_main_tze_inf_blue_horrors_0', itemType.unit, 1, 'Progressive chs_inf', 'Chaos Unit: Blue Horrors of Tzeentch'),
    64001: itemData(IC.useful, 1, 'wh3_dlc24_tze_inf_tzaangors', itemType.unit, 3, 'Progressive chs_inf', 'Chaos Unit: Tzaangors'),
    64002: itemData(IC.useful, 1, 'wh3_dlc24_tze_inf_centigors_great_weapons', itemType.unit, 2, 'Progressive chs_cav', 'Chaos Unit: Centigors of Tzeentch'),
    64003: itemData(IC.useful, 1, 'wh3_main_tze_inf_pink_horrors_1', itemType.unit, 3, 'Progressive chs_inf', 'Chaos Unit: Exalted Pink Horrors of Tzeentch'),

    64004: itemData(IC.useful, 1, 'wh3_dlc24_chs_cha_exalted_hero_mtze', itemType.unit, 1, 'Progressive chs_hro', 'Chaos Unit: Exalted Hero of Tzeentch'),
    64005: itemData(IC.useful, 1, 'wh3_dlc20_chs_cha_chaos_sorcerer_tzeentch_mtze', itemType.unit, 1, 'Progressive chs_hro', 'Chaos Unit: Chaos Sorcerer of Tzeentch (Tzeentch)'),
    64006: itemData(IC.useful, 1, 'wh3_dlc20_chs_cha_chaos_sorcerer_metal_mtze', itemType.unit, 1, 'Progressive chs_hro', 'Chaos Unit: Chaos Sorcerer of Tzeentch (Metal)'),

    64007: itemData(IC.useful, 1, 'wh3_dlc24_tze_inf_pink_horrors_ror', itemType.unit, 2, 'Progressive chs_inf', 'Chaos Unit: The Sourguts (Pink Horrors of Tzeentch)'),
    64008: itemData(IC.useful, 1, 'wh3_dlc24_tze_mon_screamers_ror', itemType.unit, 2, 'Progressive chs_bst', 'Chaos Unit: Shrieking Skyrays (Screamers of Tzeentch)'),
    64009: itemData(IC.useful, 1, 'wh3_twa06_tze_inf_pink_horrors_ror_0', itemType.unit, 3, 'Progressive chs_inf', 'Chaos Unit: Blazing Squealers (Exalted Pink Horrors of Tzeentch)'),
    64010: itemData(IC.useful, 1, 'wh3_dlc24_tze_mon_mutalith_vortex_beast_ror', itemType.unit, 5, 'Progressive chs_bst', 'Chaos Unit: Aeson the Fallen (Mutalith Vortex Beast)'),
})

buildings: dict[int, itemData] = warriorsOfChaos.buildings

techs: dict[int, itemData] = {
    64800: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_marks_tzeentch', itemType.tech, 1, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Arcane Branding Iron'),
    64801: itemData(IC.useful, 1, 'wh3_dlc20_chs_tze_shared_gift_upgrade_authority', itemType.tech, 2, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Mystical Banner'),
    64802: itemData(IC.useful, 1, 'wh3_dlc20_chs_tze_shared_gift_upgrade_corruption', itemType.tech, 3, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Enchanted Idols'),
    64803: itemData(IC.useful, 1, 'wh3_dlc20_chs_tze_vilitch_buildings', itemType.tech, 4, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Arcane Construction'),
    64804: itemData(IC.useful, 1, 'wh3_dlc20_chs_tze_vilitch_gift_slot_1', itemType.tech, 5, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Dark Meditation'),
    64805: itemData(IC.useful, 1, 'wh3_dlc20_chs_tze_vilitch_heroes_lords', itemType.tech, 6, 'Progressive tech_chs_tze_tzeentch', "Chaos Tzeentch Tech: Summoning Rite"),
    64806: itemData(IC.useful, 1, 'wh3_dlc20_chs_tze_shared_gift_upgrade_diplomacy', itemType.tech, 6, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Sacrificial Prophecy'),
    64807: itemData(IC.useful, 1, 'wh3_dlc20_chs_tze_vilitch_teleport', itemType.tech, 7, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Teleportation Stone'),
    64808: itemData(IC.useful, 1, 'wh3_dlc20_chs_tze_vilitch_military_1', itemType.tech, 3, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Temple of Tzeentch'),
    64809: itemData(IC.useful, 1, 'wh3_dlc20_chs_tze_vilitch_spells', itemType.tech, 4, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Twisted Tome'),
    64810: itemData(IC.useful, 1, 'wh3_dlc20_chs_tze_vilitch_gift_slot_2', itemType.tech, 5, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Attuning Ritual'),
    64811: itemData(IC.useful, 1, 'wh3_dlc20_chs_tze_vilitch_weapons', itemType.tech, 6, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Ritual Staff'),
    64812: itemData(IC.useful, 1, 'wh3_dlc20_chs_tze_shared_gift_upgrade_summons', itemType.tech, 6, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Pink Horrors'),
    64813: itemData(IC.useful, 1, 'wh3_dlc20_chs_tze_vilitch_military_2', itemType.tech, 7, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Enchanted Armour'),
    64814: itemData(IC.useful, 1, 'wh3_dlc20_chs_tze_vilitch_gift_slot_3', itemType.tech, 8, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Chaos Moon'),
    64815: itemData(IC.useful, 1, 'wh3_dlc20_chs_tze_vilitch_ultimate', itemType.tech, 9, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Unholy Intervention'),

    64816: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_marauders', itemType.tech, 1, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Scrutiny of the Dark Gods'),
    64817: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_chariots', itemType.tech, 2, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Charioteer'),
    64818: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_mutants', itemType.tech, 3, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: A Thousand Twisted Blessings'),
    64819: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_chosen', itemType.tech, 3, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Rite of Ascension'),
    64820: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_diplomacy', itemType.tech, 4, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Dark Diplomacy'),
    64821: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_movement', itemType.tech, 4, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Infernal March'),
    64822: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_gift_slot_1', itemType.tech, 5, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Daemonic Pact'),
    64823: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_knights', itemType.tech, 5, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Profane Weaponry'),
    64824: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_daemonic_mounts', itemType.tech, 6, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Daemon Mounts'),
    64825: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_corruption', itemType.tech, 5, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Malignant Totems'),
    64826: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_vassals', itemType.tech, 6, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Slaves to Darkness'),
    64827: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_beasts', itemType.tech, 6, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Unchained Beasts'),
    64828: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_building', itemType.tech, 6, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Erection of Ruinous Monuments'),
    64829: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_upgrades', itemType.tech, 6, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Inscribed Chaos Armour'),
    64830: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_souls', itemType.tech, 6, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Culling of the Weak'),
    64831: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_monsters', itemType.tech, 7, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Giant Manacles'),
    64832: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_gift_slot_2', itemType.tech, 8, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Gaze of the Dark Gods'),
}

progUnits: dict[int, itemData] = warriorsOfChaos.progUnits

progBuildings: dict[int, itemData] = warriorsOfChaos.progBuildings

progTechs: dict[int, itemData] = {
    65400: itemData(IC.useful, 9, "Progressive tech_chs_tze_undivided", itemType.tech, 8, None, "Progressive Chaos Tzeentch Tech: Undivided"),
    65401: itemData(IC.useful, 9, "Progressive tech_chs_tze_tzeentch", itemType.tech, 9, None, "Progressive Chaos Tzeentch Tech: Tzeentch"),
}

special: dict[int, itemData] = {

}