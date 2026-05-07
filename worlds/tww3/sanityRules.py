from rule_builder.rules import Has, HasAll, HasAny, HasFromList, CanReachLocation, True_, False_

# @formatter:off
class ruleManager:
    def __init__(self, world):
        self.groups = {
            "Empire Gunnery School Tier1": ["Empire Gunnery School: Artisan Firearm Shot", "Empire Gunnery School: Thoroughbred Steeds",
                                            "Empire Gunnery School: Extra Gunpowder", "Empire Gunnery School: Weighted Munitions",
                                            "Empire Gunnery School: Rapid Reposition Drills", "Empire Gunnery School: More Rockets",
                                            "Empire Gunnery School: Better Engines", "Empire Gunnery School: External Spearports"],
            "Empire Gunnery School Tier2": ["Empire Gunnery School: Quick-Load Mechanisms", "Empire Gunnery School: Saddle Sack Munitions",
                                            "Empire Gunnery School: Camouflaged Netting", "Empire Gunnery School: High-Pressure Barrels",
                                            "Empire Gunnery School: Suppressive Fire", "Empire Gunnery School: More Rockets!!",
                                            "Empire Gunnery School: Exploding Cannon Balls", "Empire Gunnery School: Reinforced Hulls"],
        }

        self.rules = {
            "Gunnery Workshop Tier 1": (gunneryT1 := HasFromList(*self.groups["Empire Gunnery School Tier1"], count=3) & CanReachLocation("Empire Building: Firearms Academy") &
                                         (Has("Empire Unit: Handgunners") | Has("Progressive Empire Unit: Ranged", 2 - world.options.starting_tier) | (True_() if world.options.starting_tier >= 2 else False_()))),
            #"Gunnery Workshop Tier 1": HasFromList(*self.groups["Empire Gunnery School Tier1"], count=3)
            #                            & CanReachLocation("Empire Building: Firearms Academy") & (Has("Empire Unit: Handgunners") | Has("Progressive Empire Unit: Ranged", 2 - world.options.starting_tier)),
            "Gunnery Workshop Tier 2": gunneryT1 & HasFromList(*self.groups["Empire Gunnery School Tier1"], count=5) #HasFromList(*(self.groups["Empire Gunnery School Tier1"] + self.groups["Empire Gunnery School Tier2"]), count=8)
                                        & CanReachLocation("Empire Building: Foundry"),
            #"Gunnery Workshop Tier 2": HasFromList(*(self.groups["Empire Gunnery School Tier1"] + self.groups["Empire Gunnery School Tier2"]), count=8) & HasFromList(*self.groups["Empire Gunnery School Tier1"], count=3)
            #                            & CanReachLocation("Empire Building: Foundry")
            #                            & CanReachLocation("Empire Building: Firearms Academy") & (Has("Empire Unit: Handgunners") | Has("Progressive Empire Unit: Ranged", 2 - world.options.starting_tier)),
            "Gunnery Workshop Tier 3": CanReachLocation("Empire Gunnery School: Bjuna Bombard")
                                        & CanReachLocation("Empire Gunnery School: Amethyst Ironsides Cap Increase"),# & ((Has("Empire Unit: Amethyst Ironsides") | Has("Progressive Empire Unit: Ranged", 3 - world.options.starting_tier))
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
            "HighElf Tech: Porcelain Kilns": CanReachLocation("HighElf Tech: Trade Advancements") & CanReachLocation("HighElf Building: Kilns"),

            "Skaven Tech: Volatile Plans": CanReachLocation("Skaven Building: Arsenal"),
            "Skaven Tech: Ingenious Plans": CanReachLocation("Skaven Building: Warpstone Reactor"),
            "Skaven Tech: Plans Within Plans": CanReachLocation("Skaven Building: Plague Abbey"),
            "Skaven Tech: Oppressive Plans": CanReachLocation("Skaven Building: Den of Secrets"),
            "Skaven Tech: Monstrous Plans": CanReachLocation("Skaven Building: Pits of the Packmasters"),
            "Skaven Tech: Virulent Plans": CanReachLocation("Skaven Building: Construction Cavern"),

            "Khorne Tech: Bitter Raiding": CanReachLocation("Won 5 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: Spoils of Battle": CanReachLocation("Won 10 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: War Tributes": CanReachLocation("Won 15 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: Defiant Muster": CanReachLocation("Won 20 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: Exist Always": CanReachLocation("Won 25 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: Harvester's Pride": CanReachLocation("Won 5 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: Skull Flensing": CanReachLocation("Won 10 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: Skull Harvesting": CanReachLocation("Won 15 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: Skulls to Bring": CanReachLocation("Won 20 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: Skull of the Enemy": CanReachLocation("Won 25 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: War Leaders": CanReachLocation("Won 5 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: Reaper of Ages": CanReachLocation("Won 10 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: Return for Honour": CanReachLocation("Won 15 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: Favoured One": CanReachLocation("Won 20 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: Denying the Warp": CanReachLocation("Won 25 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: Skulls for the Skull Throne": CanReachLocation("Won 5 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: Sow Death, Reap Blood": CanReachLocation("Won 10 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: Staunch Defender": CanReachLocation("Won 15 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: Abjuration-Reaper": CanReachLocation("Won 20 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: The Way of Wrath": CanReachLocation("Won 25 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: Hounds of War": CanReachLocation("Won 5 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: Admiring the Corrupt": CanReachLocation("Won 10 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: Raging Denial": CanReachLocation("Won 15 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: Renegotiate Bargains": CanReachLocation("Won 20 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: Gates of Wrath": CanReachLocation("Won 25 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: Skull-Reaper": CanReachLocation("Won 5 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: Pride to Continue": CanReachLocation("Won 10 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: The Living Fire": CanReachLocation("Won 15 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: Repel the Honourless": CanReachLocation("Won 20 Battles") if world.options.battle_sanity else True_(),
            "Khorne Tech: Glorious Deaths": CanReachLocation("Won 25 Battles") if world.options.battle_sanity else True_(),

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

            "Empire Gunnery School: Amethyst Ironsides Cap Increase": self.rules["Gunnery Workshop Tier 2"],
            "Empire Gunnery School: Amethyst Outriders Cap Increase": self.rules["Gunnery Workshop Tier 2"],
            "Empire Gunnery School: Frontline Training": self.rules["Gunnery Workshop Tier 2"],
            "Empire Gunnery School: Cycle Charge Drills": self.rules["Gunnery Workshop Tier 2"],
            "Empire Gunnery School: Bjuna Bombard": self.rules["Gunnery Workshop Tier 2"],
            "Empire Gunnery School: Ballistics Plating": self.rules["Gunnery Workshop Tier 2"],
            "Empire Gunnery School: Debilitating Shots": self.rules["Gunnery Workshop Tier 2"],
            "Empire Gunnery School: Iron Resolve": self.rules["Gunnery Workshop Tier 2"],
            "Empire Gunnery School: Guerrilla Warfare": self.rules["Gunnery Workshop Tier 2"],
            "Empire Gunnery School: Dreadknight": self.rules["Gunnery Workshop Tier 2"],
            "Empire Gunnery School: Flared Muzzles": self.rules["Gunnery Workshop Tier 2"],

            "Empire Gunnery School: Exploding Bullets": self.rules["Gunnery Workshop Tier 3"],
            "Empire Gunnery School: Interference Tactics": self.rules["Gunnery Workshop Tier 3"],
            "Empire Gunnery School: Concussive Blasts": self.rules["Gunnery Workshop Tier 3"],
            "Empire Gunnery School: Grapeshot": self.rules["Gunnery Workshop Tier 3"],
            "Empire Gunnery School: Penetrating Shots": self.rules["Gunnery Workshop Tier 3"],
            "Empire Gunnery School: MORE ROCKETS!!!": self.rules["Gunnery Workshop Tier 3"],
            "Empire Gunnery School: Field Engineers": self.rules["Gunnery Workshop Tier 3"],
            "Empire Gunnery School: Land Mines": self.rules["Gunnery Workshop Tier 3"],
            "Empire Gunnery School: Improved Trajectories": self.rules["Gunnery Workshop Tier 3"],
            "Empire Gunnery School: Amethyst Helstorm Rocket Battery Cap Increase": self.rules["Gunnery Workshop Tier 3"],
            "Empire Gunnery School: Spirit Barrage": self.rules["Gunnery Workshop Tier 3"],

            "Empire Gunnery School: Extended Training Drills": self.rules["Gunnery Workshop Tier 3"],
            "Empire Gunnery School: Greater Infusions": self.rules["Gunnery Workshop Tier 3"],
            "Empire Gunnery School: Last Rites": self.rules["Gunnery Workshop Tier 3"],

            "Empire Gunnery School: Sails of Shyish": self.rules["Gunnery Workshop Tier 3"],
            "Empire Gunnery School: Catacomb Cannon": self.rules["Gunnery Workshop Tier 3"],
            "Empire Gunnery School: Amethyst Admiral": self.rules["Gunnery Workshop Tier 3"],
            "Empire Gunnery School: Cremation Engines": self.rules["Gunnery Workshop Tier 3"],
            "Empire Gunnery School: Amethyst Land Ship Cap Increase": self.rules["Gunnery Workshop Tier 3"],
            "Empire Gunnery School: The Purple Eclipse": self.rules["Gunnery Workshop Tier 3"],

            "TombKing Mortuary Cult: Blade of Antarhak": CanReachLocation("TombKing Building: Marble Quarry") & CanReachLocation("TombKing Building: Salt Mine"),
            "TombKing Mortuary Cult: Blade of Mourning Fire": CanReachLocation("TombKing Building: Iron Mine") & CanReachLocation("TombKing Building: Caravan Master") & CanReachLocation("TombKing Building: Salt Mine"),
            "TombKing Mortuary Cult: Blade of Setep": CanReachLocation("TombKing Building: Iron Mine") & CanReachLocation("TombKing Building: Obsidian Quarry"),
            "TombKing Mortuary Cult: Crook & Flail of Radiance": CanReachLocation("TombKing Building: Obsidian Quarry") & CanReachLocation("TombKing Building: Gold Mine") & CanReachLocation("TombKing Building: Gemstone Mine") & CanReachLocation("TombKing Building: Iron Mine"),
            "TombKing Mortuary Cult: Destroyer of Eternities": CanReachLocation("TombKing Building: Obsidian Quarry") & CanReachLocation("TombKing Building: Iron Mine") & CanReachLocation("TombKing Building: Alchemy Workshop"),
            "TombKing Mortuary Cult: Double Crescent of Neru": CanReachLocation("TombKing Building: Marble Quarry") & CanReachLocation("TombKing Building: Iron Mine"),
            "TombKing Mortuary Cult: Enchanted Lapis Mace": CanReachLocation("TombKing Building: Gemstone Mine"),
            "TombKing Mortuary Cult: Fang of Qu'aph": CanReachLocation("TombKing Building: Alchemy Workshop"),
            "TombKing Mortuary Cult: Golden Dagger": CanReachLocation("TombKing Building: Gold Mine"),
            "TombKing Mortuary Cult: Inscribed Khopesh": CanReachLocation("TombKing Building: Iron Mine"),
            "TombKing Mortuary Cult: Spear of Pakth": CanReachLocation("TombKing Building: Iron Mine") & CanReachLocation("TombKing Building: Salt Mine"),

            "TombKing Mortuary Cult: Armour of Dawn": CanReachLocation("TombKing Building: Cinnabar Mining Pit") & CanReachLocation("TombKing Building: Tannery") & CanReachLocation("TombKing Building: Caravan Master"),
            "TombKing Mortuary Cult: Armour of Eternity": CanReachLocation("TombKing Building: Caravan Master") & CanReachLocation("TombKing Building: Iron Mine") & CanReachLocation("TombKing Building: Gold Mine"),
            "TombKing Mortuary Cult: Armour of the Ages": CanReachLocation("TombKing Building: Potter's Hut") & CanReachLocation("TombKing Building: Gold Mine"),
            "TombKing Mortuary Cult: Helmet of Khsar": CanReachLocation("TombKing Building: Vineyard") & CanReachLocation("TombKing Building: Salt Mine"),
            "TombKing Mortuary Cult: Mortuary Robes": CanReachLocation("TombKing Building: Potter's Hut") & CanReachLocation("TombKing Building: Cinnabar Mining Pit"),
            "TombKing Mortuary Cult: Scorpion Armour": CanReachLocation("TombKing Building: Caravan Master") & CanReachLocation("TombKing Building: Taxidermist Tomb") & CanReachLocation("TombKing Building: Gold Mine") & CanReachLocation("TombKing Building: Iron Mine"),
            "TombKing Mortuary Cult: Shield of Ptra": CanReachLocation("TombKing Building: Tannery") & CanReachLocation("TombKing Building: Lumber Camp"),
            "TombKing Mortuary Cult: Skull Cap of the Moon": CanReachLocation("TombKing Building: Tannery"),
            
            "TombKing Mortuary Cult: Brooch of the Great Desert": CanReachLocation("TombKing Building: Gemstone Mine") & CanReachLocation("TombKing Building: Cinnabar Mining Pit"),
            "TombKing Mortuary Cult: Death Mask of Kharnut": CanReachLocation("TombKing Building: Cinnabar Mining Pit") & CanReachLocation("TombKing Building: Gold Mine"),
            "TombKing Mortuary Cult: Elixir of Might": CanReachLocation("TombKing Building: Vineyard"),
            "TombKing Mortuary Cult: Hieratic Jar": CanReachLocation("TombKing Building: Potter's Hut") & CanReachLocation("TombKing Building: Vineyard"),
            "TombKing Mortuary Cult: Icon of Rulership": CanReachLocation("TombKing Building: Marble Quarry"),
            "TombKing Mortuary Cult: Ouroboros": CanReachLocation("TombKing Building: Obsidian Quarry") & CanReachLocation("TombKing Building: Marble Quarry") & CanReachLocation("TombKing Building: Taxidermist Tomb"),
            "TombKing Mortuary Cult: Potion of Foolhardiness": CanReachLocation("TombKing Building: Salt Mine"),
            "TombKing Mortuary Cult: Potion of Speed": CanReachLocation("TombKing Building: Taxidermist Tomb"),
            "TombKing Mortuary Cult: Potion of Strength": CanReachLocation("TombKing Building: Caravan Master"),
            "TombKing Mortuary Cult: Potion of Toughness": CanReachLocation("TombKing Building: Alchemy Workshop"),
            "TombKing Mortuary Cult: Shroud of Sokth": CanReachLocation("TombKing Building: Tannery") & CanReachLocation("TombKing Building: Obsidian Quarry"),
            "TombKing Mortuary Cult: Vambraces of the Sun": CanReachLocation("TombKing Building: Vineyard") & CanReachLocation("TombKing Building: Obsidian Quarry") & CanReachLocation("TombKing Building: Gemstone Mine") & CanReachLocation("TombKing Building: Gold Mine"),

            "TombKing Mortuary Cult: Amulet of Pha-Stah": CanReachLocation("TombKing Building: Cinnabar Mining Pit") & CanReachLocation("TombKing Building: Gemstone Mine") & CanReachLocation("TombKing Building: Marble Quarry") & CanReachLocation("TombKing Building: Gold Mine"),
            "TombKing Mortuary Cult: Collar of Shakkara": CanReachLocation("TombKing Building: Gemstone Mine") & CanReachLocation("TombKing Building: Gold Mine") & CanReachLocation("TombKing Building: Vineyard"),
            "TombKing Mortuary Cult: Sun Scarab": CanReachLocation("TombKing Building: Marble Quarry"),
            "TombKing Mortuary Cult: Golden Ankhra": CanReachLocation("TombKing Building: Tannery") & CanReachLocation("TombKing Building: Gold Mine"),
            "TombKing Mortuary Cult: Golden Eye of Rah-Nutt": CanReachLocation("TombKing Building: Gold Mine") & CanReachLocation("TombKing Building: Lumber Camp"),
            "TombKing Mortuary Cult: Obsidian Pendant": CanReachLocation("TombKing Building: Salt Mine") & CanReachLocation("TombKing Building: Obsidian Quarry"),

            "TombKing Mortuary Cult: Blue Khepra": CanReachLocation("TombKing Building: Marble Quarry") & CanReachLocation("TombKing Building: Gemstone Mine"),
            "TombKing Mortuary Cult: Enkhil's Kanopi": CanReachLocation("TombKing Building: Lumber Camp") & CanReachLocation("TombKing Building: Alchemy Workshop"),
            "TombKing Mortuary Cult: Neferra's Scrolls of Mighty Incantations": CanReachLocation("TombKing Building: Lumber Camp") & CanReachLocation("TombKing Building: Obsidian Quarry"),
            "TombKing Mortuary Cult: Scroll of Power": CanReachLocation("TombKing Building: Obsidian Quarry"),
            "TombKing Mortuary Cult: Scroll of Leeching": CanReachLocation("TombKing Building: Lumber Camp"),
            "TombKing Mortuary Cult: Scroll of Shielding": CanReachLocation("TombKing Building: Iron Mine"),
            "TombKing Mortuary Cult: Vizier's Kanopi": CanReachLocation("TombKing Building: Salt Mine") & CanReachLocation("TombKing Building: Gold Mine"),

            "TombKing Mortuary Cult: Indefatigable Pennant": CanReachLocation("TombKing Building: Caravan Master"),
            "TombKing Mortuary Cult: Emblem of Withering": CanReachLocation("TombKing Building: Salt Mine") & CanReachLocation("TombKing Building: Iron Mine"),
            "TombKing Mortuary Cult: Standard to Khsar's Fury": CanReachLocation("TombKing Building: Iron Mine") & CanReachLocation("TombKing Building: Obsidian Quarry"),
            "TombKing Mortuary Cult: Icon of the Sacred Eye": CanReachLocation("TombKing Building: Obsidian Quarry") & CanReachLocation("TombKing Building: Gemstone Mine"),
            "TombKing Mortuary Cult: Royal Standard of Settra": CanReachLocation("TombKing Building: Gold Mine") & CanReachLocation("TombKing Building: Gemstone Mine") & CanReachLocation("TombKing Building: Obsidian Quarry"),
            "TombKing Mortuary Cult: Ualatp's Order": CanReachLocation("TombKing Building: Gold Mine"),

            "TombKing Mortuary Cult: Venom Knights of Asaph (Necropolis Knights)": CanReachLocation("TombKing Building: Taxidermist Tomb") & CanReachLocation("TombKing Building: Iron Mine") & CanReachLocation("TombKing Building: Gold Mine"),
            "TombKing Mortuary Cult: Storm Riders of Khsar (Nehekhara Horsemen)": CanReachLocation("TombKing Building: Gold Mine") & CanReachLocation("TombKing Building: Iron Mine"),
            "TombKing Mortuary Cult: Usirian's Legion of the Netherworld (Nehekhara Warriors)": CanReachLocation("TombKing Building: Gold Mine"),
            "TombKing Mortuary Cult: A New Servant (Liche Priest)": CanReachLocation("TombKing Building: Caravan Master") & CanReachLocation("TombKing Building: Salt Mine"),
            "TombKing Mortuary Cult: A New Servant (Necrotect)": CanReachLocation("TombKing Building: Gold Mine") & CanReachLocation("TombKing Building: Marble Quarry"),
            "TombKing Mortuary Cult: A New Servant (Tomb Prince)": CanReachLocation("TombKing Building: Obsidian Quarry") & CanReachLocation("TombKing Building: Iron Mine"),

            "wh2_dlc11_vmp_ritual_bloodline_awaken_blood_dragon_01": (Has("Administrative Capacity") | Has("Diplomatic Range")) if not world.options.hard_logic else True_(),
            "wh2_dlc11_vmp_ritual_bloodline_awaken_blood_dragon_02": (Has("Administrative Capacity", 3) | Has("Diplomatic Range", 2)) if not world.options.hard_logic else True_(),
            "wh2_dlc11_vmp_ritual_bloodline_awaken_blood_dragon_03": (Has("Administrative Capacity", 5) | Has("Diplomatic Range", 3)) if not world.options.hard_logic else True_(),
            "wh2_dlc11_vmp_ritual_bloodline_awaken_lahmian_01": (Has("Administrative Capacity") | Has("Diplomatic Range")) if not world.options.hard_logic else True_(),
            "wh2_dlc11_vmp_ritual_bloodline_awaken_lahmian_02": (Has("Administrative Capacity", 3) | Has("Diplomatic Range", 2)) if not world.options.hard_logic else True_(),
            "wh2_dlc11_vmp_ritual_bloodline_awaken_lahmian_03": (Has("Administrative Capacity", 5) | Has("Diplomatic Range", 3)) if not world.options.hard_logic else True_(),
            "wh2_dlc11_vmp_ritual_bloodline_awaken_necrarch_01": (Has("Administrative Capacity") | Has("Diplomatic Range")) if not world.options.hard_logic else True_(),
            "wh2_dlc11_vmp_ritual_bloodline_awaken_necrarch_02": (Has("Administrative Capacity", 3) | Has("Diplomatic Range", 2)) if not world.options.hard_logic else True_(),
            "wh2_dlc11_vmp_ritual_bloodline_awaken_necrarch_03": (Has("Administrative Capacity", 5) | Has("Diplomatic Range", 3)) if not world.options.hard_logic else True_(),
            "wh2_dlc11_vmp_ritual_bloodline_awaken_strigoi_01": (Has("Administrative Capacity") | Has("Diplomatic Range")) if not world.options.hard_logic else True_(),
            "wh2_dlc11_vmp_ritual_bloodline_awaken_strigoi_02": (Has("Administrative Capacity", 3) | Has("Diplomatic Range", 2)) if not world.options.hard_logic else True_(),
            "wh2_dlc11_vmp_ritual_bloodline_awaken_strigoi_03": (Has("Administrative Capacity", 5) | Has("Diplomatic Range", 3)) if not world.options.hard_logic else True_(),
            "wh2_dlc11_vmp_ritual_bloodline_awaken_von_carstein_01": (Has("Administrative Capacity") | Has("Diplomatic Range")) if not world.options.hard_logic else True_(),
            "wh2_dlc11_vmp_ritual_bloodline_awaken_von_carstein_02": (Has("Administrative Capacity", 3) | Has("Diplomatic Range", 2)) if not world.options.hard_logic else True_(),
            "wh2_dlc11_vmp_ritual_bloodline_awaken_von_carstein_03": (Has("Administrative Capacity", 5) | Has("Diplomatic Range", 3)) if not world.options.hard_logic else True_(),

            #"Khorne Throne of Skulls: The Endless Fuel": (Has("Administrative Capacity") | Has("Diplomatic Range")) if not world.options.hard_logic else True_(),
            #"Khorne Throne of Skulls: The Gift of Glory": (Has("Administrative Capacity") | Has("Diplomatic Range")) if not world.options.hard_logic else True_(),
            #"Khorne Throne of Skulls: Bred in Bloodshed": (Has("Administrative Capacity") | Has("Diplomatic Range")) if not world.options.hard_logic else True_(),
            #"Khorne Throne of Skulls: Fury's Flight": (Has("Administrative Capacity", 3) | Has("Diplomatic Range", 3)) if not world.options.hard_logic else True_(),
            #"Khorne Throne of Skulls: The Wordless Edict": (Has("Administrative Capacity", 3) | Has("Diplomatic Range", 3)) if not world.options.hard_logic else True_(),
            #"Khorne Throne of Skulls: Destruction’s Diktat": (Has("Administrative Capacity", 5) | Has("Diplomatic Range", 5)) if not world.options.hard_logic else True_(),

            "Khorne Unholy Manifestation: Khorne's Glare": (Has("Administrative Capacity") | Has("Diplomatic Range")) if not world.options.hard_logic else True_(),
            "Khorne Unholy Manifestation: Slaughter Incarnate": (Has("Administrative Capacity", 2) | Has("Diplomatic Range", 2)) if not world.options.hard_logic else True_(),
            "Khorne Unholy Manifestation: Call of Battle": (Has("Administrative Capacity", 3) | Has("Diplomatic Range", 3)) if not world.options.hard_logic else True_(),

            "Tzeentch Unholy Manifestation: ": (Has("Administrative Capacity") | Has("Diplomatic Range")) if not world.options.hard_logic else True_(),
            "Tzeentch Unholy Manifestation: ": (Has("Administrative Capacity", 2) | Has("Diplomatic Range", 2)) if not world.options.hard_logic else True_(),
            "Tzeentch Unholy Manifestation: ": (Has("Administrative Capacity", 3) | Has("Diplomatic Range", 3)) if not world.options.hard_logic else True_(),

            "Nurgle Unholy Manifestation: ": (Has("Administrative Capacity") | Has("Diplomatic Range")) if not world.options.hard_logic else True_(),
            "Nurgle Unholy Manifestation: ": (Has("Administrative Capacity", 2) | Has("Diplomatic Range", 2)) if not world.options.hard_logic else True_(),
            "Nurgle Unholy Manifestation: ": (Has("Administrative Capacity", 3) | Has("Diplomatic Range", 3)) if not world.options.hard_logic else True_(),

            "Slaanesh Unholy Manifestation: ": (Has("Administrative Capacity") | Has("Diplomatic Range")) if not world.options.hard_logic else True_(),
            "Slaanesh Unholy Manifestation: ": (Has("Administrative Capacity", 2) | Has("Diplomatic Range", 2)) if not world.options.hard_logic else True_(),
            "Slaanesh Unholy Manifestation: ": (Has("Administrative Capacity", 3) | Has("Diplomatic Range", 3)) if not world.options.hard_logic else True_(),
        }

    def getTechRules(self, location):
        return self.techSanityRules[location]

    def getRitualRules(self, location):
        return self.ritualSanityRules[location]