from typing import TypedDict
from .forest_locations import forest_location_table
import math

lord_name_to_faction_dict = {
    1: "wh_dlc03_bst_beastmen",
    2: "wh_dlc05_bst_morghur_herd",
    3: "wh_dlc05_wef_argwylon",
    4: "wh_dlc05_wef_wood_elves",
    5: "wh_dlc08_nor_norsca",
    6: "wh_dlc08_nor_wintertooth",
    7: "wh_main_brt_bordeleaux",
    8: "wh_main_brt_bretonnia",
    9: "wh_main_brt_carcassonne",
    10: "wh_main_chs_chaos",
    11: "wh_main_dwf_dwarfs",
    12: "wh_main_dwf_karak_izor",
    13: "wh_main_dwf_karak_kadrin",
    14: "wh_main_emp_empire",
    15: "wh_main_emp_wissenland",
    16: "wh_main_grn_crooked_moon",
    17: "wh_main_grn_greenskins",
    18: "wh_main_grn_orcs_of_the_bloody_hand",
    19: "wh_main_vmp_schwartzhafen",
    20: "wh_main_vmp_vampire_counts",
    21: "wh2_dlc09_skv_clan_rictus",
    22: "wh2_dlc09_tmb_exiles_of_nehek",
    23: "wh2_dlc09_tmb_followers_of_nagash",
    24: "wh2_dlc09_tmb_khemri",
    25: "wh2_dlc09_tmb_lybaras",
    26: "wh2_dlc11_cst_noctilus",
    27: "wh2_dlc11_cst_pirates_of_sartosa",
    28: "wh2_dlc11_cst_the_drowned",
    29: "wh2_dlc11_cst_vampire_coast",
    30: "wh2_dlc11_def_the_blessed_dread",
    31: "wh2_dlc11_vmp_the_barrow_legion",
    32: "wh2_dlc12_lzd_cult_of_sotek",
    33: "wh2_dlc13_emp_golden_order",
    34: "wh2_dlc13_emp_the_huntmarshals_expedition",
    35: "wh2_dlc13_lzd_spirits_of_the_jungle",
    36: "wh2_dlc14_brt_chevaliers_de_lyonesse",
    37: "wh2_dlc15_grn_bonerattlaz",
    38: "wh2_dlc15_grn_broken_axe",
    39: "wh2_dlc15_hef_imrik",
    40: "wh2_dlc16_wef_drycha",
    41: "wh2_dlc16_wef_sisters_of_twilight",
    42: "wh2_dlc17_bst_malagor",
    43: "wh2_dlc17_bst_taurox",
    44: "wh2_dlc17_dwf_thorek_ironbrow",
    45: "wh2_dlc17_lzd_oxyotl",
    46: "wh2_main_def_cult_of_pleasure",
    47: "wh2_main_def_hag_graef",
    48: "wh2_main_def_har_ganeth",
    49: "wh2_main_def_naggarond",
    50: "wh2_main_hef_avelorn",
    51: "wh2_main_hef_eataine",
    52: "wh2_main_hef_nagarythe",
    53: "wh2_main_hef_order_of_loremasters",
    54: "wh2_main_hef_yvresse",
    55: "wh2_main_lzd_hexoatl",
    56: "wh2_main_lzd_itza",
    57: "wh2_main_lzd_last_defenders",
    58: "wh2_main_lzd_tlaqua",
    59: "wh2_main_skv_clan_eshin",
    60: "wh2_main_skv_clan_mors",
    61: "wh2_main_skv_clan_moulder",
    62: "wh2_main_skv_clan_pestilens",
    63: "wh2_main_skv_clan_skryre",
    64: "wh2_twa03_def_rakarth",
    65: "wh3_dlc20_chs_azazel",
    66: "wh3_dlc20_chs_festus",
    67: "wh3_dlc20_chs_kholek",
    68: "wh3_dlc20_chs_sigvald",
    69: "wh3_dlc20_chs_valkia",
    70: "wh3_dlc20_chs_vilitch",
    71: "wh3_dlc23_chd_astragoth",
    72: "wh3_dlc23_chd_legion_of_azgorh",
    73: "wh3_dlc23_chd_zhatan",
    74: "wh3_dlc24_cth_the_celestial_court",
    75: "wh3_dlc24_ksl_daughters_of_the_forest",
    76: "wh3_dlc24_tze_the_deceivers",
    77: "wh3_dlc25_dwf_malakai",
    78: "wh3_dlc25_nur_epidemius",
    79: "wh3_dlc25_nur_tamurkhan",
    80: "wh3_dlc26_grn_gorbad_ironclaw",
    81: "wh3_dlc26_kho_arbaal",
    82: "wh3_dlc26_kho_skulltaker",
    83: "wh3_dlc26_ogr_golgfag",
    84: "wh3_main_chs_shadow_legion",
    85: "wh3_main_cth_the_northern_provinces",
    86: "wh3_main_cth_the_western_provinces",
    87: "wh3_main_dae_daemon_prince",
    88: "wh3_main_dwf_the_ancestral_throng",
    89: "wh3_main_emp_cult_of_sigmar",
    90: "wh3_main_kho_exiles_of_khorne",
    91: "wh3_main_ksl_the_great_orthodoxy",
    92: "wh3_main_ksl_the_ice_court",
    93: "wh3_main_ksl_ursun_revivalists",
    94: "wh3_main_nur_poxmakers_of_nurgle",
    95: "wh3_main_ogr_disciples_of_the_maw",
    96: "wh3_main_ogr_goldtooth",
    97: "wh3_main_sla_seducers_of_slaanesh",
    98: "wh3_main_tze_oracles_of_tzeentch",
    99: "wh3_main_vmp_caravan_of_blue_roses",
    100: "wh3_dlc27_hef_aislinn",
    101: "wh3_dlc27_nor_sayl",
    102: "wh3_dlc27_sla_the_tormentors",
    103: "wh3_dlc27_sla_masque_of_slaanesh"
}

faction_name_to_readable = {
    1: "Khazrak the One-Eye (Beastmen)",
    2: "Morghur the Shadowgave (Beastmen)",
    3: "Durthu (Wood Elves)",
    4: "Orion (Wood Elves)",
    5: "Wulfrik the Wanderer (Norsca)",
    6: "Throgg (Norsca)",
    7: "Alberic de Bordeleaux (Bretonnia)",
    8: "King Louen Leoncoeur (Bretonnia)",
    9: "Fay Enchantress (Bretonnia)",
    10: "Archaon the Everchosen (Warriors of Chaos)",
    11: "Thorgrim Grudgebearer (Dwarfs)",
    12: "Belegar Ironhammer (Dwarfs)",
    13: "Ungrim Ironfist (Dwarfs)",
    14: "Karl Franz (Empire)",
    15: "Elspeth Von Draken (Empire)",
    16: "Skarsnik (Greenskins)",
    17: "Grimgor Ironhide (Greenskins)",
    18: "Wurrzag da Great Green Prophet (Greenskins)",
    19: "Vlad von Carstein (Vampire Counts)",
    20: "Mannfred von Carstein (Vampire Counts)",
    21: "Tretch Craventail (Skaven)",
    22: "Grand Hierophant Khatep (Tomb Kings)",
    23: "Arkhan the Black (Tomb Kings)",
    24: "Settra... Great King, the Imperishable, Khemrikhara, The Great King of Nehekhara, King of Kings, "
        "Opener of the Way, Wielder of the Divine Flame, Punisher of Nomads, The Great Unifier, "
        "Commander of the Golden Legion, Sacred of Appearance, Bringer of Light, Father of Hawks, "
        "Builder of Cities, Protector of the Two Worlds, Keeper of the Hours, Chosen of Ptra, "
        "High Steward of the Horizon, Sailor of the Great Vitae, Sentinel of the Two Realms, "
        "The Undisputed, Begetter of the Begat, Scourge of the Faithless, Carrion-feeder, "
        "First of the Charnel Valley, Rider of the Sacred Chariot, Vanquisher of Vermin, "
        "Champion of the Death Arena, Mighty Lion of the Infinite Desert, Emperor of the Shifting Sands, "
        "He Who Holds The Sceptre, Great Hawk Of The Heavens, Arch-Sultan of Atalan, Waker of the Hierotitan, "
        "Monarch of the Sky, Majestic Emperor of the Shifting Sands, Champion of the Desert Gods, "
        "Breaker of the Ogre Clans, Builder of the Great Pyramid, Terror of the Living, "
        "Master of the Never-Ending Horizon, Master of the Necropolises, Taker of Souls, "
        "Tyrant to the Foolish, Bearer of Ptra's Holy Blade, Scion of Usirian, Scion of Nehek, The Great, "
        "Chaser of Nightmares, Keeper of the Royal Herat, Founder of the Mortuary Cult, "
        "Banisher of the Grand Hierophant, High Lord Admiral of the Deathfleets, Guardian of the Charnal Pass, "
        "Tamer of the Liche King, Unliving Jackal Lord, Dismisser of the Warrior Queen, Charioteer of the Gods, "
        "He Who Does Not Serve, Slayer off Reddittras, Scarab Purger, Favoured of Usirian, Player of the Great Game, "
        "Liberator of Life, Lord Sand, Wrangler of Scorpions, Emperor of the Dunes, "
        "Eternal Sovereign of Khemri's Legions, Seneschal of the Great Sandy Desert, Curserer of the Living, "
        "Regent of the Eastern Mountains, Warden of the Eternal Necropolis, Herald of all Heralds, "
        "Caller of the Bitter Wind, God-Tamer, Master of the Mortis River, Guardian of the Dead, "
        "Great Keeper of the Obelisks, Deacon of the Ash River, Belated of Wakers, General of the Mighty Frame, "
        "Summoner of Sandstorms, Master of all Necrotects, Prince of Dust, Tyrant of Araby, "
        "Purger of the Greenskin Breathers, Killer of the False God's Champions, Tyrant of the Gold Dunes, "
        "Golden Bone Lord, Avenger of the Dead, Carrion Master, Eternal Warden of Nehek's Lands, "
        "Breaker of Djaf's Bonds... and many, many more... (Tomb Kings)",
    25: "High Queen Khalida (Tomb Kings)",
    26: "Count Noctilus (Vampire Coast)",
    27: "Aranessa Saltspite (Vampire Coast)",
    28: "Cylostra Direfin (Vampire Coast)",
    29: "Luthor Harkon (Vampire Coast)",
    30: "Lokhir Fellheart (Dark Elves)",
    31: "Heinrich Kemmler (Vampire Counts)",
    32: "Tehenhauin (Lizardmen)",
    33: "Balthasar Gelt (Empire)",
    34: "Markus Wulfhart (Empire)",
    35: "Nakai the Wanderer (Lizardmen)",
    36: "Repanse de Lyonesse (Bretonnia)",
    37: "Azhag the Slaughterer (Greenskins)",
    38: "Grom the Paunch (Greenskins)",
    39: "Imrik (High Elves)",
    40: "Drycha (Wood Elves)",
    41: "Sisters of Twilight (Wood Elves)",
    42: "Malagor the Dark Omen (Beastmen)",
    43: "Taurox the Brass Bull (Beastmen)",
    44: "Thorek Ironbrow (Dwarfs)",
    45: "Oxyotl (Lizardmen)",
    46: "Morathi (Dark Elves)",
    47: "Malus Darkblade (Dark Elves)",
    48: "Crone Helebron (Dark Elves)",
    49: "Malekith (Dark Elves)",
    50: "Alarielle the Radiant (High Elves)",
    51: "Tyrion (High Elves)",
    52: "Alith Anar (High Elves)",
    53: "Teclis (High Elves)",
    54: "Eltharion the Grim (High Elves)",
    55: "Lord Mazdamundi (Lizardmen)",
    56: "Gor-Rok (Lizardmen)",
    57: "Kroq-Gar (Lizardmen)",
    58: "Tiktaq'to (Lizardmen)",
    59: "Deathmaster Snikch (Skaven)",
    60: "Queek Headtaker (Skaven)",
    61: "Throt the Unclean (Skaven)",
    62: "Lord Skrolk (Skaven)",
    63: "Ikit Claw (Skaven)",
    64: "Rakarth the Beastmaster (Dark Elves)",
    65: "Azazel (Warriors of Chaos)",
    66: "Festus the Leechlord (Warriors of Chaos)",
    67: "Kholek Suneater (Warriors of Chaos)",
    68: "Prince Sigvald the Magnificent (Warriors of Chaos)",
    69: "Valkia the Bloody (Warriors of Chaos)",
    70: "Vilitch the Cursling (Warriors of Chaos)",
    71: "Astragoth Ironhand (Chaos Dwarfs)",
    72: "Drazhoath the Ashen (Chaos Dwarfs)",
    73: "Zhaten the Black (Chaos Dwarfs)",
    74: "Yuan Bo, the Jade Dragon (Grand Cathay)",
    75: "Mother Ostankya (Kislev)",
    76: "The Changeling (Tzeentch)",
    77: "Malakai Makaisson (Dwarfs)",
    78: "Epidemius (Nurgle)",
    79: "Tamurkhan the Maggot Lord (Nurgle)",
    80: "Gorbad Ironclaw (Greenskins)",
    81: "Arbaal the Undefeated (Khorne)",
    82: "Skulltaker (Khorne)",
    83: "Golgfag Maneater (Ogre Kingdoms)",
    84: "Be'lakor (Warriors of Chaos)",
    85: "Miao Ying, the Storm Dragon (Grand Cathay)",
    86: "Zhai Ming, the Iron Dragon (Grand Cathay)",
    87: "The Daemon Prince (Daemons of Chaos)",
    88: "Grombrindal - The White Dwarf (Dwarfs)",
    89: "Volkmar the Grim (Empire)",
    90: "Skarbrand (Khorne)",
    91: "Kostaltyn (Kislev)",
    92: "Tzarina Katarin (Kislev)",
    93: "Boris Ursus (Kislev)",
    94: "Ku'gath Plaguefather (Nurgle)",
    95: "Skrag the Slaughterer (Ogre Kingdoms)",
    96: "Greasus Goldtooth (Ogre Kingdoms)",
    97: "N'Kari (Slaanesh)",
    98: "Kairos Fateweaver (Tzeentch)",
    99: "Helman Ghorst (Vampire Counts)",
    100: "Sea Lord Aislinn (High Elves)",
    101: "Sayl the Faithless (Sayl)",
    102: "Dechala, the Denied One (Slaanesh)",
    103: "The Masque of Slaanesh (Slaanesh)"
}

