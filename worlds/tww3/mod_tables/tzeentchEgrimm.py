from BaseClasses import ItemClassification as IC
from worlds.tww3.item_types import ItemType, ItemData, specialItemData
from worlds.tww3.faction_tables import tzeentch

units: dict[int, ItemData] = {key+58000: ItemData(unit.classification,
                                                  unit.count,
                                                  unit.name,
                                                  unit.type,
                                                  unit.tier,
                                                  unit.progressionGroup,
                                                  unit.readableName.replace("Tze", "Tzeentch Egrimm"))
                              for key, unit in tzeentch.units.items()}
units.update({
    106045: ItemData(IC.useful, 1, ' mixu_tze_inf_cultists', ItemType.unit, 1, 'Progressive tze_inf', 'Tzeentch Egrimm Unit: Cultists of Tzeentch'),
    106046: ItemData(IC.useful, 1, 'mixu_tze_mon_trolls', ItemType.unit, 3, 'Progressive tze_inf', 'Tzeentch Egrimm Unit: Sorcerous Trolls'),

    106047: ItemData(IC.useful, 1, ' mixu_tze_inf_cultist_acolytes', ItemType.unit, 1, 'Progressive tze_rng', 'Tzeentch Egrimm Unit: Acolytes of Tzeentch'),

    106048: ItemData(IC.useful, 1, ' mixu_tze_mon_warhound', ItemType.unit, 1, 'Progressive tze_bst', 'Tzeentch Egrimm Unit: Chaos Warhounds of Tzeentch'),
    106049: ItemData(IC.useful, 1, 'mixu_tze_mon_chaos_dragon', ItemType.unit, 3, 'Progressive tze_bst', 'Tzeentch Egrimm Unit: Chaos Dragon'),
})

buildings: dict[int, ItemData] = {key+58000: ItemData(unit.classification,
                                                  unit.count,
                                                  unit.name,
                                                  unit.type,
                                                  unit.tier,
                                                  unit.progressionGroup,
                                                  unit.readableName.replace("Tze", "Tzeentch Egrimm"))
                              for key, unit in tzeentch.buildings.items()}

buildings.update({
    106408: ItemData(IC.useful, 1, 'mixu_tze_cabal_cult_1', ItemType.building, 0, 'Progressive tze_cabal_cult', 'Tzeentch Egrimm Building: Cult of Deceits'),
    106409: ItemData(IC.useful, 1, 'mixu_tze_cabal_cult_2', ItemType.building, 1, 'Progressive tze_cabal_cult', 'Tzeentch Egrimm Building: Cult of Lies'),
    106410: ItemData(IC.useful, 1, 'mixu_tze_cabal_cult_3', ItemType.building, 2, 'Progressive tze_cabal_cult', 'Tzeentch Egrimm Building: Cult of Change'),
    106433: ItemData(IC.useful, 1, 'mixu_tze_cabal_cult_4', ItemType.building, 3, 'Progressive tze_cabal_cult', 'Tzeentch Egrimm Building: Cult of Exchange'),
    106434: ItemData(IC.useful, 1, 'mixu_tze_cabal_trolls_1', ItemType.building, 0, 'Progressive tze_cabal_trolls', 'Tzeentch Egrimm Building: Chaos Troll Lair'),
    106435: ItemData(IC.useful, 1, 'mixu_tze_cabal_trolls_2', ItemType.building, 1, 'Progressive tze_cabal_trolls', 'Tzeentch Egrimm Building: Sorcerous Chaos Troll Lair'),
    106436: ItemData(IC.useful, 1, 'mixu_tze_cabal_chaos_dragon', ItemType.building, 0, 'Progressive tze_cabal_dragons', 'Tzeentch Egrimm Building: Chaos Dragon Lair'),
})
#buildings.pop(106434)
#buildings.pop(106435)

techs: dict[int, ItemData] = {key+58000: ItemData(unit.classification,
                                                  unit.count,
                                                  unit.name,
                                                  unit.type,
                                                  unit.tier,
                                                  unit.progressionGroup,
                                                  unit.readableName.replace("Tzeentch", "Tzeentch Egrimm"))
                              for key, unit in tzeentch.techs.items()}

progUnits: dict[int, ItemData] = {key+58000: ItemData(unit.classification,
                                                  unit.count,
                                                  unit.name,
                                                  unit.type,
                                                  unit.tier,
                                                  unit.progressionGroup,
                                                  unit.readableName.replace("Tzeentch", "Tzeentch Egrimm"))
                              for key, unit in tzeentch.progUnits.items()}

progBuildings: dict[int, ItemData] = {key+58000: ItemData(unit.classification,
                                                  unit.count,
                                                  unit.name,
                                                  unit.type,
                                                  unit.tier,
                                                  unit.progressionGroup,
                                                  unit.readableName.replace("Tzeentch", "Tzeentch Egrimm"))
                              for key, unit in tzeentch.progBuildings.items()}
progBuildings.update({
    107302: ItemData(IC.useful, 4, 'Progressive tze_cabal_cult', ItemType.building, 4, None, 'Progressive Tzeentch Egrimm Building: Caster'),
    107310: ItemData(IC.useful, 2, 'Progressive tze_cabal_trolls', ItemType.building, 2, None, 'Progressive Tzeentch Egrimm Building: Trolls'),
    107311: ItemData(IC.useful, 1, 'Progressive tze_cabal_dragons', ItemType.building, 1, None, 'Progressive Tzeentch Egrimm Building: Dragon Lair'),
})

progTechs: dict[int, ItemData] = {key+58000: ItemData(unit.classification,
                                                  unit.count,
                                                  unit.name,
                                                  unit.type,
                                                  unit.tier,
                                                  unit.progressionGroup,
                                                  unit.readableName.replace("Tzeentch", "Tzeentch Egrimm"))
                              for key, unit in tzeentch.progTechs.items()}

special: dict[int, specialItemData] = {}
