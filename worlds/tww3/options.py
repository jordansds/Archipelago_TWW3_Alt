from Options import Choice, DeathLink, DefaultOnToggle, Range, StartInventoryPool, PerGameCommonOptions, Toggle, \
    OptionSet
from dataclasses import dataclass
from worlds.tww3 import settlementManager as sm

class faction(Choice):
    """Choose your faction. If you pick multiple the client will tell you which one you need to play.
    All options after "Throgg" require you to have the enabled mod installed and enabled at the bottom of this yaml"""
    display_name = "Player Faction"
    option_The_Daemon_Prince = 0
    option_Skarbrand = 1
    option_Skulltaker = 2
    option_Arbaal_the_Undefeated = 3
    option_Kugath_Plaguefather = 4
    option_Tamurkhan_the_Maggot_Lord = 5
    option_Epidemius = 6
    option_NKari = 7
    option_Dechala_the_Denied_One = 8
    option_The_Masque_of_Slaanesh = 9
    option_Kairos_Fateweaver = 10
    option_The_Changeling = 11
    option_Tzarina_Katarin = 12
    option_Kostaltyn = 13
    option_Boris_Ursus = 14
    option_Mother_Ostankya = 15
    option_Greasus_Goldtooth = 16
    option_Skrag_the_Slaughterer = 17
    option_Golgfag_Maneater = 18
    option_Astragoth_Ironhand = 19
    option_Drazhoath_the_Ashen = 20
    option_Zhaten_the_Black = 21
    option_Miao_Ying_the_Storm_Dragon = 22
    option_Zhau_Ming_the_Iron_Dragon = 23
    option_Yuan_Bo_the_Jade_Dragon = 24
    option_Bhashiva = 103
    option_Tyrion = 25
    option_Teclis = 26
    option_Alarielle_the_Radiant = 27
    option_Alith_Anar = 28
    option_Eltharion_the_Grim = 29
    option_Imrik = 30
    option_Sea_Lord_Aislinn = 31
    option_Oxyotl = 32
    option_Lord_Mazdamundi = 33
    option_Kroq_Gar = 34
    option_Tehenhauin = 35
    option_Tiktaqto = 36
    option_Nakai_the_Wanderer = 37
    option_Gor_Rok = 38
    option_Malekith = 39
    option_Morathi = 40
    option_Crone_Helebron = 41
    option_Lokhir_Fellheart = 42
    option_Malus_Darkblade = 43
    option_Rakarth_the_Beastmaster = 44
    option_Queek_Headtaker = 45
    option_Lord_Skrolk = 46
    option_Tretch_Craventail = 47
    option_Ikit_Claw = 48
    option_Throt_the_Unclean = 49
    option_Deathmaster_Snikch = 50
    option_Settra_the_Imperishable = 51
    option_High_Queen_Khalida = 52
    option_Grand_Hierophant_Khatep = 53
    option_Arkhan_the_Black = 54
    option_Luthor_Harkon = 55
    option_Count_Noctilus = 56
    option_Cylostra_Direfin = 57
    option_Aranessa_Saltspite = 58
    option_Karl_Franz = 59
    option_Balthasar_Gelt = 60
    option_Volkmar_the_Grim = 61
    option_Markus_Wulfhart = 62
    option_Elspeth_Von_Draken = 63
    option_Thorgrim_Grudgebearer = 64
    option_Ungrim_Ironfist = 65
    option_Belegar_Ironhammer = 66
    option_Grombrindal_The_White_Dwarf = 67
    option_Thorek_Ironbrow = 68
    option_Malakai_Makaisson = 69
    option_Grimgor_Ironhide = 70
    option_Skarsnik = 71
    option_Azhag_the_Slaughterer = 72
    option_Wurrzag_da_Great_Green_Prophet = 73
    option_Grom_the_Paunch = 74
    option_Gorbad_Ironclaw = 75
    option_Mannfred_von_Carstein = 76
    option_Heinrich_Kemmler = 77
    option_Helman_Ghorst = 78
    option_Vlad_von_Carstein = 79
    option_Archaon_the_Everchosen = 80
    option_Kholek_Suneater = 81
    option_Prince_Sigvald_the_Magnificent = 82
    option_Azazel = 83
    option_Festus_the_Leechlord = 84
    option_Valkia_the_Bloody = 85
    option_Vilitch_the_Cursling = 86
    option_Belakor = 87
    option_Khazrak_the_One_Eye = 88
    option_Malagor_the_Dark_Omen = 89
    option_Morghur_the_Shadowgave = 90
    option_Taurox_the_Brass_Bull = 91
    option_Orion = 92
    option_Durthu = 93
    option_Sisters_of_Twilight = 94
    option_Drycha = 95
    option_King_Louen_Leoncoeur = 96
    option_Fay_Enchantress = 97
    option_Alberic_de_Bordeleaux = 98
    option_Repanse_de_Lyonesse = 99
    option_Wulfrik_the_Wanderer = 100
    option_Sayl_the_Faithless = 101
    option_Throgg = 102
    option_Mixu_Mousillon_Mallobaude = 2000
    option_Mixu_Mousillon_Lady_of_the_Black_Grail = 2001
    option_Mixu_Legendary_Lords_Molokh_Slugtongue = 1255
    option_Mixu_Legendary_Lords_Ghorros_Warhoof = 1257
    option_Mixu_Legendary_Lords_Chilfroy_d_Artois = 1264
    option_Mixu_Legendary_Lords_Bohemond_Beastslayer = 1265
    option_Mixu_Legendary_Lords_Sir_John_Tyreweld = 1267
    option_Mixu_Legendary_Lords_Adalhard_de_Lyonesse = 1269
    option_Mixu_Legendary_Lords_Cassyon_de_Parravon = 1270
    option_Mixu_Legendary_Lords_Tullaris_Dreadbringer = 1169
    option_Mixu_Legendary_Lords_Kazador_Dragonslayer = 1208
    option_Mixu_Legendary_Lords_Grimm_Burloksson = 1213
    option_Mixu_Legendary_Lords_Marius_Leitdorf = 1193
    option_Mixu_Legendary_Lords_Aldebrand_Ludenhof = 1195
    option_Mixu_Legendary_Lords_Theoderic_Gausser = 1199
    option_Mixu_Legendary_Lords_Wolfram_Hertwig = 1200
    option_Mixu_Legendary_Lords_Valmir_von_Raukov = 1201
    option_Mixu_Legendary_Lords_Alberich_Haupt_Anderssen = 1202
    option_Mixu_Legendary_Lords_Helmut_Feuerbach = 1203
    option_Mixu_Legendary_Lords_Edvard_van_der_Kraal = 2003
    option_Mixu_Legendary_Lords_Gorfang_Rotgut = 1231
    option_Mixu_Legendary_Lords_Korhil = 1147
    option_Mixu_Legendary_Lords_Belannaer_the_Wise = 1151
    option_Mixu_Legendary_Lords_Rastiltin_Bebchuk = 1120
    option_Mixu_Legendary_Lords_Lord_Huinitenuchli = 1158
    option_Mixu_Legendary_Lords_Tetto_eko = 1160
    option_Mixu_Legendary_Lords_Warlord_Feskit = 1179
    option_Mixu_Legendary_Lords_King_Tutankhanut = 1187
    option_Mixu_Legendary_Lords_Dieter_Helsnicht = 2004
    option_Mixu_Legendary_Lords_Egrimm_van_Horstmann = 2005
    option_Mixu_Legendary_Lords_Slaa_Ulaan = 2006
    option_Mixu_Legendary_Lords_Egil_Styrbjorn = 1284
    option_Mixu_Legendary_Lords_Daith = 1262
    option_Mixu_Legendary_Lords_Naieth = 1263
    option_Mixu_Legendary_Lords_Wychwethyl_the_Wild = 2007
    option_Ovn_Althran_Stormrider = 1148
    option_Medusa0_Surtha_Ek = 1287
    option_Cataph_Southern_Realms_Valmir_Gausser = 1251
    option_Cataph_Southern_Realms_Lupio_Sunscryer = 1252
    option_Cataph_Southern_Realms_Borgio_the_Besieger = 1253
    option_Cataph_Southern_Realms_Lucrezzia_Belladonna = 2019
    option_Cataph_Southern_Realms_Leonardo_Catrazza = 2020
    option_Cataph_Southern_Realms_Marco_Colombo = 2021
    option_Cataph_Southern_Realms_Gnashag_the_Black_Prince = 2022
    option_Cataph_Southern_Realms_El_Cadavo = 2023
    option_Pegaz_Crustacean_Nation_King_Crab = 2008
    option_Pegaz_Crustacean_Nation_Reefspeaker = 2009
    option_Pegaz_Crustacean_Nation_Old_Kelpbeard = 2010
    option_Pegaz_Crustacean_Nation_Tidelord_Anthron = 2011
    option_Pegaz_Crustacean_Nation_Clawdius_Beastslayer = 1012
    option_Pegaz_Crustacean_Nation_Lobstrogh_the_Betrayer = 2013
    option_Pegaz_Crustacean_Nation_Grand_Master_Corallion = 2014
    default = 0

