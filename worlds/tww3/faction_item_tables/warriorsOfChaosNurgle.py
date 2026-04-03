from BaseClasses import ItemClassification as IC
from worlds.tww3.dataStructs import itemType, itemData
from . import warriorsOfChaos

# @formatter:off
units: dict[int, itemData] = warriorsOfChaos.baseUnits
units.update(warriorsOfChaos.nurgleUnits)
units.update({
    60000: itemData(IC.useful, 1, 'wh3_dlc25_nur_inf_pestigors', itemType.unit, 3, 'Progressive chs_inf', 'Chaos Unit: Pestigors'),
    60001: itemData(IC.useful, 1, 'wh3_main_nur_inf_plaguebearers_1', itemType.unit, 3, 'Progressive chs_inf', 'Chaos Unit: Exalted Plaguebearers of Nurgle'),
    60002: itemData(IC.useful, 1, 'wh3_main_nur_mon_plague_toads_0', itemType.unit, 3, 'Progressive chs_bst', 'Chaos Unit: Plague Toads of Nurgle'),
    60003: itemData(IC.useful, 1, 'wh3_main_nur_mon_rot_flies_0', itemType.unit, 3, 'Progressive chs_bst', 'Chaos Unit: Rot Flies'),

    60004: itemData(IC.useful, 1, 'wh3_dlc20_chs_cha_exalted_hero_mnur', itemType.unit, 1, 'Progressive chs_hro', 'Chaos Unit: Exalted Hero of Nurgle'),
    60005: itemData(IC.useful, 1, 'wh3_dlc25_chs_cha_chaos_sorcerer_death_mnur', itemType.unit, 1, 'Progressive chs_hro', 'Chaos Unit: Chaos Sorcerer of Nurgle (Death)'),
    60006: itemData(IC.useful, 1, 'wh3_dlc25_chs_cha_chaos_sorcerer_nurgle_mnur', itemType.unit, 1, 'Progressive chs_hro', 'Chaos Unit: Chaos Sorcerer of Nurgle (Nurgle)'),

    60007: itemData(IC.useful, 1, 'wh3_twa07_nur_cav_pox_riders_of_nurgle_ror_0', itemType.unit, 2, 'Progressive chs_cav', 'Chaos Unit: Barons of the Bog (Pox Riders of Nurgle)'),
    60008: itemData(IC.useful, 1, 'wh3_twa06_nur_inf_plaguebearers_ror_0', itemType.unit, 3, 'Progressive chs_inf', 'Chaos Unit: Festering Stooges (Exalted Plaguebearers of Nurgle)'),
    60009: itemData(IC.useful, 1, 'wh3_dlc25_nur_cav_plague_drones_1_ror', itemType.unit, 2, 'Progressive chs_cav', "Chaos Unit: The Angels of Decay (Plague Drones - Death's Heads)"),
    60010: itemData(IC.useful, 1, 'wh3_dlc25_nur_mon_soul_grinder_0_ror', itemType.unit, 4, 'Progressive chs_bst', 'Chaos Unit: Noxbringer (Soul Grinder of Nurgle)'),
})

buildings: dict[int, itemData] = warriorsOfChaos.buildings

