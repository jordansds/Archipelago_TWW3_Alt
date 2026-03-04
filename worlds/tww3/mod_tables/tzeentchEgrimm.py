from BaseClasses import ItemClassification as IC
from worlds.tww3.item_types import ItemType, ItemData, specialItemData
import worlds.tww3.faction_tables.tzeentch as tzeentch

units: dict[int, ItemData] = {
    106000: ItemData(IC.useful, 1, ' mixu_tze_inf_cultists', ItemType.unit, 1, 'Progressive tze_inf', 'Tze Unit: Cultists of Tzeentch'),
    106001: ItemData(IC.useful, 1, ' mixu_tze_inf_cultist_acolytes', ItemType.unit, 1, 'Progressive tze_inf', 'Tze Unit: Acolytes of Tzeentch'),
    106002: ItemData(IC.useful, 1, ' mixu_tze_inf_cultist_acolytes', ItemType.unit, 1, 'Progressive tze_inf', 'Tze Unit: Acolytes of Tzeentch'),
}

buildings: dict[int, ItemData] = tzeentch.buildings

techs: dict[int, ItemData] = tzeentch.techs

progUnits: dict[int, ItemData] = tzeentch.progUnits

progBuildings: dict[int, ItemData] = tzeentch.progBuildings

progTechs: dict[int, ItemData] = tzeentch.progTechs

special: dict[int, specialItemData] = {}

"""
mixu_tze_mon_chaos_dragon	Chaos Dragon
mixu_tze_mon_trolls	Sorcerous Trolls
mixu_tze_inf_chosen_of_cabal	Chosen of the Cabal
mixu_tze_mon_warhound	Chaos Warhounds of Tzeentch
"""