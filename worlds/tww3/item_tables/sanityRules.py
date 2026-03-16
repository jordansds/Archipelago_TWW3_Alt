from rule_builder.rules import Has, HasAll, HasAny, CanReachLocation


class ruleManager:
    def __init__(self, world):
        """        self.techSanityRules = {
            "HighElf Tech: Appoint Sea Masters": HasAll() | Has(),
            "HighElf Tech: Dragon's Bond": Has(),
            "HighElf Tech: Call the Great Herds": (Has("HighElf Tech: Trade Advancements") | Has("Progressive tech_hef_trade", 2 - world.options.starting_tier)) & (HasAll("HighElf Building: Livestock Pens", "HighElf Building: Cattle Ranch") | Has("Progressive HighElf Building: Pasture", 3 - world.options.starting_tier)), #has (x | y) & (a | b)
            "HighElf Tech: Awakening the Ancient Ones": (Has("HighElf Tech: Trade Advancements") | Has("Progressive tech_hef_trade", 2 - world.options.starting_tier)) & (HasAll("HighElf Building: Exotic Pet Store", "HighElf Building: Exotic Animal Bazaar") | Has("Progressive HighElf Building: Animals", 3 - world.options.starting_tier)),
            "HighElf Tech: Great Weapons": (Has("HighElf Tech: Trade Advancements") | Has("Progressive tech_hef_trade", 2 - world.options.starting_tier)) & (HasAll("HighElf Building: Iron Mine", "HighElf Building: Iron Smelter") | Has("Progressive HighElf Building: Iron", 3 - world.options.starting_tier)),
            "HighElf Tech: Gemsetting": (Has("HighElf Tech: Trade Advancements") | Has("Progressive tech_hef_trade", 2 - world.options.starting_tier)) & (HasAll("HighElf Building: Gem Mine", "HighElf Building: Gemcutter's Atelier") | Has("Progressive HighElf Building: Gems", 3 - world.options.starting_tier)),
            "HighElf Tech: Marble Stockpiles": (Has("HighElf Tech: Trade Advancements") | Has("Progressive tech_hef_trade", 2 - world.options.starting_tier)) & (HasAll("HighElf Building: Marble Quarry", "HighElf Building: Sculptor's Workshop") | Has("Progressive HighElf Building: Marble", 3 - world.options.starting_tier)),
            "HighElf Tech: Healing Salve": (Has("HighElf Tech: Trade Advancements") | Has("Progressive tech_hef_trade", 2 - world.options.starting_tier)) & (HasAll("HighElf Building: Exotic Hothouse", "HighElf Building: Alchemy Workshop") | Has("Progressive HighElf Building: Medicine", 3 - world.options.starting_tier)),
            "HighElf Tech: Hardwood Construction": (Has("HighElf Tech: Trade Advancements") | Has("Progressive tech_hef_trade", 2 - world.options.starting_tier)) & (HasAll("HighElf Building: Timber Mill", "HighElf Building: Lumberyard") | Has("Progressive HighElf Building: Wood", 3 - world.options.starting_tier)),
            "HighElf Tech: Eastern Trade Contracts": (Has("HighElf Tech: Trade Advancements") | Has("Progressive tech_hef_trade", 2 - world.options.starting_tier)) & (HasAll("HighElf Building: Spice Trading Post", "HighElf Building: Eastern Bazaar") | Has("Progressive HighElf Building: Spices", 3 - world.options.starting_tier)),
            "HighElf Tech: Preserved Seafood": (Has("HighElf Tech: Trade Advancements") | Has("Progressive tech_hef_trade", 2 - world.options.starting_tier)) & (HasAll("HighElf Building: Salt Pans", "HighElf Building: Salt Distillery") | Has("Progressive HighElf Building: Salt", 3 - world.options.starting_tier)),
            "HighElf Tech: Monthly Festivals": (Has("HighElf Tech: Trade Advancements") | Has("Progressive tech_hef_trade", 2 - world.options.starting_tier)) & (HasAll("HighElf Building: Vineyard", "HighElf Building: Vintner") | Has("Progressive HighElf Building: Wine", 3 - world.options.starting_tier)),
            "HighElf Tech: Extravagant Murals": (Has("HighElf Tech: Trade Advancements") | Has("Progressive tech_hef_trade", 2 - world.options.starting_tier)) & (HasAll("HighElf Building: Cinnabar Mine", "HighElf Building: Dyemaker") | Has("Progressive HighElf Building: Dyes", 3 - world.options.starting_tier)),
            "HighElf Tech: Porcelain Kilns": (Has("HighElf Tech: Trade Advancements") | Has("Progressive tech_hef_trade", 2 - world.options.starting_tier)) & (HasAll("HighElf Building: Pottery Maker", "HighElf Building: Kilns") | Has("Progressive HighElf Building: Pottery", 3 - world.options.starting_tier)),
        }"""
        self.rules = {
            "Gunnery Workshop Tier 1": CanReachLocation("Empire Building: Firearms Academy") & (Has("Empire Unit: Handgunners") | Has("Progressive Empire Unit: Ranged", 2 - world.options.starting_tier)),
        }
        
        self.techSanityRules = {
            "HighElf Tech: Appoint Sea Masters": CanReachLocation("HighElf Building: Harbour"),
            "HighElf Tech: Dragon's Bond": CanReachLocation("HighElf Building: Dragon's Lair"),
            "HighElf Tech: Studies of the Vortex": CanReachLocation("HighElf Building: Tower of Mages"),
            "HighElf Tech: Call the Great Herds": CanReachLocation("HighElf Tech: Trade Advancements") & CanReachLocation("HighElf Building: Cattle Ranch"),
            "HighElf Tech: Awakening the Ancient Ones": CanReachLocation("HighElf Tech: Trade Advancements") & CanReachLocation("HighElf Building: Exotic Animal Bazaar"),
            "HighElf Tech: Great Weapons": CanReachLocation("HighElf Tech: Trade Advancements") & CanReachLocation("HighElf Building: Iron Smelter"),
            "HighElf Tech: Gemsetting": CanReachLocation("HighElf Tech: Trade Advancements") & CanReachLocation("HighElf Building: Gemcutter's Atelier"),
            "HighElf Tech: Marble Stockpiles": CanReachLocation("HighElf Tech: Trade Advancements") & CanReachLocation("HighElf Building: Sculptor's Workshop"),
            "HighElf Tech: Healing Salve": CanReachLocation("HighElf Tech: Trade Advancements") & CanReachLocation("HighElf Building: Alchemy Workshop"),
            "HighElf Tech: Hardwood Construction": CanReachLocation("HighElf Tech: Trade Advancements") & CanReachLocation("HighElf Building: Lumberyard"),
            "HighElf Tech: Eastern Trade Contracts": CanReachLocation("HighElf Tech: Trade Advancements") & CanReachLocation("HighElf Building: Eastern Bazaar"),
            "HighElf Tech: Preserved Seafood": CanReachLocation("HighElf Tech: Trade Advancements") & CanReachLocation("HighElf Building: Salt Distillery"),
            "HighElf Tech: Monthly Festivals": CanReachLocation("HighElf Tech: Trade Advancements") & CanReachLocation("HighElf Building: Vintner"),
            "HighElf Tech: Extravagant Murals": CanReachLocation("HighElf Tech: Trade Advancements") & CanReachLocation("HighElf Building: Dyemaker"),
            "HighElf Tech: Porcelain Kilns": CanReachLocation("HighElf Tech: Trade Advancements") & CanReachLocation("HighElf Building: Kilns")
        }

        self.ritualSanityRules = {
            "Empire Gunnery School: Quick-Load Mechanisms": self.rules["Gunnery Workshop Tier 1"],
            "Empire Gunnery School: Saddle Sack Munitions": self.rules["Gunnery Workshop Tier 1"],
            "Empire Gunnery School: Camouflaged Netting": self.rules["Gunnery Workshop Tier 1"],
            "Empire Gunnery School: High-Pressure Barrels": self.rules["Gunnery Workshop Tier 1"],
            "Empire Gunnery School: Suppressive Fire": self.rules["Gunnery Workshop Tier 1"],
            "Empire Gunnery School: More Rockets!!": self.rules["Gunnery Workshop Tier 1"],
            "Empire Gunnery School: Exploding Cannon Balls": self.rules["Gunnery Workshop Tier 1"],
            "Empire Gunnery School: Reinforced Hulls": self.rules["Gunnery Workshop Tier 1"],
        }

    def getTechRules(self, location):
        return self.techSanityRules[location]

    def getRitualRules(self, location):
        return self.ritualSanityRules[location]