from BaseClasses import ItemClassification as IC
from worlds.tww3.item_types import ItemType, ItemData
from . import warriorsOfChaos

# @formatter:off
units: dict[int, ItemData] = warriorsOfChaos.baseUnits
units.update(warriorsOfChaos.slaaneshUnits)
units.update({
    62000: ItemData(IC.useful, 1, 'wh3_dlc27_tze_inf_slaangors', ItemType.unit, 3, 'Progressive chs_inf', 'Chs Unit: Slaangors'),
    62001: ItemData(IC.useful, 1, 'wh3_main_sla_inf_daemonette_1', ItemType.unit, 3, 'Progressive chs_inf', 'Chs Unit: Exalted Daemonettes of Slaanesh'),
    62002: ItemData(IC.useful, 1, 'wh3_main_sla_cav_heartseekers_of_slaanesh_0', ItemType.unit, 3, 'Progressive chs_cav', 'Chs Unit: Heartseekers of Slaanesh'),

    62003: ItemData(IC.useful, 1, 'wh3_dlc27_chs_cha_exalted_hero_msla', ItemType.unit, 1, 'Progressive chs_hro', 'Chs Unit: Exalted Hero of Slaanesh'),
    62004: ItemData(IC.useful, 1, 'wh3_dlc20_chs_cha_chaos_sorcerer_shadows_msla', ItemType.unit, 1, 'Progressive chs_hro', 'Chs Unit: Chaos Sorcerer of Slaanesh (Shadows)'),
    62005: ItemData(IC.useful, 1, 'wh3_dlc20_chs_cha_chaos_sorcerer_slaanesh_msla', ItemType.unit, 1, 'Progressive chs_hro', 'Chs Unit: Chaos Sorcerer of Slaanesh (Slaanesh)'),

    62006: ItemData(IC.useful, 1, 'wh3_twa06_sla_inf_daemonette_ror_0', ItemType.unit, 3, 'Progressive chs_inf', 'Chs Unit: Bringers of Beguilement (Exalted Daemonettes of Slaanesh)'),
    62007: ItemData(IC.useful, 1, 'wh3_twa07_sla_cav_heartseekers_of_slaanesh_ror_0', ItemType.unit, 3, 'Progressive chs_cav', 'Chs Unit: Eternal Entourage (Heartseekers of Slaanesh)'),

})

buildings: dict[int, ItemData] = warriorsOfChaos.buildings

