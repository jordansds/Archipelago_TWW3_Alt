from pygments.lexer import default

from Options import Choice, DeathLink, DefaultOnToggle, Range, StartInventoryPool, PerGameCommonOptions, Toggle, \
    OptionSet
from dataclasses import dataclass
from worlds.tww3 import settlementRandomiser as sm

class faction(Choice):
    """Choose your faction. If you pick multiple the client will tell you which one you need to play.
    All options after "Throgg" require you to have the enabled mod installed and enabled at the bottom of this yaml"""
    display_name = "Player Faction"
    option_Random_Beastmen = 10
    option_Khazrak_the_One_Eye = 11
    option_Malagor_the_Dark_Omen = 12
    option_Morghur_the_Shadowgave = 13
    option_Taurox_the_Brass_Bull = 14

    option_Random_Bretonnia = 20
    option_King_Louen_Leoncoeur = 21
    option_Fay_Enchantress = 22
    option_Alberic_de_Bordeleaux = 23
    option_Repanse_de_Lyonesse = 24

    option_Random_Cathay = 30
    option_Miao_Ying_the_Storm_Dragon = 31
    option_Zhau_Ming_the_Iron_Dragon = 32
    option_Yuan_Bo_the_Jade_Dragon = 33
    option_Bhashiva = 34

    option_Random_Chaos_Dwarfs = 40
    option_Astragoth_Ironhand = 41
    option_Drazhoath_the_Ashen = 42
    option_Zhaten_the_Black = 43

    option_Random_Dark_Elves = 50
    option_Malekith = 51
    option_Morathi = 52
    option_Crone_Helebron = 53
    option_Lokhir_Fellheart = 54
    option_Malus_Darkblade = 55
    option_Rakarth_the_Beastmaster = 56

    option_The_Daemon_Prince = 61

    option_Random_Dwarfs = 70
    option_Thorgrim_Grudgebearer = 71
    option_Ungrim_Ironfist = 72
    option_Belegar_Ironhammer = 73
    option_Grombrindal_The_White_Dwarf = 74
    option_Thorek_Ironbrow = 75
    option_Malakai_Makaisson = 76

    option_Random_Empire = 80
    option_Karl_Franz = 81
    option_Balthasar_Gelt = 82
    option_Volkmar_the_Grim = 83
    option_Markus_Wulfhart = 84
    option_Elspeth_Von_Draken = 85

    option_Random_Greenskins = 90
    option_Grimgor_Ironhide = 91
    option_Skarsnik = 92
    option_Azhag_the_Slaughterer = 93
    option_Wurrzag_da_Great_Green_Prophet = 94
    option_Grom_the_Paunch = 95
    option_Gorbad_Ironclaw = 96

    option_Random_High_Elves = 100
    option_Tyrion = 101
    option_Teclis = 102
    option_Alarielle_the_Radiant = 103
    option_Alith_Anar = 104
    option_Eltharion_the_Grim = 105
    option_Imrik = 106
    option_Sea_Lord_Aislinn = 107

    option_Random_Khorne = 110
    option_Skarbrand = 111
    option_Skulltaker = 112
    option_Arbaal_the_Undefeated = 113

    option_Random_Kislev = 120
    option_Tzarina_Katarin = 121
    option_Kostaltyn = 122
    option_Boris_Ursus = 123
    option_Mother_Ostankya = 124

    option_Random_Lizardmen = 130
    option_Oxyotl = 131
    option_Lord_Mazdamundi = 132
    option_Kroq_Gar = 133
    option_Tehenhauin = 134
    option_Tiktaqto = 135
    option_Nakai_the_Wanderer = 136
    option_Gor_Rok = 137

    option_Random_Norsca = 140
    option_Wulfrik_the_Wanderer = 141
    option_Sayl_the_Faithless = 142
    option_Throgg = 143

    option_Random_Nurgle = 150
    option_Kugath_Plaguefather = 151
    option_Tamurkhan_the_Maggot_Lord = 152
    option_Epidemius = 153

    option_Random_Ogre_Kingdoms = 160
    option_Greasus_Goldtooth = 161
    option_Skrag_the_Slaughterer = 162
    option_Golgfag_Maneater = 163

    option_Random_Skaven = 170
    option_Queek_Headtaker = 171
    option_Lord_Skrolk = 172
    option_Tretch_Craventail = 173
    option_Ikit_Claw = 174
    option_Throt_the_Unclean = 175
    option_Deathmaster_Snikch = 176

    option_Random_Slaanesh = 180
    option_NKari = 181
    option_Dechala_the_Denied_One = 182
    option_The_Masque_of_Slaanesh = 183

    option_Random_Tomb_Kings = 190
    option_Settra_the_Imperishable = 191
    option_High_Queen_Khalida = 192
    option_Grand_Hierophant_Khatep = 193
    option_Arkhan_the_Black = 194

    option_Random_Tzeentch = 200
    option_Kairos_Fateweaver = 201
    option_The_Changeling = 202

    option_Random_Vampire_Coast = 210
    option_Luthor_Harkon = 211
    option_Count_Noctilus = 212
    option_Cylostra_Direfin = 213
    option_Aranessa_Saltspite = 214

    option_Random_Vampire_Counts = 220
    option_Mannfred_von_Carstein = 221
    option_Heinrich_Kemmler = 222
    option_Helman_Ghorst = 223
    option_Vlad_von_Carstein = 224

    option_Random_Chaos = 230
    option_Archaon_the_Everchosen = 231
    option_Kholek_Suneater = 232
    option_Prince_Sigvald_the_Magnificent = 233
    option_Azazel = 234
    option_Festus_the_Leechlord = 235
    option_Valkia_the_Bloody = 236
    option_Vilitch_the_Cursling = 237
    option_Belakor = 238

    option_Random_Wood_Elves = 240
    option_Orion = 241
    option_Durthu = 242
    option_Sisters_of_Twilight = 243
    option_Drycha = 244

    option_Random_mousillon = 2000
    option_Mixu_Mousillon_Mallobaude = 2001
    option_Mixu_Mousillon_Lady_of_the_Black_Grail = 2002
    
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
    
    option_Random_southern_realms = 12500
    option_Cataph_Southern_Realms_Valmir_Gausser = 1251
    option_Cataph_Southern_Realms_Lupio_Sunscryer = 1252
    option_Cataph_Southern_Realms_Borgio_the_Besieger = 1253
    option_Cataph_Southern_Realms_Lucrezzia_Belladonna = 2019
    option_Cataph_Southern_Realms_Leonardo_Catrazza = 2020
    option_Cataph_Southern_Realms_Marco_Colombo = 2021
    option_Cataph_Southern_Realms_Gnashag_the_Black_Prince = 2022
    option_Cataph_Southern_Realms_El_Cadavo = 2023
    
    option_Random_crabs = 12000
    option_Pegaz_Crustacean_Nation_King_Crab = 2008
    option_Pegaz_Crustacean_Nation_Reefspeaker = 2009
    option_Pegaz_Crustacean_Nation_Old_Kelpbeard = 2010
    option_Pegaz_Crustacean_Nation_Tidelord_Anthron = 2011
    option_Pegaz_Crustacean_Nation_Clawdius_Beastslayer = 1012
    option_Pegaz_Crustacean_Nation_Lobstrogh_the_Betrayer = 2013
    option_Pegaz_Crustacean_Nation_Grand_Master_Corallion = 2014

    default = option_The_Daemon_Prince

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

