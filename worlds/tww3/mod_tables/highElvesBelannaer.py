from BaseClasses import ItemClassification as IC
from worlds.tww3.item_types import ItemType, ItemData, specialItemData
from worlds.tww3.faction_tables import highElves

# @formatter:off

units: dict[int, ItemData] = highElves.units

buildings: dict[int, ItemData] = {key+80000: ItemData(unit.classification,
                                                  unit.count,
                                                  unit.name,
                                                  unit.type,
                                                  unit.tier,
                                                  unit.progressionGroup,
                                                  unit.readableName.replace("HighElf", "HighElf Belannaer"))
                              for key, unit in highElves.buildings.items()}

techs: dict[int, ItemData] = highElves.techs

progUnits: dict[int, ItemData] = {key+80000: ItemData(unit.classification,
                                                  unit.count,
                                                  unit.name,
                                                  unit.type,
                                                  unit.tier,
                                                  unit.progressionGroup,
                                                  unit.readableName.replace("HighElf", "HighElf Belannaer"))
                              for key, unit in highElves.progBuildings.items()}

progBuildings: dict[int, ItemData] = highElves.progBuildings

progTechs: dict[int, ItemData] = highElves.progTechs

special: dict[int, specialItemData] = {}