from random import choice

from Options import Choice, DeathLink, DefaultOnToggle, Range, StartInventoryPool, PerGameCommonOptions, Toggle
from dataclasses import dataclass
from .locations_table.settlements import settlementTable

class faction(Choice):
    """Choose your Player Faction. In case you pick multiple factions, the Client will tell you after connecting which one you play.
    Don't forget to remove the weight from the first entry.
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
    Conquest: No restrictions, just conquer settlements to find checks.
    Spheres: You can only interact with factions within a set radius of your start position,
            conquer specific settlements to find checks. [There is currently a chance for softlocks to trigger in this game mode]"""
    display_name = "Game Mode"

    option_conquest = "conquest"
    option_spheres = "spheres"

    default = option_conquest

class factionShuffle(DefaultOnToggle):
    """CONQUEST MODE ONLY
    If you want to shuffle the settlements for each faction"""
    display_name = "FactionShuffle"
    
class numberOfSettlements(Range):
    """CONQUEST MODE ONLY
    Set how large your empire needs to be for victory. The maximum value is the entire map.
    Make sure to change this value based on how fast you want your game to be.
    If world generation fails, then you will need to increase either this option or the next option.
    Items will start being found after settlement 5 (unless you don't start with a settlement, in which case
    you will receive them starting from settlement 1)."""
    display_name = "NumberOfSettlements"
    range_start = 20
    range_end = len(settlementTable)
    default = 100
    
class checksPerSettlement(Range):
    """CONQUEST MODE ONLY
    Set how many checks are triggered per empire size increase (empire size being the number of settlements you own).
    Depending on YAML settings and the chosen faction, you will likely have around 100-200 non-filler items.
    Make sure to change this value based on how many apworld "locations" you want your game to have.
    If world generation fails, then you will need to increase either this option or the previous option."""
    display_name = "ChecksPerSettlement"
    range_start = 1
    range_end = 10
    default = 3

class adminCapacity(Range):
    """CONQUEST MODE ONLY
    Set how many settlements you can own before needing an additional admin capacity item to avoid economic debuffs.
    The player will start with 2 admin capacity items to prevent early game being unable to do anything"""
    display_name = "SettlementsPerAdminCapacity"
    range_start = 1
    range_end = len(settlementTable)
    default = 5

class sphereCount(Range):
    """SPHERE MODE ONLY
    How many diplomatic Spheres are required to reach the maximum radius. You can only engage in Diplomacy with factions that are in your sphere.
    Collect Spheres of Influence to expand your Sphere."""
    range_start = 1
    range_end = 65
    default = 7

class extraSphereCount(Range):
    """SPHERE MODE ONLY
    How many extra diplomatic Spheres are in the game in addition to the ones required. Since there is at the moment a small chance to softlock, a few extra spheres should be chosen."""
    range_start = 0
    range_end = 50
    default = 0

class sphereRadius(Range):
    """SPHERE MODE ONLY
    Radius of each Sphere."""
    # Min Range between Settlements is 24. Max Range is 1300.
    range_start = 20
    range_end = 500
    default = 150

class orbCount(Range):
    """SPHERE MODE ONLY
    How many Orb of Domination items are generated in the multiworld.
    Once you have collected all of your orbs of domination, you win."""
    range_start = 1
    range_end = 100
    default = 20

class extraOrbCount(Range):
    """SPHERE MODE ONLY
    How many extra Domination Orbs should be in the game in addition to the ones required."""
    range_start = 0
    range_end = 50
    default = 0

class maxRange(Range):
    """How far away a Settlement can be from a factions other settlements during generation.
    The smallest in-game distance between two settlements is around 23 units.
    The maximum distance is around 1500 units."""
    range_start = 50
    range_end = 1500
    default = 200

class techShuffle(DefaultOnToggle):
    """If Technologies should be shuffled."""
    display_name = "TechShuffle"

class progressiveTechnologies(Toggle):
    """If Technologies should be progressive. Requires TechShuffle to be on."""
    display_name = "Progressive Technologies"

class buildingShuffle(DefaultOnToggle):
    """If Buildings should be shuffled."""
    display_name = "BuildingShuffle"

