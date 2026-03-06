from BaseClasses import ItemClassification as IC
from worlds.tww3.item_types import ItemType, ItemData
from . import warriorsOfChaos

# @formatter:off
units: dict[int, ItemData] = warriorsOfChaos.baseUnits
units.update(warriorsOfChaos.tzeentchUnits)
units.update({
    64000: ItemData(IC.useful, 1, 'wh3_main_tze_inf_blue_horrors_0', ItemType.unit, 1, 'Progressive chs_inf', 'Chaos Unit: Blue Horrors of Tzeentch'),
    64001: ItemData(IC.useful, 1, 'wh3_dlc24_tze_inf_tzaangors', ItemType.unit, 3, 'Progressive chs_inf', 'Chaos Unit: Tzaangors'),
    64002: ItemData(IC.useful, 1, 'wh3_dlc24_tze_inf_centigors_great_weapons', ItemType.unit, 2, 'Progressive chs_cav', 'Chaos Unit: Centigors of Tzeentch'),
    64003: ItemData(IC.useful, 1, 'wh3_main_tze_inf_pink_horrors_1', ItemType.unit, 3, 'Progressive chs_inf', 'Chaos Unit: Exalted Pink Horrors of Tzeentch'),

    64004: ItemData(IC.useful, 1, 'wh3_dlc24_chs_cha_exalted_hero_mtze', ItemType.unit, 1, 'Progressive chs_hro', 'Chaos Unit: Exalted Hero of Tzeentch'),
    64005: ItemData(IC.useful, 1, 'wh3_dlc20_chs_cha_chaos_sorcerer_tzeentch_mtze', ItemType.unit, 1, 'Progressive chs_hro', 'Chaos Unit: Chaos Sorcerer of Tzeentch (Tzeentch)'),
    64006: ItemData(IC.useful, 1, 'wh3_dlc20_chs_cha_chaos_sorcerer_metal_mtze', ItemType.unit, 1, 'Progressive chs_hro', 'Chaos Unit: Chaos Sorcerer of Tzeentch (Metal)'),

    64007: ItemData(IC.useful, 1, 'wh3_dlc24_tze_inf_pink_horrors_ror', ItemType.unit, 2, 'Progressive chs_inf', 'Chaos Unit: The Sourguts (Pink Horrors of Tzeentch)'),
    64008: ItemData(IC.useful, 1, 'wh3_dlc24_tze_mon_screamers_ror', ItemType.unit, 2, 'Progressive chs_bst', 'Chaos Unit: Shrieking Skyrays (Screamers of Tzeentch)'),
    64009: ItemData(IC.useful, 1, 'wh3_twa06_tze_inf_pink_horrors_ror_0', ItemType.unit, 3, 'Progressive chs_inf', 'Chaos Unit: Blazing Squealers (Exalted Pink Horrors of Tzeentch)'),
    64010: ItemData(IC.useful, 1, 'wh3_dlc24_tze_mon_mutalith_vortex_beast_ror', ItemType.unit, 5, 'Progressive chs_bst', 'Chaos Unit: Aeson the Fallen (Mutalith Vortex Beast)'),
})

buildings: dict[int, ItemData] = warriorsOfChaos.buildings