# faction table with columns faction_key, is_playable, has_home
faction_table = [
    ["wh3_main_dae_daemon_prince", True, False],
    ["wh3_main_kho_exiles_of_khorne", True, True],
    ["wh3_dlc26_kho_skulltaker", True, True],
    ["wh3_dlc26_kho_arbaal", True, True],
    ["wh3_main_nur_poxmakers_of_nurgle", True, True],
    ["wh3_dlc25_nur_tamurkhan", True, True],
    ["wh3_dlc25_nur_epidemius", True, True],
    ["wh3_main_sla_seducers_of_slaanesh", True, True],
    ["wh3_main_tze_oracles_of_tzeentch", True, True],
    ["wh3_dlc24_tze_the_deceivers", True, False],
    ["wh3_main_ksl_the_ice_court", True, True],
    ["wh3_main_ksl_the_great_orthodoxy", True, True],
    ["wh3_main_ksl_ursun_revivalists", True, False],
    ["wh3_dlc24_ksl_daughters_of_the_forest", True, True],
    ["wh3_main_ogr_goldtooth", True, True],
    ["wh3_main_ogr_disciples_of_the_maw", True, True],
    ["wh3_dlc26_ogr_golgfag", True, False],
    ["wh3_dlc23_chd_astragoth", True, True],
    ["wh3_dlc23_chd_legion_of_azgorh", True, True],
    ["wh3_dlc23_chd_zhatan", True, True],
    ["wh3_main_cth_the_northern_provinces", True, True],
    ["wh3_main_cth_the_western_provinces", True, True],
    ["wh3_dlc24_cth_the_celestial_court", True, True],
    ["wh2_main_hef_eataine", True, True],
    ["wh2_main_hef_order_of_loremasters", True, True],
    ["wh2_main_hef_avelorn", True, True],
    ["wh2_main_hef_nagarythe", True, True],
    ["wh2_main_hef_yvresse", True, True],
    ["wh2_dlc15_hef_imrik", True, True],
    ["wh2_dlc17_lzd_oxyotl", True, True],
    ["wh2_main_lzd_hexoatl", True, True],
    ["wh2_main_lzd_last_defenders", True, True],
    ["wh2_dlc12_lzd_cult_of_sotek", True, True],
    ["wh2_main_lzd_tlaqua", True, True],
    ["wh2_dlc13_lzd_spirits_of_the_jungle", True, False],
    ["wh2_main_lzd_itza", True, True],
    ["wh2_main_def_naggarond", True, True],
    ["wh2_main_def_cult_of_pleasure", True, True],
    ["wh2_main_def_har_ganeth", True, True],
    ["wh2_dlc11_def_the_blessed_dread", True, True],
    ["wh2_main_def_hag_graef", True, False],
    ["wh2_twa03_def_rakarth", True, True],
    ["wh2_main_skv_clan_mors", True, True],
    ["wh2_main_skv_clan_pestilens", True, True],
    ["wh2_dlc09_skv_clan_rictus", True, True],
    ["wh2_main_skv_clan_skryre", True, True],
    ["wh2_main_skv_clan_moulder", True, True],
    ["wh2_main_skv_clan_eshin", True, True],
    ["wh2_dlc09_tmb_khemri", True, True],
    ["wh2_dlc09_tmb_lybaras", True, True],
    ["wh2_dlc09_tmb_exiles_of_nehek", True, True],
    ["wh2_dlc09_tmb_followers_of_nagash", True, True],
    ["wh2_dlc11_cst_vampire_coast", True, True],
    ["wh2_dlc11_cst_noctilus", True, True],
    ["wh2_dlc11_cst_the_drowned", True, True],
    ["wh2_dlc11_cst_pirates_of_sartosa", True, True],
    ["wh_main_emp_empire", True, True],
    ["wh2_dlc13_emp_golden_order", True, False],
    ["wh3_main_emp_cult_of_sigmar", True, True],
    ["wh2_dlc13_emp_the_huntmarshals_expedition", True, True],
    ["wh_main_emp_wissenland", True, True],
    ["wh_main_dwf_dwarfs", True, True],
    ["wh_main_dwf_karak_kadrin", True, True],
    ["wh_main_dwf_karak_izor", True, True],
    ["wh3_main_dwf_the_ancestral_throng", True, True],
    ["wh2_dlc17_dwf_thorek_ironbrow", True, True],
    ["wh3_dlc25_dwf_malakai", True, True],
    ["wh_main_grn_greenskins", True, True],
    ["wh_main_grn_crooked_moon", True, True],
    ["wh2_dlc15_grn_bonerattlaz", True, True],
    ["wh_main_grn_orcs_of_the_bloody_hand", True, True],
    ["wh2_dlc15_grn_broken_axe", True, True],
    ["wh3_dlc26_grn_gorbad_ironclaw", True, True],
    ["wh_main_vmp_vampire_counts", True, True],
    ["wh2_dlc11_vmp_the_barrow_legion", True, True],
    ["wh3_main_vmp_caravan_of_blue_roses", True, True],
    ["wh_main_vmp_schwartzhafen", True, True],
    ["wh_main_chs_chaos", True, False],
    ["wh3_dlc20_chs_kholek", True, False],
    ["wh3_dlc20_chs_sigvald", True, False],
    ["wh3_dlc20_chs_azazel", True, False],
    ["wh3_dlc20_chs_festus", True, True],
    ["wh3_dlc20_chs_valkia", True, False],
    ["wh3_dlc20_chs_vilitch", True, False],
    ["wh3_main_chs_shadow_legion", True, False],
    ["wh_dlc03_bst_beastmen", True, False],
    ["wh2_dlc17_bst_malagor", True, False],
    ["wh_dlc05_bst_morghur_herd", True, False],
    ["wh2_dlc17_bst_taurox", True, False],
    ["wh_dlc05_wef_wood_elves", True, True],
    ["wh_dlc05_wef_argwylon", True, True],
    ["wh2_dlc16_wef_sisters_of_twilight", True, True],
    ["wh2_dlc16_wef_drycha", True, True],
    ["wh_main_brt_bretonnia", True, True],
    ["wh_main_brt_carcassonne", True, True],
    ["wh_main_brt_bordeleaux", True, True],
    ["wh2_dlc14_brt_chevaliers_de_lyonesse", True, True],
    ["wh_dlc08_nor_norsca", True, True],
    ["wh_dlc08_nor_wintertooth", True, True],
    ["wh3_main_kho_bloody_sword", False, True],
    ["wh3_main_kho_brazen_throne", False, True],
    ["wh3_main_kho_crimson_skull", False, True],
    ["wh3_main_nur_bubonic_swarm", False, True],
    ["wh3_main_nur_maggoth_kin", False, True],
    ["wh3_dlc20_nur_pallid_nurslings", False, True],
    ["wh3_main_sla_exquisite_pain", False, True],
    ["wh3_main_sla_rapturous_excess", False, True],
    ["wh3_main_sla_subtle_torture", False, True],
    ["wh3_dlc20_sla_keepers_of_bliss", False, True],
    ["wh3_main_tze_all_seeing_eye", False, True],
    ["wh3_main_tze_broken_[wheel", False, True],
    ["wh3_main_tze_flaming_scribes", False, True],
    ["wh3_main_ksl_ropsmenn_clan", False, True],
    ["wh3_dlc20_tze_the_sightless", False, True],
    ["wh3_dlc20_tze_apostles_of_change", False, True],
    ["wh3_main_tze_sarthoraels_watchers", False, True],
    ["wh3_main_ksl_brotherhood_of_the_bear", False, True],
    ["wh3_main_ksl_druzhina_enclave", False, True],
    ["wh3_main_ksl_ungol_kindred", False, True],
    ["wh3_main_ogr_blood_guzzlers", False, True],
    ["wh3_main_ogr_crossed_clubs", False, True],
    ["wh3_main_ogre_sharktooth", False, False],
    ["wh3_main_ogre_stoneshatter", False, False],
    ["wh3_main_ogr_feastmaster", False, False],
    ["wh3_main_ogre_the_famished", False, True],
    ["wh3_main_ogre_flamegullets", False, False],
    ["wh3_main_ogr_fleshgreeders", False, True],
    ["wh3_main_ogr_fulg", False, True],
    ["wh3_main_ogr_lazarghs", False, True],
    ["wh3_main_ogr_mountaineaters", False, True],
    ["wh3_main_ogr_rock_skulls", False, True],
    ["wh3_main_ogr_sabreskin", False, True],
    ["wh3_main_ogr_sons_of_the_mountain", False, True],
    ["wh3_main_ogr_thunderguts", False, True],
    ["wh3_main_ogr_treehammers", False, False],
    ["wh3_main_cth_burning_wind_nomads", False, True],
    ["wh3_main_cth_celestial_loyalists", False, True],
    ["wh3_main_cth_dissenter_lords_of_jinshen", False, True],
    ["wh3_main_cth_eastern_river_lords", False, True],
    ["wh3_main_cth_imperial_wardens", False, True],
    ["wh3_main_cth_rebel_lords_of_nan_yang", False, True],
    ["wh3_main_cth_the_jade_custodians", False, True],
    ["wh2_main_hef_caledor", False, True],
    ["wh2_main_hef_chrace", False, True],
    ["wh2_main_hef_citadel_of_dusk", False, True],
    ["wh2_main_hef_cothique", False, True],
    ["wh2_main_hef_ellyrion", False, True],
    ["wh2_main_hef_saphery", False, True],
    ["wh2_main_hef_tiranoc", False, True],
    ["wh2_main_hef_tor_elasor", False, True],
    ["wh2_main_lzd_sentinels_of_xeti", False, True],
    ["wh2_main_lzd_southern_sentinels", False, True],
    ["wh3_main_lzd_tepoks_spawn", False, True],
    ["wh2_main_lzd_tlaxtlan", False, True],
    ["wh2_dlc16_lzd_wardens_of_the_living_pools", False, True],
    ["wh2_main_lzd_xlanhuapec", False, True],
    ["wh2_main_lzd_zlatan", False, True],
    ["wh2_main_def_bleak_holds", False, True],
    ["wh2_main_def_blood_hall_coven", False, True],
    ["wh2_main_def_clar_karond", False, True],
    ["wh2_main_def_cult_of_excess", False, True],
    ["wh2_main_def_deadwood_sentinels", False, True],
    ["wh2_main_def_ghrond", False, True],
    ["wh2_main_def_karond_kar", False, True],
    ["wh2_main_def_scourge_of_khaine", False, True],
    ["wh2_main_def_ssildra_tor", False, True],
    ["wh2_main_def_drackla_coven", False, True],
    ["wh2_main_def_the_forgebound", False, True],
    ["wh3_main_skv_clan_carrion", False, True],
    ["wh2_dlc16_skv_clan_gritus", False, True],
    ["wh2_dlc15_skv_clan_kreepus", False, True],
    ["wh3_main_skv_clan_krizzor", False, True],
    ["wh2_dlc12_skv_clan_mange", False, True],
    ["wh3_main_skv_clan_morbidus", False, True],
    ["wh2_main_skv_clan_mordkin", False, True],
    ["wh2_main_skv_clan_septik", False, True],
    ["wh3_main_skv_clan_skrat", False, True],
    ["wh2_main_skv_clan_spittel", False, True],
    ["wh3_main_skv_clan_verms", False, True],
    ["wh3_main_skv_clan_treecherik", False, True],
    ["wh3_main_tmb_deserters_of_khatep", False, True],
    ["wh2_dlc09_tmb_dune_kingdoms", False, True],
    ["wh2_dlc09_tmb_numas", False, True],
    ["wh2_dlc09_tmb_rakaph_dynasty", False, True],
    ["wh2_dlc09_tmb_the_sentinels", False, True],
    ["wh2_dlc11_cst_vampire_coast_rebels", False, True],
    ["wh3_dlc21_cst_dead_flag_fleet", False, True],
    ["wh_main_emp_averland", False, True],
    ["wh_main_emp_empire_separatists", False, True],
    ["wh_main_emp_hochland", False, True],
    ["wh_main_emp_marienburg", False, True],
    ["wh_main_emp_middenland", False, True],
    ["wh2_main_emp_new_world_colonies", False, True],
    ["wh_main_emp_nordland", False, True],
    ["wh_main_emp_ostermark", False, True],
    ["wh_main_emp_ostland", False, True],
    ["wh_main_emp_stirland", False, True],
    ["wh_main_emp_talabecland", False, True],
    ["wh_main_dwf_barak_varr", False, True],
    ["wh2_dlc15_dwf_clan_helhein", False, True],
    ["wh2_main_dwf_greybeards_prospectors", False, True],
    ["wh3_main_dwf_karak_azorn", False, True],
    ["wh_main_dwf_karak_azul", False, True],
    ["wh_main_dwf_karak_hirn", False, True],
    ["wh_main_dwf_karak_norn", False, True],
    ["wh_main_dwf_karak_ziflin", False, True],
    ["wh2_main_dwf_spine_of_sotek_dwarfs", False, True],
    ["wh_main_dwf_zhufbar", False, True],
    ["wh2_main_grn_arachnos", False, True],
    ["wh_main_grn_black_venom", False, True],
    ["wh_main_grn_bloody_spearz", False, True],
    ["wh2_main_grn_blue_vipers", False, True],
    ["wh2_dlc16_grn_naggaroth_orcs", False, True],
    ["wh_main_grn_broken_nose", False, True],
    ["wh2_dlc16_grn_creeping_death", False, True],
    ["wh3_dlc26_grn_cluster_eye_tribe", False, True],
    ["wh_main_grn_necksnappers", False, True],
    ["wh3_main_grn_da_cage_breakaz", False, True],
    ["wh3_main_grn_dark_land_orcs", False, True],
    ["wh3_main_grn_dimned_sun", False, True],
    ["wh3_main_grn_drippin_fangs", False, True],
    ["wh2_dlc12_grn_leaf_cutterz_tribe", False, True],
    ["wh3_main_grn_moon_howlerz", False, True],
    ["wh_main_grn_red_eye", False, True],
    ["wh2_dlc14_grn_red_cloud", False, True],
    ["wh_main_grn_red_fangs", False, True],
    ["wh_main_grn_scabby_eye", False, True],
    ["wh_main_grn_skull-takerz", False, False],
    ["wh2_dlc15_grn_skull_crag", False, True],
    ["wh_main_grn_skullsmasherz", False, True],
    ["wh3_main_grn_slaves_of_zharr", False, True],
    ["wh_main_grn_teef_snatchaz", False, True],
    ["wh_dlc03_grn_black_pit", False, True],
    ["wh_main_grn_top_knotz", False, True],
    ["wh3_main_grn_tusked_sunz", False, True],
    ["wh3_dlc21_vmp_jiangshi_rebels", False, True],
    ["wh3_main_vmp_lahmian_sisterhood", False, True],
    ["wh_main_vmp_mousillon", False, True],
    ["wh2_main_vmp_necrarch_brotherhood", False, True],
    ["wh3_main_ie_vmp_sires_of_mourkain", False, True],
    ["wh2_main_vmp_strygos_empire", False, True],
    ["wh_main_vmp_rival_sylvanian_vamps", False, True],
    ["wh2_main_vmp_the_silver_host", False, True],
    ["wh3_dlc25_vmp_the_court_of_night", False, True],
    ["wh3_main_chs_khazag", False, True],
    ["wh_main_teb_border_princes", False, True],
    ["wh_main_teb_estalia", False, True],
    ["wh_main_teb_tilea", False, True],
    ["wh_dlc03_bst_jagged_horn", False, False],
    ["wh2_main_bst_manblight", False, False],
    ["wh_dlc03_bst_redhorn", False, False],
    ["wh2_main_bst_ripper_horn", False, False],
    ["wh2_main_bst_shadowgor", False, False],
    ["wh2_main_wef_bowmen_of_oreon", False, True],
    ["wh3_main_wef_laurelorn", False, True],
    ["wh3_dlc21_wef_spirits_of_shanlin", False, True],
    ["wh_dlc05_wef_torgovann", False, True],
    ["wh_dlc05_wef_wydrioth", False, True],
    ["wh_main_brt_artois", False, True],
    ["wh_main_brt_bastonne", False, True],
    ["wh3_main_brt_aquitaine", False, True],
    ["wh2_main_brt_knights_of_origo", False, True],
    ["wh2_main_brt_knights_of_the_flame", False, True],
    ["wh_main_brt_lyonesse", False, True],
    ["wh_main_brt_parravon", False, True],
    ["wh2_main_brt_thegans_crusaders", False, True],
    ["wh_main_nor_aesling", False, True],
    ["wh2_main_nor_aghol", False, True],
    ["wh3_dlc23_chd_minor_faction", False, True],
    ["wh3_dlc23_chd_conclave", False, True],
    ["wh_main_nor_baersonling", False, True],
    ["wh_main_nor_bjornling", False, True],
    ["wh3_dlc20_nor_dolgan", False, True],
    ["wh_dlc08_nor_goromadny_tribe", False, True],
    ["wh3_dlc20_nor_kul", False, True],
    ["wh2_main_nor_mung", False, True],
    ["wh_dlc08_nor_naglfarlings", False, True],
    ["wh_main_nor_sarl", False, True],
    ["wh_main_nor_skaeling", False, True],
    ["wh2_main_nor_skeggi", False, True],
    ["wh_dlc08_nor_vanaheimlings", False, True],
    ["wh_main_nor_varg", False, True],
    ["wh3_dlc21_nor_wyrmkins", False, True],
    ["wh3_dlc20_nor_yusak", False, True],
    ["wh2_dlc11_cst_rogue_bleak_coast_buccaneers", False, False],
    ["wh2_dlc11_cst_rogue_boyz_of_the_forbidden_coast", False, False],
    ["wh2_dlc11_cst_rogue_freebooters_of_port_royale", False, False],
    ["wh2_dlc11_cst_rogue_grey_point_scuttlers", False, False],
    ["wh2_dlc11_cst_rogue_terrors_of_the_dark_straights", False, False],
    ["wh2_dlc11_cst_rogue_the_churning_gulf_raiders", False, False],
    ["wh2_dlc11_cst_rogue_tyrants_of_the_black_ocean", False, False],
    ["wh3_dlc27_hef_aislinn", True, False],
    ["wh3_dlc27_nor_sayl", True, True],
    ["wh3_dlc27_sla_the_tormentors", True, False],
    ["wh3_dlc27_sla_masque_of_slaanesh", True, True],
    ["wh3_dlc27_nor_avags", False, True]
]