class progressiveBuildings(DefaultOnToggle):
    """If Buildings should be progressive. Requires BuildingShuffle to be on."""
    display_name = "Progressive Buildings"

class unitShuffle(DefaultOnToggle):
    """If Units should be shuffled."""
    display_name = "UnitShuffle"

class progressiveUnits(DefaultOnToggle):
    """If Units should be progressive. Requires UnitShuffle to be on."""
    display_name = "Progressive Units"

class ritualShuffle(Toggle):
    """Should Faction Mechanics like Rituals be shuffled? Will make game probably harder.
    Experimental feature, report to the discord if this does/does not work.."""
    display_name ="Shuffle Faction Mechanics like Rituals"

class startingTier(Range):
    """Start with Buildings and Units with the specified Tier."""
    range_start = 0
    range_end = 5
    default = 1

class balance(Range):
    """If you want to balance the unlocks closer to the start of the multiworld.
    0 introduces no forced balancing. 100 introduces maximised balancing.
    High values are not recommended and may result in crashes during multiworld generation."""
    display_name = "balance"
    range_start = 0
    range_end = 100
    default = 0

class forceEarlyBuildings(Range):
    """SET TO 0 TO DISABLE
    If Buildings should be forced to generate near the start of the multiworld.
    Requires building shuffle to be on and balance to be greater than 0.
    The value sets the highest tier buildings that will be forced.
    E.g. 2 means that only tier 1 and 2 buildings will be forced."""
    display_name = "ForceEarlyBuildings"
    range_start = 0
    range_end = 5
    default = 2

class forceEarlyUnits(Range):
    """SET TO O TO DISABLE
    If Buildings should be forced to generate near the start of the multiworld.
    Requires unit shuffle to be on and balance to be greater than 0.
    The value sets the highest tier units that will be forced.
    E.g. 2 means that only tier 1 and 2 units will be forced."""
    display_name = "ForceEarlyUnits"
    range_start = 0
    range_end = 5
    default = 2

class forceEarlyTechs(Toggle):
    """If Buildings should be forced to generate near the start of the multiworld.
    Requires tech shuffle to be on and balance to be greater than 0."""
    display_name = "ForceEarlyTechs"

class fillerWeak(Range):
    """Weight of weak filler items.
    Example: filler_weak: 30, filler_strong: 20, trap_harmless: 0, trap_weak: 30, trap_strong: 20
    Would mean, that approximately 30% are weak filler, 20% are strong filler, etc, since the weights add up to 100.
    You can deviate from that, but it will be less intuitive if the total number of weights is not 100."""
    range_start = 0
    range_end = 100
    default = 30

class fillerStrong(Range):
    """Weight of strong filler items."""
    range_start = 0
    range_end = 100
    default = 20

class trapHarmless(Range):
    """Weight of harmless traps Not currently implemented.
    These won't disrupt your game. They may, however, induce minor irritation."""
    range_start = 0
    range_end = 100
    default = 0

class trapWeak(Range):
    """Weight of weak traps.
    Be careful, collecting a vast amount of them may require you to start a new save."""
    range_start = 0
    range_end = 100
    default = 30

class trapStrong(Range):
    """Weight of weak traps.
    Be careful, collecting a medium amount of them may require you to start a new save."""
    range_start = 0
    range_end = 100
    default = 20

class randomizePersonalities(DefaultOnToggle):
    """Randomize AI Personalities."""
    display_name = "Randomize Personality of each AI faction"

@dataclass
class TWW3Options(PerGameCommonOptions):
    starting_faction: faction
    faction_shuffle: factionShuffle

    game_mode: gameMode
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
    filler_weak: fillerWeak
    filler_strong: fillerStrong
    trap_harmless: trapHarmless
    trap_weak: trapWeak
    trap_strong: trapStrong
    randomize_personalities: randomizePersonalities
    ritual_shuffle: ritualShuffle
    balance: balance
    force_early_buildings: forceEarlyBuildings
    force_early_units: forceEarlyUnits

    force_early_techs: forceEarlyTechs
