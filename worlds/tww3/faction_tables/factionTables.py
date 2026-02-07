from __future__ import annotations
from .item_types import ItemData
from types import ModuleType

from . import bretonnia, warriorsOfChaosKhorne, warriorsOfChaosSlaanesh, warriorsOfChaosTzeentch
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
from . import warriorsOfChaosKhorne
from . import warriorsOfChaosNurgle
from . import warriorsOfChaosSlaanesh
from . import warriorsOfChaosTzeentch
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
    "woodElves": woodElves,
    "chaos": warriorsOfChaos,
    "chaosKhorne": warriorsOfChaosKhorne,
    "chaosNurgle": warriorsOfChaosNurgle,
    "chaosSlaanesh": warriorsOfChaosSlaanesh,
    "chaosTzeentch": warriorsOfChaosTzeentch,
}

def getAllItems():
    itemDict: dict[int, ItemData] = {}
    for faction in factionModuleDict.values():
        itemDict.update(faction.units)
        itemDict.update(faction.buildings)
        itemDict.update(faction.techs)
        itemDict.update(faction.progUnits)
        itemDict.update(faction.progBuildings)
        itemDict.update(faction.progTechs)
        itemDict.update({key: ItemData(*item[:1], *item[2:6], *item[7:]) for key, item in faction.special.items()}) #Turn special item into regular item
    return itemDict

def getUnits(race, progressive):
    if progressive:
        return factionModuleDict[race].progUnits.items()
    else:
        return factionModuleDict[race].units.items()

def getBuildings(race, progressive):
    if progressive:
        return factionModuleDict[race].progBuildings.items()
    else:
        return factionModuleDict[race].buildings.items()

def getTechs(race, progressive):
    if progressive:
        return factionModuleDict[race].progTechs.items()
    else:
        return factionModuleDict[race].techs.items()

def getSpecial(race, faction):
    specialItems: dict[int, ItemData] = {}
    for key, item in factionModuleDict[race].special.items():
        if item.faction == faction:
            specialItems.update({key: item})
    return specialItems.items()