from BaseClasses import ItemClassification as IC
from worlds.tww3.item_types import ItemType, ItemData, specialItemData
from . import lizardmen

#68000
# @formatter:off
units: dict[int, ItemData] = lizardmen.units

buildings: dict[int, ItemData] = {
    68400: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_beasts_1', ItemType.building, 0, 'Progressive lzd_horde_beasts', 'Lzd Nakai Horde Building: Taming Pen'),
    68401: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_beasts_2', ItemType.building, 1, 'Progressive lzd_horde_beasts', 'Lzd Nakai Horde Building: Feral Beast Lair'),
    68402: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_beasts_3', ItemType.building, 2, 'Progressive lzd_horde_beasts', 'Lzd Nakai Horde Building: Stegadon Arena'),
    68403: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_beasts_4', ItemType.building, 3, 'Progressive lzd_horde_beasts', 'Lzd Nakai Horde Building: Ancient Stegadon Arena'),
    68404: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_coldones_1', ItemType.building, 0, 'Progressive lzd_horde_coldones', 'Lzd Nakai Horde Building: Cold One Hollow'),
    68406: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_flying_1', ItemType.building, 0, 'Progressive lzd_horde_flying', 'Lzd Nakai Horde Building: Terrarium'),
    68407: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_flying_2', ItemType.building, 1, 'Progressive lzd_horde_flying', 'Lzd Nakai Horde Building: Vivarium'),
    68408: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_great_beasts_1', ItemType.building, 0, 'Progressive lzd_horde_great_beasts', 'Lzd Nakai Horde Building: Hunting Pack Pen'),
    68409: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_great_beasts_2', ItemType.building, 1, 'Progressive lzd_horde_great_beasts', 'Lzd Nakai Horde Building: Salamander Enclosure'),
    68410: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_great_beasts_3', ItemType.building, 2, 'Progressive lzd_horde_great_beasts', 'Lzd Nakai Horde Building: Giant Beast Pit'),
    68411: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_saurus_1', ItemType.building, 0, 'Progressive lzd_horde_saurus', 'Lzd Nakai Horde Building: Ruined Spawning Chamber'),
    68412: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_saurus_2', ItemType.building, 1, 'Progressive lzd_horde_saurus', 'Lzd Nakai Horde Building: Restored Spawning Chamber'),
    68413: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_saurus_3', ItemType.building, 2, 'Progressive lzd_horde_saurus', 'Lzd Nakai Horde Building: Grand Natatorium'),
    68414: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_skinks_1', ItemType.building, 0, 'Progressive lzd_horde_skinks', 'Lzd Nakai Horde Building: Lower Caste Spawning Chamber'),
    68415: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_skinks_2', ItemType.building, 1, 'Progressive lzd_horde_skinks', 'Lzd Nakai Horde Building: Braves Spawning Chamber'),
    68416: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_skinks_3', ItemType.building, 2, 'Progressive lzd_horde_skinks', 'Lzd Nakai Horde Building: Chosen Spawning Chamber'),
    68417: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_slann_1', ItemType.building, 0, 'Progressive lzd_horde_slann', 'Lzd Nakai Horde Building: Sacred Contemplation Chamber'),
    68418: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_slann_2', ItemType.building, 1, 'Progressive lzd_horde_slann', 'Lzd Nakai Horde Building: Star Chamber'),
    68419: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_slann_3', ItemType.building, 2, 'Progressive lzd_horde_slann', 'Lzd Nakai Horde Building: Exalted Star Chamber'),

    68420: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_support_faction_1', ItemType.building, 0, 'Progressive lzd_horde_faction', 'Lzd Nakai Horde Building: Rotating Disc of Quetzl'),
    68421: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_support_faction_2', ItemType.building, 1, 'Progressive lzd_horde_faction', 'Lzd Nakai Horde Building: Gimbals of Gold'),
    68422: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_support_faction_3', ItemType.building, 2, 'Progressive lzd_horde_faction', 'Lzd Nakai Horde Building: Gyroscope of Eternal Radiance'),
    68423: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_support_horde_1', ItemType.building, 0, 'Progressive lzd_horde_horde', 'Lzd Nakai Horde Building: Old One Monument'),
    68424: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_support_horde_2', ItemType.building, 1, 'Progressive lzd_horde_horde', 'Lzd Nakai Horde Building: Sky Plaza'),
    68425: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_support_horde_3', ItemType.building, 2, 'Progressive lzd_horde_horde', 'Lzd Nakai Horde Building: Floating Gardens'),
    68426: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_support_rcost_1', ItemType.building, 0, 'Progressive lzd_horde_rcost', 'Lzd Nakai Horde Building: Portal Nexus'),
    68427: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_support_rcost_2', ItemType.building, 1, 'Progressive lzd_horde_rcost', 'Lzd Nakai Horde Building: Runic Portal Altar'),
    68428: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_support_rrank_1', ItemType.building, 0, 'Progressive lzd_horde_rrank', 'Lzd Nakai Horde Building: Training Hall'),
    68429: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_support_rrank_2', ItemType.building, 1, 'Progressive lzd_horde_rrank', 'Lzd Nakai Horde Building: Sacred Arena'),
    68430: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_support_upkeep_1', ItemType.building, 0, 'Progressive lzd_horde_upkeep', 'Lzd Nakai Horde Building: Communal Grounds'),
    68431: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_support_upkeep_2', ItemType.building, 1, 'Progressive lzd_horde_upkeep', 'Lzd Nakai Horde Building: Sanctuary to the Old Ones'),

    68432: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_ziggurat_1', ItemType.building, 0, 'Progressive lzd_horde_main', 'Lzd Nakai Horde Building: Ruined Ziggurat of Caxuatn'),
    68433: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_ziggurat_2', ItemType.building, 1, 'Progressive lzd_horde_main', 'Lzd Nakai Horde Building: Restored Ziggurat of Caxuatn'),
    68434: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_ziggurat_3', ItemType.building, 2, 'Progressive lzd_horde_main', 'Lzd Nakai Horde Building: Reactivated Ziggurat of Caxuatn'),
    68435: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_ziggurat_4', ItemType.building, 3, 'Progressive lzd_horde_main', 'Lzd Nakai Horde Building: Primed Ziggurat of Caxuatn'),
    68436: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_ziggurat_5', ItemType.building, 4, 'Progressive lzd_horde_main', 'Lzd Nakai Horde Building: Ascendant Ziggurat of Caxuatn'),
    68437: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_ziggurat_minor_1', ItemType.building, 0, 'Progressive lzd_horde_main', 'Lzd Nakai Horde Building: Refurbished Temple'),
    68438: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_ziggurat_minor_2', ItemType.building, 1, 'Progressive lzd_horde_main', 'Lzd Nakai Horde Building: Operational Ziggurat'),
    68439: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_ziggurat_minor_3', ItemType.building, 2, 'Progressive lzd_horde_main', 'Lzd Nakai Horde Building: Holy Ziggurat'),

    68440: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_saurus_veteran_1', ItemType.building, 1, 'Progressive lzd_horde_saurus', 'Lzd Nakai Horde Building: Sentinel Hall'),
    68441: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_skink_chief_1', ItemType.building, 1, 'Progressive lzd_horde_skinks', 'Lzd Nakai Horde Building: Meditation Chamber'),
    68442: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_skink_priest_1', ItemType.building, 1, 'Progressive lzd_horde_slann', 'Lzd Nakai Horde Building: Altar of Enlightenment'),

    68443: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_portal_itzl_1', ItemType.building, 0, 'Progressive lzd_horde_itzl', 'Lzd Nakai Horde Building: Lower Portal of Itzl'),
    68444: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_portal_itzl_2', ItemType.building, 1, 'Progressive lzd_horde_itzl', 'Lzd Nakai Horde Building: Portal of Itzl'),
    68445: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_portal_itzl_3', ItemType.building, 2, 'Progressive lzd_horde_itzl', 'Lzd Nakai Horde Building: Higher Portal of Itzl'),
    68446: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_portal_quetzl_1', ItemType.building, 0, 'Progressive lzd_horde_quetzl', 'Lzd Nakai Horde Building: Lower Portal of Quetzl'),
    68447: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_portal_quetzl_2', ItemType.building, 1, 'Progressive lzd_horde_quetzl', 'Lzd Nakai Horde Building: Portal of Quetzl'),
    68448: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_portal_quetzl_3', ItemType.building, 2, 'Progressive lzd_horde_quetzl', 'Lzd Nakai Horde Building: Higher Portal of Quetzl'),
    68449: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_portal_tlanxla_1', ItemType.building, 0, 'Progressive lzd_horde_tlanxa', 'Lzd Nakai Horde Building: Lower Portal of Tlanxla'),
    68450: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_portal_tlanxla_2', ItemType.building, 1, 'Progressive lzd_horde_tlanxa', 'Lzd Nakai Horde Building: Portal of Tlanxla'),
    68451: ItemData(IC.useful, 1, 'wh2_dlc13_horde_lizardmen_portal_tlanxla_3', ItemType.building, 2, 'Progressive lzd_horde_tlanxa', 'Lzd Nakai Horde Building: Higher Portal of Tlanxla'),
}