woodelve_table = [
    ["wh_dlc05_wef_wood_elves", True, True],
    ["wh_dlc05_wef_argwylon", True, True],
    ["wh2_dlc16_wef_sisters_of_twilight", True, True],
    ["wh2_dlc16_wef_drycha", True, True],
    ["wh2_main_wef_bowmen_of_oreon", False, True],
    ["wh3_main_wef_laurelorn", False, True],
    ["wh3_dlc21_wef_spirits_of_shanlin", False, True],
    ["wh_dlc05_wef_torgovann", False, True],
    ["wh_dlc05_wef_wydrioth", False, True]
]

# settlement table with columns settlement_key, x_coord, y_coord
settlement_table = [
    ["wh3_main_combi_region_zlatlan", 610, 123],
    ["wh3_main_combi_region_floating_village", 683, 372],
    ["wh3_main_combi_region_shrine_of_khaine", 258, 663],
    ["wh3_main_combi_region_mordheim", 675, 661],
    ["wh3_main_combi_region_zoishenk", 645, 794],
    ["wh3_main_combi_region_black_pyramid_of_nagash", 579, 283],
    ["wh3_main_combi_region_hanyu_port", 1127, 494],
    ["wh3_main_combi_region_tor_yvresse", 316, 574],
    ["wh3_main_combi_region_aquitaine", 421, 569],
    ["wh3_main_combi_region_the_monolith_of_katam", 451, 864],
    ["wh3_main_combi_region_helmgart", 487, 603],
    ["wh3_main_combi_region_beichai", 1356, 554],
    ["wh3_main_combi_region_lashiek", 448, 315],
    ["wh3_main_combi_region_steingart", 620, 565],
    ["wh3_main_combi_region_floating_mountain", 1025, 790],
    ["wh3_main_combi_region_shrine_of_ladrielle", 224, 777],
    ["wh3_main_combi_region_quatar", 678, 277],
    ["wh3_main_combi_region_ancient_city_of_quintex", 73, 592],
    ["wh3_main_combi_region_southern_outpost", 1280, 328],
    ["wh3_main_combi_region_black_iron_mine", 797, 481],
    ["wh3_main_combi_region_vulture_mountain", 454, 289],
    ["wh3_main_combi_region_dragons_crossroad", 1221, 684],
    ["wh3_main_combi_region_niedling", 653, 640],
    ["wh3_main_combi_region_bleak_hold_fortress", 89, 618],
    ["wh3_main_combi_region_dargoth", 249, 858],
    ["wh3_main_combi_region_nagenhof", 717, 682],
    ["wh3_main_combi_region_the_copper_landing", 113, 172],
    ["wh3_main_combi_region_tor_surpindar", 612, 77],
    ["wh3_main_combi_region_pools_of_despair", 523, 304],
    ["wh3_main_combi_region_karak_angazhar", 629, 531],
    ["wh3_main_combi_region_the_black_pillar", 214, 849],
    ["wh3_main_combi_region_temple_avenue_of_gold", 718, 120],
    ["wh3_main_combi_region_massif_orcal", 458, 567],
    ["wh3_main_combi_region_white_tower_of_hoeth", 295, 562],
    ["wh3_main_combi_region_winter_pyre", 678, 866],
    ["wh3_main_combi_region_swamp_town", 91, 459],
    ["wh3_main_combi_region_kemperbad", 565, 637],
    ["wh3_main_combi_region_shrine_of_loec", 311, 511],
    ["wh3_main_combi_region_karak_eight_peaks", 761, 459],
    ["wh3_main_combi_region_the_palace_of_ruin", 230, 904],
    ["wh3_main_combi_region_barag_dawazbag", 709, 509],
    ["wh3_main_combi_region_nahuontl", 562, 146],
    ["wh3_main_combi_region_deff_gorge", 717, 354],
    ["wh3_main_combi_region_wei_jin", 1276, 649],
    ["wh3_main_combi_region_griffon_gate", 196, 594],
    ["wh3_main_combi_region_shattered_cove", 999, 417],
    ["wh3_main_combi_region_wurtbad", 607, 634],
    ["wh3_main_combi_region_shard_bastion", 314, 900],
    ["wh3_main_combi_region_isle_of_wights", 351, 723],
    ["wh3_main_combi_region_ghrond", 157, 841],
    ["wh3_main_combi_region_skavenblight", 465, 461],
    ["wh3_main_combi_region_caverns_of_sotek", 673, 106],
    ["wh3_main_combi_region_oakenhammer", 715, 590],
    ["wh3_main_combi_region_tor_dranil", 198, 627],
    ["wh3_main_combi_region_the_black_forests", 207, 725],
    ["wh3_main_combi_region_stormvrack_mount", 809, 828],
    ["wh3_main_combi_region_terracotta_graveyard", 1200, 631],
    ["wh3_main_combi_region_the_awakening", 276, 262],
    ["wh3_main_combi_region_palace_of_princes", 404, 893],
    ["wh3_main_combi_region_xahutec", 204, 307],
    ["wh3_main_combi_region_the_writhing_fortress", 915, 887],
    ["wh3_main_combi_region_elisia", 299, 640],
    ["wh3_main_combi_region_mount_silverspear", 831, 541],
    ["wh3_main_combi_region_wellsprings_of_eternity", 71, 357],
    ["wh3_main_combi_region_tower_of_gorgoth", 904, 527],
    ["wh3_main_combi_region_sarl_encampment", 586, 846],
    ["wh3_main_combi_region_fort_jakova", 740, 702],
    ["wh3_main_combi_region_miragliano", 497, 456],
    ["wh3_main_combi_region_nuja", 381, 426],
    ["wh3_main_combi_region_longship_graveyard", 543, 789],
    ["wh3_main_combi_region_macu_peaks", 53, 457],
    ["wh3_main_combi_region_norden", 594, 770],
    ["wh3_main_combi_region_altar_of_spawns", 650, 871],
    ["wh3_main_combi_region_tribeslaughter", 847, 782],
    ["wh3_main_combi_region_sump_pit", 806, 433],
    ["wh3_main_combi_region_grenzstadt", 648, 573],
    ["wh3_main_combi_region_the_dust_gate", 140, 156],
    ["wh3_main_combi_region_kappelburg", 653, 708],
    ["wh3_main_combi_region_nan_gau", 1138, 656],
    ["wh3_main_combi_region_numas", 651, 297],
    ["wh3_main_combi_region_lyonesse", 362, 631],
    ["wh3_main_combi_region_lybaras", 825, 317],
    ["wh3_main_combi_region_the_bleeding_spire", 923, 837],
    ["wh3_main_combi_region_copher", 473, 341],
    ["wh3_main_combi_region_nagashizzar", 848, 405],
    ["wh3_main_combi_region_sunken_khernarch", 647, 362],
    ["wh3_main_combi_region_mangrove_coast", 263, 137],
    ["wh3_main_combi_region_grimtop", 1050, 489],
    ["wh3_main_combi_region_the_moon_shard", 134, 567],
    ["wh3_main_combi_region_flayed_rock", 992, 471],
    ["wh3_main_combi_region_eldar_spire", 15, 815],
    ["wh3_main_combi_region_city_of_the_shugengan", 1295, 614],
    ["wh3_main_combi_region_laurelorn_forest", 527, 730],
    ["wh3_main_combi_region_monument_of_izzatal", 105, 352],
    ["wh3_main_combi_region_karaz_a_karak", 736, 549],
    ["wh3_main_combi_region_dread_rock", 972, 399],
    ["wh3_main_combi_region_village_of_the_moon", 1251, 551],
    ["wh3_main_combi_region_fu_hung", 1230, 376],
    ["wh3_main_combi_region_great_desert_of_araby", 487, 267],
    ["wh3_main_combi_region_tlaqua", 544, 203],
    ["wh3_main_combi_region_skrap_towers", 1014, 449],
    ["wh3_main_combi_region_fort_oberstyre", 668, 621],
    ["wh3_main_combi_region_troll_fjord", 386, 795],
    ["wh3_main_combi_region_rackdo_gorge", 55, 812],
    ["wh3_main_combi_region_zandri", 541, 325],
    ["wh3_main_combi_region_zanbaijin", 1002, 838],
    ["wh3_main_combi_region_kunlan", 1251, 587],
    ["wh3_main_combi_region_monolith_of_borkill_the_bloody_handed", 450, 801],
    ["wh3_main_combi_region_venom_glade", 142, 709],
    ["wh3_main_combi_region_xhotl", 133, 238],
    ["wh3_main_combi_region_lost_plateau", 704, 243],
    ["wh3_main_combi_region_elessaeli", 317, 532],
    ["wh3_main_combi_region_spitepeak", 789, 417],
    ["wh3_main_combi_region_the_gallows_tree", 975, 819],
    ["wh3_main_combi_region_castle_carcassonne", 465, 503],
    ["wh3_main_combi_region_shrine_of_sotek", 47, 427],
    ["wh3_main_combi_region_tower_of_the_sun", 981, 133],
    ["wh3_main_combi_region_fateweavers_crevasse", 510, 27],
    ["wh3_main_combi_region_the_godless_crater", 235, 22],
    ["wh3_main_combi_region_stonemine_tower", 626, 482],
    ["wh3_main_combi_region_zavastra", 674, 736],
    ["wh3_main_combi_region_rothkar_spire", 13, 733],
    ["wh3_main_combi_region_the_daemons_stump", 969, 546],
    ["wh3_main_combi_region_xen_wu", 1123, 525],
    ["wh3_main_combi_region_shagrath", 319, 853],
    ["wh3_main_combi_region_clarak_spire", 16, 650],
    ["wh3_main_combi_region_martek", 489, 317],
    ["wh3_main_combi_region_ka_sabar", 642, 247],
    ["wh3_main_combi_region_gateway_to_khuresh", 1257, 349],
    ["wh3_main_combi_region_cairn_thel", 285, 517],
    ["wh3_main_combi_region_the_folly_of_malofex", 470, 908],
    ["wh3_main_combi_region_karond_kar", 277, 797],
    ["wh3_main_combi_region_dok_karaz", 668, 497],
    ["wh3_main_combi_region_argalis", 538, 417],
    ["wh3_main_combi_region_storag_kor", 72, 727],
    ["wh3_main_combi_region_middenheim", 554, 706],
    ["wh3_main_combi_region_languille", 384, 661],
    ["wh3_main_combi_region_karak_azorn", 996, 567],
    ["wh3_main_combi_region_black_tower_of_arkhan", 550, 294],
    ["wh3_main_combi_region_pillar_of_skulls", 876, 802],
    ["wh3_main_combi_region_desolation_of_nagash", 819, 411],
    ["wh3_main_combi_region_blackstone_post", 457, 623],
    ["wh3_main_combi_region_the_fortress_of_vorag", 889, 438],
    ["wh3_main_combi_region_gor_gazan", 589, 333],
    ["wh3_main_combi_region_pillars_of_unseen_constellations", 59, 332],
    ["wh3_main_combi_region_marks_of_the_old_ones", 225, 184],
    ["wh3_main_combi_region_karak_hirn", 590, 536],
    ["wh3_main_combi_region_karak_raziak", 759, 669],
    ["wh3_main_combi_region_zhufbar", 737, 595],
    ["wh3_main_combi_region_karak_izor", 559, 505],
    ["wh3_main_combi_region_tai_tzu", 1175, 554],
    ["wh3_main_combi_region_wolfenburg", 624, 727],
    ["wh3_main_combi_region_weng_chang", 1172, 609],
    ["wh3_main_combi_region_hergig", 601, 702],
    ["wh3_main_combi_region_fallen_gates", 44, 510],
    ["wh3_main_combi_region_tobaro", 467, 443],
    ["wh3_main_combi_region_qiang", 1112, 468],
    ["wh3_main_combi_region_cuexotl", 640, 169],
    ["wh3_main_combi_region_great_skull_lakes", 853, 692],
    ["wh3_main_combi_region_swartzhafen", 674, 593],
    ["wh3_main_combi_region_eye_of_the_panther", 481, 307],
    ["wh3_main_combi_region_fortress_of_the_damned", 375, 870],
    ["wh3_main_combi_region_yuatek", 602, 101],
    ["wh3_main_combi_region_the_blood_swamps", 239, 235],
    ["wh3_main_combi_region_red_fortress", 1317, 663],
    ["wh3_main_combi_region_desolation_of_drakenmoor", 833, 611],
    ["wh3_main_combi_region_tor_finu", 299, 585],
    ["wh3_main_combi_region_grimhold", 546, 530],
    ["wh3_main_combi_region_the_galleons_graveyard", 257, 448],
    ["wh3_main_combi_region_sartosa", 492, 390],
    ["wh3_main_combi_region_hag_hall", 106, 644],
    ["wh3_main_combi_region_montfort", 474, 593],
    ["wh3_main_combi_region_essen", 693, 662],
    ["wh3_main_combi_region_fort_soll", 582, 542],
    ["wh3_main_combi_region_bechafen", 677, 716],
    ["wh3_main_combi_region_krugenheim", 634, 654],
    ["wh3_main_combi_region_mahrak", 772, 320],
    ["wh3_main_combi_region_daemons_gate", 463, 57],
    ["wh3_main_combi_region_mine_of_the_bearded_skulls", 120, 217],
    ["wh3_main_combi_region_tor_koruali", 331, 606],
    ["wh3_main_combi_region_hell_pit", 705, 807],
    ["wh3_main_combi_region_mighdal_vongalbarak", 650, 554],
    ["wh3_main_combi_region_fortress_of_eyes", 1163, 704],
    ["wh3_main_combi_region_mousillon", 382, 605],
    ["wh3_main_combi_region_mistnar", 331, 634],
    ["wh3_main_combi_region_the_burning_monolith", 848, 896],
    ["wh3_main_combi_region_soteks_trail", 710, 163],
    ["wh3_main_combi_region_temple_of_elemental_winds", 1156, 441],
    ["wh3_main_combi_region_kraka_drak", 709, 841],
    ["wh3_main_combi_region_tor_elasor", 911, 78],
    ["wh3_main_combi_region_tor_elyr", 206, 558],
    ["wh3_main_combi_region_karak_vlag", 817, 756],
    ["wh3_main_combi_region_karak_vrag", 1010, 656],
    ["wh3_main_combi_region_the_cursed_jungle", 744, 215],
    ["wh3_main_combi_region_karag_dromar", 675, 562],
    ["wh3_main_combi_region_erengrad", 634, 770],
    ["wh3_main_combi_region_frozen_landing", 761, 820],
    ["wh3_main_combi_region_fort_straghov", 670, 806],
    ["wh3_main_combi_region_monolith_of_festerlung", 820, 868],
    ["wh3_main_combi_region_clar_karond", 117, 726],
    ["wh3_main_combi_region_agrul_migdhal", 653, 331],
    ["wh3_main_combi_region_the_falls_of_doom", 910, 652],
    ["wh3_main_combi_region_castle_artois", 410, 639],
    ["wh3_main_combi_region_tower_of_the_stars", 936, 173],
    ["wh3_main_combi_region_chupayotl", 251, 163],
    ["wh3_main_combi_region_karak_azul", 799, 452],
    ["wh3_main_combi_region_brionne", 420, 527],
    ["wh3_main_combi_region_wizard_caliphs_palace", 437, 269],
    ["wh3_main_combi_region_the_frozen_city", 284, 872],
    ["wh3_main_combi_region_ruins_end", 947, 427],
    ["wh3_main_combi_region_the_high_sentinel", 120, 404],
    ["wh3_main_combi_region_black_creek_spire", 269, 768],
    ["wh3_main_combi_region_shattered_stone_isle", 999, 384],
    ["wh3_main_combi_region_khemri", 612, 289],
    ["wh3_main_combi_region_karak_zorn", 682, 221],
    ["wh3_main_combi_region_the_black_pit", 510, 705],
    ["wh3_main_combi_region_the_pillars_of_grungni", 762, 547],
    ["wh3_main_combi_region_temple_of_addaioth", 76, 689],
    ["wh3_main_combi_region_shrine_of_kurnous", 267, 642],
    ["wh3_main_combi_region_deaths_head_monoliths", 497, 200],
    ["wh3_main_combi_region_kauark", 202, 872],
    ["wh3_main_combi_region_howling_rock", 869, 592],
    ["wh3_main_combi_region_darkhold", 899, 478],
    ["wh3_main_combi_region_tlax", 259, 289],
    ["wh3_main_combi_region_zhanshi", 1275, 519],
    ["wh3_main_combi_region_temple_of_khaine", 89, 788],
    ["wh3_main_combi_region_the_star_tower", 280, 214],
    ["wh3_main_combi_region_hualotal", 99, 309],
    ["wh3_main_combi_region_karak_norn", 534, 571],
    ["wh3_main_combi_region_the_lost_palace", 570, 19],
    ["wh3_main_combi_region_whitefire_tor", 219, 582],
    ["wh3_main_combi_region_gristle_valley", 561, 548],
    ["wh3_main_combi_region_riffraffa", 519, 435],
    ["wh3_main_combi_region_shrine_of_the_alchemist", 1124, 599],
    ["wh3_dlc20_combi_region_glacier_encampment", 79, 903],
    ["wh3_main_combi_region_crucible_of_delights", 772, 16],
    ["wh3_main_combi_region_phoenix_gate", 245, 619],
    ["wh3_main_combi_region_vale_of_titans", 1060, 560],
    ["wh3_main_combi_region_igerov", 751, 729],
    ["wh3_main_combi_region_blood_mountain", 420, 923],
    ["wh3_main_combi_region_the_blood_hall", 26, 332],
    ["wh3_main_combi_region_volcanos_heart", 697, 941],
    ["wh3_main_combi_region_altar_of_the_crimson_harvest", 503, 783],
    ["wh3_main_combi_region_salzenmund", 557, 757],
    ["wh3_main_combi_region_sjoktraken", 726, 828],
    ["wh3_main_combi_region_dringorackaz", 756, 416],
    ["wh3_main_combi_region_granite_massif", 755, 306],
    ["wh3_main_combi_region_chimai", 1313, 521],
    ["wh3_main_combi_region_okkams_forever_maze", 709, 28],
    ["wh3_main_combi_region_sorcerers_islands", 420, 309],
    ["wh3_main_combi_region_the_southern_sentinels", 224, 133],
    ["wh3_main_combi_region_chamber_of_visions", 71, 273],
    ["wh3_main_combi_region_the_oak_of_ages", 513, 531],
    ["wh3_main_combi_region_grey_rock_point", 106, 543],
    ["wh3_main_combi_region_vauls_anvil_naggaroth", 126, 670],
    ["wh3_main_combi_region_the_never_ending_chasm", 281, 18],
    ["wh3_main_combi_region_waterfall_palace", 515, 566],
    ["wh3_main_combi_region_fort_bergbres", 449, 636],
    ["wh3_dlc20_combi_region_glacial_gardens", 173, 892],
    ["wh3_main_combi_region_serpent_jetty", 416, 848],
    ["wh3_main_combi_region_chill_road", 130, 833],
    ["wh3_dlc20_combi_region_dragons_death", 1035, 756],
    ["wh3_main_combi_region_graeling_moot", 479, 829],
    ["wh3_main_combi_region_li_zhu", 1367, 470],
    ["wh3_main_combi_region_snake_gate", 1175, 665],
    ["wh3_main_combi_region_port_elistor", 284, 541],
    ["wh3_main_combi_region_eilhart", 482, 639],
    ["wh3_main_combi_region_black_rock", 583, 938],
    ["wh3_main_combi_region_grom_peak", 768, 589],
    ["wh3_main_combi_region_valley_of_horns", 1000, 523],
    ["wh3_main_combi_region_celestial_monastery", 1234, 533],
    ["wh3_main_combi_region_zvorak", 581, 490],
    ["wh3_main_combi_region_dragon_gate", 1209, 666],
    ["wh3_main_combi_region_xlanhuapec", 215, 264],
    ["wh3_main_combi_region_slavers_point", 238, 753],
    ["wh3_main_combi_region_kislev", 719, 736],
    ["wh3_main_combi_region_flensburg", 587, 618],
    ["wh3_main_combi_region_dragonhorn_mines", 647, 424],
    ["wh3_main_combi_region_vauls_anvil_loren", 502, 551],
    ["wh3_main_combi_region_varenka_hills", 702, 529],
    ["wh3_main_combi_region_jade_wind_mountain", 1284, 558],
    ["wh3_main_combi_region_karak_kadrin", 748, 644],
    ["wh3_main_combi_region_granite_spikes", 1076, 703],
    ["wh3_main_combi_region_xlanzec", 241, 109],
    ["wh3_main_combi_region_bloodwind_keep", 1244, 719],
    ["wh3_main_combi_region_dotternbach", 546, 583],
    ["wh3_main_combi_region_dietershafen", 526, 762],
    ["wh3_main_combi_region_nuln", 553, 607],
    ["wh3_main_combi_region_karak_krakaten", 1003, 491],
    ["wh3_main_combi_region_mountain_pass", 1322, 335],
    ["wh3_main_combi_region_citadel_of_lead", 355, 763],
    ["wh3_main_combi_region_gnobbly_gorge", 1072, 436],
    ["wh3_main_combi_region_bitterstone_mine", 660, 451],
    ["wh3_main_combi_region_quetza", 186, 219],
    ["wh3_main_combi_region_haichai", 1352, 622],
    ["wh3_main_combi_region_oyxl", 183, 187],
    ["wh3_main_combi_region_avethir", 187, 546],
    ["wh3_main_combi_region_akendorf", 678, 540],
    ["wh3_main_combi_region_khymerica_spire", 29, 705],
    ["wh3_dlc23_combi_region_gash_kadrak", 943, 601],
    ["wh3_main_combi_region_castle_alexandronov", 613, 792],
    ["wh3_main_combi_region_eagle_gate", 189, 572],
    ["wh3_main_combi_region_spite_reach", 190, 845],
    ["wh3_main_combi_region_zharr_naggrund", 943, 628],
    ["wh3_main_combi_region_eschen", 714, 635],
    ["wh3_main_combi_region_montenas", 414, 454],
    ["wh3_main_combi_region_al_haikk", 511, 332],
    ["wh3_main_combi_region_drackla_spire", 21, 781],
    ["wh3_main_combi_region_turtle_gate", 1246, 665],
    ["wh3_dlc20_combi_region_krudenwald", 574, 716],
    ["wh3_main_combi_region_tor_achare", 295, 619],
    ["wh3_main_combi_region_quittax", 142, 301],
    ["wh3_dlc23_combi_region_uzkulak_port", 859, 740],
    ["wh3_main_combi_region_karak_ungor", 772, 694],
    ["wh3_main_combi_region_bitter_bay", 884, 404],
    ["wh3_main_combi_region_altdorf", 527, 648],
    ["wh3_main_combi_region_altar_of_facades", 826, 30],
    ["wh3_main_combi_region_the_sacred_pools", 153, 261],
    ["wh3_main_combi_region_the_skull_carvers_abode", 664, 12],
    ["wh3_main_combi_region_the_haunted_forest", 1066, 418],
    ["wh3_main_combi_region_temple_of_skulls", 771, 248],
    ["wh3_main_combi_region_dusk_peaks", 281, 105],
    ["wh3_main_combi_region_yetchitch", 742, 798],
    ["wh3_main_combi_region_itza", 168, 239],
    ["wh3_main_combi_region_grung_zint", 434, 650],
    ["wh3_main_combi_region_bhagar", 598, 246],
    ["wh3_main_combi_region_crag_halls_of_findol", 528, 544],
    ["wh3_main_combi_region_el_kalabad", 532, 273],
    ["wh3_main_combi_region_thrice_cursed_peak", 151, 172],
    ["wh3_main_combi_region_cragroth_deep", 103, 766],
    ["wh3_main_combi_region_citadel_of_dusk", 302, 89],
    ["wh3_main_combi_region_crookback_mountain", 844, 520],
    ["wh3_main_combi_region_volksgrad", 749, 778],
    ["wh3_main_combi_region_hoteks_column", 173, 718],
    ["wh3_main_combi_region_the_crystal_spires", 749, 926],
    ["wh3_main_combi_region_ming_zhu", 1242, 612],
    ["wh3_main_combi_region_parravon", 483, 575],
    ["wh3_main_combi_region_barak_varr", 672, 512],
    ["wh3_main_combi_region_gaean_vale", 256, 579],
    ["wh3_main_combi_region_fuming_serpent", 286, 232],
    ["wh3_main_combi_region_village_of_the_tigermen", 1189, 414],
    ["wh3_main_combi_region_castle_bastonne", 428, 602],
    ["wh3_main_combi_region_amblepeak", 1027, 546],
    ["wh3_main_combi_region_har_kaldra", 81, 847],
    ["wh3_main_combi_region_gisoreux", 438, 627],
    ["wh3_main_combi_region_li_temple", 1339, 449],
    ["wh3_main_combi_region_foundry_of_bones", 1295, 697],
    ["wh3_main_combi_region_black_fang", 976, 639],
    ["wh3_main_combi_region_aarnau", 459, 724],
    ["wh3_main_combi_region_eagle_eyries", 962, 665],
    ["wh3_main_combi_region_gryphon_wood", 669, 682],
    ["wh3_main_combi_region_carroburg", 509, 656],
    ["wh3_main_combi_region_xing_po", 1200, 571],
    ["wh3_main_combi_region_praag", 723, 770],
    ["wh3_main_combi_region_tower_of_lysean", 228, 526],
    ["wh3_main_combi_region_naggarond", 112, 813],
    ["wh3_main_combi_region_great_hall_of_greasus", 1030, 503],
    ["wh3_main_combi_region_the_blighted_grove", 560, 953],
    ["wh3_main_combi_region_talabheim", 604, 690],
    ["wh3_main_combi_region_rasetra", 766, 287],
    ["wh3_main_combi_region_the_twisted_towers", 485, 939],
    ["wh3_main_combi_region_the_bone_gulch", 841, 423],
    ["wh3_main_combi_region_tlaxtlan", 164, 324],
    ["wh3_main_combi_region_the_sentinel_of_time", 190, 152],
    ["wh3_main_combi_region_ubersreik", 505, 614],
    ["wh3_main_combi_region_fort_ostrosk", 680, 786],
    ["wh3_main_combi_region_plain_of_tuskers", 560, 229],
    ["wh3_main_combi_region_volulltrax", 630, 24],
    ["wh3_main_combi_region_gronti_mingol", 585, 413],
    ["wh3_main_combi_region_yhetee_peak", 1071, 619],
    ["wh3_main_combi_region_bay_of_blades", 582, 814],
    ["wh3_main_combi_region_unicorn_gate", 216, 611],
    ["wh3_main_combi_region_ironspike", 43, 547],
    ["wh3_main_combi_region_teotiqua", 740, 187],
    ["wh3_main_combi_region_shang_wu", 1164, 479],
    ["wh3_main_combi_region_plain_of_spiders", 40, 677],
    ["wh3_main_combi_region_bloodpeak", 1043, 600],
    ["wh3_main_combi_region_weismund", 529, 681],
    ["wh3_main_combi_region_gnashraks_lair", 792, 643],
    ["wh3_main_combi_region_evershale", 240, 595],
    ["wh3_main_combi_region_scarpels_lair", 15, 600],
    ["wh3_main_combi_region_shroktak_mount", 57, 768],
    ["wh3_main_combi_region_ssildra_tor", 64, 535],
    ["wh3_main_combi_region_naglfari_plain", 552, 838],
    ["wh3_main_combi_region_tor_saroir", 270, 601],
    ["wh3_main_combi_region_dai_cheng", 1371, 381],
    ["wh3_main_combi_region_ice_rock_gorge", 74, 645],
    ["wh3_main_combi_region_bridge_of_heaven", 1231, 497],
    ["wh3_main_combi_region_marienburg", 452, 657],
    ["wh3_main_combi_region_ash_ridge_mountains", 862, 459],
    ["wh3_main_combi_region_quenelles", 481, 540],
    ["wh3_main_combi_region_axlotl", 207, 231],
    ["wh3_main_combi_region_plesk", 765, 754],
    ["wh3_main_combi_region_the_witchwood", 66, 660],
    ["wh3_main_combi_region_jungles_of_chian", 1303, 386],
    ["wh3_main_combi_region_golden_ziggurat", 37, 282],
    ["wh3_main_combi_region_skeggi", 126, 513],
    ["wh3_main_combi_region_the_moot", 648, 601],
    ["wh3_main_combi_region_har_ganeth", 212, 827],
    ["wh3_main_combi_region_karag_orrud", 720, 309],
    ["wh3_main_combi_region_mount_athull", 299, 36],
    ["wh3_main_combi_region_worlds_edge_archway", 819, 563],
    ["wh3_main_combi_region_black_fortress", 950, 479],
    ["wh3_main_combi_region_port_reaver", 98, 481],
    ["wh3_main_combi_region_chaqua", 174, 273],
    ["wh3_main_combi_region_vitevo", 709, 711],
    ["wh3_main_combi_region_morgheim", 685, 409],
    ["wh3_main_combi_region_kradtommen", 747, 392],
    ["wh3_main_combi_region_ekrund", 634, 444],
    ["wh3_main_combi_region_khazid_bordkarag", 687, 823],
    ["wh3_main_combi_region_shang_yang", 1127, 554],
    ["wh3_main_combi_region_blacklight_tower", 210, 793],
    ["wh3_main_combi_region_the_howling_citadel", 790, 913],
    ["wh3_main_combi_region_monolith_of_bubonicus", 853, 848],
    ["wh3_main_combi_region_statues_of_the_gods", 545, 175],
    ["wh3_main_combi_region_infernius", 430, 946],
    ["wh3_main_combi_region_subatuun", 146, 201],
    ["wh3_main_combi_region_novchozy", 782, 768],
    ["wh3_main_combi_region_gorssel", 460, 681],
    ["wh3_main_combi_region_po_mei", 1228, 649],
    ["wh3_main_combi_region_pahuax", 92, 430],
    ["wh3_main_combi_region_karak_azgaraz", 505, 592],
    ["wh3_main_combi_region_vauls_anvil_ulthuan", 204, 511],
    ["wh3_main_combi_region_the_gates_of_zharr", 916, 564],
    ["wh3_main_combi_region_ziggurat_of_dawn", 92, 517],
    ["wh3_main_combi_region_karak_bhufdar", 529, 499],
    ["wh3_main_combi_region_nonchang", 1271, 493],
    ["wh3_main_combi_region_wissenburg", 577, 586],
    ["wh3_main_combi_region_fortress_of_dawn", 545, 68],
    ["wh3_main_combi_region_fyrus", 495, 350],
    ["wh3_main_combi_region_the_volary", 1111, 716],
    ["wh3_main_combi_region_altar_of_the_horned_rat", 245, 206],
    ["wh3_main_combi_region_cliff_of_beasts", 527, 933],
    ["wh3_main_combi_region_fallen_king_mountain", 788, 627],
    ["wh3_main_combi_region_forest_of_gloom", 703, 549],
    ["wh3_main_combi_region_bilious_cliffs", 608, 922],
    ["wh3_main_combi_region_baleful_hills", 1190, 503],
    ["wh3_main_combi_region_the_silvered_tower_of_sorcerers", 377, 937],
    ["wh3_main_combi_region_silver_pinnacle", 824, 660],
    ["wh3_main_combi_region_konquata", 345, 745],
    ["wh3_main_combi_region_castle_drakenhof", 716, 612],
    ["wh3_main_combi_region_hidden_landing", 1373, 325],
    ["wh3_main_combi_region_sabre_mountain", 935, 700],
    ["wh3_main_combi_region_bamboo_crossing", 1262, 431],
    ["wh3_main_combi_region_bilbali", 399, 480],
    ["wh3_main_combi_region_pox_marsh", 298, 283],
    ["wh3_main_combi_region_floating_pyramid", 104, 394],
    ["wh3_main_combi_region_forest_of_arnheim", 110, 601],
    ["wh3_main_combi_region_kings_glade", 512, 519],
    ["wh3_main_combi_region_waili_village", 1267, 383],
    ["wh3_main_combi_region_antoch", 604, 219],
    ["wh3_main_combi_region_doom_glade", 809, 282],
    ["wh3_main_combi_region_valayas_sorrow", 737, 446],
    ["wh3_main_combi_region_the_forbidden_citadel", 619, 849],
    ["wh3_main_combi_region_shi_wu", 1365, 417],
    ["wh3_main_combi_region_karak_dum", 887, 764],
    ["wh3_main_combi_region_springs_of_eternal_life", 628, 268],
    ["wh3_main_combi_region_spektazuma", 87, 378],
    ["wh3_main_combi_region_plain_of_dogs", 40, 633],
    ["wh3_main_combi_region_bordeleaux", 393, 580],
    ["wh3_main_combi_region_lothern", 254, 513],
    ["wh3_main_combi_region_tower_of_ashung", 1330, 366],
    ["wh3_main_combi_region_titans_notch", 1047, 635],
    ["wh3_main_combi_region_averheim", 615, 599],
    ["wh3_main_combi_region_temple_of_tlencan", 215, 335],
    ["wh3_main_combi_region_dragon_fang_mount", 970, 350],
    ["wh3_main_combi_region_karak_azgal", 714, 395],
    ["wh3_main_combi_region_tlanxla", 125, 331],
    ["wh3_main_combi_region_lahmia", 798, 347],
    ["wh3_main_combi_region_misty_mountain", 782, 385],
    ["wh3_main_combi_region_tralinia", 344, 562],
    ["wh3_main_combi_region_khazid_irkulaz", 800, 676],
    ["wh3_main_combi_region_sun_tree_glades", 609, 180],
    ["wh3_main_combi_region_hag_graef", 139, 787],
    ["wh3_main_combi_region_arnheim", 147, 588],
    ["wh3_main_combi_region_the_tower_of_khrakk", 632, 821],
    ["wh3_main_combi_region_mount_arachnos", 713, 267],
    ["wh3_main_combi_region_the_sentinels", 947, 510],
    ["wh3_main_combi_region_oreons_camp", 641, 216],
    ["wh3_main_combi_region_tor_anroc", 178, 593],
    ["wh3_main_combi_region_nan_li", 1143, 626],
    ["wh3_main_combi_region_whitepeak", 171, 571],
    ["wh3_main_combi_region_couronne", 410, 675],
    ["wh3_main_combi_region_mount_thug", 1053, 461],
    ["wh3_main_combi_region_the_challenge_stone", 1021, 726],
    ["wh3_main_combi_region_petrified_forest", 77, 557],
    ["wh3_main_combi_region_ashrak", 135, 862],
    ["wh3_main_combi_region_mount_squighorn", 779, 535],
    ["wh3_main_combi_region_monolith_of_flesh", 600, 894],
    ["wh3_main_combi_region_karak_ziflin", 476, 608],
    ["wh3_main_combi_region_dawns_light", 584, 57],
    ["wh3_main_combi_region_myrmidens", 572, 434],
    ["wh3_main_combi_region_kaiax", 191, 118],
    ["wh3_main_combi_region_mount_gunbad", 809, 588],
    ["wh3_main_combi_region_castle_von_rauken", 646, 752],
    ["wh3_main_combi_region_temple_of_heimkel", 788, 791],
    ["wh3_main_combi_region_isle_of_the_crimson_skull", 62, 407],
    ["wh3_main_combi_region_port_of_secrets", 718, 900],
    ["wh3_main_combi_region_galbaraz", 624, 377],
    ["wh3_main_combi_region_the_tower_of_flies", 684, 921],
    ["wh3_main_combi_region_the_forest_of_decay", 640, 939],
    ["wh3_main_combi_region_monument_of_the_moon", 145, 455],
    ["wh3_main_combi_region_magritta", 417, 428],
    ["wh3_main_combi_region_zarakzil", 539, 451],
    ["wh3_main_combi_region_serpent_coast", 795, 219],
    ["wh3_main_combi_region_the_golden_colossus", 86, 211],
    ["wh3_main_combi_region_icespewer", 969, 713],
    ["wh3_main_combi_region_waldenhof", 720, 648],
    ["wh3_main_combi_region_altar_of_ultimate_darkness", 44, 842],
    ["wh3_main_combi_region_stormhenge", 568, 354],
    ["wh3_main_combi_region_tor_anlec", 234, 650],
    ["wh3_main_combi_region_fire_mouth", 1007, 596],
    ["wh3_main_combi_region_blizzardpeak", 1016, 699],
    ["wh3_main_combi_region_iron_rock", 728, 491],
    ["wh3_main_combi_region_pigbarter", 971, 458],
    ["wh3_main_combi_region_the_maw_gate", 1065, 514],
    ["wh3_main_combi_region_temple_of_kara", 152, 366],
    ["wh3_dlc23_combi_region_fort_dorznye_vort", 885, 692],
    ["wh3_main_combi_region_sentinels_of_xeti", 77, 243],
    ["wh3_main_combi_region_verdanos", 557, 451],
    ["wh3_main_combi_region_pfeildorf", 588, 571],
    ["wh3_main_combi_region_matorca", 632, 505],
    ["wh3_main_combi_region_shrine_of_asuryan", 258, 540],
    ["wh3_main_combi_region_iron_storm", 1198, 710],
    ["wh3_main_combi_region_nagrar", 271, 836],
    ["wh3_main_combi_region_hexoatl", 69, 489],
    ["wh3_main_combi_region_the_great_arena", 155, 816],
    ["wh3_main_combi_region_castle_of_splendour", 754, 48],
    ["wh3_main_combi_region_shiyamas_rest", 1269, 460],
    ["wh3_main_combi_region_tor_sethai", 206, 530],
    ["wh3_main_combi_region_grotrilexs_glare_lighthouse", 412, 51],
    ["wh3_main_combi_region_castle_templehof", 686, 628],
    ["wh3_main_combi_region_luccini", 505, 410],
    ["wh3_main_combi_region_grunburg", 548, 623],
    ["wh3_main_combi_region_brass_keep", 592, 737],
    ["wh3_main_combi_region_tyrant_peak", 21, 573],
    ["wh3_main_combi_region_pack_ice_bay", 452, 759],
    ["wh3_main_combi_region_sulpharets", 22, 532],
    ["wh3_dlc23_combi_region_blasted_expanse", 858, 634],
    ["wh3_main_combi_region_angerrial", 269, 529],
    ["wh3_main_combi_region_dagraks_end", 128, 909],
    ["wh3_main_combi_region_mount_grey_hag", 879, 515],
    ["wh3_main_combi_region_wreckers_point", 474, 748],
    ["wh3_main_combi_region_sudenburg", 550, 254],
    ["wh3_main_combi_region_middenstag", 568, 690],
    ["wh3_main_combi_region_crooked_fang_fort", 731, 416],
    ["wh3_main_combi_region_zhizhu", 1321, 584],
    ["wh3_main_combi_region_the_sinhall_monolith", 369, 37],
    ["wh3_main_combi_region_uzkulak", 854, 723],
    ["wh3_main_combi_region_gorger_rock", 997, 678],
    ["wh3_main_combi_region_fu_chow", 1354, 504],
    ["wh3_main_combi_region_the_golden_tower", 680, 198],
    ["wh3_main_combi_region_shi_long", 1239, 460],
    ["wh3_main_combi_region_the_high_place", 795, 550],
    ["wh3_main_combi_region_doomkeep", 514, 836],
    ["wh3_main_combi_region_the_fetid_catacombs", 441, 896],
    ["wh3_main_combi_region_varg_camp", 514, 874],
    ["wh3_main_combi_region_circle_of_destruction", 159, 757],
    ["wh3_main_combi_region_the_twisted_glade", 208, 692],
    ["wh3_main_combi_region_ironfrost", 40, 878],
    ["wh3_main_combi_region_the_tower_of_torment", 760, 858],
    ["wh3_main_combi_region_black_crag", 753, 483],
    ["wh3_main_combi_region_karag_dron", 752, 517],
    ["wh3_main_combi_region_great_turtle_isle", 31, 250],
    ["wh3_main_combi_region_the_monoliths", 203, 755],
    ["wh3_main_combi_region_dark_tower", 1272, 725],
    ["wh3_main_combi_region_broken_mount", 1237, 740],
    ["wh3_main_combi_region_desolation_ridge", 1199, 728],
    ["wh3_main_combi_region_rotten_stone", 1164, 733]
]

