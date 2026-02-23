from BaseClasses import ItemClassification as IC
from .item_types import ItemType, ItemData, specialItemData
from . import warriorsOfChaos

# @formatter:off
units: dict[int, ItemData] = warriorsOfChaos.baseUnits
units.update(warriorsOfChaos.nurgleUnits)
units.update({
    60000: ItemData(IC.useful, 1, 'wh3_dlc25_nur_inf_pestigors', ItemType.unit, 3, 'Progressive chs_inf', 'Chs Unit: Pestigors'),
    60001: ItemData(IC.useful, 1, 'wh3_main_nur_inf_plaguebearers_1', ItemType.unit, 3, 'Progressive chs_inf', 'Chs Unit: Exalted Plaguebearers of Nurgle'),
    60002: ItemData(IC.useful, 1, 'wh3_main_nur_mon_plague_toads_0', ItemType.unit, 3, 'Progressive chs_bst', 'Chs Unit: Plague Toads of Nurgle'),
    60003: ItemData(IC.useful, 1, 'wh3_main_nur_mon_rot_flies_0', ItemType.unit, 3, 'Progressive chs_bst', 'Chs Unit: Rot Flies'),

    60004: ItemData(IC.useful, 1, 'wh3_dlc20_chs_cha_exalted_hero_mnur', ItemType.unit, 1, 'Progressive chs_hro', 'Chs Unit: Exalted Hero of Nurgle'),
    60005: ItemData(IC.useful, 1, 'wh3_dlc25_chs_cha_chaos_sorcerer_death_mnur', ItemType.unit, 1, 'Progressive chs_hro', 'Chs Unit: Chaos Sorcerer of Nurgle (Death)'),
    60006: ItemData(IC.useful, 1, 'wh3_dlc25_chs_cha_chaos_sorcerer_nurgle_mnur', ItemType.unit, 1, 'Progressive chs_hro', 'Chs Unit: Chaos Sorcerer of Nurgle (Nurgle)'),

    60007: ItemData(IC.useful, 1, 'wh3_twa07_nur_cav_pox_riders_of_nurgle_ror_0', ItemType.unit, 2, 'Progressive chs_cav', 'Chs Unit: Barons of the Bog (Pox Riders of Nurgle)'),
    60008: ItemData(IC.useful, 1, 'wh3_twa06_nur_inf_plaguebearers_ror_0', ItemType.unit, 3, 'Progressive chs_inf', 'Chs Unit: Festering Stooges (Exalted Plaguebearers of Nurgle)'),
    60009: ItemData(IC.useful, 1, 'wh3_dlc25_nur_cav_plague_drones_1_ror', ItemType.unit, 2, 'Progressive chs_cav', "Chs Unit: The Angels of Decay (Plague Drones - Death's Heads)"),
    60010: ItemData(IC.useful, 1, 'wh3_dlc25_nur_mon_soul_grinder_0_ror', ItemType.unit, 4, 'Progressive chs_bst', 'Chs Unit: Noxbringer (Soul Grinder of Nurgle)'),
})

buildings: dict[int, ItemData] = warriorsOfChaos.buildings

