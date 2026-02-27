from random import choice
from Options import Choice, DeathLink, DefaultOnToggle, Range, StartInventoryPool, PerGameCommonOptions, Toggle, \
    OptionSet
from dataclasses import dataclass
from . import settlementManager as sm

class faction(Choice):
    """Choose your faction. If you pick multiple the client will tell you which one you need to play.
    The last 4 options were introduced in the Tides of Torment DLC, this apworld may not randomise all content from that DLC at this time."""
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
    option_Zhai_Ming_the_Iron_Dragon = 23
    option_Yuan_Bo_the_Jade_Dragon = 24
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
    default = 0

class gameMode(Choice):
    """Select which game mode you want to use.
    Conquest: No restrictions, checks are based on total settlements conquered.
    Spheres:  You can only interact with factions near your start position,
             all unique settlements are checks. [UNSTABLE]"""
    display_name = "Game Mode"

    option_conquest = "conquest"
    option_spheres = "spheres"

    default = option_conquest

class factionShuffle(DefaultOnToggle):
    """If you want to shuffle the settlements for each faction"""
    display_name = "Faction Shuffle"

class startingSettlements(Range):
    """REQUIRES FACTION SHUFFLE TO BE ENABLED
    Set how many settlements the player will start with."""
    display_name = "Starting Settlements"
    range_start = 1
    range_end = 5
    default = 2
    
class numberOfSettlements(Range):
    """CONQUEST MODE ONLY
    Set how large your empire needs to be for victory. The maximum value is the entire map.
    Make sure to change this based on how fast you want your game to be.
    If world generation fails, then you will need to increase this option or the next option.
    Items will start being found after settlement 3 (unless you don't start with a settlement,
    in which case you will receive them starting from settlement 1)."""
    display_name = "Number Of Settlements (CONQUEST)"
    range_start = 20
    range_end = len(sm.settlementDict)
    default = 100
    
class checksPerSettlement(Range):
    """CONQUEST MODE ONLY
    Set how many checks are triggered per empire size increase (empire size being the number of settlements you own).
    Depending on YAML settings and the chosen faction, you will likely have around 200-300 non-filler items.
    Make sure to change this value based on how many locations you want your game to have.
    If world generation fails, then you will either need to increase this option or the previous option."""
    display_name = "Checks Per Settlement (CONQUEST)"
    range_start = 1
    range_end = 50
    default = 3

class adminCapacity(Range):
    """CONQUEST MODE ONLY
    How many settlements each Administration Capacity item allows you to own.
    Going over the empire size limit will incur heavy penalties.
    You start with 2 admin capacity items to avoid early BK.
    If you are playing solo, set this to the maximum value as the items won't do anything anyway."""
    display_name = "Settlements Per Admin Capacity (CONQUEST)"
    range_start = 1
    range_end = len(sm.settlementDict)
    default = 5

class sphereCount(Range):
    """SPHERE MODE ONLY
    How many diplomatic radius upgrades are required to access all checks.
    You can only interact with factions that are in your radius."""
    display_name = "Radius Upgrades (SPHERES)"
    range_start = 1
    range_end = 65
    default = 7

class extraSphereCount(Range):
    """SPHERE MODE ONLY
    How many extra diplomatic radius upgrades are generated.
    Without these you are more likely to softlock."""
    display_name = "Extra Spheres (SPHERES)"
    range_start = 0
    range_end = 50
    default = 0

class sphereRadius(Range):
    """SPHERE MODE ONLY
    Determines your starting radius and radius added with each upgrade.
    The smallest distance between settlements is 25. The largest is 1400.
    If you spawn in the middle of the map it only takes a radius of 700
    for the entire world to be in logic."""
    display_name = "Diplomatic Radius Size (SPHERES)"
    range_start = 50
    range_end = 500
    default = 150

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

class maxRange(Range):
    """The furthest away two settlements can be during world generation.
    The smallest distance between settlements is 25. The largest is 1400."""
    display_name = "Max Settlement Distance"
    range_start = 50
    range_end = 1500
    default = 200

class techShuffle(DefaultOnToggle):
    """Whether technologies should be included in the item pool."""
    display_name = "Tech Shuffle"

class progressiveTechnologies(Choice):
    """If technologies should be progressive. Requires Tech Shuffle to be on."""
    display_name = "Progressive Technologies"
    option_true = 1
    option_false = 0
    default = 0

class buildingShuffle(DefaultOnToggle):
    """Whether buildings should be included in the item pool."""
    display_name = "Building Shuffle"

class progressiveBuildings(Choice):
    """If buildings should be progressive. Requires Building Shuffle to be on."""
    display_name = "Progressive Buildings"
    option_true = 1
    option_false = 0
    default = 0

class unitShuffle(DefaultOnToggle):
    """Whether units should be included in the item pool."""
    display_name = "Unit Shuffle"

class progressiveUnits(Choice):
    """If units should be progressive. Requires Unit Shuffle to be on."""
    display_name = "Progressive Units"
    option_true = 1
    option_false = 0
    default = 0

