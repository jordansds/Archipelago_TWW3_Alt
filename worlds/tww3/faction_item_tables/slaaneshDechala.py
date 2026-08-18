from BaseClasses import ItemClassification as IC
from worlds.tww3.dataStructs import itemType, itemData, specialItemData
from . import slaanesh
# @formatter:off

units: dict[int, itemData] = slaanesh.units

buildings: dict[int, itemData] = {
    70400: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_characters_1', itemType.building, 0, 'Progressive sla_palace_agents', 'Dechala Palace: Favoured Quarters'),
    70401: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_characters_2', itemType.building, 1, 'Progressive sla_palace_agents', 'Dechala Palace: Halls of Exaltation'),
    70402: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_characters_3', itemType.building, 2, 'Progressive sla_palace_agents', 'Dechala Palace: Grand Thermae'),
    70403: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_daemon_rupture_1', itemType.building, 0, 'Progressive sla_palace_daemons', 'Dechala Palace: Altar of Dissolution'),
    70404: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_daemon_rupture_2', itemType.building, 1, 'Progressive sla_palace_daemons', 'Dechala Palace: Daemonic Rupture'),
    70405: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_daemonic_mounts_1', itemType.building, 0, 'Progressive sla_palace_chariots', 'Dechala Palace: Divine Circus'),
    70406: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_daemonic_mounts_2', itemType.building, 1, 'Progressive sla_palace_chariots', 'Dechala Palace: Rapturous Circus'),
    70407: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_daemonic_mounts_3', itemType.building, 2, 'Progressive sla_palace_chariots', 'Dechala Palace: Exalted Circus'),
    70408: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_dechala_1', itemType.building, 0, 'Progressive sla_palace_egotism', 'Dechala Palace: Private Chambers'),
    70409: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_dechala_2', itemType.building, 1, 'Progressive sla_palace_egotism', 'Dechala Palace: Drifting Tower'),
    70410: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_exemplars_1', itemType.building, 0, 'Progressive sla_palace_seekers', 'Dechala Palace: Palatial Wing'),
    70411: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_exemplars_2', itemType.building, 1, 'Progressive sla_palace_seekers', 'Dechala Palace: Drifting Forge'),
    70412: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_exemplars_3', itemType.building, 2, 'Progressive sla_palace_seekers', 'Dechala Palace: Drifting Bastion'),
    70413: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_greater_servants_1', itemType.building, 0, 'Progressive sla_palace_servants', 'Dechala Palace: Sensuous Caress'),
    70414: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_greater_servants_2', itemType.building, 1, 'Progressive sla_palace_servants', 'Dechala Palace: Tormented Whisper'),
    70415: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_greater_servants_3', itemType.building, 2, 'Progressive sla_palace_servants', 'Dechala Palace: Daemonic Lure'),
    70416: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_mortal_riders_1', itemType.building, 0, 'Progressive sla_palace_riders', 'Dechala Palace: Challenge Stone'),
    70417: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_mortal_riders_2', itemType.building, 1, 'Progressive sla_palace_riders', 'Dechala Palace: Arena of Excess'),
    70418: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_research_1', itemType.building, 0, 'Progressive sla_palace_research', "Dechala Palace: Flenser's Workshop"),
    70419: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_research_2', itemType.building, 1, 'Progressive sla_palace_research', 'Dechala Palace: Halls of Sensation'),
    70420: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_research_3', itemType.building, 2, 'Progressive sla_palace_research', 'Dechala Palace: Sensatorium'),
    70421: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_rituals_1', itemType.building, 0, 'Progressive sla_palace_rituals', 'Dechala Palace: Pain Vaults'),
    70422: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_rituals_2', itemType.building, 1, 'Progressive sla_palace_rituals', "Dechala Palace: Sorcerer's Halls"),
    70423: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_settlement_1', itemType.building, 0, 'Progressive sla_settlement_major', 'Dechala Palace: Pleasure Palace'),
    70424: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_settlement_2', itemType.building, 1, 'Progressive sla_settlement_major', 'Dechala Palace: Wing of Sensation'),
    70425: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_settlement_3', itemType.building, 2, 'Progressive sla_settlement_major', 'Dechala Palace: Wing of Indulgence'),
    70426: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_settlement_4', itemType.building, 3, 'Progressive sla_settlement_major', 'Dechala Palace: Wing of Satisfaction'),
    70427: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_settlement_5', itemType.building, 4, 'Progressive sla_settlement_major', 'Dechala Palace: Wing of Perfection'),
    70428: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_tribute_1', itemType.building, 0, 'Progressive sla_palace_tribute', 'Dechala Palace: Vestibule of Tithing'),
    70429: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_tribute_2', itemType.building, 1, 'Progressive sla_palace_tribute', 'Dechala Palace: Chambers of Circumduction'),
    70430: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_tribute_3', itemType.building, 2, 'Progressive sla_palace_tribute', 'Dechala Palace: Lavish Hippodrome'),
    70431: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_walls_1', itemType.building, 0, 'Progressive sla_palace_walls', 'Dechala Palace: Dizzying Battlements'),
    70432: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_walls_2', itemType.building, 1, 'Progressive sla_palace_walls', 'Dechala Palace: Opulent Barbican'),
    70433: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_walls_3', itemType.building, 2, 'Progressive sla_palace_walls', 'Dechala Palace: Sonorous Ramparts'),
    70434: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_warrior_halls_1', itemType.building, 0, 'Progressive sla_palace_warriors', 'Dechala Palace: Halls of Strife & Succour'),
    70435: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_warrior_halls_2', itemType.building, 1, 'Progressive sla_palace_warriors', 'Dechala Palace: Halls of Blade & Lash'),

    70436: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_thrall_camp_garrison_1', itemType.building, 0, 'Progressive sla_thrall_camp_garrison', 'Dechala Thrall Camp: Forbidding Fastness'),
    70437: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_thrall_camp_garrison_2', itemType.building, 1, 'Progressive sla_thrall_camp_garrison', 'Dechala Thrall Camp: Watchposts'),
    70438: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_thrall_camp_income_1', itemType.building, 0, 'Progressive sla_thrall_camp_income', "Dechala Thrall Camp: Carvers' Cages"),
    70439: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_thrall_camp_income_2', itemType.building, 1, 'Progressive sla_thrall_camp_income', 'Dechala Thrall Camp: Asylum of Craftsmen'),
    70440: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_thrall_camp_income_3', itemType.building, 2, 'Progressive sla_thrall_camp_income', 'Dechala Thrall Camp: Monument of Toil'),
    70441: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_thrall_camp_palace_support_1', itemType.building, 0, 'Progressive sla_thrall_camp_support', 'Dechala Thrall Camp: Field Treatment'),
    70442: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_thrall_camp_palace_support_2', itemType.building, 1, 'Progressive sla_thrall_camp_support', 'Dechala Thrall Camp: Rest & Respite'),
    70443: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_thrall_camp_palace_support_3', itemType.building, 2, 'Progressive sla_thrall_camp_support', "Dechala Thrall Camp: Surgeon's Racks"),
    70444: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_thrall_camp_settlement_1', itemType.building, 0, 'Progressive sla_settlement_minor', 'Dechala Thrall Camp: Thrall Pens'),
    70445: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_thrall_camp_settlement_2', itemType.building, 1, 'Progressive sla_settlement_minor', 'Dechala Thrall Camp: Thrall Dens'),
    70446: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_thrall_camp_settlement_3', itemType.building, 2, 'Progressive sla_settlement_minor', 'Dechala Thrall Camp: Thrall Compound'),
    70447: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_thrall_camp_thrall_export_1', itemType.building, 0, 'Progressive sla_thrall_camp_export', 'Dechala Thrall Camp: The Toll'),
    70448: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_thrall_camp_thrall_export_2', itemType.building, 1, 'Progressive sla_thrall_camp_export', 'Dechala Thrall Camp: The Exodus'),

    70449: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_corruption_1', itemType.building, 0, 'Progressive sla_war_pit_corruption', "Dechala Tormentor's Hold: Ring of Steel"),
    70450: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_corruption_2', itemType.building, 1, 'Progressive sla_war_pit_corruption', "Dechala Tormentor's Hold: Ring of Pain"),
    70451: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_local_army_1', itemType.building, 0, 'Progressive sla_war_pit_army', "Dechala Tormentor's Hold: Warhost Supplies"),
    70452: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_local_army_2', itemType.building, 1, 'Progressive sla_war_pit_army', "Dechala Tormentor's Hold: Warhost Outpost"),
    70453: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_local_army_3', itemType.building, 2, 'Progressive sla_war_pit_army', "Dechala Tormentor's Hold: Warhost Fort"),
    70454: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_mortal_barracks_1', itemType.building, 0, 'Progressive sla_war_pit_mortal_barracks', "Dechala Tormentor's Hold: Marauders' Hold"),
    70455: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_mortal_barracks_2', itemType.building, 1, 'Progressive sla_war_pit_mortal_barracks', "Dechala Tormentor's Hold: Scourge Racks"),
    70456: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_mortal_barracks_3', itemType.building, 2, 'Progressive sla_war_pit_mortal_barracks', "Dechala Tormentor's Hold: Chaos Warriors' Quarters"),
    70457: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_settlement_1', itemType.building, 0, 'Progressive sla_settlement_minor', "Dechala Tormentor's Hold: Tormentors' Hold"),
    70458: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_settlement_2', itemType.building, 1, 'Progressive sla_settlement_minor', "Dechala Tormentor's Hold: Enclave of the Killing Arts"),
    70459: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_settlement_3', itemType.building, 2, 'Progressive sla_settlement_minor', "Dechala Tormentor's Hold: Ritual Arena"),
    70460: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_stables_1', itemType.building, 0, 'Progressive sla_war_pit_stables', "Dechala Tormentor's Hold: Hellstrider Pens"),
    70461: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_stables_2', itemType.building, 1, 'Progressive sla_war_pit_stables', "Dechala Tormentor's Hold: Hellscourge Cages"),
    70462: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_stables_3', itemType.building, 2, 'Progressive sla_war_pit_stables', "Dechala Tormentor's Hold: Sibilant Stables"),
    70463: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_twisted_barracks_1', itemType.building, 0, 'Progressive sla_war_pit_barracks', "Dechala Tormentor's Hold: Shrine of Decadence"),
    70464: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_twisted_barracks_2', itemType.building, 1, 'Progressive sla_war_pit_barracks', "Dechala Tormentor's Hold: Abbey of Decadence"),
    70465: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_twisted_barracks_3', itemType.building, 2, 'Progressive sla_war_pit_barracks', "Dechala Tormentor's Hold: Temple of Decadence"),
    70466: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_walls_1', itemType.building, 0, 'Progressive sla_war_pit_walls', "Dechala Tormentor's Hold: Sentinel Fields"),
    70467: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_walls_2', itemType.building, 1, 'Progressive sla_war_pit_walls', "Dechala Tormentor's Hold: Spiked Watchposts"),
    70468: itemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_walls_3', itemType.building, 2, 'Progressive sla_war_pit_walls', "Dechala Tormentor's Hold: Battle Halls"),

    70469: itemData(IC.useful, 1, 'wh3_dlc27_sla_tormentors_port_1', itemType.building, 0, 'Progressive sla_port', "Dechala Building: Enclave Port"),
    70470: itemData(IC.useful, 1, 'wh3_dlc27_sla_tormentors_port_2', itemType.building, 1, 'Progressive sla_port', "Dechala Building: Thrallport"),
    70471: itemData(IC.useful, 1, 'wh3_dlc27_sla_tormentors_port_3', itemType.building, 2, 'Progressive sla_port', "Dechala Building: Grand Thrallport"),
    70472: itemData(IC.useful, 1, 'wh3_main_foreign_slot_discovery_sla_1', itemType.building, 0, 'Progressive sla_foreign_slot_discovery', "Dechala Building: Warpstone Locus"),
    70473: itemData(IC.useful, 1, 'wh3_main_foreign_slot_discovery_sla_2', itemType.building, 1, 'Progressive sla_foreign_slot_discovery', "Dechala Building: Warpstone Traps"),
    70474: itemData(IC.useful, 1, 'wh3_main_foreign_slot_discovery_sla_3', itemType.building, 2, 'Progressive sla_foreign_slot_discovery', "Dechala Building: Guarded Warpstone"),

    70475: itemData(IC.useful, 1, 'wh3_main_sla_cult_1', itemType.building, 0, 'Progressive sla_cult', 'Dechala Building: Devotee Enticement'),
    70476: itemData(IC.useful, 1, 'wh3_main_sla_cult_2', itemType.building, 0, 'Progressive sla_cult', 'Dechala Building: Charm Offensive'),
    70477: itemData(IC.useful, 1, 'wh3_main_sla_cult_3', itemType.building, 0, 'Progressive sla_cult', 'Dechala Building: Lure of Slaanesh'),
    70478: itemData(IC.useful, 1, 'wh3_main_sla_cult_4', itemType.building, 0, 'Progressive sla_cult', 'Dechala Building: Ritual of the Disciples'),
    70479: itemData(IC.useful, 1, 'wh3_main_sla_cult_corruption_1', itemType.building, 0, 'Progressive sla_cult_corruption', 'Dechala Building: Words of Temptation'),
    70480: itemData(IC.useful, 1, 'wh3_main_sla_cult_corruption_2', itemType.building, 0, 'Progressive sla_cult_corruption', 'Dechala Building: Population Preparation'),
    70481: itemData(IC.useful, 1, 'wh3_main_sla_cult_magus', itemType.building, 0, 'Progressive sla_cult_extra', 'Dechala Building: Cult Magus Chambers'),
    70482: itemData(IC.useful, 1, 'wh3_main_sla_cult_special', itemType.building, 0, 'Progressive sla_cult_extra', 'Dechala Building: Ritual of Excess'),
    70483: itemData(IC.useful, 1, 'wh3_main_sla_cult_teleport', itemType.building, 0, 'Progressive sla_cult_extra', 'Dechala Building: Ritual of Summoning'),
}

