from BaseClasses import ItemClassification as IC
from worlds.tww3.dataStructs import itemType, itemData
from . import warriorsOfChaos

# @formatter:off
units: dict[int, itemData] = warriorsOfChaos.baseUnits
units.update(warriorsOfChaos.slaaneshUnits)
units.update({
    62000: itemData(IC.useful, 1, 'wh3_dlc27_tze_inf_slaangors', itemType.unit, 3, 'Progressive chs_inf', 'Chaos Unit: Slaangors'),
    62001: itemData(IC.useful, 1, 'wh3_main_sla_inf_daemonette_1', itemType.unit, 3, 'Progressive chs_inf', 'Chaos Unit: Exalted Daemonettes of Slaanesh'),
    62002: itemData(IC.useful, 1, 'wh3_main_sla_cav_heartseekers_of_slaanesh_0', itemType.unit, 3, 'Progressive chs_cav', 'Chaos Unit: Heartseekers of Slaanesh'),

    62003: itemData(IC.useful, 1, 'wh3_dlc27_chs_cha_exalted_hero_msla', itemType.unit, 1, 'Progressive chs_hro', 'Chaos Unit: Exalted Hero of Slaanesh'),
    62004: itemData(IC.useful, 1, 'wh3_dlc20_chs_cha_chaos_sorcerer_shadows_msla', itemType.unit, 1, 'Progressive chs_hro', 'Chaos Unit: Chaos Sorcerer of Slaanesh (Shadows)'),
    62005: itemData(IC.useful, 1, 'wh3_dlc20_chs_cha_chaos_sorcerer_slaanesh_msla', itemType.unit, 1, 'Progressive chs_hro', 'Chaos Unit: Chaos Sorcerer of Slaanesh (Slaanesh)'),

    62006: itemData(IC.useful, 1, 'wh3_twa06_sla_inf_daemonette_ror_0', itemType.unit, 3, 'Progressive chs_inf', 'Chaos Unit: Bringers of Beguilement (Exalted Daemonettes of Slaanesh)'),
    62007: itemData(IC.useful, 1, 'wh3_twa07_sla_cav_heartseekers_of_slaanesh_ror_0', itemType.unit, 3, 'Progressive chs_cav', 'Chaos Unit: Eternal Entourage (Heartseekers of Slaanesh)'),

})

buildings: dict[int, itemData] = warriorsOfChaos.buildings