techs: dict[int, ItemData] = {
    68800: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_nakai_expansion_1', ItemType.tech, 1, 'Progressive tech_lzd_nakai_horde', 'Lzd Nakai Tech: Sequence of Growth'),
    68801: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_nakai_expansion_2', ItemType.tech, 2, 'Progressive tech_lzd_nakai_horde', 'Lzd Nakai Tech: Sequence of Healing'),
    68802: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_nakai_expansion_3', ItemType.tech, 3, 'Progressive tech_lzd_nakai_horde', 'Lzd Nakai Tech: Sequence of Expansion'),
    68803: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_nakai_expansion_4', ItemType.tech, 4, 'Progressive tech_lzd_nakai_horde', 'Lzd Nakai Tech: Sequence of Restoration'),
    68804: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_nakai_expansion_5', ItemType.tech, 5, 'Progressive tech_lzd_nakai_horde', 'Lzd Nakai Tech: Sequence of Convalescence'),
    68805: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_nakai_expansion_6', ItemType.tech, 6, 'Progressive tech_lzd_nakai_horde', 'Lzd Nakai Tech: Sequence of Mending'),
    68806: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_nakai_expansion_7', ItemType.tech, 7, 'Progressive tech_lzd_nakai_horde', 'Lzd Nakai Tech: Sequence of Greater Restoration'),

    68807: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_nakai_war_1', ItemType.tech, 1, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Sequence of Creation'),
    68808: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_nakai_war_2', ItemType.tech, 2, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Sequence of Scaling'),
    68809: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_nakai_war_3', ItemType.tech, 3, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Sequence of Greater Infrastructure'),
    68810: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_nakai_war_4', ItemType.tech, 2, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Sequence of Command'),
    68811: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_nakai_war_5', ItemType.tech, 3, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Sequence of Plunder'),
    68812: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_nakai_war_6', ItemType.tech, 4, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Sequence of Traversal'),
    68813: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_army_3', ItemType.tech, 3, 'Progressive tech_lzd_war', 'Lzd Nakai Tech: Sequence of Strategy'),
    68814: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_campaign_3', ItemType.tech, 4, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Blessing of the Old Ones'),
    68815: ItemData(IC.useful, 1, 'wh2_main_tech_lzd_0_1', ItemType.tech, 5, 'Progressive tech_lzd_nakai_war', "Lzd Nakai Tech: Interpreting the Old Ones' Meaning"),
    68816: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_army_4', ItemType.tech, 4, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Sequence of War'),
    68817: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_vassal_1', ItemType.tech, 5, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Ancient Fortitude'),
    68818: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_vassal_2', ItemType.tech, 6, 'Progressive tech_lzd_nakai_war', "Lzd Nakai Tech: Champions of the Horde"),
    68819: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_army_5', ItemType.tech, 5, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Sequence of Tactics'),
    68820: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_campaign_9', ItemType.tech, 6, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Determining the Unseen Threat'),
    68821: ItemData(IC.useful, 1, 'wh2_main_tech_lzd_0_2', ItemType.tech, 7, 'Progressive tech_lzd_nakai_war', "Lzd Nakai Tech: Determining the Great Plan"),
    68822: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_army_6', ItemType.tech, 6, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Sequence of Military'),
    68823: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_campaign_7', ItemType.tech, 7, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Determining the Strength of the Old'),
    68824: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_campaign_10', ItemType.tech, 8, 'Progressive tech_lzd_nakai_war', "Lzd Nakai Tech: Sequence of Mass Spawning"),
    68825: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_army_7', ItemType.tech, 7, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Sequence of Total War'),
    68826: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_campaign_6', ItemType.tech, 8, 'Progressive tech_lzd_nakai_war', 'Lzd Nakai Tech: Sequence of Unification'),
    68827: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_campaign_8', ItemType.tech, 9, 'Progressive tech_lzd_nakai_war', "Lzd Nakai Tech: Sequence of Immunity"),

    68828: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_guardian_1', ItemType.tech, 1, 'Progressive tech_lzd_nakai_guardians', 'Lzd Nakai Tech: Sequence of the Old Guard'),
    68829: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_guardian_2', ItemType.tech, 1, 'Progressive tech_lzd_nakai_guardians', 'Lzd Nakai Tech: Sequence of the Guardian'),
    68830: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_guardian_3', ItemType.tech, 1, 'Progressive tech_lzd_nakai_guardians', 'Lzd Nakai Tech: Shrill of the Old Ones'),
    68831: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_guardian_4', ItemType.tech, 1, 'Progressive tech_lzd_nakai_guardians', 'Lzd Nakai Tech: Metamorphosis'),

    68832: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_units_6', ItemType.tech, 1, 'Progressive tech_lzd_nakai_skirmisher', 'Lzd Nakai Tech: Sequence of the Greater Skinks'),
    68833: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_units_7', ItemType.tech, 1, 'Progressive tech_lzd_nakai_skirmisher', 'Lzd Nakai Tech: Sequence of Greater Saurus'),
    68834: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_units_1', ItemType.tech, 1, 'Progressive tech_lzd_nakai_skirmisher', 'Lzd Nakai Tech: Sequence of the Skirmisher'),
    68835: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_units_2', ItemType.tech, 1, 'Progressive tech_lzd_nakai_skirmisher', 'Lzd Nakai Tech: Sequence of the Warrior'),

    68836: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_units_3', ItemType.tech, 1, 'Progressive tech_lzd_nakai_cavalry', 'Lzd Nakai Tech: Sequence of the Beasts'),
    68837: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_units_8', ItemType.tech, 1, 'Progressive tech_lzd_nakai_cavalry', 'Lzd Nakai Tech: Sequence of the Mounts'),
    68838: ItemData(IC.useful, 1, 'wh2_main_tech_lzd_8_2', ItemType.tech, 1, 'Progressive tech_lzd_nakai_cavalry', 'Lzd Nakai Tech: Sequence of Exotic Weapons'),
    68839: ItemData(IC.useful, 1, 'wh2_main_tech_lzd_8_4', ItemType.tech, 1, 'Progressive tech_lzd_nakai_cavalry', 'Lzd Nakai Tech: Sequence of the Hunt'),

    68840: ItemData(IC.useful, 1, 'wh2_main_tech_lzd_8_7', ItemType.tech, 1, 'Progressive tech_lzd_nakai_beasts', 'Lzd Nakai Tech: Sequence of the Beastkeepers'),
    68841: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_nakai_beasts_4', ItemType.tech, 1, 'Progressive tech_lzd_nakai_beasts', 'Lzd Nakai Tech: Sequence of Prowling'),
    68842: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_units_4', ItemType.tech, 1, 'Progressive tech_lzd_nakai_beasts', 'Lzd Nakai Tech: Sequence of Savagery'),
    68843: ItemData(IC.useful, 1, 'wh2_dlc13_tech_lzd_units_9', ItemType.tech, 1, 'Progressive tech_lzd_nakai_beasts', 'Lzd Nakai Tech: Sequence of the Greater Beasts'),
}