techs: dict[int, itemData] = slaanesh.techs
techs.update({
    70800: itemData(IC.useful, 1, 'wh3_dlc27_tech_sla_grasp_of_servitude', itemType.tech, 1, 'Progressive tech_sla_perfume_dechala', "Slaanesh Tech: Servitude's Grasp"),
    70801: itemData(IC.useful, 1, 'wh3_dlc27_tech_sla_caress_of_slaanesh', itemType.tech, 2, 'Progressive tech_sla_perfume_dechala', 'Slaanesh Tech: Boons of Slaanesh'),
    70802: itemData(IC.useful, 1, 'wh3_dlc27_tech_sla_dark_domination', itemType.tech, 2, 'Progressive tech_sla_perfume_dechala', 'Slaanesh Tech: Dark Domination'),
    70803: itemData(IC.useful, 1, 'wh3_dlc27_tech_sla_dominate_units', itemType.tech, 2, 'Progressive tech_sla_perfume_dechala', 'Slaanesh Tech: Arrogant Dismissal'),
    70804: itemData(IC.useful, 1, 'wh3_dlc27_tech_sla_in_praise_of_slaanesh', itemType.tech, 2, 'Progressive tech_sla_perfume_dechala', 'Slaanesh Tech: In Praise of Slaanesh'),
    70805: itemData(IC.useful, 1, 'wh3_dlc27_tech_sla_daemonic_attraction', itemType.tech, 3, 'Progressive tech_sla_perfume_dechala', 'Slaanesh Tech: Daemonic Attraction'),
})

