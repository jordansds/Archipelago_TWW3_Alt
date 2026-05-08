from BaseClasses import ItemClassification as IC
from worlds.tww3.dataStructs import itemType, itemData, specialItemData
from . import lizardmen

# 68000
# @formatter:off
units: dict[int, itemData] = lizardmen.units

buildings: dict[int, itemData] = {
    68400: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_beasts_1', itemType.building, 0, 'Progressive lzd_horde_beasts', 'Lzd Nakai Horde Building: Taming Pen'),
    68401: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_beasts_2', itemType.building, 1, 'Progressive lzd_horde_beasts', 'Lzd Nakai Horde Building: Feral Beast Lair'),
    68402: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_beasts_3', itemType.building, 2, 'Progressive lzd_horde_beasts', 'Lzd Nakai Horde Building: Stegadon Arena'),
    68403: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_beasts_4', itemType.building, 3, 'Progressive lzd_horde_beasts', 'Lzd Nakai Horde Building: Ancient Stegadon Arena'),
    68404: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_coldones_1', itemType.building, 0, 'Progressive lzd_horde_coldones', 'Lzd Nakai Horde Building: Cold One Hollow'),
    68406: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_flying_1', itemType.building, 0, 'Progressive lzd_horde_flying', 'Lzd Nakai Horde Building: Terrarium'),
    68407: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_flying_2', itemType.building, 1, 'Progressive lzd_horde_flying', 'Lzd Nakai Horde Building: Vivarium'),
    68408: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_great_beasts_1', itemType.building, 0, 'Progressive lzd_horde_great_beasts', 'Lzd Nakai Horde Building: Hunting Pack Pen'),
    68409: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_great_beasts_2', itemType.building, 1, 'Progressive lzd_horde_great_beasts', 'Lzd Nakai Horde Building: Salamander Enclosure'),
    68410: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_great_beasts_3', itemType.building, 2, 'Progressive lzd_horde_great_beasts', 'Lzd Nakai Horde Building: Giant Beast Pit'),
    68411: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_saurus_1', itemType.building, 0, 'Progressive lzd_horde_saurus', 'Lzd Nakai Horde Building: Ruined Spawning Chamber'),
    68412: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_saurus_2', itemType.building, 1, 'Progressive lzd_horde_saurus', 'Lzd Nakai Horde Building: Restored Spawning Chamber'),
    68413: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_saurus_3', itemType.building, 2, 'Progressive lzd_horde_saurus', 'Lzd Nakai Horde Building: Grand Natatorium'),
    68414: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_skinks_1', itemType.building, 0, 'Progressive lzd_horde_skinks', 'Lzd Nakai Horde Building: Lower Caste Spawning Chamber'),
    68415: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_skinks_2', itemType.building, 1, 'Progressive lzd_horde_skinks', 'Lzd Nakai Horde Building: Braves Spawning Chamber'),
    68416: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_skinks_3', itemType.building, 2, 'Progressive lzd_horde_skinks', 'Lzd Nakai Horde Building: Chosen Spawning Chamber'),
    68417: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_slann_1', itemType.building, 0, 'Progressive lzd_horde_slann', 'Lzd Nakai Horde Building: Sacred Contemplation Chamber'),
    68418: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_slann_2', itemType.building, 1, 'Progressive lzd_horde_slann', 'Lzd Nakai Horde Building: Star Chamber'),
    68419: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_slann_3', itemType.building, 2, 'Progressive lzd_horde_slann', 'Lzd Nakai Horde Building: Exalted Star Chamber'),

    68420: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_support_faction_1', itemType.building, 0, 'Progressive lzd_horde_faction', 'Lzd Nakai Horde Building: Rotating Disc of Quetzl'),
    68421: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_support_faction_2', itemType.building, 1, 'Progressive lzd_horde_faction', 'Lzd Nakai Horde Building: Gimbals of Gold'),
    68422: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_support_faction_3', itemType.building, 2, 'Progressive lzd_horde_faction', 'Lzd Nakai Horde Building: Gyroscope of Eternal Radiance'),
    68423: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_support_horde_1', itemType.building, 0, 'Progressive lzd_horde_horde', 'Lzd Nakai Horde Building: Old One Monument'),
    68424: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_support_horde_2', itemType.building, 1, 'Progressive lzd_horde_horde', 'Lzd Nakai Horde Building: Sky Plaza'),
    68425: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_support_horde_3', itemType.building, 2, 'Progressive lzd_horde_horde', 'Lzd Nakai Horde Building: Floating Gardens'),
    68426: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_support_rcost_1', itemType.building, 0, 'Progressive lzd_horde_rcost', 'Lzd Nakai Horde Building: Portal Nexus'),
    68427: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_support_rcost_2', itemType.building, 1, 'Progressive lzd_horde_rcost', 'Lzd Nakai Horde Building: Runic Portal Altar'),
    68428: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_support_rrank_1', itemType.building, 0, 'Progressive lzd_horde_rrank', 'Lzd Nakai Horde Building: Training Hall'),
    68429: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_support_rrank_2', itemType.building, 1, 'Progressive lzd_horde_rrank', 'Lzd Nakai Horde Building: Sacred Arena'),
    68430: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_support_upkeep_1', itemType.building, 0, 'Progressive lzd_horde_upkeep', 'Lzd Nakai Horde Building: Communal Grounds'),
    68431: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_support_upkeep_2', itemType.building, 1, 'Progressive lzd_horde_upkeep', 'Lzd Nakai Horde Building: Sanctuary to the Old Ones'),

    68432: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_ziggurat_1', itemType.building, 0, 'Progressive lzd_horde_main', 'Lzd Nakai Horde Building: Ruined Ziggurat of Caxuatn'),
    68433: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_ziggurat_2', itemType.building, 1, 'Progressive lzd_horde_main', 'Lzd Nakai Horde Building: Restored Ziggurat of Caxuatn'),
    68434: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_ziggurat_3', itemType.building, 2, 'Progressive lzd_horde_main', 'Lzd Nakai Horde Building: Reactivated Ziggurat of Caxuatn'),
    68435: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_ziggurat_4', itemType.building, 3, 'Progressive lzd_horde_main', 'Lzd Nakai Horde Building: Primed Ziggurat of Caxuatn'),
    68436: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_ziggurat_5', itemType.building, 4, 'Progressive lzd_horde_main', 'Lzd Nakai Horde Building: Ascendant Ziggurat of Caxuatn'),
    68437: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_ziggurat_minor_1', itemType.building, 0, 'Progressive lzd_horde_main', 'Lzd Nakai Horde Building: Refurbished Temple'),
    68438: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_ziggurat_minor_2', itemType.building, 1, 'Progressive lzd_horde_main', 'Lzd Nakai Horde Building: Operational Ziggurat'),
    68439: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_ziggurat_minor_3', itemType.building, 2, 'Progressive lzd_horde_main', 'Lzd Nakai Horde Building: Holy Ziggurat'),

    68440: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_saurus_veteran_1', itemType.building, 1, 'Progressive lzd_horde_saurus', 'Lzd Nakai Horde Building: Sentinel Hall'),
    68441: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_skink_chief_1', itemType.building, 1, 'Progressive lzd_horde_skinks', 'Lzd Nakai Horde Building: Meditation Chamber'),
    68442: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_skink_priest_1', itemType.building, 1, 'Progressive lzd_horde_slann', 'Lzd Nakai Horde Building: Altar of Enlightenment'),

    68443: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_portal_itzl_1', itemType.building, 0, 'Progressive lzd_horde_itzl', 'Lzd Nakai Horde Building: Lower Portal of Itzl'),
    68444: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_portal_itzl_2', itemType.building, 1, 'Progressive lzd_horde_itzl', 'Lzd Nakai Horde Building: Portal of Itzl'),
    68445: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_portal_itzl_3', itemType.building, 2, 'Progressive lzd_horde_itzl', 'Lzd Nakai Horde Building: Higher Portal of Itzl'),
    68446: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_portal_quetzl_1', itemType.building, 0, 'Progressive lzd_horde_quetzl', 'Lzd Nakai Horde Building: Lower Portal of Quetzl'),
    68447: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_portal_quetzl_2', itemType.building, 1, 'Progressive lzd_horde_quetzl', 'Lzd Nakai Horde Building: Portal of Quetzl'),
    68448: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_portal_quetzl_3', itemType.building, 2, 'Progressive lzd_horde_quetzl', 'Lzd Nakai Horde Building: Higher Portal of Quetzl'),
    68449: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_portal_tlanxla_1', itemType.building, 0, 'Progressive lzd_horde_tlanxa', 'Lzd Nakai Horde Building: Lower Portal of Tlanxla'),
    68450: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_portal_tlanxla_2', itemType.building, 1, 'Progressive lzd_horde_tlanxa', 'Lzd Nakai Horde Building: Portal of Tlanxla'),
    68451: itemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_portal_tlanxla_3', itemType.building, 2, 'Progressive lzd_horde_tlanxa', 'Lzd Nakai Horde Building: Higher Portal of Tlanxla'),
}

