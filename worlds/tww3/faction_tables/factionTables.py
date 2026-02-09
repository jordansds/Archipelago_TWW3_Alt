from __future__ import annotations
from .item_types import ItemData, ItemType
from types import ModuleType

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
from . import highElvesAislinn
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

raceModuleDict: dict[str, ModuleType] = {
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
    "highElvesAislinn": highElvesAislinn,
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
    for race in raceModuleDict.values():
        itemDict.update(race.units)
        itemDict.update(race.buildings)
        itemDict.update(race.techs)
        itemDict.update(race.progUnits)
        itemDict.update(race.progBuildings)
        itemDict.update(race.progTechs)
        itemDict.update({key: ItemData(*item[:1], *item[2:6], item[7], item[9]) for key, item in race.special.items()}) #Turn special item into regular item
    return itemDict

def getUnits(race, progressive):
    if progressive:
        return raceModuleDict[race].progUnits.items()
    else:
        return raceModuleDict[race].units.items()

def getBuildings(race, progressive):
    if progressive:
        return raceModuleDict[race].progBuildings.items()
    else:
        return raceModuleDict[race].buildings.items()

def getTechs(race, progressive):
    if progressive:
        return raceModuleDict[race].progTechs.items()
    else:
        return raceModuleDict[race].techs.items()

def getSpecial(world):
    specialItems: dict[int, ItemData] = {}
    for key, item in raceModuleDict[world.playerFaction.race].special.items():
        if item.faction == world.playerFaction.name or item.faction == "":
            if item.type == ItemType.unit:
                if world.options.progressive_units:
                    specialItems.update({key: item})
                continue
            elif item.type == ItemType.building:
                if world.options.progressive_buildings:
                    specialItems.update({key: item})
                continue
            elif item.type == ItemType.tech:
                if world.options.progressive_technologies:
                    specialItems.update({key: item})
                continue
            specialItems.update({key: item})

    return specialItems.items()