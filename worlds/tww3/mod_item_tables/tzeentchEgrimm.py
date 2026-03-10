from BaseClasses import ItemClassification as IC
from worlds.tww3.itemTypes import itemType, itemData, specialItemData
from worlds.tww3.faction_item_tables import tzeentch

units: dict[int, itemData] = {key + 58000: itemData(unit.classification,
                                                    unit.count,
                                                    unit.name,
                                                    unit.type,
                                                    unit.tier,
                                                    unit.progressionGroup,
                                                    unit.readableName.replace("Tzeentch ", "Tzeentch Egrimm "))
                              for key, unit in tzeentch.units.items()}
units.update({
    106045: itemData(IC.useful, 1, 'mixu_tze_inf_cultists', itemType.unit, 1, 'Progressive tze_inf', 'Tzeentch Egrimm Unit: Cultists of Tzeentch'),
    106046: itemData(IC.useful, 1, 'mixu_tze_mon_trolls', itemType.unit, 3, 'Progressive tze_inf', 'Tzeentch Egrimm Unit: Sorcerous Trolls'),

    106047: itemData(IC.useful, 1, 'mixu_tze_inf_cultist_acolytes', itemType.unit, 1, 'Progressive tze_rng', 'Tzeentch Egrimm Unit: Acolytes of Tzeentch'),

    106048: itemData(IC.useful, 1, 'mixu_tze_mon_warhound', itemType.unit, 1, 'Progressive tze_bst', 'Tzeentch Egrimm Unit: Chaos Warhounds of Tzeentch'),
    106049: itemData(IC.useful, 1, 'mixu_tze_mon_chaos_dragon', itemType.unit, 3, 'Progressive tze_bst', 'Tzeentch Egrimm Unit: Chaos Dragon'),
})

buildings: dict[int, itemData] = {key + 58000: itemData(unit.classification,
                                                        unit.count,
                                                        unit.name,
                                                        unit.type,
                                                        unit.tier,
                                                        unit.progressionGroup,
                                                        unit.readableName.replace("Tzeentch ", "Tzeentch Egrimm "))
                                  for key, unit in tzeentch.buildings.items()}

buildings.update({
    106408: itemData(IC.useful, 1, 'mixu_tze_cabal_cult_1', itemType.building, 0, 'Progressive tze_cabal_cult', 'Tzeentch Egrimm Building: Cult of Deceits'),
    106409: itemData(IC.useful, 1, 'mixu_tze_cabal_cult_2', itemType.building, 1, 'Progressive tze_cabal_cult', 'Tzeentch Egrimm Building: Cult of Lies'),
    106410: itemData(IC.useful, 1, 'mixu_tze_cabal_cult_3', itemType.building, 2, 'Progressive tze_cabal_cult', 'Tzeentch Egrimm Building: Cult of Change'),
    106433: itemData(IC.useful, 1, 'mixu_tze_cabal_cult_4', itemType.building, 3, 'Progressive tze_cabal_cult', 'Tzeentch Egrimm Building: Cult of Exchange'),
    106434: itemData(IC.useful, 1, 'mixu_tze_cabal_trolls_1', itemType.building, 0, 'Progressive tze_cabal_trolls', 'Tzeentch Egrimm Building: Chaos Troll Lair'),
    106435: itemData(IC.useful, 1, 'mixu_tze_cabal_trolls_2', itemType.building, 1, 'Progressive tze_cabal_trolls', 'Tzeentch Egrimm Building: Sorcerous Chaos Troll Lair'),
    106436: itemData(IC.useful, 1, 'mixu_tze_cabal_chaos_dragon', itemType.building, 0, 'Progressive tze_cabal_dragons', 'Tzeentch Egrimm Building: Chaos Dragon Lair'),
})
#buildings.pop(106434)
#buildings.pop(106435)

techs: dict[int, itemData] = {key + 58000: itemData(unit.classification,
                                                    unit.count,
                                                    unit.name,
                                                    unit.type,
                                                    unit.tier,
                                                    unit.progressionGroup,
                                                    unit.readableName.replace("Tzeentch ", "Tzeentch Egrimm "))
                              for key, unit in tzeentch.techs.items()}

progUnits: dict[int, itemData] = {key + 58000: itemData(unit.classification,
                                                        unit.count,
                                                        unit.name,
                                                        unit.type,
                                                        unit.tier,
                                                        unit.progressionGroup,
                                                        unit.readableName.replace("Tzeentch ", "Tzeentch Egrimm "))
                                  for key, unit in tzeentch.progUnits.items()}

progBuildings: dict[int, itemData] = {key + 58000: itemData(unit.classification,
                                                            unit.count,
                                                            unit.name,
                                                            unit.type,
                                                            unit.tier,
                                                            unit.progressionGroup,
                                                            unit.readableName.replace("Tzeentch ", "Tzeentch Egrimm "))
                                      for key, unit in tzeentch.progBuildings.items()}
progBuildings.update({
    107302: itemData(IC.useful, 4, 'Progressive tze_cabal_cult', itemType.building, 4, None, 'Progressive Tzeentch Egrimm Building: Caster'),
    107310: itemData(IC.useful, 2, 'Progressive tze_cabal_trolls', itemType.building, 2, None, 'Progressive Tzeentch Egrimm Building: Trolls'),
    107311: itemData(IC.useful, 1, 'Progressive tze_cabal_dragons', itemType.building, 1, None, 'Progressive Tzeentch Egrimm Building: Dragon Lair'),
})

progTechs: dict[int, itemData] = {key + 58000: itemData(unit.classification,
                                                        unit.count,
                                                        unit.name,
                                                        unit.type,
                                                        unit.tier,
                                                        unit.progressionGroup,
                                                        unit.readableName.replace("Tzeentch ", "Tzeentch Egrimm "))
                                  for key, unit in tzeentch.progTechs.items()}

special: dict[int, specialItemData] = {}