techs: dict[int, itemData] = {
62800: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_marks_slaanesh', itemType.tech, 1, 'Progressive tech_chs_sla_slaanesh', 'Chaos Slaanesh Tech: Sensuous Branding Iron'),
62801: itemData(IC.useful, 1, 'wh3_dlc20_chs_sla_shared_gift_upgrade_authority', itemType.tech, 2, 'Progressive tech_chs_sla_slaanesh', 'Chaos Slaanesh Tech: Echo Chamber'),
62802: itemData(IC.useful, 1, 'wh3_dlc20_chs_sla_shared_gift_upgrade_corruption', itemType.tech, 3, 'Progressive tech_chs_sla_slaanesh', 'Chaos Slaanesh Tech: Corrupted Offerings'),
62803: itemData(IC.useful, 1, 'wh3_dlc20_chs_sla_azazel_buildings', itemType.tech, 4, 'Progressive tech_chs_sla_slaanesh', 'Chaos Slaanesh Tech: Debauched Designs'),
62804: itemData(IC.useful, 1, 'wh3_dlc20_chs_sla_azazel_gift_slot_2', itemType.tech, 5, 'Progressive tech_chs_sla_slaanesh', 'Chaos Slaanesh Tech: Sensuous Gifts'),
62805: itemData(IC.useful, 1, 'wh3_dlc20_chs_sla_azazel_heroes_lords', itemType.tech, 6, 'Progressive tech_chs_sla_slaanesh', "Chaos Slaanesh Tech: Sensation's Call"),
62806: itemData(IC.useful, 1, 'wh3_dlc20_chs_sla_shared_gift_upgrade_diplomacy', itemType.tech, 6, 'Progressive tech_chs_sla_slaanesh', 'Chaos Slaanesh Tech: Herald of Sacrifice'),
62807: itemData(IC.useful, 1, 'wh3_dlc20_chs_sla_azazel_mark', itemType.tech, 7, 'Progressive tech_chs_sla_slaanesh', 'Chaos Slaanesh Tech: Unholy Aid'),
62808: itemData(IC.useful, 1, 'wh3_dlc20_chs_sla_azazel_military_1', itemType.tech, 3, 'Progressive tech_chs_sla_slaanesh', 'Chaos Slaanesh Tech: Pleasure Altars'),
62809: itemData(IC.useful, 1, 'wh3_dlc20_chs_sla_azazel_spells', itemType.tech, 4, 'Progressive tech_chs_sla_slaanesh', 'Chaos Slaanesh Tech: Flesh-Bound Book'),
62810: itemData(IC.useful, 1, 'wh3_dlc20_chs_sla_azazel_gift_slot_1', itemType.tech, 5, 'Progressive tech_chs_sla_slaanesh', 'Chaos Slaanesh Tech: Vows of Excess'),
62811: itemData(IC.useful, 1, 'wh3_dlc20_chs_sla_azazel_weapons', itemType.tech, 6, 'Progressive tech_chs_sla_slaanesh', 'Chaos Slaanesh Tech: Vicious Lash'),
62812: itemData(IC.useful, 1, 'wh3_dlc20_chs_sla_shared_gift_upgrade_summons', itemType.tech, 6, 'Progressive tech_chs_sla_slaanesh', 'Chaos Slaanesh Tech: Summons of Slaanesh'),
62813: itemData(IC.useful, 1, 'wh3_dlc20_chs_sla_azazel_military_2', itemType.tech, 7, 'Progressive tech_chs_sla_slaanesh', 'Chaos Slaanesh Tech: Urgent Whispers'),
62814: itemData(IC.useful, 1, 'wh3_dlc20_chs_sla_azazel_gift_slot_3', itemType.tech, 8, 'Progressive tech_chs_sla_slaanesh', 'Chaos Slaanesh Tech: Blessings of Slaanesh'),
62815: itemData(IC.useful, 1, 'wh3_dlc20_chs_sla_azazel_ultimate', itemType.tech, 9, 'Progressive tech_chs_sla_slaanesh', 'Chaos Slaanesh Tech: Daemonic Aid'),

62816: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_marauders', itemType.tech, 1, 'Progressive tech_chs_sla_undivided', 'Chaos Slaanesh Tech: Scrutiny of the Dark Gods'),
62817: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_chariots', itemType.tech, 2, 'Progressive tech_chs_sla_undivided', 'Chaos Slaanesh Tech: Charioteer'),
62818: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_mutants', itemType.tech, 3, 'Progressive tech_chs_sla_undivided', 'Chaos Slaanesh Tech: A Thousand Twisted Blessings'),
62819: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_chosen', itemType.tech, 3, 'Progressive tech_chs_sla_undivided', 'Chaos Slaanesh Tech: Rite of Ascension'),
62820: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_diplomacy', itemType.tech, 4, 'Progressive tech_chs_sla_undivided', 'Chaos Slaanesh Tech: Dark Diplomacy'),
62821: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_movement', itemType.tech, 4, 'Progressive tech_chs_sla_undivided', 'Chaos Slaanesh Tech: Infernal March'),
62822: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_gift_slot_1', itemType.tech, 5, 'Progressive tech_chs_sla_undivided', 'Chaos Slaanesh Tech: Daemonic Pact'),
62823: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_knights', itemType.tech, 5, 'Progressive tech_chs_sla_undivided', 'Chaos Slaanesh Tech: Profane Weaponry'),
62824: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_daemonic_mounts', itemType.tech, 6, 'Progressive tech_chs_sla_undivided', 'Chaos Slaanesh Tech: Daemon Mounts'),
62825: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_corruption', itemType.tech, 5, 'Progressive tech_chs_sla_undivided', 'Chaos Slaanesh Tech: Malignant Totems'),
62826: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_vassals', itemType.tech, 6, 'Progressive tech_chs_sla_undivided', 'Chaos Slaanesh Tech: Slaves to Darkness'),
62827: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_beasts', itemType.tech, 6, 'Progressive tech_chs_sla_undivided', 'Chaos Slaanesh Tech: Unchained Beasts'),
62828: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_building', itemType.tech, 6, 'Progressive tech_chs_sla_undivided', 'Chaos Slaanesh Tech: Erection of Ruinous Monuments'),
62829: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_upgrades', itemType.tech, 6, 'Progressive tech_chs_sla_undivided', 'Chaos Slaanesh Tech: Inscribed Chaos Armour'),
62830: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_souls', itemType.tech, 6, 'Progressive tech_chs_sla_undivided', 'Chaos Slaanesh Tech: Culling of the Weak'),
62831: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_monsters', itemType.tech, 7, 'Progressive tech_chs_sla_undivided', 'Chaos Slaanesh Tech: Giant Manacles'),
62832: itemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_gift_slot_2', itemType.tech, 8, 'Progressive tech_chs_sla_undivided', 'Chaos Slaanesh Tech: Gaze of the Dark Gods'),
}

progUnits: dict[int, itemData] = warriorsOfChaos.progUnits

progBuildings: dict[int, itemData] = warriorsOfChaos.progBuildings

progTechs: dict[int, itemData] = {
    63400: itemData(IC.useful, 9, "Progressive tech_chs_sla_undivided", itemType.tech, 8, None, "Progressive Chaos Slaanesh Tech: Undivided"),
    63401: itemData(IC.useful, 9, "Progressive tech_chs_sla_slaanesh", itemType.tech, 9, None, "Progressive Chaos Slaanesh Tech: Slaanesh"),
}

special: dict[int, itemData] = {

}

rituals = warriorsOfChaos.rituals