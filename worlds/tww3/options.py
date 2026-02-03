from random import choice
from Options import Choice, DeathLink, DefaultOnToggle, Range, StartInventoryPool, PerGameCommonOptions, Toggle
from dataclasses import dataclass
from . import settlementManager as sm

class faction(Choice):
    """Choose your faction. If you pick multiple the client will tell you which one you need to play.
    The last 4 options were introduced in the Tides of Torment DLC, this apworld may not randomise all content from that DLC at this time."""
    display_name = "Player Faction"
    option_beastmen = 1
    option_morghur_herd = 2
    option_argwylon = 3
    option_wood_elves = 4
    option_norsca = 5
    option_wintertooth = 6
    option_bordeleaux = 7
    option_bretonnia = 8
    option_carcassonne = 9
    option_chaos = 10
    option_dwarfs = 11
    option_karak_izor = 12
    option_karak_kadrin = 13
    option_empire = 14
    option_wissenland = 15
    option_crooked_moon = 16
    option_greenskins = 17
    option_orcs_of_the_bloody_hand = 18
    option_schwartzhafen = 19
    option_vampire_counts = 20
    option_clan_rictus = 21
    option_exiles_of_nehek = 22
    option_followers_of_nagash = 23
    option_khemri = 24
    option_lybaras = 25
    option_noctilus = 26
    option_pirates_of_sartosa = 27
    option_the_drowned = 28
    option_vampire_coast = 29
    option_the_blessed_dread = 30
    option_the_barrow_legion = 31
    option_cult_of_sotek = 32
    option_golden_order = 33
    option_the_huntmarshals_expedition = 34
    option_spirits_of_the_jungle = 35
    option_chevaliers_de_lyonesse = 36
    option_bonerattlaz = 37
    option_broken_axe = 38
    option_imrik = 39
    option_drycha = 40
    option_sisters_of_twilight = 41
    option_malagor = 42
    option_taurox = 43
    option_thorek_ironbrow = 44
    option_oxyotl = 45
    option_cult_of_pleasure = 46
    option_hag_graef = 47
    option_har_ganeth = 48
    option_naggarond = 49
    option_avelorn = 50
    option_eataine = 51
    option_nagarythe = 52
    option_order_of_loremasters = 53
    option_yvresse = 54
    option_hexoatl = 55
    option_itza = 56
    option_last_defenders = 57
    option_tlaqua = 58
    option_clan_eshin = 59
    option_clan_mors = 60
    option_clan_moulder = 61
    option_clan_pestilens = 62
    option_clan_skryre = 63
    option_rakarth = 64
    option_azazel = 65
    option_festus = 66
    option_kholek = 67
    option_sigvald = 68
    option_valkia = 69
    option_vilitch = 70
    option_astragoth = 71
    option_legion_of_azgorh = 72
    option_zhatan = 73
    option_the_celestial_court = 74
    option_daughters_of_the_forest = 75
    option_the_deceivers = 76
    option_malakai = 77
    option_epidemius = 78
    option_tamurkhan = 79
    option_gorbad_ironclaw = 80
    option_arbaal = 81
    option_skulltaker = 82
    option_golgfag = 83
    option_shadow_legion = 84
    option_the_northern_provinces = 85
    option_the_western_provinces = 86
    option_daemon_prince = 87
    option_the_ancestral_throng = 88
    option_cult_of_sigmar = 89
    option_exiles_of_khorne = 90
    option_the_great_orthodoxy = 91
    option_the_ice_court = 92
    option_ursun_revivalists = 93
    option_poxmakers_of_nurgle = 94
    option_disciples_of_the_maw = 95
    option_goldtooth = 96
    option_seducers_of_slaanesh = 97
    option_oracles_of_tzeentch = 98
    option_caravan_of_blue_roses = 99
    option_high_elf_sea_patrol = 100
    option_dolgan = 101
    option_the_tormentors = 102
    option_masque_of_slaanesh = 103
    default = 1

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
    Depending on YAML settings and the chosen faction, you will likely have around 100-200 non-filler items.
    Make sure to change this value based on how many locations you want your game to have.
    If world generation fails, then you will either need to increase this option or the previous option."""
    display_name = "Checks Per Settlement (CONQUEST)"
    range_start = 1
    range_end = 10
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

class progressiveTechnologies(Toggle):
    """If technologies should be progressive. Requires Tech Shuffle to be on."""
    display_name = "Progressive Technologies"

class buildingShuffle(DefaultOnToggle):
    """Whether buildings should be included in the item pool."""
    display_name = "Building Shuffle"

class progressiveBuildings(Toggle):
    """If buildings should be progressive. Requires Building Shuffle to be on."""
    display_name = "Progressive Buildings"

class unitShuffle(DefaultOnToggle):
    """Whether units should be included in the item pool."""
    display_name = "Unit Shuffle"

class progressiveUnits(Toggle):
    """If units should be progressive. Requires Unit Shuffle to be on."""
    display_name = "Progressive Units"

class ritualShuffle(Toggle):
    """Should faction mechanics like rituals be shuffled? Will make the game harder.
    Experimental feature, report on Discord if this does/does not work."""
    display_name = "Shuffle Faction Mechanics"

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

    randomize_personalities: randomizePersonalities
    ritual_shuffle: ritualShuffle