class ritualShuffle(Choice):
    """CURRENTLY DISABLED - I don't think this ever worked.
    Should faction mechanics like rituals be shuffled? Will make the game harder.
    Experimental feature, report on Discord if this does/does not work."""
    display_name = "Shuffle Faction Mechanics"
    option_false = 0
    default = 0

class startingTier(Range):
    """Start with buildings and units of this tier already unlocked."""
    display_name = "Starting Tier"
    range_start = 0
    range_end = 5
    default = 1

class balance(Range):
    """Percentage of your early items that are forced unlocks.
    0 doesn't force unlocks at all. 100 means that all of your early items will be unlocks.
    High values are not recommended."""
    display_name = "Force Early Upgrades"
    range_start = 0
    range_end = 100
    default = 0

class forceEarlyBuildings(Range):
    """SET TO 0 TO DISABLE
    Whether buildings should be a forced unlock and determines the tier.
    Building shuffle must be on and balance must be greater than 0.
    The value sets the highest tier of buildings that will be forced.
    E.g. 2 means that only tier 1 and 2 buildings will be forced."""
    display_name = "Early Building Tiers"
    range_start = 0
    range_end = 5
    default = 0

class forceEarlyUnits(Range):
    """SET TO 0 TO DISABLE
    Whether units should be a forced unlock and determines the tier.
    Unit shuffle must be on and balance must be greater than 0.
    The value sets the highest tier of units that will be forced.
    E.g. 2 means that only tier 1 and 2 units will be forced."""
    display_name = "Early Unit Tiers"
    range_start = 0
    range_end = 5
    default = 0

class forceEarlyTechs(Toggle):
    """Whether tech should be a forced unlock.
    Tech shuffle must be on and balance must be greater than 0."""
    display_name = "Early Tech"

class fillerWeak(Range):
    """Weight of weak filler items.
    For example: filler_weak: 15, filler_strong: 10, trap_harmless: 0, trap_weak: 15, trap_strong: 10
    Would mean: 30% weak filler, 20% strong filler, 0% harmless traps, 30% weak traps, 20% strong traps
    because the weights add up to 50."""
    display_name = "Weak Filler Weight"
    range_start = 0
    range_end = 100
    default = 40

class fillerStrong(Range):
    """Weight of strong filler items."""
    display_name = "Strong Filler Weight"
    range_start = 0
    range_end = 100
    default = 20

class trapHarmless(Range):
    """Weight of harmless traps.
    These won't disrupt your game, but may be annoying."""
    display_name = "Harmless Trap Weight"
    range_start = 0
    range_end = 100
    default = 10

class trapWeak(Range):
    """Weight of weak traps.
    Receiving a lot of them very quickly may require you to reload a previous save."""
    display_name = "Weak Trap Weight"
    range_start = 0
    range_end = 100
    default = 20

class trapStrong(Range):
    """Weight of strong traps.
    A few badly timed strong traps may require you to reload a previous save."""
    display_name = "Strong Trap Weight"
    range_start = 0
    range_end = 100
    default = 10

class randomizePersonalities(DefaultOnToggle):
    """Randomize AI Personalities."""
    display_name = "Randomize AI Personalities"

class deathLink(DefaultOnToggle):
    """NOT CURRENTLY ENABLED
    Enable or Disable death linking."""
    display_name = "Death Link"

class deathLinkEffect(OptionSet):
    display_name = "Death Link Effect"
    valid_keys = ["10% Treasury", "25% Treasury", "50% Treasury", "Wound Hero", "Wound Lord", "Rebellion", "Raze Random Settlement"]
    default = frozenset({"25% Treasury"})

@dataclass
class TWW3Options(PerGameCommonOptions):
    starting_faction: faction
    game_mode: gameMode
    faction_shuffle: factionShuffle
    starting_settlements: startingSettlements

    number_of_settlements: numberOfSettlements
    checks_per_settlement: checksPerSettlement
    admin_capacity: adminCapacity

    sphere_count: sphereCount
    extra_sphere_count: extraSphereCount
    sphere_radius: sphereRadius
    orb_count: orbCount
    extra_orb_count: extraOrbCount

    max_range: maxRange

    tech_shuffle: techShuffle
    progressive_technologies: progressiveTechnologies
    building_shuffle: buildingShuffle
    progressive_buildings: progressiveBuildings
    unit_shuffle: unitShuffle
    progressive_units: progressiveUnits

    starting_tier: startingTier
    balance: balance
    force_early_buildings: forceEarlyBuildings
    force_early_units: forceEarlyUnits
    force_early_techs: forceEarlyTechs

    filler_weak: fillerWeak
    filler_strong: fillerStrong
    trap_harmless: trapHarmless
    trap_weak: trapWeak
    trap_strong: trapStrong

    death_link: deathLink
    death_link_effect: deathLinkEffect

    randomize_personalities: randomizePersonalities
    ritual_shuffle: ritualShuffle




