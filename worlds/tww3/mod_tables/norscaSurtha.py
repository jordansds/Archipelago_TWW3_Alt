from BaseClasses import ItemClassification as IC
from worlds.tww3.item_types import ItemType, ItemData, specialItemData
import worlds.tww3.faction_tables.norsca as norsca

units: dict[int, ItemData] = {key+70000: unit for key, unit in norsca.progUnits.items()}
units.update({
    #Overwriting non-varg units
    108006: ItemData(IC.useful, 1, 'wh_mod_nor_inf_varg_champions', ItemType.unit, 2, 'Progressive  nor_rng', 'Nor Unit: Bowgunners'),
    108011: ItemData(IC.useful, 1, 'wh_mod_nor_mon_gorebeasts', ItemType.unit, 2, 'Progressive nor_bst', 'Nor Unit: Gorebeasts'),
    108018: ItemData(IC.useful, 1, 'wh_mod_nor_veh_war_wagon_0', ItemType.unit, 2, 'Progressive nor_veh', 'Nor Unit: Varg War Wagons'),
    108021: ItemData(IC.useful, 1, 'wh_mod_nor_veh_varg_chariot', ItemType.unit, 1, 'Progressive nor_veh', 'Nor Unit: Varg Chariots'),
    108022: ItemData(IC.useful, 1, 'wh_mod_nor_veh_varg_warwolves_chariot', ItemType.unit, 2, 'Progressive nor_veh', 'Nor Unit: Varg Ice Wolf Chariots'),
    108033: ItemData(IC.useful, 1, 'wh_mod_nor_veh_giant_war_wagon_0', ItemType.unit, 4, 'Progressive nor_bst', 'Nor Unit: Mammoth War Wagon'),
    108034: ItemData(IC.useful, 1, 'wh_mod_nor_veh_giant_cannon_wagon_0', ItemType.unit, 5, 'Progressive nor_bst', 'Nor Unit: Mammoth War Wagon (Hellcannon)'),
    108035: ItemData(IC.useful, 1, 'wh_mod_nor_veh_giant_temple_wagon_0', ItemType.unit, 5, 'Progressive nor_bst', 'Nor Unit: Mammoth War Wagon (Warshrine)'),

    #Overwriting this key with an unrelated unit as the key needed erasing anyway
    108007: ItemData(IC.useful, 1, 'wh_mod_nor_veh_gorebeast_chariot', ItemType.unit, 4, 'Progressive nor_veh','Nor Unit: Varg Gorebeast Chariots'),
    #Adding additional units
    108063: ItemData(IC.useful, 1, 'wh_mod_nor_veh_seeker_chariots', ItemType.unit, 3, 'Progressive nor_veh', 'Nor Unit: Seeker Chariots'),
    108064: ItemData(IC.useful, 1, 'wh_mod_nor_veh_burning_chariots', ItemType.unit, 4, 'Progressive nor_veh', 'Nor Unit: Burning Chariots'),
    108065: ItemData(IC.useful, 1, 'wh_mod_nor_veh_skullcannon', ItemType.unit, 4, 'Progressive nor_veh', 'Nor Unit: Skullcannon'),
    108066: ItemData(IC.useful, 1, 'wh_mod_nor_veh_razorgor_chariots', ItemType.unit, 4, 'Progressive nor_veh', 'Nor Unit: Plague Chariots'),
})

buildings: dict[int, ItemData] = norsca.buildings

techs: dict[int, ItemData] = norsca.techs

progUnits: dict[int, ItemData] = {key+70000: unit for key, unit in norsca.progUnits.items()}
progUnits.update({
    109201: ItemData(IC.useful, 2, "Progressive nor_rng", ItemType.unit, 2, "", "Progressive Nor Unit: Ranged"),
    109202: ItemData(IC.useful, 2, "Progressive nor_cav", ItemType.unit, 2, "", "Progressive Nor Unit: Cavalry"),
    109204: ItemData(IC.useful, 4, "Progressive nor_veh", ItemType.unit, 4, "", "Progressive Nor Unit: Chariot"),
})

progBuildings: dict[int, ItemData] = norsca.progBuildings

progTechs: dict[int, ItemData] = norsca.progTechs

special: dict[int, specialItemData] = norsca.special