techs: dict[int, ItemData] = {
62800: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_marks_slaanesh', ItemType.tech, 1, 'Progressive tech_chs_sla_slaanesh', 'Chs Tech: Sensuous Branding Iron'),
62801: ItemData(IC.useful, 1, 'wh3_dlc20_chs_sla_shared_gift_upgrade_authority', ItemType.tech, 2, 'Progressive tech_chs_sla_slaanesh', 'Chs Tech: Echo Chamber'),
62802: ItemData(IC.useful, 1, 'wh3_dlc20_chs_sla_shared_gift_upgrade_corruption', ItemType.tech, 3, 'Progressive tech_chs_sla_slaanesh', 'Chs Tech: Corrupted Offerings'),
62803: ItemData(IC.useful, 1, 'wh3_dlc20_chs_sla_azazel_buildings', ItemType.tech, 4, 'Progressive tech_chs_sla_slaanesh', 'Chs Tech: Debauched Designs'),
62804: ItemData(IC.useful, 1, 'wh3_dlc20_chs_sla_azazel_gift_slot_2', ItemType.tech, 5, 'Progressive tech_chs_sla_slaanesh', 'Chs Tech: Sensuous Gifts'),
62805: ItemData(IC.useful, 1, 'wh3_dlc20_chs_sla_azazel_heroes_lords', ItemType.tech, 6, 'Progressive tech_chs_sla_slaanesh', "Chs Tech: Sensation's Call"),
62806: ItemData(IC.useful, 1, 'wh3_dlc20_chs_sla_shared_gift_upgrade_diplomacy', ItemType.tech, 6, 'Progressive tech_chs_sla_slaanesh', 'Chs Tech: Herald of Sacrifice'),
62807: ItemData(IC.useful, 1, 'wh3_dlc20_chs_sla_azazel_mark', ItemType.tech, 7, 'Progressive tech_chs_sla_slaanesh', 'Chs Tech: Unholy Aid'),
62808: ItemData(IC.useful, 1, 'wh3_dlc20_chs_sla_azazel_military_1', ItemType.tech, 3, 'Progressive tech_chs_sla_slaanesh', 'Chs Tech: Pleasure Altars'),
62809: ItemData(IC.useful, 1, 'wh3_dlc20_chs_sla_azazel_spells', ItemType.tech, 4, 'Progressive tech_chs_sla_slaanesh', 'Chs Tech: Flesh-Bound Book'),
62810: ItemData(IC.useful, 1, 'wh3_dlc20_chs_sla_azazel_gift_slot_1', ItemType.tech, 5, 'Progressive tech_chs_sla_slaanesh', 'Chs Tech: Vows of Excess'),
62811: ItemData(IC.useful, 1, 'wh3_dlc20_chs_sla_azazel_weapons', ItemType.tech, 6, 'Progressive tech_chs_sla_slaanesh', 'Chs Tech: Vicious Lash'),
62812: ItemData(IC.useful, 1, 'wh3_dlc20_chs_sla_shared_gift_upgrade_summons', ItemType.tech, 6, 'Progressive tech_chs_sla_slaanesh', 'Chs Tech: Summons of Slaanesh'),
62813: ItemData(IC.useful, 1, 'wh3_dlc20_chs_sla_azazel_military_2', ItemType.tech, 7, 'Progressive tech_chs_sla_slaanesh', 'Chs Tech: Urgent Whispers'),
62814: ItemData(IC.useful, 1, 'wh3_dlc20_chs_sla_azazel_gift_slot_3', ItemType.tech, 8, 'Progressive tech_chs_sla_slaanesh', 'Chs Tech: Blessings of Slaanesh'),
62815: ItemData(IC.useful, 1, 'wh3_dlc20_chs_sla_azazel_ultimate', ItemType.tech, 9, 'Progressive tech_chs_sla_slaanesh', 'Chs Tech: Daemonic Aid'),

62816: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_marauders', ItemType.tech, 1, 'Progressive tech_chs_sla_undivided', 'Chs Tech: Scrutiny of the Dark Gods'),
62817: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_chariots', ItemType.tech, 2, 'Progressive tech_chs_sla_undivided', 'Chs Tech: Charioteer'),
62818: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_mutants', ItemType.tech, 3, 'Progressive tech_chs_sla_undivided', 'Chs Tech: A Thousand Twisted Blessings'),
62819: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_chosen', ItemType.tech, 3, 'Progressive tech_chs_sla_undivided', 'Chs Tech: Rite of Ascension'),
62820: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_diplomacy', ItemType.tech, 4, 'Progressive tech_chs_sla_undivided', 'Chs Tech: Dark Diplomacy'),
62821: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_movement', ItemType.tech, 4, 'Progressive tech_chs_sla_undivided', 'Chs Tech: Infernal March'),
62822: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_gift_slot_1', ItemType.tech, 5, 'Progressive tech_chs_sla_undivided', 'Chs Tech: Daemonic Pact'),
62823: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_knights', ItemType.tech, 5, 'Progressive tech_chs_sla_undivided', 'Chs Tech: Profane Weaponry'),
62824: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_daemonic_mounts', ItemType.tech, 6, 'Progressive tech_chs_sla_undivided', 'Chs Tech: Daemon Mounts'),
62825: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_corruption', ItemType.tech, 5, 'Progressive tech_chs_sla_undivided', 'Chs Tech: Malignant Totems'),
62826: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_vassals', ItemType.tech, 6, 'Progressive tech_chs_sla_undivided', 'Chs Tech: Slaves to Darkness'),
62827: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_beasts', ItemType.tech, 6, 'Progressive tech_chs_sla_undivided', 'Chs Tech: Unchained Beasts'),
62828: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_building', ItemType.tech, 6, 'Progressive tech_chs_sla_undivided', 'Chs Tech: Erection of Ruinous Monuments'),
62829: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_upgrades', ItemType.tech, 6, 'Progressive tech_chs_sla_undivided', 'Chs Tech: Inscribed Chaos Armour'),
62830: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_souls', ItemType.tech, 6, 'Progressive tech_chs_sla_undivided', 'Chs Tech: Culling of the Weak'),
62831: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_monsters', ItemType.tech, 7, 'Progressive tech_chs_sla_undivided', 'Chs Tech: Giant Manacles'),
62832: ItemData(IC.useful, 1, 'wh3_dlc20_chs_und_shared_gift_slot_2', ItemType.tech, 8, 'Progressive tech_chs_sla_undivided', 'Chs Tech: Gaze of the Dark Gods'),
}

progUnits: dict[int, ItemData] = warriorsOfChaos.progUnits

progBuildings: dict[int, ItemData] = warriorsOfChaos.progBuildings

progTechs: dict[int, ItemData] = {
    63400: ItemData(IC.useful, 9, "Progressive tech_chs_sla_undivided", ItemType.tech, 8, None, "Progressive Chs Tech: Undivided"),
    63401: ItemData(IC.useful, 9, "Progressive tech_chs_sla_slaanesh", ItemType.tech, 9, None, "Progressive Chs Tech: Slaanesh"),
}

special: dict[int, ItemData] = {

}