class gameMode(Choice):
    """Select which game mode you want to use.
    Conquest: No restrictions, checks are based on total settlements conquered.
    Spheres:  You can only interact with factions near your start position,
             all unique settlements are checks.
             [MAKE SURE YOU HAVE READ THE README TO PREVENT SOFTLOCKING]"""
    display_name = "Game Mode"

    option_conquest = "conquest"
    option_spheres = "spheres"

    default = option_conquest

class factionShuffle(DefaultOnToggle):
    """If you want to shuffle the settlements for each faction"""
    display_name = "Faction Shuffle"

class checksPerSettlement(Range):
    """Set how many checks are triggered per settlement captured.
    Depending on YAML settings and the chosen faction, you will likely have around 150-250 non-filler items.
    Make sure to change this value based on how many locations you want your game to have.
    If world generation fails, then try increasing this option."""
    display_name = "Checks Per Settlement"
    range_start = 1
    range_end = 5
    default = 3

class startingSettlements(Range):
    """REQUIRES FACTION SHUFFLE TO BE ENABLED
    Set how many settlements the player will start with."""
    display_name = "Starting Settlements"
    range_start = 1
    range_end = 5
    default = 2

#class buildingSanity(Toggle):
#    """If you want every building to be a location. [EXPERIMENTAL, REQUIRES BUILDING SHUFFLE TO BE ENABLED]
#    RECCOMENDED TO USE BUILDING/TECH/RITUALSANITY TOGETHER, GENERATION LOGIC MAY BE FLAWED IF USED ALONE"""
#    display_name = "BuildingSanity"