techs: dict[int, ItemData] = {
    64800: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_marks_tzeentch', ItemType.tech, 1, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Arcane Branding Iron'),
    64801: ItemData(IC.useful, 1, 'wh3_dlc20_chs_tze_shared_gift_upgrade_authority', ItemType.tech, 2, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Mystical Banner'),
    64802: ItemData(IC.useful, 1, 'wh3_dlc20_chs_tze_shared_gift_upgrade_corruption', ItemType.tech, 3, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Enchanted Idols'),
    64803: ItemData(IC.useful, 1, 'wh3_dlc20_chs_tze_vilitch_buildings', ItemType.tech, 4, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Arcane Construction'),
    64804: ItemData(IC.useful, 1, 'wh3_dlc20_chs_tze_vilitch_gift_slot_1', ItemType.tech, 5, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Dark Meditation'),
    64805: ItemData(IC.useful, 1, 'wh3_dlc20_chs_tze_vilitch_heroes_lords', ItemType.tech, 6, 'Progressive tech_chs_tze_tzeentch', "Chaos Tzeentch Tech: Summoning Rite"),
    64806: ItemData(IC.useful, 1, 'wh3_dlc20_chs_tze_shared_gift_upgrade_diplomacy', ItemType.tech, 6, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Sacrificial Prophecy'),
    64807: ItemData(IC.useful, 1, 'wh3_dlc20_chs_tze_vilitch_teleport', ItemType.tech, 7, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Teleportation Stone'),
    64808: ItemData(IC.useful, 1, 'wh3_dlc20_chs_tze_vilitch_military_1', ItemType.tech, 3, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Temple of Tzeentch'),
    64809: ItemData(IC.useful, 1, 'wh3_dlc20_chs_tze_vilitch_spells', ItemType.tech, 4, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Twisted Tome'),
    64810: ItemData(IC.useful, 1, 'wh3_dlc20_chs_tze_vilitch_gift_slot_2', ItemType.tech, 5, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Attuning Ritual'),
    64811: ItemData(IC.useful, 1, 'wh3_dlc20_chs_tze_vilitch_weapons', ItemType.tech, 6, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Ritual Staff'),
    64812: ItemData(IC.useful, 1, 'wh3_dlc20_chs_tze_shared_gift_upgrade_summons', ItemType.tech, 6, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Pink Horrors'),
    64813: ItemData(IC.useful, 1, 'wh3_dlc20_chs_tze_vilitch_military_2', ItemType.tech, 7, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Enchanted Armour'),
    64814: ItemData(IC.useful, 1, 'wh3_dlc20_chs_tze_vilitch_gift_slot_3', ItemType.tech, 8, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Chaos Moon'),
    64815: ItemData(IC.useful, 1, 'wh3_dlc20_chs_tze_vilitch_ultimate', ItemType.tech, 9, 'Progressive tech_chs_tze_tzeentch', 'Chaos Tzeentch Tech: Unholy Intervention'),

    64816: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_marauders', ItemType.tech, 1, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Scrutiny of the Dark Gods'),
    64817: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_chariots', ItemType.tech, 2, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Charioteer'),
    64818: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_mutants', ItemType.tech, 3, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: A Thousand Twisted Blessings'),
    64819: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_chosen', ItemType.tech, 3, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Rite of Ascension'),
    64820: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_diplomacy', ItemType.tech, 4, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Dark Diplomacy'),
    64821: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_movement', ItemType.tech, 4, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Infernal March'),
    64822: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_gift_slot_1', ItemType.tech, 5, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Daemonic Pact'),
    64823: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_knights', ItemType.tech, 5, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Profane Weaponry'),
    64824: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_daemonic_mounts', ItemType.tech, 6, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Daemon Mounts'),
    64825: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_corruption', ItemType.tech, 5, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Malignant Totems'),
    64826: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_vassals', ItemType.tech, 6, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Slaves to Darkness'),
    64827: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_beasts', ItemType.tech, 6, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Unchained Beasts'),
    64828: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_building', ItemType.tech, 6, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Erection of Ruinous Monuments'),
    64829: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_upgrades', ItemType.tech, 6, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Inscribed Chaos Armour'),
    64830: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_souls', ItemType.tech, 6, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Culling of the Weak'),
    64831: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_monsters', ItemType.tech, 7, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Giant Manacles'),
    64832: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_gift_slot_2', ItemType.tech, 8, 'Progressive tech_chs_tze_undivided', 'Chaos Tzeentch Tech: Gaze of the Dark Gods'),
}

progUnits: dict[int, ItemData] = warriorsOfChaos.progUnits

progBuildings: dict[int, ItemData] = warriorsOfChaos.progBuildings

progTechs: dict[int, ItemData] = {
    65400: ItemData(IC.useful, 9, "Progressive tech_chs_tze_undivided", ItemType.tech, 8, None, "Progressive Chaos Tzeentch Tech: Undivided"),
    65401: ItemData(IC.useful, 9, "Progressive tech_chs_tze_tzeentch", ItemType.tech, 9, None, "Progressive Chaos Tzeentch Tech: Tzeentch"),
}

special: dict[int, ItemData] = {

}