techs: dict[int, itemData] = {
    68800: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_nakai_expansion_1', itemType.tech, 1, 'Progressive tech_lzd_nakai_horde', 'Lzd Nakai Tech: Sequence of Growth'),
    68801: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_nakai_expansion_2', itemType.tech, 2, 'Progressive tech_lzd_nakai_horde', 'Lzd Nakai Tech: Sequence of Healing'),
    68802: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_nakai_expansion_3', itemType.tech, 3, 'Progressive tech_lzd_nakai_horde', 'Lzd Nakai Tech: Sequence of Expansion'),
    68803: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_nakai_expansion_4', itemType.tech, 4, 'Progressive tech_lzd_nakai_horde', 'Lzd Nakai Tech: Sequence of Restoration'),
    68804: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_nakai_expansion_5', itemType.tech, 5, 'Progressive tech_lzd_nakai_horde', 'Lzd Nakai Tech: Sequence of Convalescence'),
    68805: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_nakai_expansion_6', itemType.tech, 6, 'Progressive tech_lzd_nakai_horde', 'Lzd Nakai Tech: Sequence of Mending'),
    68806: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_nakai_expansion_7', itemType.tech, 7, 'Progressive tech_lzd_nakai_horde', 'Lzd Nakai Tech: Sequence of Greater Restoration'),

    68807: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_nakai_war_1', itemType.tech, 1, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Sequence of Creation'),
    68808: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_nakai_war_2', itemType.tech, 2, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Sequence of Scaling'),
    68809: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_nakai_war_3', itemType.tech, 3, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Sequence of Greater Infrastructure'),
    68810: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_nakai_war_4', itemType.tech, 2, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Sequence of Command'),
    68811: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_nakai_war_5', itemType.tech, 3, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Sequence of Plunder'),
    68812: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_nakai_war_6', itemType.tech, 4, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Sequence of Traversal'),
    68813: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_army_3', itemType.tech, 3, 'Progressive tech_lzd_war', 'Lzd Nakai Tech: Sequence of Strategy'),
    68814: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_campaign_3', itemType.tech, 4, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Blessing of the Old Ones'),
    68815: itemData(IC.useful, 1, 'wh2_main_tech_lzd_0_1', itemType.tech, 5, 'Progressive tech_lzd_nakai_war', "Lzd Nakai Tech: Interpreting the Old Ones' Meaning"),
    68816: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_army_4', itemType.tech, 4, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Sequence of War'),
    68817: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_vassal_1', itemType.tech, 5, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Ancient Fortitude'),
    68818: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_vassal_2', itemType.tech, 6, 'Progressive tech_lzd_nakai_war', "Lzd Nakai Tech: Champions of the Horde"),
    68819: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_army_5', itemType.tech, 5, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Sequence of Tactics'),
    68820: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_campaign_9', itemType.tech, 6, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Determining the Unseen Threat'),
    68821: itemData(IC.useful, 1, 'wh2_main_tech_lzd_0_2', itemType.tech, 7, 'Progressive tech_lzd_nakai_war', "Lzd Nakai Tech: Determining the Great Plan"),
    68822: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_army_6', itemType.tech, 6, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Sequence of Military'),
    68823: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_campaign_7', itemType.tech, 7, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Determining the Strength of the Old'),
    68824: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_campaign_10', itemType.tech, 8, 'Progressive tech_lzd_nakai_war', "Lzd Nakai Tech: Sequence of Mass Spawning"),
    68825: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_army_7', itemType.tech, 7, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Sequence of Total War'),
    68826: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_campaign_6', itemType.tech, 8, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Sequence of Unification'),
    68827: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_campaign_8', itemType.tech, 9, 'Progressive tech_lzd_nakai_war', "Lzd Nakai Tech: Sequence of Immunity"),

    68828: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_guardian_1', itemType.tech, 1, 'Progressive tech_lzd_nakai_guardians', 'Lzd Nakai Tech: Sequence of the Old Guard'),
    68829: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_guardian_2', itemType.tech, 1, 'Progressive tech_lzd_nakai_guardians', 'Lzd Nakai Tech: Sequence of the Guardian'),
    68830: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_guardian_3', itemType.tech, 1, 'Progressive tech_lzd_nakai_guardians', 'Lzd Nakai Tech: Shrill of the Old Ones'),
    68831: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_guardian_4', itemType.tech, 1, 'Progressive tech_lzd_nakai_guardians', 'Lzd Nakai Tech: Metamorphosis'),

    68832: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_units_6', itemType.tech, 1, 'Progressive tech_lzd_nakai_skirmisher', 'Lzd Nakai Tech: Sequence of the Greater Skinks'),
    68833: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_units_7', itemType.tech, 1, 'Progressive tech_lzd_nakai_skirmisher', 'Lzd Nakai Tech: Sequence of Greater Saurus'),
    68834: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_units_1', itemType.tech, 1, 'Progressive tech_lzd_nakai_skirmisher', 'Lzd Nakai Tech: Sequence of the Skirmisher'),
    68835: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_units_2', itemType.tech, 1, 'Progressive tech_lzd_nakai_skirmisher', 'Lzd Nakai Tech: Sequence of the Warrior'),

    68836: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_units_3', itemType.tech, 1, 'Progressive tech_lzd_nakai_cavalry', 'Lzd Nakai Tech: Sequence of the Beasts'),
    68837: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_units_8', itemType.tech, 1, 'Progressive tech_lzd_nakai_cavalry', 'Lzd Nakai Tech: Sequence of the Mounts'),
    68838: itemData(IC.useful, 1, 'wh2_main_tech_lzd_8_2', itemType.tech, 1, 'Progressive tech_lzd_nakai_cavalry', 'Lzd Nakai Tech: Sequence of Exotic Weapons'),
    68839: itemData(IC.useful, 1, 'wh2_main_tech_lzd_8_4', itemType.tech, 1, 'Progressive tech_lzd_nakai_cavalry', 'Lzd Nakai Tech: Sequence of the Hunt'),

    68840: itemData(IC.useful, 1, 'wh2_main_tech_lzd_8_7', itemType.tech, 1, 'Progressive tech_lzd_nakai_beasts', 'Lzd Nakai Tech: Sequence of the Beastkeepers'),
    68841: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_nakai_beasts_4', itemType.tech, 1, 'Progressive tech_lzd_nakai_beasts', 'Lzd Nakai Tech: Sequence of Prowling'),
    68842: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_units_4', itemType.tech, 1, 'Progressive tech_lzd_nakai_beasts', 'Lzd Nakai Tech: Sequence of Savagery'),
    68843: itemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_units_9', itemType.tech, 1, 'Progressive tech_lzd_nakai_beasts', 'Lzd Nakai Tech: Sequence of the Greater Beasts'),
}

