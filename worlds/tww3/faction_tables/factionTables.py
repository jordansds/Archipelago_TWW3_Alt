from __future__ import annotations
from .item_types import ItemData, ItemType
from types import ModuleType

#Base Game
from . import beastmen, bretonnia, cathay, chaosDwarfs, daemons, darkElves, dwarfs, empire, greenskins, highElves
from . import highElvesAislinn, khorne, kislev, lizardmen, lizardmenNakai, norsca, nurgle, ogreKingdoms, skaven
from . import slaanesh, slaaneshDechala, tombKings, tzeentch, vampireCoast, vampireCounts, warriorsOfChaos
from . import warriorsOfChaosKhorne, warriorsOfChaosNurgle, warriorsOfChaosSlaanesh, warriorsOfChaosTzeentch, woodElves

#Mod Support
from . import expandedRoster

raceModuleDict: dict[str, ModuleType] = {
    "beastmen": beastmen, #10000
    "bretonnia": bretonnia, #12000
    "cathay": cathay, #14000
    "chaosDwarfs": chaosDwarfs, #16000
    "daemons": daemons, #18000
    "darkElves": darkElves, #20000
    "dwarfs": dwarfs, #22000
    "empire": empire, #24000
    "greenskins": greenskins, #28000
    "highElves": highElves, #30000
    "highElvesAislinn": highElvesAislinn, #66000
    "khorne": khorne, #32000
    "kislev": kislev, #34000
    "lizardmen": lizardmen, #36000
    "lizardmenNakai": lizardmenNakai, #68000
    "norsca": norsca, #38000
    "nurgle": nurgle, #40000
    "ogreKingdoms": ogreKingdoms, #26000
    "skaven": skaven, #42000
    "slaanesh": slaanesh, #44000
    "slaaneshDechala": slaaneshDechala, #70000
    "tombKings": tombKings, #46000
    "tzeentch": tzeentch, #48000
    "vampireCoast": vampireCoast, #50000
    "vampireCounts": vampireCounts, #52000
    "woodElves": woodElves, #54000
    "chaos": warriorsOfChaos, #56000
    "chaosKhorne": warriorsOfChaosKhorne, #58000
    "chaosNurgle": warriorsOfChaosNurgle, #60000
    "chaosSlaanesh": warriorsOfChaosSlaanesh, #62000
    "chaosTzeentch": warriorsOfChaosTzeentch, #64000
}

moddedItemDict: dict[str, ModuleType] = {
    "expanded roster": expandedRoster, #72000
}

def getAllItems(playerRace = "", modList = None) -> dict[int, ItemData]:
    itemDict: dict[int, ItemData] = {}
    for race, module in raceModuleDict.items():
        if playerRace == race or playerRace == "":
            itemDict.update(module.units)
            itemDict.update(module.buildings)
            itemDict.update(module.techs)
            itemDict.update(module.progUnits)
            itemDict.update(module.progBuildings)
            itemDict.update(module.progTechs)
            itemDict.update({key: ItemData(*item[:2], *item[3:6], item[6], item[9]) for key, item in module.special.items()}) #Turn special item into regular item

    for modName, module in moddedItemDict.items():
        if modList is None or modName in modList:
            for table in module.dicts:
                itemDict.update({key: ItemData(*item[:2], *item[4:]) for key, item in table.items()}) #Turn mod item into regular item
    return itemDict

def getModdedItems(playerRace = "", playerFaction = "", modList = []):
    modList = [mod.lower() for mod in modList] #In case the player used capitalisation in the name
    #modList = ["expanded roster"]
    moddedItems: dict[int, ItemData] = {}
    for modName, module in moddedItemDict.items():
        if modList != [] and modName in modList:
            for table in module.dicts:
                moddedItems.update({key: ItemData(*item[:2], *item[4:]) for key, item in table.items() if item.race == playerRace and (item.faction == playerFaction or item.faction == "")})
    return moddedItems.items()

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
                if world.options.progressive_units and item.isProgressionItem:
                    specialItems.update({key: item})
                elif not (world.options.progressive_units or item.isProgressionItem):
                    specialItems.update({key: item})
                continue
            elif item.type == ItemType.building:
                if world.options.progressive_buildings and item.isProgressionItem:
                    specialItems.update({key: item})
                elif not (world.options.progressive_buildings or item.isProgressionItem):
                    specialItems.update({key: item})
                continue
            elif item.type == ItemType.tech:
                if world.options.progressive_technologies and item.isProgressionItem:
                    specialItems.update({key: item})
                elif not (world.options.progressive_technologies or item.isProgressionItem):
                    specialItems.update({key: item})
                continue
            specialItems.update({key: item})
    return specialItems.items()