#class techSanity(Toggle):
#    """If you want every tech to be a location. [EXPERIMENTAL, REQUIRES TECH SHUFFLE TO BE ENABLED]
#    RECCOMENDED TO USE BUILDING/TECH/RITUALSANITY TOGETHER, GENERATION LOGIC MAY BE FLAWED IF USED ALONE"""
#    display_name = "TechSanity"

#class ritualSanity(Toggle):
#    """If you want unique faction mechanics to be locations. [EXPERIMENTAL, REQUIRES RITUAL SHUFFLE TO BE ENABLED, NOT ALL FACTIONS IMPLEMENTED]
#    RECCOMENDED TO USE BUILDING/TECH/RITUALSANITY TOGETHER, GENERATION LOGIC MAY BE FLAWED IF USED ALONE"""
#    display_name = "RitualSanity"

class sanity(DefaultOnToggle):
    """If you want every building and tech to be a location.
    [EXPERIMENTAL, WILL ENABLE BUILDING AND TECH SHUFFLE]"""
    display_name = "BuildingTechSanity"

class ritualSanity(Toggle):
    """If you want every faction mechanic to be a location.
    [EXPERIMENTAL, WILL ENABLE RITUAL SHUFFLE AND SANITY, Will force settlements to a minimum of 30]"""
    display_name = "RitualSanity"

class battleSanity(Toggle):
    """If you want every 5 battles won up to be locations up to 100 battles
        [EXPERIMENTAL]"""
    display_name = "BattleSanity"

class despoilerSanity(Toggle):
    """If you want every 2 settlements sacked and razed to be locations up to 20 settlements
        [EXPERIMENTAL]"""
    display_name = "DespoilerSanity"
    
class numberOfSettlements(Range):
    """CONQUEST MODE ONLY
    Set how large your empire needs to be for victory. The maximum value is the entire map.
    Make sure to change this based on how fast you want your game to be.
    If world generation fails, then you will need to increase this option or checks_per_settlement.
    Items will not be found in any of your starting settlements."""
    display_name = "Number Of Settlements (CONQUEST)"
    range_start = 5
    range_end = len(sm.settlementDict)
    default = 50

#class adminCapacity(Range):
#    """CONQUEST MODE ONLY
#    How many settlements each Administration Capacity item allows you to own.
#    Going over the empire size limit will incur heavy penalties.
#    You start with 1 admin capacity item so make sure that you set it higher than STARTING SETTLEMENTS.
#    If you are playing solo, set this to the maximum value as the items won't do anything anyway."""
#    display_name = "Settlements Per Admin Capacity (CONQUEST)"
#    range_start = 2
#    range_end = len(sm.settlementDict)
#    default = 10

class sphereCount(Range):
    """SPHERE MODE ONLY
    How many diplomatic radius upgrades are required to access all checks.
    You can only interact with factions that are within this radius of your starting capital."""
    display_name = "Radius Upgrades (SPHERES)"
    range_start = 3
    range_end = 10
    default = 5