progUnits: dict[int, itemData] = lizardmen.progUnits

progBuildings: dict[int, itemData] = {
    69300: itemData(IC.useful, 4, 'Progressive lzd_horde_beasts', itemType.building, 4, None, 'Progressive Lzd Nakai Horde Building: Beasts'),
    69301: itemData(IC.useful, 1, 'Progressive lzd_horde_coldones', itemType.building, 1, None, 'Progressive Lzd Nakai Horde Building: Cold Ones'),
    69302: itemData(IC.useful, 2, 'Progressive lzd_horde_flying', itemType.building, 2, None, 'Progressive Lzd Nakai Horde Building: Terrarium'),
    69303: itemData(IC.useful, 3, 'Progressive lzd_horde_great_beasts', itemType.building, 3, None, 'Progressive Lzd Nakai Horde Building: Great Beasts'),
    69304: itemData(IC.useful, 3, 'Progressive lzd_horde_saurus', itemType.building, 3, None, 'Progressive Lzd Nakai Horde Building: Natatorium'),
    69305: itemData(IC.useful, 3, 'Progressive lzd_horde_skinks', itemType.building, 3, None, 'Progressive Lzd Nakai Horde Building: Spawning Chamber'),
    69306: itemData(IC.useful, 3, 'Progressive lzd_horde_slann', itemType.building, 3, None, 'Progressive Lzd Nakai Horde Building: Slann'),
    69307: itemData(IC.useful, 3, 'Progressive lzd_horde_faction', itemType.building, 3, None, 'Progressive Lzd Nakai Horde Building: Gyroscope'),
    69308: itemData(IC.useful, 3, 'Progressive lzd_horde_horde', itemType.building, 3, None, 'Progressive Lzd Nakai Horde Building: Monuments'),
    69309: itemData(IC.useful, 2, 'Progressive lzd_horde_rcost', itemType.building, 2, None, 'Progressive Lzd Nakai Horde Building: Sanctuary'),
    69310: itemData(IC.useful, 2, 'Progressive lzd_horde_rrank', itemType.building, 2, None, 'Progressive Lzd Nakai Horde Building: Nexus'),
    69311: itemData(IC.useful, 2, 'Progressive lzd_horde_upkeep', itemType.building, 2, None, 'Progressive Lzd Nakai Horde Building: Arena'),
    69312: itemData(IC.useful, 5, 'Progressive lzd_horde_main', itemType.building, 5, None, 'Progressive Lzd Nakai Horde Building: Ziggurat'),
    69313: itemData(IC.useful, 5, 'Progressive lzd_horde_itzl', itemType.building, 5, None, 'Progressive Lzd Nakai Horde Building: Itzl Portal'),
    69314: itemData(IC.useful, 5, 'Progressive lzd_horde_quetzl', itemType.building, 5, None, 'Progressive Lzd Nakai Horde Building: Quetzl Portal'),
    69315: itemData(IC.useful, 5, 'Progressive lzd_horde_tlanxa', itemType.building, 5, None, 'Progressive Lzd Nakai Horde Building: Tlanxa Portal'),
}

