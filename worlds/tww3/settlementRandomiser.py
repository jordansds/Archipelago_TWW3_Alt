from __future__ import annotations

from worlds.tww3.dataStructs import factionData, settlementData
from worlds.tww3.item_tables import settlements
from worlds.tww3.item_tables import factions
from collections import Counter
import time

# Return the distance between two settlements
def getDistance(s1: settlementData, s2: settlementData) -> int:
    return ((s1.x-s2.x)**2 + (s1.y-s2.y)**2)**0.5

class settlementRandomiser:

    def __init__(self, random, playerFaction, playerKey, startingSettlementCount, map):
        self.start = time.time()
        self.random = random
        self.playerFaction = playerFaction
        self.playerKey = playerKey
        self.startingSettlementCount = startingSettlementCount
        self.settlementDict = settlements.mapDict[map]
        self.factionDict = factions.factionDict
        self.hordeList = factions.hordeList

        self.factionKeys: list[int] = [key for key in self.factionDict.keys() if key % 10 != 0]
        random.shuffle(self.factionKeys)
        self.settlementKeys: list[int] = list(self.settlementDict.keys())
        random.shuffle(self.settlementKeys)

        self.shuffledFactionList: list[str] = []
        self.shuffledSettlementDict: dict[int, settlementData] = {}
        self.capitals: dict[str, str] = {}

        self.keysToRemove: list[int] = []

    def getSettlements(self):
        self.shuffledSettlementDict = self.settlementDict
        return self.shuffledSettlementDict
    #Remove the settlements that have been assigned.
    def removeKeys(self) -> None:
        for key in self.keysToRemove:
            if key in self.settlementKeys:
                self.settlementKeys.remove(key)
        self.keysToRemove: list[int] = []

    def assignSettlement(self, key, settlement, faction) -> None:
        try:
            factionName = faction.name
        except AttributeError:
            factionName = faction
        self.shuffledSettlementDict[key] = settlementData(settlement.name, settlement.type, settlement.x,
                                                      settlement.y, factionName,
                                                      settlement.climate,
                                                      settlement.readableName)
        self.shuffledFactionList.append(factionName)
        self.keysToRemove.append(key)

    def randomisePlayer(self):
        playerFaction = self.factionDict[self.playerKey]
        if playerFaction.name not in self.hordeList:
            # Assign player their first settlement
            if playerFaction.race == "woodElves":
                for i, sKey in enumerate(self.settlementKeys):
                    playerSettlement: settlementData = self.settlementDict[sKey]
                    if playerSettlement.type == "magical forest":
                        self.assignSettlement(sKey, playerSettlement, playerFaction)
                        break
            elif playerFaction.race[:5] == "chaos" or playerFaction.race == "lobsters":
                for i, sKey in enumerate(self.settlementKeys):
                    playerSettlement: settlementData = self.settlementDict[sKey]
                    if playerSettlement.type == "dark fortress":
                        self.assignSettlement(sKey, playerSettlement, playerFaction)
                        break
            else:
                sKey = self.settlementKeys[0]
                playerSettlement: settlementData = self.settlementDict[sKey]
                self.assignSettlement(sKey, self.settlementDict[sKey], playerFaction)
            self.removeKeys()
            self.capitals.update({playerFaction.name: playerSettlement.name})


            # Assign the player extra settlements
            for i in range(self.startingSettlementCount - 1):
                distance: int = 10000
                for j, sKey in enumerate(self.settlementKeys):
                    settlement: settlementData = self.settlementDict[sKey]

                    settlementDistance: int = getDistance(settlement, playerSettlement)

                    if settlementDistance < distance:
                        distance = settlementDistance
                        closestKey = sKey
                        closestSettlement = settlement

                self.assignSettlement(closestKey, closestSettlement, playerFaction)
                self.removeKeys()

    def randomiseWoodElves(self) -> None:
        # Assigns each wood elf a magical forest
        for sKey in self.settlementKeys:
            settlement: settlementData = self.settlementDict[sKey]
            if settlement.type == "magical forest":
                for i, fKey in enumerate(self.factionKeys):
                    faction: factionData = self.factionDict[fKey]
                    if faction.race == "woodElves" and faction.name not in self.shuffledFactionList:
                        self.assignSettlement(sKey, settlement, faction)
                        self.factionKeys.pop(i)
                        self.capitals.update({faction.name: settlement.name})
                        break
        self.removeKeys() # Remove the magical forests that have been assigned.

    def randomiseChaos(self) -> None:
        # Assigns each chaos faction a magical forest
        for sKey in self.settlementKeys:
            settlement: settlementData = self.settlementDict[sKey]
            if settlement.type == "dark fortress":
                for i, fKey in enumerate(self.factionKeys):
                    faction: factionData = self.factionDict[fKey]
                    if (faction.race[:5] == "chaos" or faction.race == "lobsters") and faction.name not in self.shuffledFactionList:
                        self.assignSettlement(sKey, settlement, faction)
                        self.factionKeys.pop(i)
                        self.capitals.update({faction.name: settlement.name})
                        break
        self.removeKeys() # Remove the magical forests that have been assigned.


    # Assigns all other factions their first settlement (if they aren't a horde)
    def randomiseFirstSettlement(self) -> None:
        for sKey in self.settlementKeys:
            settlement: settlementData = self.settlementDict[sKey]

            for i, fKey in enumerate(self.factionKeys):
                faction: factionData = self.factionDict[fKey]
                if faction.name not in self.hordeList and faction.name not in self.shuffledFactionList:
                    self.assignSettlement(sKey, settlement, faction)
                    self.factionKeys.pop(i)
                    self.capitals.update({faction.name: settlement.name})
                    break
        self.removeKeys() #Remove the settlements that have been assigned

    def randomiseRemainingSettlements(self) -> None:
        blackList: list[str] = []
        shuffledSettlementDict = self.shuffledSettlementDict
        shuffledSettlementList = list(shuffledSettlementDict.items())

        #Asign each faction new settlements, based on distance from their capital
        for i, sKey in enumerate(self.settlementKeys):
            settlement: settlementData = self.settlementDict[sKey]
            distance: int = 10000

            for aKey, assignedSettlement in shuffledSettlementList:
                faction: str = assignedSettlement.faction
                if faction in self.hordeList:
                    continue

                settlementsOwned: int = 0

                #shuffledSettlementList2 = list(shuffledSettlementDict.keys())
                # need to check if faction already has too many settlements.
                for fKey in shuffledSettlementDict.keys():
                    if faction == self.playerFaction.name:
                        settlementsOwned = 3
                        break

                    if shuffledSettlementDict[fKey].faction == faction:
                        settlementsOwned += 1
                        if settlementsOwned == 3:
                            blackList.append(faction)
                            break

                if settlementsOwned == 3:
                    continue

                newDistance: int = getDistance(settlement, assignedSettlement)

                if newDistance < distance and settlementsOwned < 3:
                    distance = newDistance
                    closestFaction = assignedSettlement.faction

            self.assignSettlement(sKey, settlement, closestFaction)
            #self.shuffledFactionList.append(closestFaction)

    def randomiseHordes(self) -> dict[str, str]:
        hordes: dict[str, str] = {}
        for fKey in self.factionKeys:
            faction = self.factionDict[fKey]
            if faction.name in self.hordeList:
                settlement = self.random.choice(self.settlementDict)
                hordes.update({faction.name: settlement.name})
        return hordes

    def randomiseSettlements(self):
        self.randomisePlayer()
        self.randomiseWoodElves()
        self.randomiseChaos()
        #self.random.shuffle(self.settlementKeys)
        self.randomiseFirstSettlement()
        self.randomiseRemainingSettlements()

        return self.shuffledSettlementDict

    def getRequiredDiploRange(self, sphereCount, sphereRadius: int) -> tuple[list[int], dict[str, int]]:
        #factionSpheres: list[list[str]] = []
        factionSpheres: dict[str, int] = {}
        settlementSpheres: list[int] = []
        #playerCapital = next(iter(self.shuffledSettlementDict.values()))
        playerCapital = [settlement for settlement in self.shuffledSettlementDict.values() if settlement.faction == self.playerFaction.name][0]
        for settlement in self.shuffledSettlementDict.values():
            distance = getDistance(playerCapital, settlement)
            sphere = int(distance / sphereRadius)
            if sphere <= sphereCount:
                factionSpheres.update({settlement.faction: sphere})
                settlementSpheres.append(sphere)
            else:
                factionSpheres.update({settlement.faction: sphere})
                #factionSpheres.append([settlement.faction, str(sphereCount)])
                settlementSpheres.append(sphereCount.value + 1)

        return settlementSpheres, factionSpheres

    def debug(self):
        x = []
        for i, d in self.shuffledSettlementDict.items():
            x.append(d.faction)
        counter = Counter(x)

        #print(counter)

        #print(time.time() - self.start)

"""import random
for i in range(2):
    test = SettlementManager(random, self.factionDict[92], 92, 3) #92 = "wh_dlc05_wef_wood_elves"
    settlements = test.randomiseSettlements()
    hordes = test.randomiseHordes()
    factionSpheres = test.getRequiredDiploRange(5, 100)
    print(factionSpheres)
    test.debug()"""
