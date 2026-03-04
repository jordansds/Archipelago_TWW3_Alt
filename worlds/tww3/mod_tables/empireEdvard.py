from BaseClasses import ItemClassification as IC
from worlds.tww3.item_types import ItemType, ItemData, specialItemData
import worlds.tww3.faction_tables.empire as empire
"""
land_units_onscreen_name_mixu_emp_inf_celebrants	Celebrants
land_units_onscreen_name_mixu_emp_inf_horned_hunters	Horned Hunters
land_units_onscreen_name_mixu_emp_cav_daughters_of_rhya	Daughters of Rhya

land_units_onscreen_name_mixu_emp_art_carronade	Carronade
land_units_onscreen_name_mixu_emp_art_mortar	Mortar

land_units_onscreen_name_mixu_emp_mon_promethean_riders	Promethean Riders
land_units_onscreen_name_mixu_emp_inf_norscan_reavers	Norscan Reavers

land_units_onscreen_name_mixu_emp_inf_norscan_reavers	Norscan Reavers
land_units_onscreen_name_mixu_emp_inf_norscan_reavers_great_weapons	Norscan Reavers (Great Weapons)
land_units_onscreen_name_mixu_emp_inf_pirate_deckhands_swords	Pirate Deckhands
land_units_onscreen_name_mixu_emp_inf_pirate_deckhands_polearms	Pirate Deckhands (Polearms)
land_units_onscreen_name_mixu_emp_inf_gunnery_mob_pistols	Pirate Gunnery Mob (Pistols)
land_units_onscreen_name_mixu_emp_inf_gunnery_mob_handguns	Pirate Gunnery Mob (Handguns)
land_units_onscreen_name_mixu_emp_inf_gunnery_mob_blunderbuss	Pirate Gunnery Mob (Blunderbuss)
land_units_onscreen_name_mixu_emp_inf_grog_carriers	Grog Carriers
land_units_onscreen_name_mixu_emp_inf_buccaneers_great_axe	Buccaneers (Great Weapons)
land_units_onscreen_name_mixu_emp_inf_buccaneers_sword_and_bombs	Buccaneers (Sword and Bombs)
land_units_onscreen_name_mixu_emp_mon_prometheans	Prometheans
land_units_onscreen_name_mixu_emp_mon_leviathan	Leviathan
"""

units: dict[int, ItemData] = empire.units
units.update({})

buildings: dict[int, ItemData] = {}

techs: dict[int, ItemData] = {}

progUnits: dict[int, ItemData] = empire.progUnits

progBuildings: dict[int, ItemData] = {}

progTechs: dict[int, ItemData] = {}

special: dict[int, specialItemData]  = {}