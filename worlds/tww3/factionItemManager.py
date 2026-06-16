from __future__ import annotations
from worlds.tww3.dataStructs import itemData, itemType
from types import ModuleType

#Base Game
from worlds.tww3.faction_item_tables import (beastmen, bretonnia, cathay, cathayBhashiva, chaosDwarfs, daemons,
                                             darkElves, dwarfs, empire, greenskins, highElves, highElvesAislinn, khorne,
                                             kislev, lizardmen, lizardmenNakai, norsca, nurgle, ogreKingdoms, skaven,
                                             slaanesh, slaaneshDechala, tombKings, tzeentch, tzeentchChangeling,
                                             vampireCoast, vampireCounts, warriorsOfChaos, warriorsOfChaosKhorne,
                                             warriorsOfChaosNurgle, warriorsOfChaosSlaanesh, warriorsOfChaosTzeentch,
                                             woodElves)

#Mod Support
from worlds.tww3.mod_item_tables import (expandedRoster, mousillon, empireEdvard, tzeentchEgrimm, norscaSurtha,
                                         southernRealms, crustaceans, lobsters)

raceModuleDict: dict[str, ModuleType] = {
    "beastmen": beastmen, #10000
    "bretonnia": bretonnia, #12000
    "cathay": cathay, #14000
    "cathayBhashiva": cathayBhashiva, #74000
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
    "tzeentchChangeling": tzeentchChangeling, #72000
    "vampireCoast": vampireCoast, #50000
    "vampireCounts": vampireCounts, #52000
    "woodElves": woodElves, #54000
    "chaos": warriorsOfChaos, #56000
    "chaosKhorne": warriorsOfChaosKhorne, #58000
    "chaosNurgle": warriorsOfChaosNurgle, #60000
    "chaosSlaanesh": warriorsOfChaosSlaanesh, #62000
    "chaosTzeentch": warriorsOfChaosTzeentch, #64000
}

raceToMainRaceDict: dict[str, str] = {
    "highElvesAislinn": "highElves",
    "lizardmenNakai": "lizardmen",
    "slaaneshDechala": "slaanesh",
    "empireEdvard": "empire",
    "tzeentchEgrimm": "tzeentch",
    "norscaSurtha": "norsca",
}

moddedItemDict: dict[str, ModuleType] = {
    "decomposed expanded roster": expandedRoster, #100000
}

for race, module in raceModuleDict.items():
    fo = open(f"C:/Users/jorda/Documents/output_{race}.csv", "w+")
    lines = []

    items = module.units.items()
    items.update({key: itemData(*item[:2], *item[3:6], item[6], item[9]) for key, item in module.special.items() if item.type == itemType.unit})

    for ukey, unit in items:
        for bkey, building in enumerate(module.buildings.values()):
            if "settlement" in building.name and "hro" not in unit.progressionGroup: # and not "_ror" in unit.name
                if race == "daemons":
                    if "sla" in unit.name and not "sla" in building.name:
                        continue
                    elif "tze" in unit.name and not "tze" in building.name:
                        continue
                    elif "kho" in unit.name and not "kho" in building.name:
                        continue
                    elif "nur" in unit.name and not "nur" in building.name:
                        continue

                line = f"{ukey}{bkey},{building.name},{unit.name}\n"

                if line in lines:
                    continue
                fo.write(line)
                lines.append(line)
                #print(f"{ukey}{bkey},{building.name},{unit.name}")
    fo.close()


raceModuleDict.update({
    "mousillon": mousillon,  #102000
    "empireEdvard": empireEdvard, #104000
    "tzeentchEgrimm": tzeentchEgrimm, #106000
    "norscaSurtha": norscaSurtha, #108000
    "southernRealms": southernRealms, #110000
    "crustaceans": crustaceans, #112000
    "lobsters": lobsters, #114000
})

def getAllItems(playerRace = "", playerFaction = "", modList = None) -> dict[int, itemData]:
    itemDict: dict[int, itemData] = {}
    for race, module in raceModuleDict.items():
        if playerRace == race or playerRace == "":
            itemDict.update(module.units)
            itemDict.update(module.buildings)
            itemDict.update(module.techs)
            itemDict.update(module.progUnits)
            itemDict.update(module.progBuildings)
            itemDict.update(module.progTechs)
            itemDict.update({key: itemData(*item[:2], *item[3:6], item[6], item[9]) for key, item in module.special.items() if playerFaction in item.faction or playerFaction == "" or item.faction == []}) #Turn special item into regular item
            try:
                #print(module.rituals.items())
                itemDict.update({key: itemData(*item[:2], *item[3:6], item[6], item[9]) for key, item in module.rituals.items() if playerFaction in item.faction or playerFaction == "" or item.faction == []})
            except AttributeError:
                pass
        if playerRace == race:
            try:
                for key in module.removeKeys:
                    itemDict.pop(key)
            except AttributeError:
                pass

    for modName, module in moddedItemDict.items():
        if modList is None or modName in modList:
            for table in module.dicts:
                itemDict.update({key: itemData(*item[:2], *item[4:]) for key, item in table.items()}) #Turn mod item into regular item

    return itemDict

def getModdedItems(world):
    modList = [mod.lower() for mod in world.options.mod_list] #In case the player used capitalisation in the name

    #If the player is playing a special subfaction that has it's own module, then we need to check the main faction mod content
    try:
        playerRace = raceToMainRaceDict[world.playerFaction.race]
    except KeyError:
        playerRace = world.playerFaction.race

    moddedItems: dict[int, itemData] = {}
    for modName, module in moddedItemDict.items():
        if modList != [] and modName in modList:
            for table in module.dicts:
                moddedItems.update({key: itemData(*item[:2], *item[4:]) for key, item in table.items() if
                                    item.race == playerRace and
                                    (item.faction == world.playerFaction.name or item.faction == "")})
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

def getSpecial(world, bypass = False):
    specialItems: dict[int, itemData] = {}
    for key, item in raceModuleDict[world.playerFaction.race].special.items():
        if world.playerFaction.name in item.faction or item.faction == []:
            if item.type == itemType.unit:
                if world.options.progressive_units and item.isProgressiveItem:
                    specialItems.update({key: item})
                elif not (world.options.progressive_units or item.isProgressiveItem):
                    specialItems.update({key: item})
                continue
            elif item.type == itemType.building:
                if bypass:
                    specialItems.update({key: item})
                elif world.options.progressive_buildings and item.isProgressiveItem:
                    specialItems.update({key: item})
                elif not (world.options.progressive_buildings or item.isProgressiveItem):
                    specialItems.update({key: item})
                continue
            elif item.type == itemType.tech:
                if bypass:
                    specialItems.update({key: item})
                elif world.options.progressive_technologies and item.isProgressiveItem:
                    specialItems.update({key: item})
                elif not (world.options.progressive_technologies or item.isProgressiveItem):
                    specialItems.update({key: item})
                continue
            specialItems.update({key: item})
    return specialItems.items()

def getRituals(world):
    ritualItems: dict[int, itemData] = {}
    for key, item in raceModuleDict[world.playerFaction.race].rituals.items():
        if world.playerFaction.name in item.faction or item.faction == []:
            ritualItems.update({key: item})
    return ritualItems.items()