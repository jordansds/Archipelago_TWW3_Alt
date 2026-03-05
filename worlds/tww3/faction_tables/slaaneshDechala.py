from BaseClasses import ItemClassification as IC
from worlds.tww3.item_types import ItemType, ItemData, specialItemData
from . import slaanesh
# @formatter:off

units: dict[int, ItemData] = slaanesh.units

buildings: dict[int, ItemData] = {
    70400: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_characters_1', ItemType.building, 0, 'Progressive sla_palace_agents', 'Sla DechalaPalace: Favoured Quarters'),
    70401: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_characters_2', ItemType.building, 1, 'Progressive sla_palace_agents', 'Sla DechalaPalace: Halls of Exaltation'),
    70402: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_characters_3', ItemType.building, 2, 'Progressive sla_palace_agents', 'Sla DechalaPalace: Grand Thermae'),
    70403: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_daemon_rupture_1', ItemType.building, 0, 'Progressive sla_palace_daemons', 'Sla DechalaPalace: Altar of Dissolution'),
    70404: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_daemon_rupture_2', ItemType.building, 1, 'Progressive sla_palace_daemons', 'Sla DechalaPalace: Daemonic Rupture'),
    70405: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_daemonic_mounts_1', ItemType.building, 0, 'Progressive sla_palace_chariots', 'Sla DechalaPalace: Divine Circus'),
    70406: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_daemonic_mounts_2', ItemType.building, 1, 'Progressive sla_palace_chariots', 'Sla DechalaPalace: Rapturous Circus'),
    70407: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_daemonic_mounts_3', ItemType.building, 2, 'Progressive sla_palace_chariots', 'Sla DechalaPalace: Exalted Circus'),
    70408: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_dechala_1', ItemType.building, 0, 'Progressive sla_palace_egotism', 'Sla DechalaPalace: Private Chambers'),
    70409: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_dechala_2', ItemType.building, 1, 'Progressive sla_palace_egotism', 'Sla DechalaPalace: Drifting Tower'),
    70410: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_exemplars_1', ItemType.building, 0, 'Progressive sla_palace_seekers', 'Sla DechalaPalace: Palatial Wing'),
    70411: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_exemplars_2', ItemType.building, 1, 'Progressive sla_palace_seekers', 'Sla DechalaPalace: Drifting Forge'),
    70412: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_exemplars_3', ItemType.building, 2, 'Progressive sla_palace_seekers', 'Sla DechalaPalace: Drifting Bastion'),
    70413: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_greater_servants_1', ItemType.building, 0, 'Progressive sla_palace_servants', 'Sla DechalaPalace: Sensuous Caress'),
    70414: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_greater_servants_2', ItemType.building, 1, 'Progressive sla_palace_servants', 'Sla DechalaPalace: Tormented Whisper'),
    70415: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_greater_servants_3', ItemType.building, 2, 'Progressive sla_palace_servants', 'Sla DechalaPalace: Daemonic Lure'),
    70416: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_mortal_riders_1', ItemType.building, 0, 'Progressive sla_palace_riders', 'Sla DechalaPalace: Challenge Stone'),
    70417: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_mortal_riders_2', ItemType.building, 1, 'Progressive sla_palace_riders', 'Sla DechalaPalace: Arena of Excess'),
    70418: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_research_1', ItemType.building, 0, 'Progressive sla_palace_research', "Sla DechalaPalace: Flenser's Workshop"),
    70419: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_research_2', ItemType.building, 1, 'Progressive sla_palace_research', 'Sla DechalaPalace: Halls of Sensation'),
    70420: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_research_3', ItemType.building, 2, 'Progressive sla_palace_research', 'Sla DechalaPalace: Sensatorium'),
    70421: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_rituals_1', ItemType.building, 0, 'Progressive sla_palace_rituals', 'Sla DechalaPalace: Pain Vaults'),
    70422: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_rituals_2', ItemType.building, 1, 'Progressive sla_palace_rituals', "Sla DechalaPalace: Sorcerer's Halls"),
    70423: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_settlement_1', ItemType.building, 0, 'Progressive sla_settlement_major', 'Sla DechalaPalace: Pleasure Palace'),
    70424: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_settlement_2', ItemType.building, 1, 'Progressive sla_settlement_major', 'Sla DechalaPalace: Wing of Sensation'),
    70425: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_settlement_3', ItemType.building, 2, 'Progressive sla_settlement_major', 'Sla DechalaPalace: Wing of Indulgence'),
    70426: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_settlement_4', ItemType.building, 3, 'Progressive sla_settlement_major', 'Sla DechalaPalace: Wing of Satisfaction'),
    70427: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_settlement_5', ItemType.building, 4, 'Progressive sla_settlement_major', 'Sla DechalaPalace: Wing of Perfection'),
    70428: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_tribute_1', ItemType.building, 0, 'Progressive sla_palace_tribute', 'Sla DechalaPalace: Vestibule of Tithing'),
    70429: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_tribute_2', ItemType.building, 1, 'Progressive sla_palace_tribute', 'Sla DechalaPalace: Chambers of Circumduction'),
    70430: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_tribute_3', ItemType.building, 2, 'Progressive sla_palace_tribute', 'Sla DechalaPalace: Lavish Hippodrome'),
    70431: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_walls_1', ItemType.building, 0, 'Progressive sla_palace_walls', 'Sla DechalaPalace: Dizzying Battlements'),
    70432: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_walls_2', ItemType.building, 1, 'Progressive sla_palace_walls', 'Sla DechalaPalace: Opulent Barbican'),
    70433: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_walls_3', ItemType.building, 2, 'Progressive sla_palace_walls', 'Sla DechalaPalace: Sonorous Ramparts'),
    70434: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_warrior_halls_1', ItemType.building, 0, 'Progressive sla_palace_warriors', 'Sla DechalaPalace: Halls of Strife & Succour'),
    70435: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_palace_warrior_halls_2', ItemType.building, 1, 'Progressive sla_palace_warriors', 'Sla DechalaPalace: Halls of Blade & Lash'),

    70436: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_thrall_camp_garrison_1', ItemType.building, 0, 'Progressive sla_thrall_camp_garrison', 'Sla DechalaThrall Camp: Forbidding Fastness'),
    70437: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_thrall_camp_garrison_2', ItemType.building, 1, 'Progressive sla_thrall_camp_garrison', 'Sla DechalaThrall Camp: Watchposts'),
    70438: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_thrall_camp_income_1', ItemType.building, 0, 'Progressive sla_thrall_camp_income', "Sla DechalaThrall Camp: Carvers' Cages"),
    70439: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_thrall_camp_income_2', ItemType.building, 1, 'Progressive sla_thrall_camp_income', 'Sla DechalaThrall Camp: Asylum of Craftsmen'),
    70440: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_thrall_camp_income_3', ItemType.building, 2, 'Progressive sla_thrall_camp_income', 'Sla DechalaThrall Camp: Monument of Toil'),
    70441: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_thrall_camp_palace_support_1', ItemType.building, 0, 'Progressive sla_thrall_camp_support', 'Sla DechalaThrall Camp: Field Treatment'),
    70442: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_thrall_camp_palace_support_2', ItemType.building, 1, 'Progressive sla_thrall_camp_support', 'Sla DechalaThrall Camp: Rest & Respite'),
    70443: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_thrall_camp_palace_support_3', ItemType.building, 2, 'Progressive sla_thrall_camp_support', "Sla DechalaThrall Camp: Surgeon's Racks"),
    70444: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_thrall_camp_settlement_1', ItemType.building, 0, 'Progressive sla_settlement_minor', 'Sla DechalaThrall Camp: Thrall Pens'),
    70445: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_thrall_camp_settlement_2', ItemType.building, 1, 'Progressive sla_settlement_minor', 'Sla DechalaThrall Camp: Thrall Dens'),
    70446: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_thrall_camp_settlement_3', ItemType.building, 2, 'Progressive sla_settlement_minor', 'Sla DechalaThrall Camp: Thrall Compound'),
    70447: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_thrall_camp_thrall_export_1', ItemType.building, 0, 'Progressive sla_thrall_camp_export', 'Sla DechalaThrall Camp: The Toll'),
    70448: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_thrall_camp_thrall_export_2', ItemType.building, 1, 'Progressive sla_thrall_camp_export', 'Sla DechalaThrall Camp: The Exodus'),

    70449: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_corruption_1', ItemType.building, 0, 'Progressive sla_war_pit_corruption', "Sla DechalaTormentor's Hold: Ring of Steel"),
    70450: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_corruption_2', ItemType.building, 1, 'Progressive sla_war_pit_corruption', "Sla DechalaTormentor's Hold: Ring of Pain"),
    70451: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_local_army_1', ItemType.building, 0, 'Progressive sla_war_pit_army', "Sla DechalaTormentor's Hold: Warhost Supplies"),
    70452: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_local_army_2', ItemType.building, 1, 'Progressive sla_war_pit_army', "Sla DechalaTormentor's Hold: Warhost Outpost"),
    70453: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_local_army_3', ItemType.building, 2, 'Progressive sla_war_pit_army', "Sla DechalaTormentor's Hold: Warhost Fort"),
    70454: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_mortal_barracks_1', ItemType.building, 0, 'Progressive sla_war_pit_mortal_barracks', "Sla DechalaTormentor's Hold: Marauders' Hold"),
    70455: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_mortal_barracks_2', ItemType.building, 1, 'Progressive sla_war_pit_mortal_barracks', "Sla DechalaTormentor's Hold: Scourge Racks"),
    70456: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_mortal_barracks_3', ItemType.building, 2, 'Progressive sla_war_pit_mortal_barracks', "Sla DechalaTormentor's Hold: Chaos Warriors' Quarters"),
    70457: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_settlement_1', ItemType.building, 0, 'Progressive sla_settlement_minor', "Sla DechalaTormentor's Hold: Tormentors' Hold"),
    70458: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_settlement_2', ItemType.building, 1, 'Progressive sla_settlement_minor', "Sla DechalaTormentor's Hold: Enclave of the Killing Arts"),
    70459: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_settlement_3', ItemType.building, 2, 'Progressive sla_settlement_minor', "Sla DechalaTormentor's Hold: Ritual Arena"),
    70460: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_stables_1', ItemType.building, 0, 'Progressive sla_war_pit_stables', "Sla DechalaTormentor's Hold: Hellstrider Pens"),
    70461: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_stables_2', ItemType.building, 1, 'Progressive sla_war_pit_stables', "Sla DechalaTormentor's Hold: Hellscourge Cages"),
    70462: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_stables_3', ItemType.building, 2, 'Progressive sla_war_pit_stables', "Sla DechalaTormentor's Hold: Sibilant Stables"),
    70463: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_twisted_barracks_1', ItemType.building, 0, 'Progressive sla_war_pit_barracks', "Sla DechalaTormentor's Hold: Shrine of Decadence"),
    70464: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_twisted_barracks_2', ItemType.building, 1, 'Progressive sla_war_pit_barracks', "Sla DechalaTormentor's Hold: Abbey of Decadence"),
    70465: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_twisted_barracks_3', ItemType.building, 2, 'Progressive sla_war_pit_barracks', "Sla DechalaTormentor's Hold: Temple of Decadence"),
    70466: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_walls_1', ItemType.building, 0, 'Progressive sla_war_pit_walls', "Sla DechalaTormentor's Hold: Sentinel Fields"),
    70467: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_walls_2', ItemType.building, 1, 'Progressive sla_war_pit_walls', "Sla DechalaTormentor's Hold: Spiked Watchposts"),
    70468: ItemData(IC.useful, 1, 'wh3_dlc27_sla_dec_war_pit_walls_3', ItemType.building, 2, 'Progressive sla_war_pit_walls', "Sla DechalaTormentor's Hold: Battle Halls"),

    70469: ItemData(IC.useful, 1, 'wh3_dlc27_sla_tormentors_port_1', ItemType.building, 0, 'Progressive sla_port', "Sla DechalaBuilding: Enclave Port"),
    70470: ItemData(IC.useful, 1, 'wh3_dlc27_sla_tormentors_port_2', ItemType.building, 1, 'Progressive sla_port', "Sla DechalaBuilding: Thrallport"),
    70471: ItemData(IC.useful, 1, 'wh3_dlc27_sla_tormentors_port_3', ItemType.building, 2, 'Progressive sla_port', "Sla DechalaBuilding: Grand Thrallport"),
    70472: ItemData(IC.useful, 1, 'wh3_main_foreign_slot_discovery_sla_1', ItemType.building, 0, 'Progressive sla_foreign_slot_discovery', "Sla DechalaBuilding: Warpstone Locus"),
    70473: ItemData(IC.useful, 1, 'wh3_main_foreign_slot_discovery_sla_2', ItemType.building, 1, 'Progressive sla_foreign_slot_discovery', "Sla DechalaBuilding: Warpstone Traps"),
    70474: ItemData(IC.useful, 1, 'wh3_main_foreign_slot_discovery_sla_3', ItemType.building, 2, 'Progressive sla_foreign_slot_discovery', "Sla DechalaBuilding: Guarded Warpstone"),

    70475: ItemData(IC.useful, 1, 'wh3_main_sla_cult_1', ItemType.building, 0, 'Progressive sla_cult', 'Sla DechalaBuilding: Devotee Enticement'),
    70476: ItemData(IC.useful, 1, 'wh3_main_sla_cult_2', ItemType.building, 0, 'Progressive sla_cult', 'Sla DechalaBuilding: Charm Offensive'),
    70477: ItemData(IC.useful, 1, 'wh3_main_sla_cult_3', ItemType.building, 0, 'Progressive sla_cult', 'Sla DechalaBuilding: Lure of Slaanesh'),
    70478: ItemData(IC.useful, 1, 'wh3_main_sla_cult_4', ItemType.building, 0, 'Progressive sla_cult', 'Sla DechalaBuilding: Ritual of the Disciples'),
    70479: ItemData(IC.useful, 1, 'wh3_main_sla_cult_corruption_1', ItemType.building, 0, 'Progressive sla_cult_corruption', 'Sla DechalaBuilding: Words of Temptation'),
    70480: ItemData(IC.useful, 1, 'wh3_main_sla_cult_corruption_2', ItemType.building, 0, 'Progressive sla_cult_corruption', 'Sla DechalaBuilding: Population Preparation'),
    70481: ItemData(IC.useful, 1, 'wh3_main_sla_cult_magus', ItemType.building, 0, 'Progressive sla_cult_extra', 'Sla DechalaBuilding: Cult Magus Chambers'),
    70482: ItemData(IC.useful, 1, 'wh3_main_sla_cult_special', ItemType.building, 0, 'Progressive sla_cult_extra', 'Sla DechalaBuilding: Ritual of Excess'),
    70483: ItemData(IC.useful, 1, 'wh3_main_sla_cult_teleport', ItemType.building, 0, 'Progressive sla_cult_extra', 'Sla DechalaBuilding: Ritual of Summoning'),
}