#class extraSphereCount(Range):
#    """SPHERE MODE ONLY
#    How many extra diplomatic radius upgrades are generated"""
#    display_name = "Extra Spheres (SPHERES)"
#    range_start = 0
#    range_end = 50
#    default = 0

#class sphereRadius(Range):
#    """SPHERE MODE ONLY
#    Determines your starting radius and radius added with each upgrade.
#    The smallest distance between settlements is 25. The largest is 1400.
#    If you spawn in the middle of the map it only takes a radius of 700
#    for the entire world to be in logic."""
#    display_name = "Diplomatic Radius Size (SPHERES)"
#    range_start = 50
#    range_end = 500
#    default = 150

class orbCount(Range):
    """SPHERE MODE ONLY
    How many orbs of domination are generated.
    Once you have this many orbs, you win."""
    display_name = "Max Orbs (SPHERES)"
    range_start = 1
    range_end = 100
    default = 20

class extraOrbCount(Range):
    """SPHERE MODE ONLY
    How many extra orbs should be generated."""
    display_name = "Extra Orbs (SPHERES)"
    range_start = 0
    range_end = 50
    default = 0

#class maxRange(Range):
#    """The furthest away two settlements can be during world generation.
#    The smallest distance between settlements is 25. The largest is 1400."""
#    display_name = "Max Settlement Distance"
#    range_start = 50
#    range_end = 1500
#    default = 200
class ritualShuffle(DefaultOnToggle):
    """Whether faction mechanics should be included in the item pool.
    Not all mechanics are shuffled as some cannot be locked."""
    display_name = "Ritual Shuffle"

class techShuffle(DefaultOnToggle):
    """Whether technologies should be included in the item pool."""
    display_name = "Tech Shuffle"

class progressiveTechnologies(Toggle):
    """If technologies should be progressive. Requires Tech Shuffle to be on."""
    display_name = "Progressive Technologies"

class buildingShuffle(DefaultOnToggle):
    """Whether buildings should be included in the item pool."""
    display_name = "Building Shuffle"

class progressiveBuildings(DefaultOnToggle):
    """If buildings should be progressive. Requires Building Shuffle to be on."""
    display_name = "Progressive Buildings"

class unitShuffle(DefaultOnToggle):
    """Whether units should be included in the item pool."""
    display_name = "Unit Shuffle"

class progressiveUnits(Toggle):
    """If units should be progressive. Requires Unit Shuffle to be on."""
    display_name = "Progressive Units"

class startingTier(Range):
    """Start with buildings and units of this tier already unlocked.
    Warning: Setting this to 0 will result in you having no buildings or units unlocked at the start.
    DO NOT SET THIS TO RANDOM, IT'S PURPOSE IS FOR MAKING THE GAME EASIER BY GIVING YOU ITEMS AT THE START"""
    display_name = "Starting Tier"
    range_start = 0
    range_end = 4
    default = 1

class balance(Range):
    """Percentage of your early items that are forced to be useful/progression.
    0 doesn't force unlocks at all. 100 means that all of your early items will be unlocks.
    High values are not recommended. SOFT LOGIC, Not recommended for large syncs/asyncs."""
    display_name = "Force Early Upgrades"
    range_start = 0
    range_end = 100
    default = 0

class forceEarlyBuildings(Range):
    """SET TO 0 TO DISABLE
    Whether buildings should be a forced unlock and determines the tier.
    Building shuffle must be on and balance must be greater than 0.
    The value sets the highest tier of buildings that will be forced.
    E.g. 2 means that only tier 1 and 2 buildings will be forced.
    SOFT LOGIC, Not recommended for large syncs/asyncs."""
    display_name = "Early Building Tiers"
    range_start = 0
    range_end = 5
    default = 0

class forceEarlyUnits(Range):
    """SET TO 0 TO DISABLE
    Whether units should be a forced unlock and determines the tier.
    Unit shuffle must be on and balance must be greater than 0.
    The value sets the highest tier of units that will be forced.
    E.g. 2 means that only tier 1 and 2 units will be forced.
    SOFT LOGIC, Not recommended for large syncs/asyncs."""
    display_name = "Early Unit Tiers"
    range_start = 0
    range_end = 5
    default = 0

class forceEarlyTechs(Toggle):
    """Whether tech should be a forced unlock.
    Tech shuffle must be on and balance must be greater than 0.
    SOFT LOGIC, Not recommended for large syncs/asyncs."""
    display_name = "Early Tech"

