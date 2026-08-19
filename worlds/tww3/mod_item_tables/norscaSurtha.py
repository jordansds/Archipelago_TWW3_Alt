from BaseClasses import ItemClassification as IC
from worlds.tww3.dataStructs import itemType, itemData, specialItemData
from worlds.tww3.faction_item_tables import norsca

units: dict[int, itemData] = {key + 70000: itemData(unit.classification,
                                                    unit.count,
                                                    unit.name,
                                                    unit.type,
                                                    unit.tier,
                                                    unit.progressionGroup,
                                                    unit.readableName.replace("Norsca", "Norsca Surtha"))
                              for key, unit in norsca.units.items()}
units.update({
    #Overwriting non-varg units
    108006: itemData(IC.useful, 1, 'wh_mod_nor_inf_varg_champions', itemType.unit, 2, 'Progressive  nor_rng', 'Norsca Surtha Unit: Bowgunners'),
    108011: itemData(IC.useful, 1, 'wh_mod_nor_mon_gorebeasts', itemType.unit, 2, 'Progressive nor_bst', 'Norsca Surtha Unit: Gorebeasts'),
    108018: itemData(IC.useful, 1, 'wh_mod_nor_veh_war_wagon_0', itemType.unit, 2, 'Progressive nor_veh', 'Norsca Surtha Unit: Varg War Wagons'),
    108021: itemData(IC.useful, 1, 'wh_mod_nor_veh_varg_chariot', itemType.unit, 1, 'Progressive nor_veh', 'Norsca Surtha Unit: Varg Chariots'),
    108022: itemData(IC.useful, 1, 'wh_mod_nor_veh_varg_warwolves_chariot', itemType.unit, 2, 'Progressive nor_veh', 'Norsca Surtha Unit: Varg Ice Wolf Chariots'),
    108033: itemData(IC.useful, 1, 'wh_mod_nor_veh_giant_war_wagon_0', itemType.unit, 4, 'Progressive nor_bst', 'Norsca Surtha Unit: Mammoth War Wagon'),
    108034: itemData(IC.useful, 1, 'wh_mod_nor_veh_giant_cannon_wagon_0', itemType.unit, 5, 'Progressive nor_bst', 'Norsca Surtha Unit: Mammoth War Wagon (Hellcannon)'),
    108035: itemData(IC.useful, 1, 'wh_mod_nor_veh_giant_temple_wagon_0', itemType.unit, 5, 'Progressive nor_bst', 'Norsca Surtha Unit: Mammoth War Wagon (Warshrine)'),

    #Overwriting this key with an unrelated unit as the key needed erasing anyway
    108007: itemData(IC.useful, 1, 'wh_mod_nor_veh_gorebeast_chariot', itemType.unit, 4, 'Progressive nor_veh', 'Norsca Surtha Unit: Varg Gorebeast Chariots'),
    #Adding additional units
    108063: itemData(IC.useful, 1, 'wh_mod_nor_veh_seeker_chariots', itemType.unit, 3, 'Progressive nor_veh', 'Norsca Surtha Unit: Seeker Chariots'),
    108064: itemData(IC.useful, 1, 'wh_mod_nor_veh_burning_chariots', itemType.unit, 4, 'Progressive nor_veh', 'Norsca Surtha Unit: Burning Chariots'),
    108065: itemData(IC.useful, 1, 'wh_mod_nor_veh_skullcannon', itemType.unit, 4, 'Progressive nor_veh', 'Norsca Surtha Unit: Skullcannon'),
    108066: itemData(IC.useful, 1, 'wh_mod_nor_veh_razorgor_chariots', itemType.unit, 4, 'Progressive nor_veh', 'Norsca Surtha Unit: Plague Chariots'),
})

buildings: dict[int, itemData] = {key + 70000: itemData(unit.classification,
                                                        unit.count,
                                                        unit.name,
                                                        unit.type,
                                                        unit.tier,
                                                        unit.progressionGroup,
                                                        unit.readableName.replace("Norsca ", "Norsca Surtha "))
                                  for key, unit in norsca.buildings.items()}

techs: dict[int, itemData] = {key + 70000: itemData(unit.classification,
                                                    unit.count,
                                                    unit.name,
                                                    unit.type,
                                                    unit.tier,
                                                    unit.progressionGroup,
                                                    unit.readableName.replace("Norsca ", "Norsca Surtha "))
                              for key, unit in norsca.techs.items()}

progUnits: dict[int, itemData] = {key + 70000: itemData(unit.classification,
                                                        unit.count,
                                                        unit.name,
                                                        unit.type,
                                                        unit.tier,
                                                        unit.progressionGroup,
                                                        unit.readableName.replace("Norsca ", "Norsca Surtha "))
                                  for key, unit in norsca.progUnits.items()}
progUnits.update({
    109201: itemData(IC.useful, 2, "Progressive nor_rng", itemType.unit, 2, None, "Progressive Norsca Surtha Unit: Ranged"),
    109202: itemData(IC.useful, 2, "Progressive nor_cav", itemType.unit, 2, None, "Progressive Norsca Surtha Unit: Cavalry"),
    109204: itemData(IC.useful, 4, "Progressive nor_veh", itemType.unit, 4, None, "Progressive Norsca Surtha Unit: Chariot"),
})

progBuildings: dict[int, itemData] = {key + 70000: itemData(unit.classification,
                                                            unit.count,
                                                            unit.name,
                                                            unit.type,
                                                            unit.tier,
                                                            unit.progressionGroup,
                                                            unit.readableName.replace("Norsca ", "Norsca Surtha "))
                                      for key, unit in norsca.progBuildings.items()}

progTechs: dict[int, itemData] = {key + 70000: itemData(unit.classification,
                                                        unit.count,
                                                        unit.name,
                                                        unit.type,
                                                        unit.tier,
                                                        unit.progressionGroup,
                                                        unit.readableName.replace("Norsca ", "Norsca Surtha "))
                                  for key, unit in norsca.progTechs.items()}

special: dict[int, specialItemData] = {}

rituals: dict[int, specialItemData] = {}