progTechs: dict[int, itemData] = {
    69400: itemData(IC.useful, 7, "Progressive tech_lzd_nakai_horde", itemType.tech, 7, None, "Progressive Lzd Nakai Tech: The Horde Expands"),
    69401: itemData(IC.useful, 9, "Progressive tech_lzd_nakai_war", itemType.tech, 9, None, "Progressive Lzd Nakai Tech: The Scale of War"),
    69402: itemData(IC.useful, 1, "Progressive tech_lzd_nakai_guardians", itemType.tech, 1, None, "Progressive Lzd Nakai Tech: Guardians"),
    69403: itemData(IC.useful, 1, "Progressive tech_lzd_nakai_skirmisher", itemType.tech, 1, None, "Progressive Lzd Nakai Tech: Skirmisher"),
    69404: itemData(IC.useful, 1, "Progressive tech_lzd_nakai_cavalry", itemType.tech, 1, None, "Progressive Lzd Nakai Tech: Cavalry"),
    69405: itemData(IC.useful, 1, "Progressive tech_lzd_nakai_beasts", itemType.tech, 1, None, "Progressive Lzd Nakai Tech: Beasts"),
}

special: dict[int, specialItemData] = {
    #37502: specialItemData(IC.useful, 1, "wh2_dlc13_lzd_spirits_of_the_jungle", 'wh2_dlc13_lzd_nakai_itzl', ItemType.building, 0, 'Progressive lzd_nakai', False, False, 'Lzd Nakai Building: Temple of Itzl'),
    #37503: specialItemData(IC.useful, 1, "wh2_dlc13_lzd_spirits_of_the_jungle", 'wh2_dlc13_lzd_nakai_quetzl', ItemType.building, 0, 'Progressive lzd_nakai', False, False, 'Lzd Nakai Building: Temple of Quetzl'),
    #37504: specialItemData(IC.useful, 1, "wh2_dlc13_lzd_spirits_of_the_jungle", 'wh2_dlc13_lzd_nakai_xholankha', ItemType.building, 0, 'Progressive lzd_nakai', False, False, 'Lzd Nakai Building: Temple of Xholankha'),
    #37505: specialItemData(IC.useful, 1, "wh2_dlc13_lzd_spirits_of_the_jungle", 'wh2_dlc13_lzd_port_nakai_itzl', ItemType.building, 0, 'Progressive lzd_port_nakai', False, False, 'Lzd Nakai Building: Temple of Itzl'),
    #37506: specialItemData(IC.useful, 1, "wh2_dlc13_lzd_spirits_of_the_jungle", 'wh2_dlc13_lzd_port_nakai_quetzl', ItemType.building, 0, 'Progressive lzd_port_nakai', False, False, 'Lzd Nakai Building: Temple of Quetzl'),
    #37507: specialItemData(IC.useful, 1, "wh2_dlc13_lzd_spirits_of_the_jungle", 'wh2_dlc13_lzd_port_nakai_xholankha', ItemType.building, 0, 'Progressive lzd_port_nakai', False, False, 'Lzd Nakai Building: Temple of Xholankha'),
    #37508: specialItemData(IC.useful, 1, "wh2_dlc13_lzd_spirits_of_the_jungle", 'wh2_dlc13_lzd_port_nakai_xholankha', ItemType.building, 0, 'Progressive lzd_port_nakai', False, False, 'Lzd Nakai Building: Temple of Xholankha'),
    #37509: specialItemData(IC.useful, 1, "wh2_dlc13_lzd_spirits_of_the_jungle", 'wh2_dlc13_lzd_port_nakai_xholankha', ItemType.building, 0, 'Progressive lzd_port_nakai', False, False, 'Lzd Nakai Building: Temple of Xholankha'),
    #37510: specialItemData(IC.useful, 1, "wh2_dlc13_lzd_spirits_of_the_jungle", 'Progressive lzd_nakai', ItemType.building, 0, None, False, True, 'Lzd Nakai Building: Temple of Xholankha'),
    #37511: specialItemData(IC.useful, 1, "wh2_dlc13_lzd_spirits_of_the_jungle", 'Progressive lzd_port_nakai', ItemType.building, 0, None, False, True, 'Lzd Nakai Building: Temple of Xholankha'),
}

rituals = lizardmen.rituals