class filler(Range):
    """Weight of filler items to trap items.
    For example: filler: 70
    Would mean: 70% filler, 30% traps"""
    display_name = "Filler Weight"
    range_start = 0
    range_end = 100
    default = 70

class trap(Range):
    """Weight of trap items"""
    display_name = "Trap Weight"
    range_start = 0
    range_end = 100
    default = 30

class deathLink(Toggle):
    """Enable or Disable death linking."""
    display_name = "Death Link"

class deathLinkEffect(OptionSet):
    """Valid options for death link effect. Include as many or as few as you like in the list. Valid Options:
    "10% Treasury", "25% Treasury", "50% Treasury", "Wound Hero", "Wound Lord", "Rebellion", "Raze Random Settlement", "Disable Replenishment (2 turns)"
    E.g. ["10% Treasury", "Wound Lord"]"""
    display_name = "Death Link Effect"
    valid_keys = ["10% Treasury", "25% Treasury", "50% Treasury", "Wound Hero", "Wound Lord", "Rebellion", "Raze Random Settlement", "Disable Replenishment (2 turns)"]
    default = frozenset({"10% Treasury"})

class modList(OptionSet):
    """List of mods with built-in support. Please add them to this list if you have them installed and enabled. Valid Options:
    "decomposed expanded roster", "mixu mousillon", "mixu legendary lords", "ovn citadel of dusk", "medusa0 surtha ek", "cataph southern realms", "pegaz the crustacean nation"
    E.g. ["decomposed expanded roster", "mixu legendary lords"]"""
    display_name = "Supported Mods"
    valid_keys = ["decomposed expanded roster", "mixu mousillon", "mixu legendary lords", "ovn citadel of dusk", "medusa0 surtha ek", "cataph southern realms", "pegaz the crustacean nation"]

class trapBlacklist(OptionSet):
    """Trap Blacklist (if you blacklist them all, then nothing will happen). Valid Options:
    "Handful of Unrest", "Unionize This", "Where is our Map?", "Schizophrenia", "Make Love, Not War", "Torches and Pitchforks", "Let's trade", "You too, Brutus?", "We're Going on a Trip", "En Garde!"
    """
    display_name = "Trap Blacklist"
    valid_keys = ["Handful of Unrest", "Unionize This", "Where is our Map?", "Schizophrenia", "Make Love, Not War", "Torches and Pitchforks", "Let's trade", "You too, Brutus?", "We're Going on a Trip", "En Garde!"]

class randomizePersonalities(DefaultOnToggle):
    """Randomize AI Personalities."""
    display_name = "Randomize AI Personalities"

class hardLogic(DefaultOnToggle):
    """Enforce hard logic so checks cannot be sent without the required logic items even if the player hits the in-game location.
    Recommended for large syncs/asyncs to prevent soft logic issues."""
    display_name = "Hard Logic"

class locationBalancing(DefaultOnToggle):
    """Experimental option that tries to balance building/tech locations based on how much admin capacity the player has received.
    This should help balance the building/tech locations a bit better.
    Warning: Soft Logic, may in rare circumstances result in out of logic locations.
    [EXPERIMENTAL]"""
    display_name = "Location Balancing"

@dataclass
class TWW3Options(PerGameCommonOptions):
    starting_faction: faction
    game_mode: gameMode

    faction_shuffle: factionShuffle
    randomize_personalities: randomizePersonalities
    starting_settlements: startingSettlements
    checks_per_settlement: checksPerSettlement

    sanity: sanity
    ritual_sanity: ritualSanity
    battle_sanity: battleSanity
    despoiler_sanity: despoilerSanity

    number_of_settlements: numberOfSettlements
    #admin_capacity: adminCapacity

    sphere_count: sphereCount
    #extra_sphere_count: extraSphereCount
    #sphere_radius: sphereRadius
    #orb_count: orbCount
    #extra_orb_count: extraOrbCount

    tech_shuffle: techShuffle
    progressive_technologies: progressiveTechnologies
    building_shuffle: buildingShuffle
    progressive_buildings: progressiveBuildings
    unit_shuffle: unitShuffle
    progressive_units: progressiveUnits
    ritual_shuffle: ritualShuffle

    filler: filler
    #trap: trap

    death_link: deathLink
    death_link_effects: deathLinkEffect

    starting_tier: startingTier
    balance: balance
    #force_early_buildings: forceEarlyBuildings
    #force_early_units: forceEarlyUnits
    #force_early_techs: forceEarlyTechs

    #location_balancing: locationBalancing
    hard_logic: hardLogic

    mod_list: modList
    trap_blacklist: trapBlacklist