techs: dict[int, ItemData] = slaanesh.techs

progUnits: dict[int, ItemData] = slaanesh.progUnits

progBuildings: dict[int, ItemData] = {
    71300: ItemData(IC.useful, 1, 'Progressive sla_palace_agents', ItemType.building, 3, None, 'Progressive Sla DechalaPalace: Lords & Agents'),
    71301: ItemData(IC.useful, 1, 'Progressive sla_palace_daemons', ItemType.building, 2, None, 'Progressive Sla DechalaPalace: Daemon Portal'),
    71302: ItemData(IC.useful, 1, 'Progressive sla_palace_chariots', ItemType.building, 2, None, 'Progressive Sla DechalaPalace: Daemonic Mounts'),
    71303: ItemData(IC.useful, 1, 'Progressive sla_palace_egotism', ItemType.building, 2, None, 'Progressive Sla DechalaPalace: Egotism'),
    71304: ItemData(IC.useful, 1, 'Progressive sla_palace_seekers', ItemType.building, 2, None, 'Progressive Sla DechalaPalace: Exemplars of Excess'),
    71305: ItemData(IC.useful, 1, 'Progressive sla_palace_servants', ItemType.building, 2, None, 'Progressive Sla DechalaPalace: Greater Servants'),
    71306: ItemData(IC.useful, 1, 'Progressive sla_palace_riders', ItemType.building, 2, None, 'Progressive Sla DechalaPalace: Mortal Riders'),
    71307: ItemData(IC.useful, 1, 'Progressive sla_palace_research', ItemType.building, 2, None, 'Progressive Sla DechalaPalace: Innovative Pleasures'),
    71308: ItemData(IC.useful, 1, 'Progressive sla_palace_rituals', ItemType.building, 2, None, 'Progressive Sla DechalaPalace: Pain & Power'),
    71309: ItemData(IC.useful, 1, 'Progressive sla_sla_settlement_major', ItemType.building, 2, None, 'Progressive Sla DechalaPalace: Settlement Major'),
    71310: ItemData(IC.useful, 1, 'Progressive sla_palace_tribute', ItemType.building, 2, None, 'Progressive Sla DechalaPalace: Lavish Gifts'),
    71311: ItemData(IC.useful, 1, 'Progressive sla_palace_walls', ItemType.building, 2, None, 'Progressive Sla DechalaPalace: Palace Walls'),
    71312: ItemData(IC.useful, 1, 'Progressive sla_palace_warriors', ItemType.building, 2, None, 'Progressive Sla DechalaPalace: Warrior Halls'),

    71313: ItemData(IC.useful, 1, 'Progressive sla_thrall_camp_garrison', ItemType.building, 2, None, 'Progressive Sla DechalaThrall Camp: Garrison'),
    71314: ItemData(IC.useful, 1, 'Progressive sla_thrall_camp_income', ItemType.building, 2, None, 'Progressive Sla DechalaThrall Camp: Toil'),
    71315: ItemData(IC.useful, 1, 'Progressive sla_thrall_camp_support', ItemType.building, 2, None, 'Progressive Sla DechalaThrall Camp: Service'),
    71316: ItemData(IC.useful, 1, 'Progressive sla_settlement_minor', ItemType.building, 2, None, 'Progressive Sla DechalaThrall Camp: Settlement Minor'),
    71317: ItemData(IC.useful, 1, 'Progressive sla_thrall_camp_export', ItemType.building, 2, None, 'Progressive Sla DechalaThrall Camp: Toll'),

    71318: ItemData(IC.useful, 1, 'Progressive sla_war_pit_corruption', ItemType.building, 2, None, "Progressive Sla DechalaTormentor's Hold: Ritual Combat"),
    71319: ItemData(IC.useful, 1, 'Progressive sla_war_pit_army', ItemType.building, 3, None, "Progressive Sla DechalaTormentor's Hold: Warhosts"),
    71320: ItemData(IC.useful, 1, 'Progressive sla_war_pit_mortal_barracks', ItemType.building, 3, None, "Progressive Sla DechalaTormentor's Hold: Mortal Servants"),
    71321: ItemData(IC.useful, 1, 'Progressive sla_war_pit_stables', ItemType.building, 3, None, "Progressive Sla DechalaTormentor's Hold: Mounted Servants"),
    71322: ItemData(IC.useful, 1, 'Progressive sla_war_pit_barracks', ItemType.building, 3, None, "Progressive Sla DechalaTormentor's Hold: Twisted Servants"),
    71323: ItemData(IC.useful, 1, 'Progressive sla_war_pit_walls', ItemType.building, 3, None, "Progressive Sla DechalaTormentor's Hold: Walls"),

    71324: ItemData(IC.useful, 1, 'Progressive sla_port', ItemType.building, 3, None, "Progressive Sla DechalaBuilding: Ports"),
    71325: ItemData(IC.useful, 1, 'Progressive sla_foreign_slot_discovery', ItemType.building, 3, None, "Progressive Sla DechalaBuilding: Foreign Slot Discovery"),
}

progTechs: dict[int, ItemData] = slaanesh.progTechs

special: dict[int, specialItemData] = {

}