techs: dict[int, ItemData] = {
    60800: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_marks_nurgle', ItemType.tech, 1, 'Progressive tech_chs_nur_nurgle', 'Chs Tech: Rusted Branding Iron'),
    60801: ItemData(IC.useful, 1, 'wh3_dlc20_chs_nur_shared_gift_upgrade_authority', ItemType.tech, 2, 'Progressive tech_chs_nur_nurgle', 'Chs Tech: Rotten Altar'),
    60802: ItemData(IC.useful, 1, 'wh3_dlc20_chs_nur_shared_gift_upgrade_corruption', ItemType.tech, 3, 'Progressive tech_chs_nur_nurgle', 'Chs Tech: Swamp of Souls'),
    60803: ItemData(IC.useful, 1, 'wh3_dlc20_chs_nur_festus_buildings', ItemType.tech, 4, 'Progressive tech_chs_nur_nurgle', 'Chs Tech: Rancid Structures'),
    60804: ItemData(IC.useful, 1, 'wh3_dlc20_chs_nur_festus_gift_slot_1', ItemType.tech, 5, 'Progressive tech_chs_nur_nurgle', 'Chs Tech: Maddening Gifts'),
    60805: ItemData(IC.useful, 1, 'wh3_dlc20_chs_nur_festus_heroes_lords', ItemType.tech, 6, 'Progressive tech_chs_nur_nurgle', "Chs Tech: Powerful Patients"),
    60806: ItemData(IC.useful, 1, 'wh3_dlc20_chs_nur_shared_gift_upgrade_diplomacy', ItemType.tech, 6, 'Progressive tech_chs_nur_nurgle', 'Chs Tech: Messenger of Decay'),
    60807: ItemData(IC.useful, 1, 'wh3_dlc20_chs_nur_festus_plagues', ItemType.tech, 7, 'Progressive tech_chs_nur_nurgle', 'Chs Tech: Experimental Diseases'),
    60808: ItemData(IC.useful, 1, 'wh3_dlc20_chs_nur_festus_military_1', ItemType.tech, 3, 'Progressive tech_chs_nur_nurgle', 'Chs Tech: Rotten Relics'),
    60809: ItemData(IC.useful, 1, 'wh3_dlc20_chs_nur_festus_magic', ItemType.tech, 4, 'Progressive tech_chs_nur_nurgle', 'Chs Tech: Human Trials'),
    60810: ItemData(IC.useful, 1, 'wh3_dlc20_chs_nur_festus_gift_slot_2', ItemType.tech, 5, 'Progressive tech_chs_nur_nurgle', 'Chs Tech: Virulent Blessings'),
    60811: ItemData(IC.useful, 1, 'wh3_dlc20_chs_nur_festus_weapons', ItemType.tech, 6, 'Progressive tech_chs_nur_nurgle', 'Chs Tech: Hideous Amputation'),
    60812: ItemData(IC.useful, 1, 'wh3_dlc20_chs_nur_shared_gift_upgrade_summons', ItemType.tech, 6, 'Progressive tech_chs_nur_nurgle', 'Chs Tech: Rampant Plaguebearers'),
    60813: ItemData(IC.useful, 1, 'wh3_dlc20_chs_nur_festus_military_2', ItemType.tech, 7, 'Progressive tech_chs_nur_nurgle', 'Chs Tech: Prayers of Sickness'),
    60814: ItemData(IC.useful, 1, 'wh3_dlc20_chs_nur_festus_gift_slot_3', ItemType.tech, 8, 'Progressive tech_chs_nur_nurgle', 'Chs Tech: Doctor of Death'),
    60815: ItemData(IC.useful, 1, 'wh3_dlc20_chs_nur_festus_ultimate', ItemType.tech, 9, 'Progressive tech_chs_nur_nurgle', 'Chs Tech: Blasphemous Summons'),

    60816: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_marauders', ItemType.tech, 1, 'Progressive tech_chs_nur_undivided', 'Chs Tech: Scrutiny of the Dark Gods'),
    60817: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_chariots', ItemType.tech, 2, 'Progressive tech_chs_nur_undivided', 'Chs Tech: Charioteer'),
    60818: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_mutants', ItemType.tech, 3, 'Progressive tech_chs_nur_undivided', 'Chs Tech: A Thousand Twisted Blessings'),
    60819: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_chosen', ItemType.tech, 3, 'Progressive tech_chs_nur_undivided', 'Chs Tech: Rite of Ascension'),
    60820: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_diplomacy', ItemType.tech, 4, 'Progressive tech_chs_nur_undivided', 'Chs Tech: Dark Diplomacy'),
    60821: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_movement', ItemType.tech, 4, 'Progressive tech_chs_nur_undivided', 'Chs Tech: Infernal March'),
    60822: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_gift_slot_1', ItemType.tech, 5, 'Progressive tech_chs_nur_undivided', 'Chs Tech: Daemonic Pact'),
    60823: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_knights', ItemType.tech, 5, 'Progressive tech_chs_nur_undivided', 'Chs Tech: Profane Weaponry'),
    60824: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_daemonic_mounts', ItemType.tech, 6, 'Progressive tech_chs_nur_undivided', 'Chs Tech: Daemon Mounts'),
    60825: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_corruption', ItemType.tech, 5, 'Progressive tech_chs_nur_undivided', 'Chs Tech: Malignant Totems'),
    60826: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_vassals', ItemType.tech, 6, 'Progressive tech_chs_nur_undivided', 'Chs Tech: Slaves to Darkness'),
    60827: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_beasts', ItemType.tech, 6, 'Progressive tech_chs_nur_undivided', 'Chs Tech: Unchained Beasts'),
    60828: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_building', ItemType.tech, 6, 'Progressive tech_chs_nur_undivided', 'Chs Tech: Erection of Ruinous Monuments'),
    60829: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_upgrades', ItemType.tech, 6, 'Progressive tech_chs_nur_undivided', 'Chs Tech: Inscribed Chaos Armour'),
    60830: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_souls', ItemType.tech, 6, 'Progressive tech_chs_nur_undivided', 'Chs Tech: Culling of the Weak'),
    60831: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_monsters', ItemType.tech, 7, 'Progressive tech_chs_nur_undivided', 'Chs Tech: Giant Manacles'),
    60832: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_gift_slot_2', ItemType.tech, 8, 'Progressive tech_chs_nur_undivided', 'Chs Tech: Gaze of the Dark Gods'),
}

progUnits: dict[int, ItemData] = warriorsOfChaos.progUnits

progBuildings: dict[int, ItemData] = warriorsOfChaos.progBuildings

progTechs: dict[int, ItemData] = {
    61400: ItemData(IC.useful, 9, "Progressive tech_chs_nur_undivided", ItemType.tech, 8, None, "Progressive Chs Tech: Undivided"),
    61401: ItemData(IC.useful, 9, "Progressive tech_chs_nur_nurgle", ItemType.tech, 9, None, "Progressive Chs Tech: Nurgle"),
}

special: dict[int, ItemData] = {

}