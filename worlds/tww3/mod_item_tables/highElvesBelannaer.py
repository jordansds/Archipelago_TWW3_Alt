from BaseClasses import ItemClassification as IC
from worlds.tww3.itemTypes import itemType, itemData, specialItemData
from worlds.tww3.faction_item_tables import highElves

# @formatter:off

units: dict[int, itemData] = highElves.units

buildings: dict[int, itemData] = {key+80000: itemData(unit.classification,
                                                  unit.count,
                                                  unit.name,
                                                  unit.type,
                                                  unit.tier,
                                                  unit.progressionGroup,
                                                  unit.readableName.replace("HighElf", "HighElf Belannaer"))
                              for key, unit in highElves.buildings.items()}

techs: dict[int, itemData] = highElves.techs

progUnits: dict[int, itemData] = {key+80000: itemData(unit.classification,
                                                  unit.count,
                                                  unit.name,
                                                  unit.type,
                                                  unit.tier,
                                                  unit.progressionGroup,
                                                  unit.readableName.replace("HighElf", "HighElf Belannaer"))
                              for key, unit in highElves.progBuildings.items()}

progBuildings: dict[int, itemData] = highElves.progBuildings

progTechs: dict[int, itemData] = highElves.progTechs

special: dict[int, specialItemData] = {}