progUnits: dict[int, itemData] = slaanesh.progUnits

progBuildings: dict[int, itemData] = {
    71300: itemData(IC.useful, 3, 'Progressive sla_palace_agents', itemType.building, 3, None, 'Progressive Dechala Palace: Lords & Agents'),
    71301: itemData(IC.useful, 2, 'Progressive sla_palace_daemons', itemType.building, 2, None, 'Progressive Dechala Palace: Daemon Portal'),
    71302: itemData(IC.useful, 2, 'Progressive sla_palace_chariots', itemType.building, 2, None, 'Progressive Dechala Palace: Daemonic Mounts'),
    71303: itemData(IC.useful, 2, 'Progressive sla_palace_egotism', itemType.building, 2, None, 'Progressive Dechala Palace: Egotism'),
    71304: itemData(IC.useful, 2, 'Progressive sla_palace_seekers', itemType.building, 2, None, 'Progressive Dechala Palace: Exemplars of Excess'),
    71305: itemData(IC.useful, 2, 'Progressive sla_palace_servants', itemType.building, 2, None, 'Progressive Dechala Palace: Greater Servants'),
    71306: itemData(IC.useful, 2, 'Progressive sla_palace_riders', itemType.building, 2, None, 'Progressive Dechala Palace: Mortal Riders'),
    71307: itemData(IC.useful, 2, 'Progressive sla_palace_research', itemType.building, 2, None, 'Progressive Dechala Palace: Innovative Pleasures'),
    71308: itemData(IC.useful, 2, 'Progressive sla_palace_rituals', itemType.building, 2, None, 'Progressive Dechala Palace: Pain & Power'),
    71309: itemData(IC.useful, 2, 'Progressive sla_sla_settlement_major', itemType.building, 2, None, 'Progressive Dechala Palace: Settlement Major'),
    71310: itemData(IC.useful, 2, 'Progressive sla_palace_tribute', itemType.building, 2, None, 'Progressive Dechala Palace: Lavish Gifts'),
    71311: itemData(IC.useful, 2, 'Progressive sla_palace_walls', itemType.building, 2, None, 'Progressive Dechala Palace: Palace Walls'),
    71312: itemData(IC.useful, 2, 'Progressive sla_palace_warriors', itemType.building, 2, None, 'Progressive Dechala Palace: Warrior Halls'),

    71313: itemData(IC.useful, 2, 'Progressive sla_thrall_camp_garrison', itemType.building, 2, None, 'Progressive Dechala Thrall Camp: Garrison'),
    71314: itemData(IC.useful, 2, 'Progressive sla_thrall_camp_income', itemType.building, 2, None, 'Progressive Dechala Thrall Camp: Toil'),
    71315: itemData(IC.useful, 2, 'Progressive sla_thrall_camp_support', itemType.building, 2, None, 'Progressive Dechala Thrall Camp: Service'),
    71316: itemData(IC.useful, 2, 'Progressive sla_settlement_minor', itemType.building, 2, None, 'Progressive Dechala Thrall Camp: Settlement Minor'),
    71317: itemData(IC.useful, 2, 'Progressive sla_thrall_camp_export', itemType.building, 2, None, 'Progressive Dechala Thrall Camp: Toll'),

    71318: itemData(IC.useful, 2, 'Progressive sla_war_pit_corruption', itemType.building, 2, None, "Progressive Dechala Tormentor's Hold: Ritual Combat"),
    71319: itemData(IC.useful, 3, 'Progressive sla_war_pit_army', itemType.building, 3, None, "Progressive Dechala Tormentor's Hold: Warhosts"),
    71320: itemData(IC.useful, 3, 'Progressive sla_war_pit_mortal_barracks', itemType.building, 3, None, "Progressive Dechala Tormentor's Hold: Mortal Servants"),
    71321: itemData(IC.useful, 3, 'Progressive sla_war_pit_stables', itemType.building, 3, None, "Progressive Dechala Tormentor's Hold: Mounted Servants"),
    71322: itemData(IC.useful, 3, 'Progressive sla_war_pit_barracks', itemType.building, 3, None, "Progressive Dechala Tormentor's Hold: Twisted Servants"),
    71323: itemData(IC.useful, 3, 'Progressive sla_war_pit_walls', itemType.building, 3, None, "Progressive Dechala Tormentor's Hold: Walls"),

    71324: itemData(IC.useful, 3, 'Progressive sla_port', itemType.building, 3, None, "Progressive Dechala Building: Ports"),
    71325: itemData(IC.useful, 3, 'Progressive sla_foreign_slot_discovery', itemType.building, 3, None, "Progressive Dechala Building: Foreign Slot Discovery"),
}

progTechs: dict[int, itemData] = slaanesh.progTechs
progTechs.update({
    71500: itemData(IC.useful, 3,"Progressive tech_sla_perfume_dechala", itemType.tech, 3, None, "Progressive Slaanesh Tech: Perfume of Domination"),
})

special: dict[int, specialItemData] = {

}

rituals = slaanesh.rituals