class sphereCount(Range):
    """SPHERE MODE ONLY
    How many diplomatic radius upgrades are required to access all checks.
    You can only interact with factions that are within this radius of your starting capital.
    Depending on starting location, 15-25 will likely include the entire world.
    This value will automatically be reduced by the apworld to ensure there are no empty spheres."""
    display_name = "Radius Upgrades (SPHERES)"
    range_start = 3
    range_end = 25
    default = 3


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

class fillerBlacklist(OptionSet):
    """Filler Blacklist (if you blacklist them all, then nothing will happen). Valid Options:
        "Get-Rich-Slow Scroll", "Get-Rich-Quick Scroll", "Handful of Order", "The GroBro 3000", "Give me that", "Make Love, Not War"
        """
    display_name = "Filler Blacklist"
    valid_keys = ["Get-Rich-Slow Scroll", "Get-Rich-Quick Scroll", "Handful of Order", "The GroBro 3000", "Give me that", "Make Love, Not War"]
class trapBlacklist(OptionSet):
    """Trap Blacklist (if you blacklist them all, then nothing will happen). Valid Options:
    "Handful of Unrest", "Unionize This", "Where is our Map?", "Schizophrenia", "Make Love, Not War", "Torches and Pitchforks", "Let's trade", "You too, Brutus?", "We're Going on a Trip", "En Garde!"
    """
    display_name = "Trap Blacklist"
    valid_keys = ["Handful of Unrest", "Unionize This", "Where is our Map?", "Schizophrenia", "Make Love, Not War", "Torches and Pitchforks", "Let's trade", "You too, Brutus?", "We're Going on a Trip", "En Garde!"]

class randomizePersonalities(DefaultOnToggle):
    """Randomize AI Personalities [Does this work? It's hard to tell, the AI go crazy when shuffled anyway]."""
    display_name = "Randomize AI Personalities"

class hardLogic(DefaultOnToggle):
    """Enforce hard logic so checks cannot be sent without the required logic items even if the player hits the in-game location.
    Recommended for large syncs/asyncs to prevent soft logic issues."""
    display_name = "Hard Logic"

class fastResearch(Toggle):
    """Instantly completes any research that you are sent from the multiworld, but disables techs from being locations if sanity is enabled"""
    display_name = "Fast Research"

class revealHints(Toggle):
    """In-game missions reveal which items can be found in the locations and hint them to the multiworld"""
    display_name = "Reveal Hints"

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
    sphere_count: sphereCount

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

    hard_logic: hardLogic
    fast_research: fastResearch
    reveal_hints: revealHints

    mod_list: modList
    filler_blacklist: fillerBlacklist
    trap_blacklist: trapBlacklist