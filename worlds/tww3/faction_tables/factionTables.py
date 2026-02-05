from __future__ import annotations
from item_types import ItemData, specialItemData
from typing import TYPE_CHECKING
from types import ModuleType
if TYPE_CHECKING:
    from ..world import TWW3World

from . import beastmen
from . import bretonnia
from . import cathay
from . import chaosDwarfs
from . import daemons
from . import darkElves
from . import dwarfs
from . import empire
from . import greenskins
from . import highElves
from . import khorne
from . import kislev
from . import lizardmen
from . import norsca
from . import nurgle
from . import ogreKingdoms
from . import skaven
from . import slaanesh
from . import tombKings
from . import tzeentch
from . import vampireCoast
from . import vampireCounts
from . import warriorsOfChaos
from . import woodElves

factionModuleDict: dict[str, ModuleType] = {
    "beastmen": beastmen,
    "bretonnia": bretonnia,
    "cathay": cathay,
    "chaosDwarfs": chaosDwarfs,
    "daemons": daemons,
    "darkElves": darkElves,
    "dwarfs": dwarfs,
    "empire": empire,
    "greenskins": greenskins,
    "highElves": highElves,
    "khorne": khorne,
    "kislev": kislev,
    "lizardmen": lizardmen,
    "norsca": norsca,
    "nurgle": nurgle,
    "ogreKingdoms": ogreKingdoms,
    "skaven": skaven,
    "slaanesh": slaanesh,
    "tombKings": tombKings,
    "tzeentch": tzeentch,
    "vampireCoast": vampireCoast,
    "VampireCounts": vampireCounts,
    "warriorsOfChaos": warriorsOfChaos,
    "woodElves": woodElves
}

def getUnits(race, progressive):
    if progressive:
        return factionModuleDict[race].progUnits
    else:
        return factionModuleDict[race].units

def getBuildings(race, progressive):
    if progressive:
        return factionModuleDict[race].progBuildings
    else:
        return factionModuleDict[race].buildings

def getTechs(race, progressive):
    if progressive:
        return factionModuleDict[race].progTechs
    else:
        return factionModuleDict[race].techs

def getSpecial(race, faction):
    specialItems: dict[int, ItemData] = {}
    for key, item in factionModuleDict[race].special:
        if item.faction == faction:
            specialItems.update({key: ItemData(*item[:1], *item[2:])}) #remove the faction tag from the item, we don't need it anymore.
    return specialItems