techs: dict[int, itemData] = {
    60800: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_marks_nurgle', itemType.tech, 1, 'Progressive tech_chs_nur_nurgle', 'Chaos Nurgle Tech: Rusted Branding Iron'),
    60801: itemData(IC.useful, 1, 'wh3_dlc20_chs_nur_shared_gift_upgrade_authority', itemType.tech, 2, 'Progressive tech_chs_nur_nurgle', 'Chaos Nurgle Tech: Rotten Altar'),
    60802: itemData(IC.useful, 1, 'wh3_dlc20_chs_nur_shared_gift_upgrade_corruption', itemType.tech, 3, 'Progressive tech_chs_nur_nurgle', 'Chaos Nurgle Tech: Swamp of Souls'),
    60803: itemData(IC.useful, 1, 'wh3_dlc20_chs_nur_festus_buildings', itemType.tech, 4, 'Progressive tech_chs_nur_nurgle', 'Chaos Nurgle Tech: Rancid Structures'),
    60804: itemData(IC.useful, 1, 'wh3_dlc20_chs_nur_festus_gift_slot_1', itemType.tech, 5, 'Progressive tech_chs_nur_nurgle', 'Chaos Nurgle Tech: Maddening Gifts'),
    60805: itemData(IC.useful, 1, 'wh3_dlc20_chs_nur_festus_heroes_lords', itemType.tech, 6, 'Progressive tech_chs_nur_nurgle', "Chaos Nurgle Tech: Powerful Patients"),
    60806: itemData(IC.useful, 1, 'wh3_dlc20_chs_nur_shared_gift_upgrade_diplomacy', itemType.tech, 6, 'Progressive tech_chs_nur_nurgle', 'Chaos Nurgle Tech: Messenger of Decay'),
    60807: itemData(IC.useful, 1, 'wh3_dlc20_chs_nur_festus_plagues', itemType.tech, 7, 'Progressive tech_chs_nur_nurgle', 'Chaos Nurgle Tech: Experimental Diseases'),
    60808: itemData(IC.useful, 1, 'wh3_dlc20_chs_nur_festus_military_1', itemType.tech, 3, 'Progressive tech_chs_nur_nurgle', 'Chaos Nurgle Tech: Rotten Relics'),
    60809: itemData(IC.useful, 1, 'wh3_dlc20_chs_nur_festus_magic', itemType.tech, 4, 'Progressive tech_chs_nur_nurgle', 'Chaos Nurgle Tech: Human Trials'),
    60810: itemData(IC.useful, 1, 'wh3_dlc20_chs_nur_festus_gift_slot_2', itemType.tech, 5, 'Progressive tech_chs_nur_nurgle', 'Chaos Nurgle Tech: Virulent Blessings'),
    60811: itemData(IC.useful, 1, 'wh3_dlc20_chs_nur_festus_weapons', itemType.tech, 6, 'Progressive tech_chs_nur_nurgle', 'Chaos Nurgle Tech: Hideous Amputation'),
    60812: itemData(IC.useful, 1, 'wh3_dlc20_chs_nur_shared_gift_upgrade_summons', itemType.tech, 6, 'Progressive tech_chs_nur_nurgle', 'Chaos Nurgle Tech: Rampant Plaguebearers'),
    60813: itemData(IC.useful, 1, 'wh3_dlc20_chs_nur_festus_military_2', itemType.tech, 7, 'Progressive tech_chs_nur_nurgle', 'Chaos Nurgle Tech: Prayers of Sickness'),
    60814: itemData(IC.useful, 1, 'wh3_dlc20_chs_nur_festus_gift_slot_3', itemType.tech, 8, 'Progressive tech_chs_nur_nurgle', 'Chaos Nurgle Tech: Doctor of Death'),
    60815: itemData(IC.useful, 1, 'wh3_dlc20_chs_nur_festus_ultimate', itemType.tech, 9, 'Progressive tech_chs_nur_nurgle', 'Chaos Nurgle Tech: Blasphemous Summons'),

    60816: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_marauders', itemType.tech, 1, 'Progressive tech_chs_nur_undivided', 'Chaos Nurgle Tech: Scrutiny of the Dark Gods'),
    60817: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_chariots', itemType.tech, 2, 'Progressive tech_chs_nur_undivided', 'Chaos Nurgle Tech: Charioteer'),
    60818: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_mutants', itemType.tech, 3, 'Progressive tech_chs_nur_undivided', 'Chaos Nurgle Tech: A Thousand Twisted Blessings'),
    60819: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_chosen', itemType.tech, 3, 'Progressive tech_chs_nur_undivided', 'Chaos Nurgle Tech: Rite of Ascension'),
    60820: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_diplomacy', itemType.tech, 4, 'Progressive tech_chs_nur_undivided', 'Chaos Nurgle Tech: Dark Diplomacy'),
    60821: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_movement', itemType.tech, 4, 'Progressive tech_chs_nur_undivided', 'Chaos Nurgle Tech: Infernal March'),
    60822: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_gift_slot_1', itemType.tech, 5, 'Progressive tech_chs_nur_undivided', 'Chaos Nurgle Tech: Daemonic Pact'),
    60823: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_knights', itemType.tech, 5, 'Progressive tech_chs_nur_undivided', 'Chaos Nurgle Tech: Profane Weaponry'),
    60824: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_daemonic_mounts', itemType.tech, 6, 'Progressive tech_chs_nur_undivided', 'Chaos Nurgle Tech: Daemon Mounts'),
    60825: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_corruption', itemType.tech, 5, 'Progressive tech_chs_nur_undivided', 'Chaos Nurgle Tech: Malignant Totems'),
    60826: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_vassals', itemType.tech, 6, 'Progressive tech_chs_nur_undivided', 'Chaos Nurgle Tech: Slaves to Darkness'),
    60827: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_beasts', itemType.tech, 6, 'Progressive tech_chs_nur_undivided', 'Chaos Nurgle Tech: Unchained Beasts'),
    60828: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_building', itemType.tech, 6, 'Progressive tech_chs_nur_undivided', 'Chaos Nurgle Tech: Erection of Ruinous Monuments'),
    60829: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_upgrades', itemType.tech, 6, 'Progressive tech_chs_nur_undivided', 'Chaos Nurgle Tech: Inscribed Chaos Armour'),
    60830: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_souls', itemType.tech, 6, 'Progressive tech_chs_nur_undivided', 'Chaos Nurgle Tech: Culling of the Weak'),
    60831: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_monsters', itemType.tech, 7, 'Progressive tech_chs_nur_undivided', 'Chaos Nurgle Tech: Giant Manacles'),
    60832: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_gift_slot_2', itemType.tech, 8, 'Progressive tech_chs_nur_undivided', 'Chaos Nurgle Tech: Gaze of the Dark Gods'),
}

progUnits: dict[int, itemData] = warriorsOfChaos.progUnits

progBuildings: dict[int, itemData] = warriorsOfChaos.progBuildings

progTechs: dict[int, itemData] = {
    61400: itemData(IC.useful, 9, "Progressive tech_chs_nur_undivided", itemType.tech, 8, None, "Progressive Chaos Nurgle Tech: Undivided"),
    61401: itemData(IC.useful, 9, "Progressive tech_chs_nur_nurgle", itemType.tech, 9, None, "Progressive Chaos Nurgle Tech: Nurgle"),
}

special: dict[int, itemData] = {

}