class DistancesDict(TypedDict):
    distance: int

class SettlementDict(TypedDict, total=False):
    settlement: str
    faction: str

class Settlement_Manager():

    def __init__(self, random):
        self.faction_table = faction_table
        self.settlement_table = settlement_table
        self.new_settlement_dict = {}
        self.new_horde_dict = {}
        self.faction_distance_dict = {}
        self.capital_dict = {}
        self.random = random

    def calculateDistance(self, s1: int, s2: int) -> int:
        st = self.settlement_table
        return int(math.hypot(st[s2][1] - st[s1][1], st[s2][2] - st[s1][2]))

    def faction_to_faction_id(self,faction):
        for i in range(len(faction_table)):
            if faction_table[i][0] == faction:
                return i
        raise Exception("Faction " + str(faction) + " not found in faction table")

    def faction_id_to_faction(self, faction_id):
        i = faction_table[faction_id][0]
        return i
     
    def has_home_region(self, playerFaction):
        for row in faction_table:
            if row[0] == playerFaction:
                return row[2]
    
    def settlement_to_id(self, settlement: str) -> int:
        for i in range(len(settlement_table)):
            if settlement_table[i][0] == settlement:
                return i
        raise Exception("Settlement " + str(settlement) + " not found in faction table")
    
    def settlement_to_faction(self, settlement_name: str) -> str:
        return self.new_settlement_dict[settlement_name]

    def get_major_faction_ids(self):
        shuffled_major_faction_ids = []
        for i in range(len(faction_table)):
            if faction_table[i][1] == True and faction_table[i][2] == True:
                shuffled_major_faction_ids.append(i)
        return shuffled_major_faction_ids

    def get_minor_faction_ids(self):
        shuffled_minor_faction_ids = []
        for i in range(len(faction_table)):
            if faction_table[i][1] == False and faction_table[i][2] == True:
                shuffled_minor_faction_ids.append(i)
        return shuffled_minor_faction_ids

    def get_major_horde_faction_ids(self):
        shuffled_major_faction_ids = []
        for i in range(len(faction_table)):
            if faction_table[i][1] == True and faction_table[i][2] == False:
                shuffled_major_faction_ids.append(i)
        return shuffled_major_faction_ids

    def get_minor_horde_faction_ids(self):
        shuffled_minor_faction_ids = []
        for i in range(len(faction_table)):
            if faction_table[i][1] == False and faction_table[i][2] == False:
                shuffled_minor_faction_ids.append(i)
        return shuffled_minor_faction_ids
        
    def get_distance(self, faction_key: str) -> int:
        return self.faction_distance_dict[faction_key]
    
    def factions_to_spheres(self, sphere_amount: int, sphere_distance: int):
        self.factions_to_spheres = {}
        for key, value in self.faction_distance_dict.items():
            sphere = int(value/sphere_distance)
            if (sphere <sphere_amount):
                self.factions_to_spheres[key] = sphere
            else:
                self.factions_to_spheres[key] = sphere_amount -1
        return self.factions_to_spheres

    def table_to_dict(self, table) -> TypedDict:
        settlement_table: dict[int, SettlementDict] = {}
        for i,settlement in enumerate(table):
            settlement_table[i] = {
                "settlement": settlement[0],
                "faction": settlement[1]
            }
        return settlement_table
    
    def get_capital_dict(self):
        return self.capital_dict
    
    def get_closest_available_settlement(self, target_settlement_id: int, remaining_settlements_ids, new_settlement_table, max_range):
        if not remaining_settlements_ids:
            return None
        sorted_settlements = sorted(
            remaining_settlements_ids,
            key=lambda sid: self.calculateDistance(
                target_settlement_id, sid
            )
        )
        if (sorted_settlements[0] <= max_range):
            return sorted_settlements[0]
        else:
            return None
        
    def is_woodelve(self, faction):
        for i in range(len(woodelve_table)):
            if faction == woodelve_table[i][0]:
                return True
        return False

    def shuffle_settlements(self, player_faction: str, max_range: int):
        remaining_settlements = len(settlement_table)
        remaining_settlements_ids = [i for i in range(len(settlement_table))]
        remaining_horde_settlement_ids = [i for i in range(len(settlement_table))]
        new_settlement_table = [[settlement[0], 0] for settlement in settlement_table]
        new_horde_table = []
        remaining_forests_ids = [i for i in range(len(forest_location_table))]
        if (self.is_woodelve(player_faction)):
            i = self.random.randint(0, len(remaining_forests_ids) - 1)
            forest_name = forest_location_table[remaining_forests_ids[i]]
            for number, settlement in enumerate(new_settlement_table):
                if settlement[0] == forest_name:
                    new_settlement_table[number][1] = self.faction_to_faction_id(player_faction)
                    player_settlement = new_settlement_table[number][0]
                    remaining_forests_ids.pop(i)
                    remaining_settlements -= 1
                    remaining_settlements_ids.remove(number)
                    self.capital_dict[player_faction] = settlement[0]
                    self.faction_distance_dict[player_faction] = 0
                    break
        else:
            i = self.random.randint(0, len(new_settlement_table) - 1)
            if self.has_home_region(player_faction):
                new_settlement_table[i][1] = self.faction_to_faction_id(player_faction)
            else:
                new_horde_table.append([new_settlement_table[i][0], self.faction_to_faction_id(player_faction)])
            player_settlement = new_settlement_table[i][0]
            self.capital_dict[player_faction] = player_settlement
            self.faction_distance_dict[player_faction] = 0
            if self.has_home_region(player_faction):
                remaining_settlements_ids.pop(i)
                remaining_settlements -= 1
            else:
                remaining_horde_settlement_ids.pop(i)
        
        # Force Woodelves to be in forest_regions
        for i in range(len(woodelve_table)):
            woodelve_faction = woodelve_table[i][0]
            if woodelve_faction == player_faction :
                continue
            j = self.random.randint(0, len(remaining_forests_ids) - 1)
            forest_name = forest_location_table[remaining_forests_ids[j]]
            for number, settlement in enumerate(new_settlement_table):
                if settlement[0] == forest_name:
                    new_settlement_table[number][1] = self.faction_to_faction_id(woodelve_faction)
                    remaining_forests_ids.pop(j)
                    remaining_settlements -= 1
                    remaining_settlements_ids.remove(number)
                    self.capital_dict[woodelve_faction] = settlement[0]
                    self.faction_distance_dict[woodelve_faction] = (
                        self.calculateDistance(self.settlement_to_id(player_settlement), self.settlement_to_id(forest_name))
                    )
                    break

        first_loop = True
        major_factions_keys = self.get_major_faction_ids()
        minor_factions_keys = self.get_minor_faction_ids()
        self.random.shuffle(major_factions_keys)
        if self.has_home_region(player_faction):
            major_factions_keys.remove(self.faction_to_faction_id(player_faction))
        self.random.shuffle(minor_factions_keys)
        # Remove Woodelves from first iteration
        for i in range(0, 4):
            if not woodelve_table[i][0] == player_faction :
                major_factions_keys.remove(self.faction_to_faction_id(woodelve_table[i][0]))
        for i in range(4, 9):
            minor_factions_keys.remove(self.faction_to_faction_id(woodelve_table[i][0]))
        for i in range(len(major_factions_keys)):
                if (remaining_settlements > 0):
                    a = self.random.randint(0, len(remaining_settlements_ids) - 1)
                    new_settlement_table[remaining_settlements_ids[a]][1] = major_factions_keys[i]
                    if first_loop == True:
                        faction_settlement = new_settlement_table[remaining_settlements_ids[a]][0]
                        self.faction_distance_dict[self.faction_id_to_faction(major_factions_keys[i])] = (
                            self.calculateDistance(self.settlement_to_id(player_settlement), self.settlement_to_id(faction_settlement))
                        )
                        self.capital_dict[self.faction_id_to_faction(major_factions_keys[i])] = faction_settlement
                    remaining_settlements_ids.pop(a)
                    remaining_settlements -= 1
                else:
                    break
        for i in range(len(minor_factions_keys)):
            if (remaining_settlements > 0):
                a = self.random.randint(0, len(remaining_settlements_ids) - 1)
                new_settlement_table[remaining_settlements_ids[a]][1] = minor_factions_keys[i]
                if first_loop == True:
                    faction_settlement = new_settlement_table[remaining_settlements_ids[a]][0]
                    self.faction_distance_dict[self.faction_id_to_faction(minor_factions_keys[i])] = (
                        self.calculateDistance(self.settlement_to_id(player_settlement), self.settlement_to_id(faction_settlement))
                    )
                    self.capital_dict[self.faction_id_to_faction(minor_factions_keys[i])] = faction_settlement
                remaining_settlements_ids.pop(a)
                remaining_settlements -= 1
            else:
                break
        if self.has_home_region(player_faction):
            major_factions_keys.append(self.faction_to_faction_id(player_faction))
                
        # Add Woodelves from first iteration
        for i in range(0, 4):
            if not woodelve_table[i][0] == player_faction :
                major_factions_keys.append(self.faction_to_faction_id(woodelve_table[i][0]))
        for i in range(4, 9):
            minor_factions_keys.append(self.faction_to_faction_id(woodelve_table[i][0]))

        breakout_counter = 0
        while (remaining_settlements > 0):
            # Randomize faction order
            self.random.shuffle(major_factions_keys)
            for faction in major_factions_keys:
                if (remaining_settlements == 0):
                    break
                faction_settlement_list = []
                for i in range(len(new_settlement_table)):
                    if new_settlement_table[i][1] == faction:
                        faction_settlement_list.append(self.settlement_to_id(new_settlement_table[i][0]))
                r = self.random.randint(0, len(faction_settlement_list) - 1)
                if (breakout_counter < 7):
                    closest_Settlement = self.get_closest_available_settlement(faction_settlement_list[r], remaining_settlements_ids, new_settlement_table, max_range)
                else:
                    closest_Settlement = self.get_closest_available_settlement(faction_settlement_list[r], remaining_settlements_ids, new_settlement_table, 1500)
                if closest_Settlement != None:
                    new_settlement_table[closest_Settlement][1] = faction
                    remaining_settlements_ids.remove(closest_Settlement)
                    remaining_settlements -= 1
            self.random.shuffle(minor_factions_keys)
            for faction in minor_factions_keys:
                if (remaining_settlements == 0):
                    break
                faction_settlement_list = []
                for i in range(len(new_settlement_table)):
                    if new_settlement_table[i][1] == faction:
                        faction_settlement_list.append(self.settlement_to_id(new_settlement_table[i][0]))
                r = self.random.randint(0, len(faction_settlement_list) - 1)
                if (breakout_counter < 7):
                    closest_Settlement = self.get_closest_available_settlement(faction_settlement_list[r], remaining_settlements_ids, new_settlement_table, max_range)
                else:
                    closest_Settlement = self.get_closest_available_settlement(faction_settlement_list[r], remaining_settlements_ids, new_settlement_table, 1500)
                if closest_Settlement != None:
                    new_settlement_table[closest_Settlement][1] = faction
                    remaining_settlements_ids.remove(closest_Settlement)
                    remaining_settlements -= 1
            breakout_counter += 1
        horde_keys = self.get_major_horde_faction_ids()
        horde_keys.append(self.get_minor_faction_ids())
        if (not self.has_home_region(player_faction)):
            horde_keys.remove(self.faction_to_faction_id(player_faction))
        for faction in horde_keys:
            i = self.random.randint(0, len(remaining_horde_settlement_ids) - 1)
            new_horde_table.append([new_settlement_table[i][0], faction])
            remaining_horde_settlement_ids.pop(i)

        for i in range(len(new_settlement_table)):
            if isinstance(new_settlement_table[i][1], int):
                new_settlement_table[i][1] = self.faction_id_to_faction(new_settlement_table[i][1])
        self.new_settlement_dict = {row[0]: row[1] for row in new_settlement_table}
        for i in range(len(new_horde_table)):
            if isinstance(new_horde_table[i][1], int):
                new_horde_table[i][1] = self.faction_id_to_faction(new_horde_table[i][1])
        self.new_horde_dict = {row[0]: row[1] for row in new_horde_table}
        return self.new_settlement_dict, self.new_horde_dict