progUnits: dict[int, ItemData] = lizardmen.progUnits

progBuildings: dict[int, ItemData] = {
    69300: ItemData(IC.useful, 4, 'Progressive lzd_horde_beasts', ItemType.building, 4, None, 'Progressive Lzd Nakai Horde Building: Beasts'),
    69301: ItemData(IC.useful, 1, 'Progressive lzd_horde_coldones', ItemType.building, 1, None, 'Progressive Lzd Nakai Horde Building: Cold Ones'),
    69302: ItemData(IC.useful, 2, 'Progressive lzd_horde_flying', ItemType.building, 2, None, 'Progressive Lzd Nakai Horde Building: Terrarium'),
    69303: ItemData(IC.useful, 3, 'Progressive lzd_horde_great_beasts', ItemType.building, 3, None, 'Progressive Lzd Nakai Horde Building: Great Beasts'),
    69304: ItemData(IC.useful, 3, 'Progressive lzd_horde_saurus', ItemType.building, 3, None, 'Progressive Lzd Nakai Horde Building: Natatorium'),
    69305: ItemData(IC.useful, 3, 'Progressive lzd_horde_skinks', ItemType.building, 3, None, 'Progressive Lzd Nakai Horde Building: Spawning Chamber'),
    69306: ItemData(IC.useful, 3, 'Progressive lzd_horde_slann', ItemType.building, 3, None, 'Progressive Lzd Nakai Horde Building: Slann'),
    69307: ItemData(IC.useful, 3, 'Progressive lzd_horde_faction', ItemType.building, 3, None, 'Progressive Lzd Nakai Horde Building: Gyroscope'),
    69308: ItemData(IC.useful, 3, 'Progressive lzd_horde_horde', ItemType.building, 3, None, 'Progressive Lzd Nakai Horde Building: Monuments'),
    69309: ItemData(IC.useful, 2, 'Progressive lzd_horde_rcost', ItemType.building, 2, None, 'Progressive Lzd Nakai Horde Building: Sanctuary'),
    69310: ItemData(IC.useful, 2, 'Progressive lzd_horde_rrank', ItemType.building, 2, None, 'Progressive Lzd Nakai Horde Building: Nexus'),
    69311: ItemData(IC.useful, 2, 'Progressive lzd_horde_upkeep', ItemType.building, 2, None, 'Progressive Lzd Nakai Horde Building: Arena'),
    69312: ItemData(IC.useful, 5, 'Progressive lzd_horde_main', ItemType.building, 5, None, 'Progressive Lzd Nakai Horde Building: Ziggurat'),
    69313: ItemData(IC.useful, 5, 'Progressive lzd_horde_itzl', ItemType.building, 5, None, 'Progressive Lzd Nakai Horde Building: Itzl Portal'),
    69314: ItemData(IC.useful, 5, 'Progressive lzd_horde_quetzl', ItemType.building, 5, None, 'Progressive Lzd Nakai Horde Building: Quetzl Portal'),
    69315: ItemData(IC.useful, 5, 'Progressive lzd_horde_tlanxa', ItemType.building, 5, None, 'Progressive Lzd Nakai Horde Building: Tlanxa Portal'),
}

progTechs: dict[int, ItemData] = {
    69400: ItemData(IC.useful, 7, "Progressive tech_lzd_nakai_horde", ItemType.tech, 7, None, "Progressive Lzd Nakai Tech: The Horde Expands"),
    69401: ItemData(IC.useful, 9, "Progressive tech_lzd_nakai_war", ItemType.tech, 9, None, "Progressive Lzd Nakai Tech: The Scale of War"),
    69402: ItemData(IC.useful, 1, "Progressive tech_lzd_nakai_guardians", ItemType.tech, 1, None, "Progressive Lzd Nakai Tech: Guardians"),
    69403: ItemData(IC.useful, 1, "Progressive tech_lzd_nakai_skirmisher", ItemType.tech, 1, None, "Progressive Lzd Nakai Tech: Skirmisher"),
    69404: ItemData(IC.useful, 1, "Progressive tech_lzd_nakai_cavalry", ItemType.tech, 1, None, "Progressive Lzd Nakai Tech: Cavalry"),
    69405: ItemData(IC.useful, 1, "Progressive tech_lzd_nakai_beasts", ItemType.tech, 1, None, "Progressive Lzd Nakai Tech: Beasts"),
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