from __future__ import annotations
from typing import TYPE_CHECKING

from .faction_tables.item_types import factionData, settlementData
from collections import Counter
import time

trueHordeList = ["wh_dlc03_bst_beastmen", "wh2_dlc17_bst_malagor", "wh_dlc05_bst_morghur_herd", "wh2_dlc17_bst_taurox", "wh2_dlc13_lzd_spirits_of_the_jungle", "wh3_dlc26_ogr_golgfag", "wh3_dlc27_hef_aislinn"]

factionDict: dict[int, factionData] = {
    0: factionData('wh3_main_dae_daemon_prince', True, False, 'daemons', 'The Daemon Prince (Daemons of Chaos)'),
    1: factionData('wh3_main_kho_exiles_of_khorne', True, True, 'khorne', 'Skarbrand (Khorne)'),
    2: factionData('wh3_dlc26_kho_skulltaker', True, True, 'khorne', 'Skulltaker (Khorne)'),
    3: factionData('wh3_dlc26_kho_arbaal', True, True, 'khorne', 'Arbaal the Undefeated (Khorne)'),
    4: factionData('wh3_main_nur_poxmakers_of_nurgle', True, True, 'nurgle', "Ku'gath Plaguefather (Nurgle)"),
    5: factionData('wh3_dlc25_nur_tamurkhan', True, True, 'nurgle', 'Tamurkhan the Maggot Lord (Nurgle)'),
    6: factionData('wh3_dlc25_nur_epidemius', True, True, 'nurgle', 'Epidemius (Nurgle)'),
    7: factionData('wh3_main_sla_seducers_of_slaanesh', True, True, 'slaanesh', "N'Kari (Slaanesh)"),
    8: factionData('wh3_dlc27_sla_the_tormentors', True, False, 'slaaneshDechala', 'Dechala, the Denied One (Slaanesh)'),
    9: factionData('wh3_dlc27_sla_masque_of_slaanesh', True, True, 'slaanesh', 'The Masque of Slaanesh (Slaanesh)'),
    10: factionData('wh3_main_tze_oracles_of_tzeentch', True, True, 'tzeentch', 'Kairos Fateweaver (Tzeentch)'),
    11: factionData('wh3_dlc24_tze_the_deceivers', True, False, 'tzeentch', 'The Changeling (Tzeentch)'),
    12: factionData('wh3_main_ksl_the_ice_court', True, True, 'kislev', 'Tzarina Katarin (Kislev)'),
    13: factionData('wh3_main_ksl_the_great_orthodoxy', True, True, 'kislev', 'Kostaltyn (Kislev)'),
    14: factionData('wh3_main_ksl_ursun_revivalists', True, False, 'kislev', 'Boris Ursus (Kislev)'),
    15: factionData('wh3_dlc24_ksl_daughters_of_the_forest', True, True, 'kislev', 'Mother Ostankya (Kislev)'),
    16: factionData('wh3_main_ogr_goldtooth', True, True, 'ogres', 'Greasus Goldtooth (Ogre Kingdoms)'),
    17: factionData('wh3_main_ogr_disciples_of_the_maw', True, True, 'ogres', 'Skrag the Slaughterer (Ogre Kingdoms)'),
    18: factionData('wh3_dlc26_ogr_golgfag', True, False, 'ogres', 'Golgfag Maneater (Ogre Kingdoms)'),
    19: factionData('wh3_dlc23_chd_astragoth', True, True, 'chaosDwarfs', 'Astragoth Ironhand (Chaos Dwarfs)'),
    20: factionData('wh3_dlc23_chd_legion_of_azgorh', True, True, 'chaosDwarfs', 'Drazhoath the Ashen (Chaos Dwarfs)'),
    21: factionData('wh3_dlc23_chd_zhatan', True, True, 'chaosDwarfs', 'Zhaten the Black (Chaos Dwarfs)'),
    22: factionData('wh3_main_cth_the_northern_provinces', True, True, 'cathay', 'Miao Ying, the Storm Dragon (Grand Cathay)'),
    23: factionData('wh3_main_cth_the_western_provinces', True, True, 'cathay', 'Zhai Ming, the Iron Dragon (Grand Cathay)'),
    24: factionData('wh3_dlc24_cth_the_celestial_court', True, True, 'cathay', 'Yuan Bo, the Jade Dragon (Grand Cathay)'),
    25: factionData('wh2_main_hef_eataine', True, True, 'highElves', 'Tyrion (High Elves)'),
    26: factionData('wh2_main_hef_order_of_loremasters', True, True, 'highElves', 'Teclis (High Elves)'),
    27: factionData('wh2_main_hef_avelorn', True, True, 'highElves', 'Alarielle the Radiant (High Elves)'),
    28: factionData('wh2_main_hef_nagarythe', True, True, 'highElves', 'Alith Anar (High Elves)'),
    29: factionData('wh2_main_hef_yvresse', True, True, 'highElves', 'Eltharion the Grim (High Elves)'),
    30: factionData('wh2_dlc15_hef_imrik', True, True, 'highElves', 'Imrik (High Elves)'),
    31: factionData('wh3_dlc27_hef_aislinn', True, False, 'highElvesAislinn', 'Sea Lord Aislinn (High Elves)'),
    32: factionData('wh2_dlc17_lzd_oxyotl', True, True, 'lizardmen', 'Oxyotl (Lizardmen)'),
    33: factionData('wh2_main_lzd_hexoatl', True, True, 'lizardmen', 'Lord Mazdamundi (Lizardmen)'),
    34: factionData('wh2_main_lzd_last_defenders', True, True, 'lizardmen', 'Kroq-Gar (Lizardmen)'),
    35: factionData('wh2_dlc12_lzd_cult_of_sotek', True, True, 'lizardmen', 'Tehenhauin (Lizardmen)'),
    36: factionData('wh2_main_lzd_tlaqua', True, True, 'lizardmen', "Tiktaq'to (Lizardmen)"),
    37: factionData('wh2_dlc13_lzd_spirits_of_the_jungle', True, False, 'lizardmenNakai', 'Nakai the Wanderer (Lizardmen)'),
    38: factionData('wh2_main_lzd_itza', True, True, 'lizardmen', 'Gor-Rok (Lizardmen)'),
    39: factionData('wh2_main_def_naggarond', True, True, 'darkElves', 'Malekith (Dark Elves)'),
    40: factionData('wh2_main_def_cult_of_pleasure', True, True, 'darkElves', 'Morathi (Dark Elves)'),
    41: factionData('wh2_main_def_har_ganeth', True, True, 'darkElves', 'Crone Helebron (Dark Elves)'),
    42: factionData('wh2_dlc11_def_the_blessed_dread', True, True, 'darkElves', 'Lokhir Fellheart (Dark Elves)'),
    43: factionData('wh2_main_def_hag_graef', True, False, 'darkElves', 'Malus Darkblade (Dark Elves)'),
    44: factionData('wh2_twa03_def_rakarth', True, True, 'darkElves', 'Rakarth the Beastmaster (Dark Elves)'),
    45: factionData('wh2_main_skv_clan_mors', True, True, 'skaven', 'Queek Headtaker (Skaven)'),
    46: factionData('wh2_main_skv_clan_pestilens', True, True, 'skaven', 'Lord Skrolk (Skaven)'),
    47: factionData('wh2_dlc09_skv_clan_rictus', True, True, 'skaven', 'Tretch Craventail (Skaven)'),
    48: factionData('wh2_main_skv_clan_skryre', True, True, 'skaven', 'Ikit Claw (Skaven)'),
    49: factionData('wh2_main_skv_clan_moulder', True, True, 'skaven', 'Throt the Unclean (Skaven)'),
    50: factionData('wh2_main_skv_clan_eshin', True, True, 'skaven', 'Deathmaster Snikch (Skaven)'),
    51: factionData('wh2_dlc09_tmb_khemri', True, True, 'tombKings','Settra The Imperishable (Tomb Kings)'),
    52: factionData('wh2_dlc09_tmb_lybaras', True, True, 'tombKings', 'High Queen Khalida (Tomb Kings)'),
    53: factionData('wh2_dlc09_tmb_exiles_of_nehek', True, True, 'tombKings', 'Grand Hierophant Khatep (Tomb Kings)'),
    54: factionData('wh2_dlc09_tmb_followers_of_nagash', True, True, 'tombKings', 'Arkhan the Black (Tomb Kings)'),
    55: factionData('wh2_dlc11_cst_vampire_coast', True, True, 'vampireCoast', 'Luthor Harkon (Vampire Coast)'),
    56: factionData('wh2_dlc11_cst_noctilus', True, True, 'vampireCoast', 'Count Noctilus (Vampire Coast)'),
    57: factionData('wh2_dlc11_cst_the_drowned', True, True, 'vampireCoast', 'Cylostra Direfin (Vampire Coast)'),
    58: factionData('wh2_dlc11_cst_pirates_of_sartosa', True, True, 'vampireCoast', 'Aranessa Saltspite (Vampire Coast)'),
    59: factionData('wh_main_emp_empire', True, True, 'empire', 'Karl Franz (Empire)'),
    60: factionData('wh2_dlc13_emp_golden_order', True, False, 'empire', 'Balthasar Gelt (Empire)'),
    61: factionData('wh3_main_emp_cult_of_sigmar', True, True, 'empire', 'Volkmar the Grim (Empire)'),
    62: factionData('wh2_dlc13_emp_the_huntmarshals_expedition', True, True, 'empire', 'Markus Wulfhart (Empire)'),
    63: factionData('wh_main_emp_wissenland', True, True, 'empire', 'Elspeth Von Draken (Empire)'),
    64: factionData('wh_main_dwf_dwarfs', True, True, 'dwarfs', 'Thorgrim Grudgebearer (Dwarfs)'),
    65: factionData('wh_main_dwf_karak_kadrin', True, True, 'dwarfs', 'Ungrim Ironfist (Dwarfs)'),
    66: factionData('wh_main_dwf_karak_izor', True, True, 'dwarfs', 'Belegar Ironhammer (Dwarfs)'),
    67: factionData('wh3_main_dwf_the_ancestral_throng', True, True, 'dwarfs', 'Grombrindal - The White Dwarf (Dwarfs)'),
    68: factionData('wh2_dlc17_dwf_thorek_ironbrow', True, True, 'dwarfs', 'Thorek Ironbrow (Dwarfs)'),
    69: factionData('wh3_dlc25_dwf_malakai', True, True, 'dwarfs', 'Malakai Makaisson (Dwarfs)'),
    70: factionData('wh_main_grn_greenskins', True, True, 'greenskins', 'Grimgor Ironhide (Greenskins)'),
    71: factionData('wh_main_grn_crooked_moon', True, True, 'greenskins', 'Skarsnik (Greenskins)'),
    72: factionData('wh2_dlc15_grn_bonerattlaz', True, True, 'greenskins', 'Azhag the Slaughterer (Greenskins)'),
    73: factionData('wh_main_grn_orcs_of_the_bloody_hand', True, True, 'greenskins', 'Wurrzag da Great Green Prophet (Greenskins)'),
    74: factionData('wh2_dlc15_grn_broken_axe', True, True, 'greenskins', 'Grom the Paunch (Greenskins)'),
    75: factionData('wh3_dlc26_grn_gorbad_ironclaw', True, True, 'greenskins', 'Gorbad Ironclaw (Greenskins)'),
    76: factionData('wh_main_vmp_vampire_counts', True, True, 'vampireCounts', 'Mannfred von Carstein (Vampire Counts)'),
    77: factionData('wh2_dlc11_vmp_the_barrow_legion', True, True, 'vampireCounts', 'Heinrich Kemmler (Vampire Counts)'),
    78: factionData('wh3_main_vmp_caravan_of_blue_roses', True, True, 'vampireCounts', 'Helman Ghorst (Vampire Counts)'),
    79: factionData('wh_main_vmp_schwartzhafen', True, True, 'vampireCounts', 'Vlad von Carstein (Vampire Counts)'),
    80: factionData('wh_main_chs_chaos', True, False, 'chaos', 'Archaon the Everchosen (Warriors of Chaos)'),
    81: factionData('wh3_dlc20_chs_kholek', True, False, 'chaos', 'Kholek Suneater (Warriors of Chaos)'),
    82: factionData('wh3_dlc20_chs_sigvald', True, False, 'chaos', 'Prince Sigvald the Magnificent (Warriors of Chaos)'),
    83: factionData('wh3_dlc20_chs_azazel', True, False, 'chaosSlaanesh', 'Azazel (Warriors of Chaos)'),
    84: factionData('wh3_dlc20_chs_festus', True, True, 'chaosNurgle', 'Festus the Leechlord (Warriors of Chaos)'),
    85: factionData('wh3_dlc20_chs_valkia', True, False, 'chaosKhorne', 'Valkia the Bloody (Warriors of Chaos)'),
    86: factionData('wh3_dlc20_chs_vilitch', True, False, 'chaosTzeentch', 'Vilitch the Cursling (Warriors of Chaos)'),
    87: factionData('wh3_main_chs_shadow_legion', True, False, 'chaos', "Be'lakor (Warriors of Chaos)"),
    88: factionData('wh_dlc03_bst_beastmen', True, False, 'beastmen', 'Khazrak the One-Eye (Beastmen)'),
    89: factionData('wh2_dlc17_bst_malagor', True, False, 'beastmen', 'Malagor the Dark Omen (Beastmen)'),
    90: factionData('wh_dlc05_bst_morghur_herd', True, False, 'beastmen', 'Morghur the Shadowgave (Beastmen)'),
    91: factionData('wh2_dlc17_bst_taurox', True, False, 'beastmen', 'Taurox the Brass Bull (Beastmen)'),
    92: factionData('wh_dlc05_wef_wood_elves', True, True, 'woodElves', 'Orion (Wood Elves)'),
    93: factionData('wh_dlc05_wef_argwylon', True, True, 'woodElves', 'Durthu (Wood Elves)'),
    94: factionData('wh2_dlc16_wef_sisters_of_twilight', True, True, 'woodElves', 'Sisters of Twilight (Wood Elves)'),
    95: factionData('wh2_dlc16_wef_drycha', True, True, 'woodElves', 'Drycha (Wood Elves)'),
    96: factionData('wh_main_brt_bretonnia', True, True, 'bretonnia', 'King Louen Leoncoeur (Bretonnia)'),
    97: factionData('wh_main_brt_carcassonne', True, True, 'bretonnia', 'Fay Enchantress (Bretonnia)'),
    98: factionData('wh_main_brt_bordeleaux', True, True, 'bretonnia', 'Alberic de Bordeleaux (Bretonnia)'),
    99: factionData('wh2_dlc14_brt_chevaliers_de_lyonesse', True, True, 'bretonnia', 'Repanse de Lyonesse (Bretonnia)'),
    100: factionData('wh_dlc08_nor_norsca', True, True, 'norsca', 'Wulfrik the Wanderer (Norsca)'),
    101: factionData('wh3_dlc27_nor_sayl', True, True, 'norsca', 'Sayl the Faithless (Sayl)'),
    102: factionData('wh_dlc08_nor_wintertooth', True, True, 'norsca', 'Throgg (Norsca)'),
    103: factionData('wh3_main_kho_bloody_sword', False, True, 'ai', None),
    104: factionData('wh3_main_kho_brazen_throne', False, True, 'ai', None),
    105: factionData('wh3_main_kho_crimson_skull', False, True, 'ai', None),
    106: factionData('wh3_main_nur_bubonic_swarm', False, True, 'ai', None),
    107: factionData('wh3_main_nur_maggoth_kin', False, True, 'ai', None),
    108: factionData('wh3_dlc20_nur_pallid_nurslings', False, True, 'ai', None),
    109: factionData('wh3_main_sla_exquisite_pain', False, True, 'ai', None),
    110: factionData('wh3_main_sla_rapturous_excess', False, True, 'ai', None),
    111: factionData('wh3_main_sla_subtle_torture', False, True, 'ai', None),
    112: factionData('wh3_dlc20_sla_keepers_of_bliss', False, True, 'ai', None),
    113: factionData('wh3_main_tze_all_seeing_eye', False, True, 'ai', None),
    114: factionData('wh3_main_tze_broken_wheel', False, True, 'ai', None),
    115: factionData('wh3_main_tze_flaming_scribes', False, True, 'ai', None),
    116: factionData('wh3_main_ksl_ropsmenn_clan', False, True, 'ai', None),
    117: factionData('wh3_dlc20_tze_the_sightless', False, True, 'ai', None),
    118: factionData('wh3_dlc20_tze_apostles_of_change', False, True, 'ai', None),
    119: factionData('wh3_main_tze_sarthoraels_watchers', False, True, 'ai', None),
    120: factionData('wh3_main_ksl_brotherhood_of_the_bear', False, True, 'ai', None),
    121: factionData('wh3_main_ksl_druzhina_enclave', False, True, 'ai', None),
    122: factionData('wh3_main_ksl_ungol_kindred', False, True, 'ai', None),
    123: factionData('wh3_main_ogr_blood_guzzlers', False, True, 'ai', None),
    124: factionData('wh3_main_ogr_crossed_clubs', False, True, 'ai', None),
    125: factionData('wh3_main_ogre_sharktooth', False, False, 'ai', None),
    126: factionData('wh3_main_ogre_stoneshatter', False, False, 'ai', None),
    127: factionData('wh3_main_ogr_feastmaster', False, False, 'ai', None),
    128: factionData('wh3_main_ogre_the_famished', False, True, 'ai', None),
    129: factionData('wh3_main_ogre_flamegullets', False, False, 'ai', None),
    130: factionData('wh3_main_ogr_fleshgreeders', False, True, 'ai', None),
    131: factionData('wh3_main_ogr_fulg', False, True, 'ai', None),
    132: factionData('wh3_main_ogr_lazarghs', False, True, 'ai', None),
    133: factionData('wh3_main_ogr_mountaineaters', False, True, 'ai', None),
    134: factionData('wh3_main_ogr_rock_skulls', False, True, 'ai', None),
    135: factionData('wh3_main_ogr_sabreskin', False, True, 'ai', None),
    136: factionData('wh3_main_ogr_sons_of_the_mountain', False, True, 'ai', None),
    137: factionData('wh3_main_ogr_thunderguts', False, True, 'ai', None),
    138: factionData('wh3_main_ogr_treehammers', False, False, 'ai', None),
    139: factionData('wh3_main_cth_burning_wind_nomads', False, True, 'ai', None),
    140: factionData('wh3_main_cth_celestial_loyalists', False, True, 'ai', None),
    141: factionData('wh3_main_cth_dissenter_lords_of_jinshen', False, True, 'ai', None),
    142: factionData('wh3_main_cth_eastern_river_lords', False, True, 'ai', None),
    143: factionData('wh3_main_cth_imperial_wardens', False, True, 'ai', None),
    144: factionData('wh3_main_cth_rebel_lords_of_nan_yang', False, True, 'ai', None),
    145: factionData('wh3_main_cth_the_jade_custodians', False, True, 'ai', None),
    146: factionData('wh2_main_hef_caledor', False, True, 'ai', None),
    147: factionData('wh2_main_hef_chrace', False, True, 'ai', None),
    148: factionData('wh2_main_hef_citadel_of_dusk', False, True, 'ai', None),
    149: factionData('wh2_main_hef_cothique', False, True, 'ai', None),
    150: factionData('wh2_main_hef_ellyrion', False, True, 'ai', None),
    151: factionData('wh2_main_hef_saphery', False, True, 'ai', None),
    152: factionData('wh2_main_hef_tiranoc', False, True, 'ai', None),
    153: factionData('wh2_main_hef_tor_elasor', False, True, 'ai', None),
    154: factionData('wh3_dlc27_hef_aislinn_confederation_owner', False, True, 'ai', None),
    155: factionData('wh2_main_lzd_sentinels_of_xeti', False, True, 'ai', None),
    156: factionData('wh2_main_lzd_southern_sentinels', False, True, 'ai', None),
    157: factionData('wh3_main_lzd_tepoks_spawn', False, True, 'ai', None),
    158: factionData('wh2_main_lzd_tlaxtlan', False, True, 'ai', None),
    159: factionData('wh2_dlc16_lzd_wardens_of_the_living_pools', False, True, 'ai', None),
    160: factionData('wh2_main_lzd_xlanhuapec', False, True, 'ai', None),
    161: factionData('wh2_main_lzd_zlatan', False, True, 'ai', None),
    162: factionData('wh2_main_def_bleak_holds', False, True, 'ai', None),
    163: factionData('wh2_main_def_blood_hall_coven', False, True, 'ai', None),
    164: factionData('wh2_main_def_clar_karond', False, True, 'ai', None),
    165: factionData('wh2_main_def_cult_of_excess', False, True, 'ai', None),
    166: factionData('wh2_main_def_deadwood_sentinels', False, True, 'ai', None),
    167: factionData('wh2_main_def_ghrond', False, True, 'ai', None),
    168: factionData('wh2_main_def_karond_kar', False, True, 'ai', None),
    169: factionData('wh2_main_def_scourge_of_khaine', False, True, 'ai', None),
    170: factionData('wh2_main_def_ssildra_tor', False, True, 'ai', None),
    171: factionData('wh2_main_def_drackla_coven', False, True, 'ai', None),
    172: factionData('wh2_main_def_the_forgebound', False, True, 'ai', None),
    173: factionData('wh3_main_skv_clan_carrion', False, True, 'ai', None),
    174: factionData('wh2_dlc16_skv_clan_gritus', False, True, 'ai', None),
    175: factionData('wh2_dlc15_skv_clan_kreepus', False, True, 'ai', None),
    176: factionData('wh3_main_skv_clan_krizzor', False, True, 'ai', None),
    177: factionData('wh2_dlc12_skv_clan_mange', False, True, 'ai', None),
    178: factionData('wh3_main_skv_clan_morbidus', False, True, 'ai', None),
    179: factionData('wh2_main_skv_clan_mordkin', False, True, 'ai', None),
    180: factionData('wh2_main_skv_clan_septik', False, True, 'ai', None),
    181: factionData('wh3_main_skv_clan_skrat', False, True, 'ai', None),
    182: factionData('wh2_main_skv_clan_spittel', False, True, 'ai', None),
    183: factionData('wh3_main_skv_clan_verms', False, True, 'ai', None),
    184: factionData('wh3_main_skv_clan_treecherik', False, True, 'ai', None),
    185: factionData('wh3_main_tmb_deserters_of_khatep', False, True, 'ai', None),
    186: factionData('wh2_dlc09_tmb_dune_kingdoms', False, True, 'ai', None),
    187: factionData('wh2_dlc09_tmb_numas', False, True, 'ai', None),
    188: factionData('wh2_dlc09_tmb_rakaph_dynasty', False, True, 'ai', None),
    189: factionData('wh2_dlc09_tmb_the_sentinels', False, True, 'ai', None),
    190: factionData('wh2_dlc11_cst_vampire_coast_rebels', False, True, 'ai', None),
    191: factionData('wh3_dlc21_cst_dead_flag_fleet', False, True, 'ai', None),
    192: factionData('wh3_main_cst_dread_rock_privateers', False, True, 'ai', None),
    193: factionData('wh_main_emp_averland', False, True, 'ai', None),
    194: factionData('wh_main_emp_empire_separatists', False, True, 'ai', None),
    195: factionData('wh_main_emp_hochland', False, True, 'ai', None),
    196: factionData('wh_main_emp_marienburg', False, True, 'ai', None),
    197: factionData('wh_main_emp_middenland', False, True, 'ai', None),
    198: factionData('wh2_main_emp_new_world_colonies', False, True, 'ai', None),
    199: factionData('wh_main_emp_nordland', False, True, 'ai', None),
    200: factionData('wh_main_emp_ostermark', False, True, 'ai', None),
    201: factionData('wh_main_emp_ostland', False, True, 'ai', None),
    202: factionData('wh_main_emp_stirland', False, True, 'ai', None),
    203: factionData('wh_main_emp_talabecland', False, True, 'ai', None),
    204: factionData('wh_main_dwf_barak_varr', False, True, 'ai', None),
    205: factionData('wh2_dlc15_dwf_clan_helhein', False, True, 'ai', None),
    206: factionData('wh2_main_dwf_greybeards_prospectors', False, True, 'ai', None),
    207: factionData('wh3_main_dwf_karak_azorn', False, True, 'ai', None),
    208: factionData('wh_main_dwf_karak_azul', False, True, 'ai', None),
    209: factionData('wh_main_dwf_karak_hirn', False, True, 'ai', None),
    210: factionData('wh_main_dwf_karak_norn', False, True, 'ai', None),
    211: factionData('wh_main_dwf_karak_ziflin', False, True, 'ai', None),
    212: factionData('wh2_main_dwf_spine_of_sotek_dwarfs', False, True, 'ai', None),
    213: factionData('wh_main_dwf_zhufbar', False, True, 'ai', None),
    214: factionData('wh2_main_grn_arachnos', False, True, 'ai', None),
    215: factionData('wh_main_grn_black_venom', False, True, 'ai', None),
    216: factionData('wh_main_grn_bloody_spearz', False, True, 'ai', None),
    217: factionData('wh2_main_grn_blue_vipers', False, True, 'ai', None),
    218: factionData('wh2_dlc16_grn_naggaroth_orcs', False, True, 'ai', None),
    219: factionData('wh_main_grn_broken_nose', False, True, 'ai', None),
    220: factionData('wh2_dlc16_grn_creeping_death', False, True, 'ai', None),
    221: factionData('wh3_dlc26_grn_cluster_eye_tribe', False, True, 'ai', None),
    222: factionData('wh_main_grn_necksnappers', False, True, 'ai', None),
    223: factionData('wh3_main_grn_da_cage_breakaz', False, True, 'ai', None),
    224: factionData('wh3_main_grn_dark_land_orcs', False, True, 'ai', None),
    225: factionData('wh3_main_grn_dimned_sun', False, True, 'ai', None),
    226: factionData('wh3_main_grn_drippin_fangs', False, True, 'ai', None),
    227: factionData('wh2_dlc12_grn_leaf_cutterz_tribe', False, True, 'ai', None),
    228: factionData('wh3_main_grn_moon_howlerz', False, True, 'ai', None),
    229: factionData('wh_main_grn_red_eye', False, True, 'ai', None),
    230: factionData('wh2_dlc14_grn_red_cloud', False, True, 'ai', None),
    231: factionData('wh_main_grn_red_fangs', False, True, 'ai', None),
    232: factionData('wh_main_grn_scabby_eye', False, True, 'ai', None),
    233: factionData('wh_main_grn_skull-takerz', False, False, 'ai', None),
    234: factionData('wh2_dlc15_grn_skull_crag', False, True, 'ai', None),
    235: factionData('wh_main_grn_skullsmasherz', False, True, 'ai', None),
    236: factionData('wh3_main_grn_slaves_of_zharr', False, True, 'ai', None),
    237: factionData('wh_main_grn_teef_snatchaz', False, True, 'ai', None),
    238: factionData('wh_dlc03_grn_black_pit', False, True, 'ai', None),
    239: factionData('wh_main_grn_top_knotz', False, True, 'ai', None),
    240: factionData('wh3_main_grn_tusked_sunz', False, True, 'ai', None),
    241: factionData('wh3_dlc21_vmp_jiangshi_rebels', False, True, 'ai', None),
    242: factionData('wh3_main_vmp_lahmian_sisterhood', False, True, 'ai', None),
    243: factionData('wh_main_vmp_mousillon', False, True, 'ai', None),
    244: factionData('wh2_main_vmp_necrarch_brotherhood', False, True, 'ai', None),
    245: factionData('wh3_main_ie_vmp_sires_of_mourkain', False, True, 'ai', None),
    246: factionData('wh2_main_vmp_strygos_empire', False, True, 'ai', None),
    247: factionData('wh_main_vmp_rival_sylvanian_vamps', False, True, 'ai', None),
    248: factionData('wh2_main_vmp_the_silver_host', False, True, 'ai', None),
    249: factionData('wh3_dlc25_vmp_the_court_of_night', False, True, 'ai', None),
    250: factionData('wh3_main_chs_khazag', False, True, 'ai', None),
    251: factionData('wh_main_teb_border_princes', False, True, 'ai', None),
    252: factionData('wh_main_teb_estalia', False, True, 'ai', None),
    253: factionData('wh_main_teb_tilea', False, True, 'ai', None),
    254: factionData('wh_dlc03_bst_jagged_horn', False, False, 'aiHorde', None),
    255: factionData('wh2_main_bst_manblight', False, False, 'aiHorde', None),
    256: factionData('wh_dlc03_bst_redhorn', False, False, 'aiHorde', None),
    257: factionData('wh2_main_bst_ripper_horn', False, False, 'aiHorde', None),
    258: factionData('wh2_main_bst_shadowgor', False, False, 'ai', None),
    259: factionData('wh2_main_wef_bowmen_of_oreon', False, True, 'woodElves', None),
    260: factionData('wh3_main_wef_laurelorn', False, True, 'woodElves', None),
    261: factionData('wh3_dlc21_wef_spirits_of_shanlin', False, True, 'woodElves', None),
    262: factionData('wh_dlc05_wef_torgovann', False, True, 'woodElves', None),
    263: factionData('wh_dlc05_wef_wydrioth', False, True, 'woodElves', None),
    264: factionData('wh_main_brt_artois', False, True, 'ai', None),
    265: factionData('wh_main_brt_bastonne', False, True, 'ai', None),
    266: factionData('wh3_main_brt_aquitaine', False, True, 'ai', None),
    267: factionData('wh2_main_brt_knights_of_origo', False, True, 'ai', None),
    268: factionData('wh2_main_brt_knights_of_the_flame', False, True, 'ai', None),
    269: factionData('wh_main_brt_lyonesse', False, True, 'ai', None),
    270: factionData('wh_main_brt_parravon', False, True, 'ai', None),
    271: factionData('wh2_main_brt_thegans_crusaders', False, True, 'ai', None),
    272: factionData('wh_main_nor_aesling', False, True, 'ai', None),
    273: factionData('wh2_main_nor_aghol', False, True, 'ai', None),
    274: factionData('wh3_dlc23_chd_minor_faction', False, True, 'ai', None),
    275: factionData('wh3_dlc23_chd_conclave', False, True, 'ai', None),
    276: factionData('wh_main_nor_baersonling', False, True, 'ai', None),
    277: factionData('wh_main_nor_bjornling', False, True, 'ai', None),
    278: factionData('wh3_dlc20_nor_dolgan', False, True, 'ai', None),
    279: factionData('wh_dlc08_nor_goromadny_tribe', False, True, 'ai', None),
    280: factionData('wh3_dlc20_nor_kul', False, True, 'ai', None),
    281: factionData('wh2_main_nor_mung', False, True, 'ai', None),
    282: factionData('wh_dlc08_nor_naglfarlings', False, True, 'ai', None),
    283: factionData('wh_main_nor_sarl', False, True, 'ai', None),
    284: factionData('wh_main_nor_skaeling', False, True, 'ai', None),
    285: factionData('wh2_main_nor_skeggi', False, True, 'ai', None),
    286: factionData('wh_dlc08_nor_vanaheimlings', False, True, 'ai', None),
    287: factionData('wh_main_nor_varg', False, True, 'ai', None),
    288: factionData('wh3_dlc27_nor_avags', False, True, 'ai', None),
    289: factionData('wh3_dlc21_nor_wyrmkins', False, True, 'ai', None),
    290: factionData('wh3_dlc20_nor_yusak', False, True, 'ai', None),
    291: factionData('wh3_dlc27_the_narj', False, True, 'ai', None),
    292: factionData('wh2_dlc11_cst_rogue_bleak_coast_buccaneers', False, False, 'aiHorde', None),
    293: factionData('wh2_dlc11_cst_rogue_boyz_of_the_forbidden_coast', False, False, 'aiHorde', None),
    294: factionData('wh2_dlc11_cst_rogue_freebooters_of_port_royale', False, False, 'aiHorde', None),
    295: factionData('wh2_dlc11_cst_rogue_grey_point_scuttlers', False, False, 'aiHorde', None),
    296: factionData('wh2_dlc11_cst_rogue_terrors_of_the_dark_straights', False, False, 'aiHorde', None),
    297: factionData('wh2_dlc11_cst_rogue_the_churning_gulf_raiders', False, False, 'aiHorde', None),
    298: factionData('wh2_dlc11_cst_rogue_tyrants_of_the_black_ocean', False, False, 'aiHorde', None)
}

settlementDict: dict[int, settlementData] = {
     0: settlementData('wh3_main_combi_region_zlatlan', 'regular', 610, 123, 'wh2_main_lzd_zlatan', 'jungle', 'Zlatlan'),
     1: settlementData('wh3_main_combi_region_floating_village', 'regular', 683, 372, 'wh3_main_ie_vmp_sires_of_mourkain', 'wasteland', 'Floating Village'),
     2: settlementData('wh3_main_combi_region_shrine_of_khaine', 'regular', 258, 663, 'wh2_main_def_scourge_of_khaine', 'wasteland', 'Shrine of Khaine'),
     3: settlementData('wh3_main_combi_region_mordheim', 'regular', 675, 661, 'wh2_dlc15_skv_clan_kreepus', 'temperate', 'Mordheim'),
     4: settlementData('wh3_main_combi_region_zoishenk', 'regular', 645, 794, 'wh3_main_ksl_ungol_kindred', 'frozen', 'Zoishenk'),
     5: settlementData('wh3_main_combi_region_black_pyramid_of_nagash', 'regular', 579, 283, 'wh2_dlc09_tmb_the_sentinels', 'desert', 'Black Pyramid of Nagash'),
     6: settlementData('wh3_main_combi_region_hanyu_port', 'regular', 1127, 494, 'wh3_main_cth_dissenter_lords_of_jinshen', 'temperate', 'Hanyu Port'),
     7: settlementData('wh3_main_combi_region_tor_yvresse', 'regular', 316, 574, 'wh2_main_hef_yvresse', 'temperate island', 'Tor Yvresse'),
     8: settlementData('wh3_main_combi_region_aquitaine', 'regular', 421, 569, 'wh3_main_brt_aquitaine', 'temperate', 'Aquitaine'),
     9: settlementData('wh3_main_combi_region_the_monolith_of_katam', 'dark fortress', 451, 864, 'wh_main_nor_varg', 'frozen', 'The Monolith of Katam'),
     10: settlementData('wh3_main_combi_region_helmgart', 'regular', 487, 603, 'wh_main_emp_empire', 'temperate', 'Helmgart'),
     11: settlementData('wh3_main_combi_region_beichai', 'regular', 1356, 554, 'wh3_dlc21_cst_dead_flag_fleet', 'temperate', 'Beichai'),
     12: settlementData('wh3_main_combi_region_lashiek', 'regular', 448, 315, 'wh2_main_brt_knights_of_the_flame', 'desert', 'Lashiek'),
     13: settlementData('wh3_main_combi_region_steingart', 'regular', 620, 565, 'wh_main_grn_black_venom', 'temperate', 'Steingart'),
     14: settlementData('wh3_main_combi_region_floating_mountain', 'regular', 1025, 790, 'wh3_dlc20_nor_dolgan', 'chaotic wasteland', 'Floating Mountain'),
     15: settlementData('wh3_main_combi_region_shrine_of_ladrielle', 'regular', 224, 777, 'wh2_main_def_karond_kar', 'frozen', 'Shrine of Ladrielle'),
     16: settlementData('wh3_main_combi_region_quatar', 'regular', 678, 277, 'wh2_dlc09_tmb_numas', 'desert', 'Quatar'),
     17: settlementData('wh3_main_combi_region_ancient_city_of_quintex', 'dark fortress', 73, 592, 'wh2_main_def_cult_of_pleasure', 'frozen', 'Ancient City of Quintex'),
     18: settlementData('wh3_main_combi_region_southern_outpost', 'regular', 1280, 328, 'wh3_dlc26_grn_cluster_eye_tribe', 'jungle', 'Southern Outpost'),
     19: settlementData('wh3_main_combi_region_black_iron_mine', 'regular', 797, 481, 'wh_main_dwf_karak_azul', 'mountain', 'Black Iron Mine'),
     20: settlementData('wh3_main_combi_region_vulture_mountain', 'regular', 454, 289, 'wh2_main_dwf_greybeards_prospectors', 'mountain', 'Vulture Mountain'),
     21: settlementData('wh3_main_combi_region_dragons_crossroad', 'regular', 1221, 684, 'wh3_main_cth_imperial_wardens', 'frozen', "Dragon's Crossroad"),
     22: settlementData('wh3_main_combi_region_niedling', 'regular', 653, 640, 'wh_main_emp_stirland', 'temperate', 'Niedling'),
     23: settlementData('wh3_main_combi_region_bleak_hold_fortress', 'regular', 89, 618, 'wh3_dlc24_ksl_daughters_of_the_forest', 'frozen', 'Bleak Hold Fortress'),
     24: settlementData('wh3_main_combi_region_dargoth', 'regular', 249, 858, 'wh3_main_grn_da_cage_breakaz', 'frozen', 'Dargoth'),
     25: settlementData('wh3_main_combi_region_nagenhof', 'regular', 717, 682, 'wh_main_emp_ostermark', 'temperate', 'Nagenhof'),
     26: settlementData('wh3_main_combi_region_the_copper_landing', 'regular', 113, 172, 'wh3_main_tmb_deserters_of_khatep', 'desert', 'The Copper Landing'),
     27: settlementData('wh3_main_combi_region_tor_surpindar', 'regular', 612, 77, 'wh3_main_tze_sarthoraels_watchers', 'savannah', 'Tor Surpindar'),
     28: settlementData('wh3_main_combi_region_pools_of_despair', 'regular', 523, 304, 'wh2_dlc09_tmb_rakaph_dynasty', 'desert', 'Pools of Despair'),
     29: settlementData('wh3_main_combi_region_karak_angazhar', 'regular', 629, 531, 'wh3_main_ogr_disciples_of_the_maw', 'mountain', 'Karak Angazhar'),
     30: settlementData('wh3_main_combi_region_the_black_pillar', 'regular', 214, 849, 'wh3_main_grn_da_cage_breakaz', 'frozen', 'The Black Pillar'),
     31: settlementData('wh3_main_combi_region_temple_avenue_of_gold', 'regular', 718, 120, 'wh3_main_skv_clan_morbidus', 'jungle', 'Temple Avenue of Gold'),
     32: settlementData('wh3_main_combi_region_massif_orcal', 'regular', 458, 567, 'wh2_dlc15_grn_broken_axe', 'mountain', 'Massif Orcal'),
     33: settlementData('wh3_main_combi_region_white_tower_of_hoeth', 'regular', 295, 562, 'wh2_main_hef_saphery', 'temperate island', 'White Tower of Hoeth'),
     34: settlementData('wh3_main_combi_region_winter_pyre', 'regular', 678, 866, 'wh_main_nor_aesling', 'frozen', 'Winter Pyre'),
     35: settlementData('wh3_main_combi_region_swamp_town', 'regular', 91, 459, 'wh2_main_emp_new_world_colonies', 'savannah', 'Swamp Town'),
     36: settlementData('wh3_main_combi_region_kemperbad', 'regular', 565, 637, 'wh_main_emp_talabecland', 'temperate', 'Kemperbad'),
     37: settlementData('wh3_main_combi_region_shrine_of_loec', 'regular', 311, 511, 'wh2_dlc15_grn_skull_crag', 'temperate island', 'Shrine of Loec'),
     38: settlementData('wh3_main_combi_region_karak_eight_peaks', 'regular', 761, 459, 'wh_main_grn_necksnappers', 'mountain', 'Karak Eight Peaks'),
     39: settlementData('wh3_main_combi_region_the_palace_of_ruin', 'dark fortress', 230, 904, None, 'frozen', 'The Palace of Ruin'),
     40: settlementData('wh3_main_combi_region_barag_dawazbag', 'regular', 709, 509, 'wh_main_grn_scabby_eye', 'wasteland', 'Barag Dawazbag'),
     41: settlementData('wh3_main_combi_region_nahuontl', 'regular', 562, 146, 'wh2_dlc12_grn_leaf_cutterz_tribe', 'jungle', 'Nahuontl'),
     42: settlementData('wh3_main_combi_region_deff_gorge', 'regular', 717, 354, 'wh3_main_kho_exiles_of_khorne', 'mountain', 'Deff Gorge'),
     43: settlementData('wh3_main_combi_region_wei_jin', 'dark fortress', 1276, 649, 'wh3_main_cth_celestial_loyalists', 'temperate', 'Wei Jin'),
     44: settlementData('wh3_main_combi_region_griffon_gate', 'regular', 196, 594, 'wh2_main_hef_tiranoc', 'temperate island', 'Griffon Gate'),
     45: settlementData('wh3_main_combi_region_shattered_cove', 'regular', 999, 417, 'wh3_main_lzd_tepoks_spawn', 'temperate', 'Shattered Stone Bay'),
     46: settlementData('wh3_main_combi_region_wurtbad', 'regular', 607, 634, 'wh_main_emp_stirland', 'temperate', 'Wurtbad'),
     47: settlementData('wh3_main_combi_region_shard_bastion', 'regular', 314, 900, 'wh2_main_nor_aghol', 'frozen', 'Shard Bastion'),
     48: settlementData('wh3_main_combi_region_isle_of_wights', 'regular', 351, 723, 'wh_dlc08_nor_vanaheimlings', 'frozen', 'Isle of Wights'),
     49: settlementData('wh3_main_combi_region_ghrond', 'regular', 157, 841, 'wh2_main_def_ghrond', 'frozen', 'Ghrond'),
     50: settlementData('wh3_main_combi_region_skavenblight', 'regular', 465, 461, 'wh2_main_skv_clan_skryre', 'wasteland', 'Skavenblight'),
     51: settlementData('wh3_main_combi_region_caverns_of_sotek', 'regular', 673, 106, 'wh3_main_skv_clan_morbidus', 'jungle', 'Caverns of Sotek'),
     52: settlementData('wh3_main_combi_region_oakenhammer', 'regular', 715, 590, 'wh_main_dwf_zhufbar', 'mountain', 'Oakenhammer'),
     53: settlementData('wh3_main_combi_region_tor_dranil', 'regular', 198, 627, 'wh2_main_def_scourge_of_khaine', 'wasteland', 'Tor Dranil'),
     54: settlementData('wh3_main_combi_region_the_black_forests', 'regular', 207, 725, 'wh2_main_def_the_forgebound', 'frozen', 'The Black Forests'),
     55: settlementData('wh3_main_combi_region_stormvrack_mount', 'regular', 809, 828, 'wh3_dlc26_kho_arbaal', 'mountain', 'Stormvrack Mount'),
     56: settlementData('wh3_main_combi_region_terracotta_graveyard', 'regular', 1200, 631, 'wh3_main_cth_rebel_lords_of_nan_yang', 'temperate', 'Terracotta Graveyard'),
     57: settlementData('wh3_main_combi_region_the_awakening', 'regular', 276, 262, 'wh2_dlc11_cst_vampire_coast', 'jungle', 'The Awakening'),
     58: settlementData('wh3_main_combi_region_palace_of_princes', 'regular', 404, 893, 'wh3_main_sla_subtle_torture', 'chaotic wasteland', 'Palace of Princes'),
     59: settlementData('wh3_main_combi_region_xahutec', 'regular', 204, 307, 'wh2_main_lzd_tlaxtlan', 'jungle', 'Xahutec'),
     60: settlementData('wh3_main_combi_region_the_writhing_fortress', 'dark fortress', 915, 887, 'wh3_main_sla_exquisite_pain', 'chaotic wasteland', 'The Writhing Fortress'),
     61: settlementData('wh3_main_combi_region_elisia', 'regular', 299, 640, 'wh2_main_hef_chrace', 'temperate island', 'Elisia'),
     62: settlementData('wh3_main_combi_region_mount_silverspear', 'regular', 831, 541, 'wh3_main_grn_moon_howlerz', 'mountain', 'Mount Silverspear'),
     63: settlementData('wh3_main_combi_region_wellsprings_of_eternity', 'regular', 71, 357, 'wh2_main_def_blood_hall_coven', 'jungle', 'Wellsprings of Eternity'),
     64: settlementData('wh3_main_combi_region_tower_of_gorgoth', 'dark fortress', 904, 527, 'wh3_dlc23_chd_minor_faction', 'mountain', 'Tower of Gorgoth'),
     65: settlementData('wh3_main_combi_region_sarl_encampment', 'regular', 586, 846, 'wh_main_nor_sarl', 'mountain', 'Sarl Encampment'),
     66: settlementData('wh3_main_combi_region_fort_jakova', 'regular', 740, 702, 'wh_main_nor_baersonling', 'temperate', 'Fort Jakova'),
     67: settlementData('wh3_main_combi_region_miragliano', 'regular', 497, 456, 'wh_main_teb_tilea', 'temperate', 'Miragliano'),
     68: settlementData('wh3_main_combi_region_nuja', 'regular', 381, 426, 'wh_main_teb_estalia', 'temperate', 'Nuja'),
     69: settlementData('wh3_main_combi_region_longship_graveyard', 'regular', 543, 789, 'wh_main_nor_skaeling', 'frozen', 'Longship Graveyard'),
     70: settlementData('wh3_main_combi_region_macu_peaks', 'regular', 53, 457, 'wh3_dlc20_sla_keepers_of_bliss', 'jungle', 'Macu Peaks'),
     71: settlementData('wh3_main_combi_region_norden', 'regular', 594, 770, 'wh_main_emp_nordland', 'temperate', 'Norden'),
     72: settlementData('wh3_main_combi_region_altar_of_spawns', 'regular', 650, 871, 'wh_main_nor_aesling', 'frozen', 'Altar of Spawns'),
     73: settlementData('wh3_main_combi_region_tribeslaughter', 'regular', 847, 782, 'wh3_main_ogr_lazarghs', 'frozen', 'Tribeslaughter'),
     74: settlementData('wh3_main_combi_region_sump_pit', 'regular', 806, 433, 'wh_main_dwf_karak_azul', 'mountain', 'Sump Pit'),
     75: settlementData('wh3_main_combi_region_grenzstadt', 'regular', 648, 573, 'wh_main_emp_averland', 'temperate', 'Grenzstadt'),
     76: settlementData('wh3_main_combi_region_the_dust_gate', 'regular', 140, 156, 'wh3_main_tmb_deserters_of_khatep', 'desert', 'The Dust Gate'),
     77: settlementData('wh3_main_combi_region_kappelburg', 'regular', 653, 708, 'wh_main_emp_talabecland', 'temperate', 'Kappelburg'),
     78: settlementData('wh3_main_combi_region_nan_gau', 'dark fortress', 1138, 656, 'wh3_main_cth_the_northern_provinces', 'temperate', 'Nan Gau'),
     79: settlementData('wh3_main_combi_region_numas', 'regular', 651, 297, 'wh2_dlc09_tmb_numas', 'desert', 'Numas'),
     80: settlementData('wh3_main_combi_region_lyonesse', 'regular', 362, 631, 'wh_main_brt_lyonesse', 'temperate', 'Lyonesse'),
     81: settlementData('wh3_main_combi_region_lybaras', 'regular', 825, 317, 'wh2_dlc09_tmb_lybaras', 'desert', 'Lybaras'),
     82: settlementData('wh3_main_combi_region_the_bleeding_spire', 'regular', 923, 837, 'wh3_dlc20_nor_kul', 'chaotic wasteland', 'The Bleeding Spire'),
     83: settlementData('wh3_main_combi_region_copher', 'regular', 473, 341, 'wh2_dlc14_brt_chevaliers_de_lyonesse', 'desert', 'Copher'),
     84: settlementData('wh3_main_combi_region_nagashizzar', 'regular', 848, 405, 'wh3_main_skv_clan_carrion', 'wasteland', 'Nagashizzar'),
     85: settlementData('wh3_main_combi_region_sunken_khernarch', 'regular', 647, 362, 'wh3_main_ie_vmp_sires_of_mourkain', 'wasteland', 'Sunken Khernarch'),
     86: settlementData('wh3_main_combi_region_mangrove_coast', 'regular', 263, 137, 'wh2_main_lzd_southern_sentinels', 'jungle', 'Mangrove Coast'),
     87: settlementData('wh3_main_combi_region_grimtop', 'regular', 1050, 489, 'wh3_main_ogr_crossed_clubs', 'mountain', 'Grimtop'),
     88: settlementData('wh3_main_combi_region_the_moon_shard', 'regular', 134, 567, 'wh2_main_def_bleak_holds', 'frozen', 'The Moon Shard'),
     89: settlementData('wh3_main_combi_region_flayed_rock', 'regular', 992, 471, 'wh3_main_skv_clan_treecherik', 'mountain', 'Flayed Rock'),
     90: settlementData('wh3_main_combi_region_eldar_spire', 'regular', 15, 815, 'wh2_main_skv_clan_septik', 'mountain', 'Eldar Spire'),
     91: settlementData('wh3_main_combi_region_city_of_the_shugengan', 'regular', 1295, 614, 'wh3_main_cth_celestial_loyalists', 'temperate', 'City of The Shugengan'),
     92: settlementData('wh3_main_combi_region_laurelorn_forest', 'magical forest', 527, 730, 'wh3_main_wef_laurelorn', 'magical forest', 'Laurelorn Forest'),
     93: settlementData('wh3_main_combi_region_monument_of_izzatal', 'regular', 105, 352, 'wh2_dlc12_skv_clan_mange', 'mountain', 'Monument of Izzatal'),
     94: settlementData('wh3_main_combi_region_karaz_a_karak', 'regular', 736, 549, 'wh_main_dwf_dwarfs', 'mountain', 'Karaz-a-Karak'),
     95: settlementData('wh3_main_combi_region_dread_rock', 'regular', 972, 399, 'wh3_main_lzd_tepoks_spawn', 'jungle', 'Dread Rock'),
     96: settlementData('wh3_main_combi_region_village_of_the_moon', 'regular', 1251, 551, 'wh3_main_grn_dimned_sun', 'temperate', 'Village of the Moon'),
     97: settlementData('wh3_main_combi_region_fu_hung', 'regular', 1230, 376, 'wh3_main_cth_burning_wind_nomads', 'temperate', 'Fu Hung'),
     98: settlementData('wh3_main_combi_region_great_desert_of_araby', 'regular', 487, 267, 'wh3_main_ogre_the_famished', '', ''),
     99: settlementData('wh3_main_combi_region_tlaqua', 'regular', 544, 203, 'wh2_main_lzd_tlaqua', 'jungle', 'Tlaqua'),
     100: settlementData('wh3_main_combi_region_skrap_towers', 'regular', 1014, 449, 'wh3_main_skv_clan_treecherik', 'temperate', 'Skrap Towers'),
     101: settlementData('wh3_main_combi_region_fort_oberstyre', 'regular', 668, 621, 'wh_main_vmp_rival_sylvanian_vamps', 'temperate', 'Fort Oberstyre'),
     102: settlementData('wh3_main_combi_region_troll_fjord', 'regular', 386, 795, 'wh_dlc08_nor_norsca', 'frozen', 'Troll Fjord'),
     103: settlementData('wh3_main_combi_region_rackdo_gorge', 'regular', 55, 812, 'wh2_main_skv_clan_septik', 'mountain', 'Rackdo Gorge'),
     104: settlementData('wh3_main_combi_region_zandri', 'regular', 541, 325, 'wh2_main_brt_knights_of_origo', 'desert', 'Zandri'),
     105: settlementData('wh3_main_combi_region_zanbaijin', 'dark fortress', 1002, 838, 'wh3_dlc25_nur_tamurkhan', 'chaotic wasteland', 'Plains of Zanbaijin'),
     106: settlementData('wh3_main_combi_region_kunlan', 'regular', 1251, 587, 'wh3_main_grn_dimned_sun', 'temperate', 'Kunlan'),
     107: settlementData('wh3_main_combi_region_monolith_of_borkill_the_bloody_handed', 'dark fortress', 450, 801, 'wh_main_nor_bjornling', 'mountain', 'Monolith of Borkill The Bloody Handed'),
     108: settlementData('wh3_main_combi_region_venom_glade', 'regular', 142, 709, 'wh2_main_def_clar_karond', 'frozen', 'Venom Glade'),
     109: settlementData('wh3_main_combi_region_xhotl', 'regular', 133, 238, 'wh3_dlc20_nur_pallid_nurslings', 'jungle', 'Xhotl'),
     110: settlementData('wh3_main_combi_region_lost_plateau', 'regular', 704, 243, 'wh2_main_grn_arachnos', 'mountain', 'Lost Plateau'),
     111: settlementData('wh3_main_combi_region_elessaeli', 'regular', 317, 532, 'wh2_dlc15_grn_skull_crag', 'temperate island', 'Elessaeli'),
     112: settlementData('wh3_main_combi_region_spitepeak', 'regular', 789, 417, 'wh_main_dwf_karak_azul', 'mountain', 'Spitepeak'),
     113: settlementData('wh3_main_combi_region_the_gallows_tree', 'regular', 975, 819, 'wh3_dlc27_the_narj', 'chaotic wasteland', 'The Gallows Tree'),
     114: settlementData('wh3_main_combi_region_castle_carcassonne', 'regular', 465, 503, 'wh_main_brt_carcassonne', 'temperate', 'Castle Carcassonne'),
     115: settlementData('wh3_main_combi_region_shrine_of_sotek', 'regular', 47, 427, 'wh2_main_grn_blue_vipers', 'savannah', 'Shrine of Sotek'),
     116: settlementData('wh3_main_combi_region_tower_of_the_sun', 'regular', 981, 133, 'wh3_dlc27_hef_aislinn', 'temperate island', ' Tower of the Sun'),
     117: settlementData('wh3_main_combi_region_fateweavers_crevasse', 'dark fortress', 510, 27, 'wh3_main_tze_oracles_of_tzeentch', 'chaotic wasteland', "Fateweaver's Crevasse"),
     118: settlementData('wh3_main_combi_region_the_godless_crater', 'dark fortress', 235, 22, 'wh2_dlc17_lzd_oxyotl', 'chaotic wasteland', 'The Godless Crater'),
     119: settlementData('wh3_main_combi_region_stonemine_tower', 'regular', 626, 482, 'wh3_main_skv_clan_verms', 'wasteland', 'Stonemine Tower'),
     120: settlementData('wh3_main_combi_region_zavastra', 'regular', 674, 736, 'wh3_main_ksl_the_ice_court', 'temperate', 'Zavastra'),
     121: settlementData('wh3_main_combi_region_rothkar_spire', 'regular', 13, 733, 'wh2_dlc16_grn_naggaroth_orcs', 'desert', 'Rothkar Spire'),
     122: settlementData('wh3_main_combi_region_the_daemons_stump', 'regular', 969, 546, 'wh3_dlc23_chd_minor_faction', 'wasteland', "The Daemon's Stump"),
     123: settlementData('wh3_main_combi_region_xen_wu', 'regular', 1123, 525, 'wh3_main_skv_clan_krizzor', 'temperate', 'Xen Wu'),
     124: settlementData('wh3_main_combi_region_shagrath', 'regular', 319, 853, 'wh2_main_def_deadwood_sentinels', 'frozen', 'Shagrath'),
     125: settlementData('wh3_main_combi_region_clarak_spire', 'regular', 16, 650, 'wh2_dlc09_tmb_exiles_of_nehek', 'wasteland', 'Clarak Spire'),
     126: settlementData('wh3_main_combi_region_martek', 'regular', 489, 317, 'wh2_main_brt_thegans_crusaders', 'mountain', 'Martek'),
     127: settlementData('wh3_main_combi_region_ka_sabar', 'regular', 642, 247, 'wh_main_vmp_vampire_counts', 'desert', 'Ka-Sabar'),
     128: settlementData('wh3_main_combi_region_gateway_to_khuresh', 'regular', 1257, 349, 'wh3_dlc26_grn_cluster_eye_tribe', 'jungle', 'Gateway to Khuresh'),
     129: settlementData('wh3_main_combi_region_cairn_thel', 'regular', 285, 517, 'wh2_dlc15_grn_skull_crag', 'temperate island', 'Cairn Thel'),
     130: settlementData('wh3_main_combi_region_the_folly_of_malofex', 'regular', 470, 908, 'wh3_main_sla_subtle_torture', 'chaotic wasteland', 'The Folly of Malofex'),
     131: settlementData('wh3_main_combi_region_karond_kar', 'regular', 277, 797, 'wh2_main_def_karond_kar', 'frozen', 'Karond Kar'),
     132: settlementData('wh3_main_combi_region_dok_karaz', 'regular', 668, 497, 'wh_main_grn_scabby_eye', 'wasteland', 'Dok Karaz'),
     133: settlementData('wh3_main_combi_region_argalis', 'regular', 538, 417, 'wh_main_teb_border_princes', 'temperate', 'Argalis'),
     134: settlementData('wh3_main_combi_region_storag_kor', 'regular', 72, 727, None, 'mountain', 'Storag Kor'),
     135: settlementData('wh3_main_combi_region_middenheim', 'dark fortress', 554, 706, 'wh_main_emp_middenland', 'temperate', 'Middenheim'),
     136: settlementData('wh3_main_combi_region_languille', 'regular', 384, 661, 'wh_main_vmp_mousillon', 'temperate', "L'Anguille"),
     137: settlementData('wh3_main_combi_region_karak_azorn', 'regular', 996, 567, 'wh3_main_dwf_karak_azorn', 'mountain', 'Karak Azorn'),
     138: settlementData('wh3_main_combi_region_black_tower_of_arkhan', 'regular', 550, 294, 'wh2_dlc09_tmb_rakaph_dynasty', 'desert', 'Black Tower of Arkhan'),
     139: settlementData('wh3_main_combi_region_pillar_of_skulls', 'regular', 876, 802, 'wh3_main_ogr_lazarghs', 'frozen', 'Pillar of Skulls'),
     140: settlementData('wh3_main_combi_region_desolation_of_nagash', 'regular', 819, 411, None, 'wasteland', 'Desolation of Nagash'),
     141: settlementData('wh3_main_combi_region_blackstone_post', 'regular', 457, 623, 'wh2_dlc11_vmp_the_barrow_legion', 'mountain', 'Blackstone Post'),
     142: settlementData('wh3_main_combi_region_the_fortress_of_vorag', 'regular', 889, 438, 'wh2_dlc15_hef_imrik', 'wasteland', 'The Fortress of Vorag'),
     143: settlementData('wh3_main_combi_region_gor_gazan', 'regular', 589, 333, 'wh_main_grn_top_knotz', 'wasteland', 'Gor Gazan'),
     144: settlementData('wh3_main_combi_region_pillars_of_unseen_constellations', 'regular', 59, 332, 'wh2_main_def_blood_hall_coven', 'jungle', 'Pillars of Unseen Constellations'),
     145: settlementData('wh3_main_combi_region_marks_of_the_old_ones', 'regular', 225, 184, 'wh2_main_skv_clan_spittel', 'jungle', 'Marks of The Old Ones'),
     146: settlementData('wh3_main_combi_region_karak_hirn', 'regular', 590, 536, 'wh_main_dwf_karak_hirn', 'mountain', 'Karak Hirn'),
     147: settlementData('wh3_main_combi_region_karak_raziak', 'regular', 759, 669, 'wh3_main_ogr_rock_skulls', 'mountain', 'Karak Raziak'),
     148: settlementData('wh3_main_combi_region_zhufbar', 'regular', 737, 595, 'wh_main_dwf_zhufbar', 'mountain', 'Zhufbar'),
     149: settlementData('wh3_main_combi_region_karak_izor', 'regular', 559, 505, 'wh_main_grn_broken_nose', 'mountain', 'Karak Izor'),
     150: settlementData('wh3_main_combi_region_tai_tzu', 'regular', 1175, 554, 'wh3_main_cth_dissenter_lords_of_jinshen', 'mountain', 'Tai Tzu'),
     151: settlementData('wh3_main_combi_region_wolfenburg', 'regular', 624, 727, 'wh_main_emp_ostland', 'temperate', 'Wolfenburg'),
     152: settlementData('wh3_main_combi_region_weng_chang', 'regular', 1172, 609, 'wh3_main_cth_rebel_lords_of_nan_yang', 'mountain', 'Weng Chang'),
     153: settlementData('wh3_main_combi_region_hergig', 'regular', 601, 702, 'wh_main_emp_hochland', 'temperate', 'Hergig'),
     154: settlementData('wh3_main_combi_region_fallen_gates', 'regular', 44, 510, 'wh3_dlc20_sla_keepers_of_bliss', 'savannah', 'Fallen Gates'),
     155: settlementData('wh3_main_combi_region_tobaro', 'regular', 467, 443, 'wh_main_teb_estalia', 'temperate', 'Tobaro'),
     156: settlementData('wh3_main_combi_region_qiang', 'regular', 1112, 468, 'wh3_main_cth_the_western_provinces', 'temperate', 'Qiang'),
     157: settlementData('wh3_main_combi_region_cuexotl', 'regular', 640, 169, 'wh_main_grn_orcs_of_the_bloody_hand', 'jungle', 'Cuexotl'),
     158: settlementData('wh3_main_combi_region_great_skull_lakes', 'regular', 853, 692, 'wh3_main_grn_slaves_of_zharr', 'wasteland', 'Great Skull Lakes'),
     159: settlementData('wh3_main_combi_region_swartzhafen', 'regular', 674, 593, 'wh_main_vmp_schwartzhafen', 'temperate', 'Schwartzhafen'),
     160: settlementData('wh3_main_combi_region_eye_of_the_panther', 'regular', 481, 307, 'wh2_main_dwf_greybeards_prospectors', 'mountain', 'Eye of the Panther'),
     161: settlementData('wh3_main_combi_region_fortress_of_the_damned', 'dark fortress', 375, 870, 'wh2_main_def_deadwood_sentinels', 'chaotic wasteland', 'Fortress of the Damned'),
     162: settlementData('wh3_main_combi_region_yuatek', 'regular', 602, 101, 'wh2_main_lzd_zlatan', 'jungle', 'Yuatek'),
     163: settlementData('wh3_main_combi_region_the_blood_swamps', 'regular', 239, 235, None, 'jungle', 'The Blood Swamps'),
     164: settlementData('wh3_main_combi_region_red_fortress', 'dark fortress', 1317, 663, 'wh3_main_cth_imperial_wardens', 'chaotic wasteland', 'Red Fortress'),
     165: settlementData('wh3_main_combi_region_desolation_of_drakenmoor', 'regular', 833, 611, 'wh3_main_grn_drippin_fangs', 'wasteland', 'Desolation of Drakenmoor'),
     166: settlementData('wh3_main_combi_region_tor_finu', 'regular', 299, 585, 'wh2_main_hef_saphery', 'temperate island', 'Tor Finu'),
     167: settlementData('wh3_main_combi_region_grimhold', 'regular', 546, 530, 'wh_main_dwf_karak_norn', 'mountain', 'Grimhold'),
     168: settlementData('wh3_main_combi_region_the_galleons_graveyard', 'regular', 257, 448, 'wh2_dlc11_cst_noctilus', 'ocean', "The Galleon's Graveyard"),
     169: settlementData('wh3_main_combi_region_sartosa', 'regular', 492, 390, 'wh2_dlc11_cst_pirates_of_sartosa', 'temperate', 'Sartosa'),
     170: settlementData('wh3_main_combi_region_hag_hall', 'regular', 106, 644, 'wh2_main_def_drackla_coven', 'frozen', 'Hag Hall'),
     171: settlementData('wh3_main_combi_region_montfort', 'regular', 474, 593, 'wh_main_brt_bastonne', 'temperate', 'Montfort'),
     172: settlementData('wh3_main_combi_region_essen', 'regular', 693, 662, 'wh_main_emp_ostermark', 'temperate', 'Essen'),
     173: settlementData('wh3_main_combi_region_fort_soll', 'regular', 582, 542, 'wh_main_grn_black_venom', 'temperate', 'Fort Soll'),
     174: settlementData('wh3_main_combi_region_bechafen', 'regular', 677, 716, 'wh_main_emp_ostermark', 'temperate', 'Bechafen'),
     175: settlementData('wh3_main_combi_region_krugenheim', 'regular', 634, 654, 'wh_main_emp_talabecland', 'temperate', 'Krugenheim'),
     176: settlementData('wh3_main_combi_region_mahrak', 'regular', 772, 320, 'wh2_main_vmp_the_silver_host', 'desert', 'Mahrak'),
     177: settlementData('wh3_main_combi_region_daemons_gate', 'dark fortress', 463, 57, 'wh3_main_tze_flaming_scribes', 'chaotic wasteland', "Daemon's Gate"),
     178: settlementData('wh3_main_combi_region_mine_of_the_bearded_skulls', 'regular', 120, 217, 'wh2_main_dwf_spine_of_sotek_dwarfs', 'mountain', 'Mine of The Bearded Skulls'),
     179: settlementData('wh3_main_combi_region_tor_koruali', 'regular', 331, 606, 'wh2_main_hef_cothique', 'temperate island', 'Tor Koruali'),
     180: settlementData('wh3_main_combi_region_hell_pit', 'regular', 705, 807, 'wh2_main_skv_clan_moulder', 'wasteland', 'Hell Pit'),
     181: settlementData('wh3_main_combi_region_mighdal_vongalbarak', 'regular', 650, 554, 'wh_main_dwf_karak_hirn', 'mountain', 'Mighdal Vongalbarak'),
     182: settlementData('wh3_main_combi_region_fortress_of_eyes', 'regular', 1163, 704, 'wh3_main_chs_khazag', 'chaotic wasteland', 'Fortress of Eyes'),
     183: settlementData('wh3_main_combi_region_mousillon', 'regular', 382, 605, 'wh_main_vmp_mousillon', 'temperate', 'Mousillon'),
     184: settlementData('wh3_main_combi_region_mistnar', 'regular', 331, 634, 'wh2_main_hef_cothique', 'temperate island', 'Mistnar'),
     185: settlementData('wh3_main_combi_region_the_burning_monolith', 'regular', 848, 896, 'wh3_main_kho_bloody_sword', 'chaotic wasteland', 'The Burning Monolith'),
     186: settlementData('wh3_main_combi_region_soteks_trail', 'regular', 710, 163, 'wh3_main_skv_clan_morbidus', 'jungle', "Sotek's Trail"),
     187: settlementData('wh3_main_combi_region_temple_of_elemental_winds', 'regular', 1156, 441, 'wh3_main_cth_burning_wind_nomads', 'temperate', 'Temple of Elemental Winds'),
     188: settlementData('wh3_main_combi_region_kraka_drak', 'regular', 709, 841, 'wh3_dlc25_dwf_malakai', 'mountain', 'Kraka Drak'),
     189: settlementData('wh3_main_combi_region_tor_elasor', 'regular', 911, 78, 'wh3_main_cst_dread_rock_privateers', 'temperate island', 'Tor Elasor'),
     190: settlementData('wh3_main_combi_region_tor_elyr', 'regular', 206, 558, 'wh2_main_hef_ellyrion', 'temperate island', 'Tor Elyr'),
     191: settlementData('wh3_main_combi_region_karak_vlag', 'dark fortress', 817, 756, 'wh_dlc08_nor_goromadny_tribe', 'mountain', 'Karak Vlag'),
     192: settlementData('wh3_main_combi_region_karak_vrag', 'regular', 1010, 656, 'wh3_main_ogr_fulg', 'mountain', 'Karak Vrag'),
     193: settlementData('wh3_main_combi_region_the_cursed_jungle', 'regular', 744, 215, 'wh2_main_skv_clan_mordkin', 'jungle', 'The Cursed Jungle'),
     194: settlementData('wh3_main_combi_region_karag_dromar', 'regular', 675, 562, 'wh_main_dwf_zhufbar', 'mountain', 'Karag Dromar'),
     195: settlementData('wh3_main_combi_region_erengrad', 'regular', 634, 770, 'wh3_main_ksl_the_great_orthodoxy', 'temperate', 'Erengrad'),
     196: settlementData('wh3_main_combi_region_frozen_landing', 'regular', 761, 820, None, 'frozen', 'Frozen Landing'),
     197: settlementData('wh3_main_combi_region_fort_straghov', 'regular', 670, 806, 'wh3_main_ksl_druzhina_enclave', 'frozen', 'Fort Straghov'),
     198: settlementData('wh3_main_combi_region_monolith_of_festerlung', 'regular', 820, 868, 'wh3_main_kho_bloody_sword', 'chaotic wasteland', 'Monolith of Festerlung'),
     199: settlementData('wh3_main_combi_region_clar_karond', 'regular', 117, 726, 'wh2_main_def_clar_karond', 'frozen', 'Clar Karond'),
     200: settlementData('wh3_main_combi_region_agrul_migdhal', 'regular', 653, 331, 'wh_main_grn_top_knotz', 'wasteland', 'Agrul Migdhal'),
     201: settlementData('wh3_main_combi_region_the_falls_of_doom', 'regular', 910, 652, 'wh3_dlc23_chd_conclave', 'wasteland', 'The Falls of Doom'),
     202: settlementData('wh3_main_combi_region_castle_artois', 'regular', 410, 639, 'wh_main_brt_artois', 'temperate', 'Castle Artois'),
     203: settlementData('wh3_main_combi_region_tower_of_the_stars', 'regular', 936, 173, 'wh3_main_cst_dread_rock_privateers', 'temperate island', 'Tower of the Stars'),
     204: settlementData('wh3_main_combi_region_chupayotl', 'regular', 251, 163, 'wh2_main_lzd_southern_sentinels', 'savannah', 'Chupayotl'),
     205: settlementData('wh3_main_combi_region_karak_azul', 'regular', 799, 452, 'wh_main_dwf_karak_azul', 'mountain', 'Karak Azul'),
     206: settlementData('wh3_main_combi_region_brionne', 'regular', 420, 527, 'wh2_dlc14_grn_red_cloud', 'temperate', 'Brionne'),
     207: settlementData('wh3_main_combi_region_wizard_caliphs_palace', 'regular', 437, 269, 'wh2_dlc09_tmb_followers_of_nagash', 'desert', "Wizard Caliph's Palace"),
     208: settlementData('wh3_main_combi_region_the_frozen_city', 'dark fortress', 284, 872, 'wh2_main_def_deadwood_sentinels', 'frozen', 'The Frozen City'),
     209: settlementData('wh3_main_combi_region_ruins_end', 'regular', 947, 427, 'wh3_main_ogr_thunderguts', 'wasteland', "Ruin's End"),
     210: settlementData('wh3_main_combi_region_the_high_sentinel', 'regular', 120, 404, 'wh2_main_grn_blue_vipers', 'savannah', 'The High Sentinel'),
     211: settlementData('wh3_main_combi_region_black_creek_spire', 'regular', 269, 768, 'wh2_main_def_karond_kar', 'frozen', 'Black Creek Spire'),
     212: settlementData('wh3_main_combi_region_shattered_stone_isle', 'regular', 999, 384, 'wh3_main_lzd_tepoks_spawn', 'jungle', 'Shattered Stone Isle'),
     213: settlementData('wh3_main_combi_region_khemri', 'regular', 612, 289, 'wh2_dlc09_tmb_khemri', 'desert', 'Khemri'),
     214: settlementData('wh3_main_combi_region_karak_zorn', 'regular', 682, 221, 'wh2_dlc17_dwf_thorek_ironbrow', 'mountain', 'Karak Zorn'),
     215: settlementData('wh3_main_combi_region_the_black_pit', 'regular', 510, 705, 'wh_dlc03_grn_black_pit', 'mountain', 'The Black Pit'),
     216: settlementData('wh3_main_combi_region_the_pillars_of_grungni', 'regular', 762, 547, 'wh_main_grn_bloody_spearz', 'mountain', 'The Pillars of Grungni'),
     217: settlementData('wh3_main_combi_region_temple_of_addaioth', 'regular', 76, 689, 'wh2_main_def_drackla_coven', 'frozen', 'Temple of Addaioth'),
     218: settlementData('wh3_main_combi_region_shrine_of_kurnous', 'regular', 267, 642, 'wh3_main_sla_seducers_of_slaanesh', 'temperate island', 'Shrine of Kurnous'),
     219: settlementData('wh3_main_combi_region_deaths_head_monoliths', 'regular', 497, 200, 'wh2_dlc12_grn_leaf_cutterz_tribe', 'desert', 'Dead-Head Monoliths'),
     220: settlementData('wh3_main_combi_region_kauark', 'regular', 202, 872, 'wh3_main_grn_da_cage_breakaz', 'frozen', 'Kauark'),
     221: settlementData('wh3_main_combi_region_howling_rock', 'regular', 869, 592, 'wh3_main_grn_drippin_fangs', 'wasteland', 'Howling Rock'),
     222: settlementData('wh3_main_combi_region_darkhold', 'regular', 899, 478, 'wh3_main_grn_dark_land_orcs', 'wasteland', 'Darkhold'),
     223: settlementData('wh3_main_combi_region_tlax', 'regular', 259, 289, 'wh2_dlc11_cst_vampire_coast_rebels', 'jungle', 'Tlax'),
     224: settlementData('wh3_main_combi_region_zhanshi', 'regular', 1275, 519, 'wh3_main_cth_the_jade_custodians', 'temperate', 'Zhanshi'),
     225: settlementData('wh3_main_combi_region_temple_of_khaine', 'regular', 89, 788, None, 'frozen', 'Temple of Khaine'),
     226: settlementData('wh3_main_combi_region_the_star_tower', 'regular', 280, 214, 'wh2_main_skv_clan_spittel', 'jungle', 'The Star Tower'),
     227: settlementData('wh3_main_combi_region_hualotal', 'regular', 99, 309, 'wh3_dlc26_kho_skulltaker', 'mountain', 'Hualotal'),
     228: settlementData('wh3_main_combi_region_karak_norn', 'regular', 534, 571, 'wh_main_dwf_karak_norn', 'mountain', 'Karak Norn'),
     229: settlementData('wh3_main_combi_region_the_lost_palace', 'regular', 570, 19, 'wh3_main_nur_bubonic_swarm', 'chaotic wasteland', 'The Lost Palace'),
     230: settlementData('wh3_main_combi_region_whitefire_tor', 'regular', 219, 582, 'wh2_main_hef_ellyrion', 'temperate island', 'Whitefire Tor'),
     231: settlementData('wh3_main_combi_region_gristle_valley', 'regular', 561, 548, None, 'mountain', 'Gristle Valley'),
     232: settlementData('wh3_main_combi_region_riffraffa', 'regular', 519, 435, 'wh_main_teb_tilea', 'temperate', 'Rifraffa'),
     233: settlementData('wh3_main_combi_region_shrine_of_the_alchemist', 'regular', 1124, 599, 'wh3_main_cth_dissenter_lords_of_jinshen', 'desert', 'Shrine of The Alchemist'),
     234: settlementData('wh3_dlc20_combi_region_glacier_encampment', 'regular', 79, 903, 'wh2_main_nor_mung', 'frozen', 'Glacier Encampment'),
     235: settlementData('wh3_main_combi_region_crucible_of_delights', 'regular', 772, 16, 'wh3_main_sla_rapturous_excess', 'chaotic wasteland', 'Crucible of Delights'),
     236: settlementData('wh3_main_combi_region_phoenix_gate', 'regular', 245, 619, 'wh2_main_def_scourge_of_khaine', 'temperate island', 'Phoenix Gate'),
     237: settlementData('wh3_main_combi_region_vale_of_titans', 'regular', 1060, 560, None, 'mountain', 'Vale of Titans'),
     238: settlementData('wh3_main_combi_region_igerov', 'regular', 751, 729, 'wh_main_nor_baersonling', 'temperate', 'Igerov'),
     239: settlementData('wh3_main_combi_region_blood_mountain', 'regular', 420, 923, 'wh3_main_kho_crimson_skull', 'chaotic wasteland', 'Blood Mountain'),
     240: settlementData('wh3_main_combi_region_the_blood_hall', 'regular', 26, 332, 'wh3_dlc27_sla_masque_of_slaanesh', 'temperate island', 'The Blood Hall'),
     241: settlementData('wh3_main_combi_region_volcanos_heart', 'regular', 697, 941, 'wh3_main_tze_all_seeing_eye', 'chaotic wasteland', "Volcano's Heart"),
     242: settlementData('wh3_main_combi_region_altar_of_the_crimson_harvest', 'dark fortress', 503, 783, 'wh_main_nor_skaeling', 'frozen', 'Altar of The Crimson Harvest'),
     243: settlementData('wh3_main_combi_region_salzenmund', 'regular', 557, 757, 'wh_main_emp_nordland', 'temperate', 'Salzenmund'),
     244: settlementData('wh3_main_combi_region_sjoktraken', 'regular', 726, 828, 'wh3_main_nur_maggoth_kin', 'frozen', 'Sjoktraken'),
     245: settlementData('wh3_main_combi_region_dringorackaz', 'regular', 756, 416, 'wh_main_dwf_karak_azul', 'mountain', 'Dringorackaz'),
     246: settlementData('wh3_main_combi_region_granite_massif', 'regular', 755, 306, None, 'mountain', 'Granite Massif'),
     247: settlementData('wh3_main_combi_region_chimai', 'regular', 1313, 521, 'wh3_dlc21_cst_dead_flag_fleet', 'temperate', 'Chimai'),
     248: settlementData('wh3_main_combi_region_okkams_forever_maze', 'dark fortress', 709, 28, 'wh3_main_sla_rapturous_excess', 'chaotic wasteland', "Okkam's Forever Maze"),
     249: settlementData('wh3_main_combi_region_sorcerers_islands', 'regular', 420, 309, 'wh2_dlc09_tmb_followers_of_nagash', 'desert', "Sorcerer's Island"),
     250: settlementData('wh3_main_combi_region_the_southern_sentinels', 'regular', 224, 133, 'wh2_main_lzd_southern_sentinels', 'savannah', 'The Southern Sentinels'),
     251: settlementData('wh3_main_combi_region_chamber_of_visions', 'regular', 71, 273, 'wh2_main_lzd_sentinels_of_xeti', 'jungle', 'Chamber of Visions'),
     252: settlementData('wh3_main_combi_region_the_oak_of_ages', 'magical forest', 513, 531, 'wh_dlc05_wef_wood_elves', 'magical forest', 'The Oak of Ages'),
     253: settlementData('wh3_main_combi_region_grey_rock_point', 'regular', 106, 543, 'wh2_main_def_ssildra_tor', 'frozen', 'Grey Rock Point'),
     254: settlementData('wh3_main_combi_region_vauls_anvil_naggaroth', 'regular', 126, 670, 'wh2_main_def_drackla_coven', 'frozen', "Vaul's Anvil (Naggaroth)"),
     255: settlementData('wh3_main_combi_region_the_never_ending_chasm', 'regular', 281, 18, 'wh3_main_kho_brazen_throne', 'chaotic wasteland', 'The Never Ending Chasm'),
     256: settlementData('wh3_main_combi_region_waterfall_palace', 'magical forest', 515, 566, 'wh_dlc05_wef_argwylon', 'magical forest', 'Waterfall Palace'),
     257: settlementData('wh3_main_combi_region_fort_bergbres', 'regular', 449, 636, 'wh_main_emp_marienburg', 'temperate', 'Fort Bergbres'),
     258: settlementData('wh3_dlc20_combi_region_glacial_gardens', 'regular', 173, 892, None, 'frozen', 'Glacial Gardens'),
     259: settlementData('wh3_main_combi_region_serpent_jetty', 'regular', 416, 848, 'wh_main_nor_varg', 'frozen', 'Serpent Jetty'),
     260: settlementData('wh3_main_combi_region_chill_road', 'regular', 130, 833, 'wh2_main_def_ghrond', 'frozen', 'Chill Road'),
     261: settlementData('wh3_dlc20_combi_region_dragons_death', 'regular', 1035, 756, 'wh3_dlc20_nor_dolgan', 'chaotic wasteland', "Dragon's Death"),
     262: settlementData('wh3_main_combi_region_graeling_moot', 'regular', 479, 829, 'wh_dlc08_nor_naglfarlings', 'mountain', 'Graeling Moot'),
     263: settlementData('wh3_main_combi_region_li_zhu', 'regular', 1367, 470, 'wh3_main_cth_eastern_river_lords', 'temperate', 'Li Zhu'),
     264: settlementData('wh3_main_combi_region_snake_gate', 'regular', 1175, 665, 'wh3_main_cth_imperial_wardens', 'temperate', 'Snake Gate'),
     265: settlementData('wh3_main_combi_region_port_elistor', 'regular', 284, 541, 'wh2_main_hef_saphery', 'temperate island', 'Port Elistor'),
     266: settlementData('wh3_main_combi_region_eilhart', 'regular', 482, 639, 'wh_main_emp_empire_separatists', 'temperate', 'Eilhart'),
     267: settlementData('wh3_main_combi_region_black_rock', 'dark fortress', 583, 938, 'wh3_main_tze_broken_wheel', 'chaotic wasteland', 'Black Rock'),
     268: settlementData('wh3_main_combi_region_grom_peak', 'regular', 768, 589, 'wh_main_grn_red_eye', 'mountain', 'Grom Peak'),
     269: settlementData('wh3_main_combi_region_valley_of_horns', 'regular', 1000, 523, 'wh3_main_ogr_sons_of_the_mountain', 'mountain', 'Valley of Horns'),
     270: settlementData('wh3_main_combi_region_celestial_monastery', 'regular', 1234, 533, 'wh3_main_cth_the_jade_custodians', 'temperate', 'Celestial Monastery'),
     271: settlementData('wh3_main_combi_region_zvorak', 'regular', 581, 490, 'wh_main_teb_border_princes', 'temperate', 'Zvorak'),
     272: settlementData('wh3_main_combi_region_dragon_gate', 'regular', 1209, 666, 'wh3_main_cth_imperial_wardens', 'temperate', 'Dragon Gate'),
     273: settlementData('wh3_main_combi_region_xlanhuapec', 'regular', 215, 264, 'wh2_main_lzd_xlanhuapec', 'jungle', 'Xlanhuapec'),
     274: settlementData('wh3_main_combi_region_slavers_point', 'regular', 238, 753, 'wh2_main_def_karond_kar', 'frozen', "Slaver's Point"),
     275: settlementData('wh3_main_combi_region_kislev', 'regular', 719, 736, 'wh3_main_ksl_the_ice_court', 'temperate', 'Kislev'),
     276: settlementData('wh3_main_combi_region_flensburg', 'regular', 587, 618, 'wh_main_emp_stirland', 'temperate', 'Flensburg'),
     277: settlementData('wh3_main_combi_region_dragonhorn_mines', 'regular', 647, 424, 'wh3_main_skv_clan_verms', 'wasteland', 'Dragonhorn Mines'),
     278: settlementData('wh3_main_combi_region_vauls_anvil_loren', 'magical forest', 502, 551, 'wh_dlc05_wef_torgovann', 'magical forest', "Vaul's Anvil (Athel Loren)"),
     279: settlementData('wh3_main_combi_region_varenka_hills', 'regular', 702, 529, 'wh_main_dwf_barak_varr', 'wasteland', 'Varenka Hills'),
     280: settlementData('wh3_main_combi_region_jade_wind_mountain', 'regular', 1284, 558, 'wh3_main_grn_dimned_sun', 'temperate', 'Jade Wind Mountain'),
     281: settlementData('wh3_main_combi_region_karak_kadrin', 'regular', 748, 644, 'wh_main_dwf_karak_kadrin', 'mountain', 'Karak Kadrin'),
     282: settlementData('wh3_main_combi_region_granite_spikes', 'regular', 1076, 703, 'wh3_dlc23_chd_zhatan', 'chaotic wasteland', 'Granite Spikes'),
     283: settlementData('wh3_main_combi_region_xlanzec', 'regular', 241, 109, 'wh2_dlc12_lzd_cult_of_sotek', 'savannah', 'Xlanzec'),
     284: settlementData('wh3_main_combi_region_bloodwind_keep', 'dark fortress', 1244, 719, 'wh3_main_chs_khazag', 'chaotic wasteland', 'Bloodwind Keep'),
     285: settlementData('wh3_main_combi_region_dotternbach', 'regular', 546, 583, 'wh3_dlc25_vmp_the_court_of_night', 'temperate', 'Dotternbach'),
     286: settlementData('wh3_main_combi_region_dietershafen', 'regular', 526, 762, 'wh_main_emp_nordland', 'temperate', 'Dietershafen'),
     287: settlementData('wh3_main_combi_region_nuln', 'dark fortress', 553, 607, 'wh_main_emp_wissenland', 'temperate', 'Nuln'),
     288: settlementData('wh3_main_combi_region_karak_krakaten', 'regular', 1003, 491, 'wh3_main_ogr_goldtooth', 'mountain', 'Karak Krakaten'),
     289: settlementData('wh3_main_combi_region_mountain_pass', 'regular', 1322, 335, 'wh3_dlc26_grn_cluster_eye_tribe', 'mountain', 'Mountain Pass'),
     290: settlementData('wh3_main_combi_region_citadel_of_lead', 'regular', 355, 763, 'wh3_dlc20_tze_the_sightless', 'frozen', 'Citadel of Lead'),
     291: settlementData('wh3_main_combi_region_gnobbly_gorge', 'regular', 1072, 436, 'wh3_main_skv_clan_treecherik', 'temperate', 'Gnobbly Gorge'),
     292: settlementData('wh3_main_combi_region_bitterstone_mine', 'regular', 660, 451, 'wh_main_grn_teef_snatchaz', 'wasteland', 'Bitterstone Mine'),
     293: settlementData('wh3_main_combi_region_quetza', 'regular', 186, 219, 'wh3_dlc20_nur_pallid_nurslings', 'jungle', 'Quetza'),
     294: settlementData('wh3_main_combi_region_haichai', 'regular', 1352, 622, 'wh2_dlc11_def_the_blessed_dread', 'temperate', 'Haichai'),
     295: settlementData('wh3_main_combi_region_oyxl', 'regular', 183, 187, 'wh2_main_skv_clan_pestilens', 'jungle', 'Oyxl'),
     296: settlementData('wh3_main_combi_region_avethir', 'regular', 187, 546, 'wh2_main_hef_tiranoc', 'temperate island', 'Avethir'),
     297: settlementData('wh3_main_combi_region_akendorf', 'regular', 678, 540, 'wh_main_teb_border_princes', 'temperate', 'Akendorf'),
     298: settlementData('wh3_main_combi_region_khymerica_spire', 'regular', 29, 705, 'wh2_dlc16_grn_naggaroth_orcs', 'desert', 'Khymerica Spire'),
     299: settlementData('wh3_dlc23_combi_region_gash_kadrak', 'regular', 943, 601, 'wh3_dlc23_chd_conclave', 'wasteland', 'Vale of Woe'),
     300: settlementData('wh3_main_combi_region_castle_alexandronov', 'regular', 613, 792, 'wh3_main_ksl_the_great_orthodoxy', 'frozen', 'Castle Alexandronov'),
     301: settlementData('wh3_main_combi_region_eagle_gate', 'regular', 189, 572, 'wh2_main_hef_ellyrion', 'temperate island', 'Eagle Gate'),
     302: settlementData('wh3_main_combi_region_spite_reach', 'regular', 190, 845, 'wh3_main_grn_da_cage_breakaz', 'frozen', 'Spite Reach'),
     303: settlementData('wh3_main_combi_region_zharr_naggrund', 'dark fortress', 943, 628, 'wh3_dlc23_chd_conclave', 'wasteland', 'Zharr Naggrund'),
     304: settlementData('wh3_main_combi_region_eschen', 'regular', 714, 635, 'wh_main_vmp_rival_sylvanian_vamps', 'temperate', 'Eschen'),
     305: settlementData('wh3_main_combi_region_montenas', 'regular', 414, 454, 'wh_main_teb_estalia', 'temperate', 'Montenas'),
     306: settlementData('wh3_main_combi_region_al_haikk', 'regular', 511, 332, 'wh2_main_vmp_strygos_empire', 'desert', 'Al Haikk'),
     307: settlementData('wh3_main_combi_region_drackla_spire', 'regular', 21, 781, 'wh3_main_dwf_the_ancestral_throng', 'mountain', 'Drackla Spire'),
     308: settlementData('wh3_main_combi_region_turtle_gate', 'regular', 1246, 665, 'wh3_main_cth_imperial_wardens', 'temperate', 'Turtle Gate'),
     309: settlementData('wh3_dlc20_combi_region_krudenwald', 'regular', 574, 716, 'wh_main_emp_hochland', 'temperate', 'Krudenwald'),
     310: settlementData('wh3_main_combi_region_tor_achare', 'regular', 295, 619, 'wh2_main_hef_chrace', 'temperate island', 'Tor Achare'),
     311: settlementData('wh3_main_combi_region_quittax', 'regular', 142, 301, 'wh3_dlc20_tze_apostles_of_change', 'jungle', 'Quittax'),
     312: settlementData('wh3_dlc23_combi_region_uzkulak_port', 'regular', 859, 740, 'wh_dlc08_nor_goromadny_tribe', 'mountain', 'Fort Dwarslav'),
     313: settlementData('wh3_main_combi_region_karak_ungor', 'regular', 772, 694, 'wh3_main_ogr_rock_skulls', 'mountain', 'Karak Ungor'),
     314: settlementData('wh3_main_combi_region_bitter_bay', 'regular', 884, 404, None, 'wasteland', 'Bitter Bay'),
     315: settlementData('wh3_main_combi_region_altdorf', 'regular', 527, 648, 'wh_main_emp_empire', 'temperate', 'Altdorf'),
     316: settlementData('wh3_main_combi_region_altar_of_facades', 'regular', 826, 30, 'wh3_main_sla_rapturous_excess', 'chaotic wasteland', 'Altar of Facades'),
     317: settlementData('wh3_main_combi_region_the_sacred_pools', 'magical forest', 153, 261, 'wh2_dlc16_lzd_wardens_of_the_living_pools', 'magical forest', 'The Sacred Pools'),
     318: settlementData('wh3_main_combi_region_the_skull_carvers_abode', 'regular', 664, 12, 'wh3_main_nur_bubonic_swarm', 'chaotic wasteland', "The Skull Carver's Abode"),
     319: settlementData('wh3_main_combi_region_the_haunted_forest', 'magical forest', 1066, 418, 'wh3_main_vmp_caravan_of_blue_roses', 'magical forest', 'The Haunted Forest'),
     320: settlementData('wh3_main_combi_region_temple_of_skulls', 'regular', 771, 248, 'wh2_main_skv_clan_mordkin', 'jungle', 'Temple of Skulls'),
     321: settlementData('wh3_main_combi_region_dusk_peaks', 'regular', 281, 105, 'wh2_main_hef_citadel_of_dusk', 'savannah', 'Dusk Peaks'),
     322: settlementData('wh3_main_combi_region_yetchitch', 'regular', 742, 798, None, 'frozen', 'Yetchitch'),
     323: settlementData('wh3_main_combi_region_itza', 'regular', 168, 239, 'wh2_main_lzd_itza', 'jungle', 'Itza'),
     324: settlementData('wh3_main_combi_region_grung_zint', 'regular', 434, 650, 'wh_main_grn_skullsmasherz', 'mountain', 'Grung Zint'),
     325: settlementData('wh3_main_combi_region_bhagar', 'regular', 598, 246, 'wh2_dlc09_tmb_dune_kingdoms', 'desert', 'Bhagar'),
     326: settlementData('wh3_main_combi_region_crag_halls_of_findol', 'magical forest', 528, 544, 'wh_dlc05_wef_wydrioth', 'magical forest', 'Crag Halls of Findol'),
     327: settlementData('wh3_main_combi_region_el_kalabad', 'regular', 532, 273, 'wh2_dlc09_tmb_rakaph_dynasty', 'desert', 'El Kalabad'),
     328: settlementData('wh3_main_combi_region_thrice_cursed_peak', 'regular', 151, 172, 'wh2_main_dwf_spine_of_sotek_dwarfs', 'mountain', 'Thrice Cursed Peak'),
     329: settlementData('wh3_main_combi_region_cragroth_deep', 'regular', 103, 766, None, 'mountain', 'Cragroth Deep'),
     330: settlementData('wh3_main_combi_region_citadel_of_dusk', 'regular', 302, 89, 'wh2_main_hef_citadel_of_dusk', 'savannah', 'Citadel of Dusk'),
     331: settlementData('wh3_main_combi_region_crookback_mountain', 'regular', 844, 520, 'wh2_dlc09_skv_clan_rictus', 'mountain', 'Crookback Mountain'),
     332: settlementData('wh3_main_combi_region_volksgrad', 'regular', 749, 778, 'wh3_main_ksl_ropsmenn_clan', 'frozen', 'Volksgrad'),
     333: settlementData('wh3_main_combi_region_hoteks_column', 'regular', 173, 718, 'wh2_main_def_the_forgebound', 'frozen', "Hotek's Column"),
     334: settlementData('wh3_main_combi_region_the_crystal_spires', 'dark fortress', 749, 926, 'wh3_main_tze_all_seeing_eye', 'chaotic wasteland', 'The Crystal Spires'),
     335: settlementData('wh3_main_combi_region_ming_zhu', 'regular', 1242, 612, 'wh3_main_cth_celestial_loyalists', 'temperate', 'Ming Zhu'),
     336: settlementData('wh3_main_combi_region_parravon', 'regular', 483, 575, 'wh_main_brt_parravon', 'temperate', 'Parravon'),
     337: settlementData('wh3_main_combi_region_barak_varr', 'regular', 672, 512, 'wh_main_dwf_barak_varr', 'mountain', 'Barak Varr'),
     338: settlementData('wh3_main_combi_region_gaean_vale', 'magical forest', 256, 579, 'wh2_main_hef_avelorn', 'magical forest', 'Gaean Vale'),
     339: settlementData('wh3_main_combi_region_fuming_serpent', 'regular', 286, 232, None, 'jungle', 'Fuming Serpent'),
     340: settlementData('wh3_main_combi_region_village_of_the_tigermen', 'regular', 1189, 414, 'wh3_main_cth_burning_wind_nomads', 'temperate', 'Village of The Tigermen'),
     341: settlementData('wh3_main_combi_region_castle_bastonne', 'regular', 428, 602, 'wh_main_brt_bastonne', 'temperate', 'Castle Bastonne'),
     342: settlementData('wh3_main_combi_region_amblepeak', 'regular', 1027, 546, 'wh3_main_ogr_sons_of_the_mountain', 'mountain', 'Amblepeak'),
     343: settlementData('wh3_main_combi_region_har_kaldra', 'regular', 81, 847, 'wh2_main_skv_clan_septik', 'frozen', 'Har Kaldra'),
     344: settlementData('wh3_main_combi_region_gisoreux', 'regular', 438, 627, 'wh_main_brt_artois', 'temperate', 'Gisoreux'),
     345: settlementData('wh3_main_combi_region_li_temple', 'regular', 1339, 449, 'wh3_main_cth_eastern_river_lords', 'mountain', 'Li Temple'),
     346: settlementData('wh3_main_combi_region_foundry_of_bones', 'regular', 1295, 697, 'wh3_dlc20_nor_yusak', 'chaotic wasteland', 'Foundry of Bones'),
     347: settlementData('wh3_main_combi_region_black_fang', 'regular', 976, 639, 'wh3_main_ogr_fulg', 'mountain', 'Black Fang'),
     348: settlementData('wh3_main_combi_region_aarnau', 'regular', 459, 724, 'wh_main_emp_marienburg', 'temperate', 'Aarnau'),
     349: settlementData('wh3_main_combi_region_eagle_eyries', 'regular', 962, 665, 'wh_main_grn_greenskins', 'mountain', 'Eagle Eyries'),
     350: settlementData('wh3_main_combi_region_gryphon_wood', 'magical forest', 669, 682, 'wh2_dlc16_wef_drycha', 'magical forest', 'Gryphon Wood'),
     351: settlementData('wh3_main_combi_region_carroburg', 'regular', 509, 656, 'wh_main_emp_middenland', 'temperate', 'Carroburg'),
     352: settlementData('wh3_main_combi_region_xing_po', 'regular', 1200, 571, 'wh2_main_skv_clan_eshin', 'mountain', 'Xing Po'),
     353: settlementData('wh3_main_combi_region_praag', 'regular', 723, 770, 'wh3_main_ksl_ropsmenn_clan', 'frozen', 'Praag'),
     354: settlementData('wh3_main_combi_region_tower_of_lysean', 'regular', 228, 526, 'wh2_main_def_cult_of_excess', 'temperate island', 'Tower of Lysean'),
     355: settlementData('wh3_main_combi_region_naggarond', 'regular', 112, 813, 'wh2_main_def_naggarond', 'frozen', 'Naggarond'),
     356: settlementData('wh3_main_combi_region_great_hall_of_greasus', 'regular', 1030, 503, 'wh3_main_ogr_goldtooth', 'mountain', 'Great Hall of Greasus'),
     357: settlementData('wh3_main_combi_region_the_blighted_grove', 'regular', 560, 953, 'wh3_main_tze_broken_wheel', 'chaotic wasteland', 'The Blighted Grove'),
     358: settlementData('wh3_main_combi_region_talabheim', 'regular', 604, 690, 'wh_main_emp_talabecland', 'temperate', 'Talabheim'),
     359: settlementData('wh3_main_combi_region_rasetra', 'regular', 766, 287, 'wh2_main_vmp_the_silver_host', 'desert', 'Rasetra'),
     360: settlementData('wh3_main_combi_region_the_twisted_towers', 'dark fortress', 485, 939, 'wh3_main_sla_subtle_torture', 'chaotic wasteland', 'The Twisted Towers'),
     361: settlementData('wh3_main_combi_region_the_bone_gulch', 'regular', 841, 423, 'wh2_dlc15_dwf_clan_helhein', 'mountain', 'The Bone Gulch'),
     362: settlementData('wh3_main_combi_region_tlaxtlan', 'regular', 164, 324, 'wh2_main_lzd_tlaxtlan', 'jungle', 'Tlaxtlan'),
     363: settlementData('wh3_main_combi_region_the_sentinel_of_time', 'regular', 190, 152, 'wh2_main_lzd_southern_sentinels', 'savannah', 'The Sentinel of Time'),
     364: settlementData('wh3_main_combi_region_ubersreik', 'regular', 505, 614, 'wh_main_emp_empire_separatists', 'temperate', 'Ubersreik'),
     365: settlementData('wh3_main_combi_region_fort_ostrosk', 'regular', 680, 786, 'wh3_main_ksl_druzhina_enclave', 'frozen', 'Fort Ostrosk'),
     366: settlementData('wh3_main_combi_region_plain_of_tuskers', 'regular', 560, 229, 'wh2_dlc09_tmb_dune_kingdoms', 'desert', 'Plain of Tuskers'),
     367: settlementData('wh3_main_combi_region_volulltrax', 'regular', 630, 24, 'wh3_main_nur_bubonic_swarm', 'chaotic wasteland', 'Volulltrax'),
     368: settlementData('wh3_main_combi_region_gronti_mingol', 'regular', 585, 413, 'wh_main_grn_top_knotz', 'wasteland', 'Gronti Mingol'),
     369: settlementData('wh3_main_combi_region_yhetee_peak', 'regular', 1071, 619, 'wh3_main_ogr_mountaineaters', 'mountain', 'Yhetee Peak'),
     370: settlementData('wh3_main_combi_region_bay_of_blades', 'regular', 582, 814, 'wh3_main_ksl_brotherhood_of_the_bear', 'frozen', 'Bay of Blades'),
     371: settlementData('wh3_main_combi_region_unicorn_gate', 'regular', 216, 611, 'wh2_main_hef_ellyrion', 'temperate island', 'Unicorn Gate'),
     372: settlementData('wh3_main_combi_region_ironspike', 'regular', 43, 547, 'wh2_main_def_ssildra_tor', 'frozen', 'Ironspike'),
     373: settlementData('wh3_main_combi_region_teotiqua', 'regular', 740, 187, 'wh2_main_skv_clan_mordkin', 'jungle', 'Teotiqua'),
     374: settlementData('wh3_main_combi_region_shang_wu', 'regular', 1164, 479, 'wh3_dlc21_vmp_jiangshi_rebels', 'savannah', 'Shang-Wu'),
     375: settlementData('wh3_main_combi_region_plain_of_spiders', 'regular', 40, 677, 'wh2_dlc16_grn_naggaroth_orcs', 'wasteland', 'Plain of Spiders'),
     376: settlementData('wh3_main_combi_region_bloodpeak', 'regular', 1043, 600, 'wh3_main_ogr_blood_guzzlers', 'mountain', 'Bloodpeak'),
     377: settlementData('wh3_main_combi_region_weismund', 'regular', 529, 681, 'wh_main_emp_middenland', 'temperate', 'Weismund'),
     378: settlementData('wh3_main_combi_region_gnashraks_lair', 'regular', 792, 643, 'wh_main_grn_red_eye', 'mountain', "Gnashrak's Lair"),
     379: settlementData('wh3_main_combi_region_evershale', 'regular', 240, 595, 'wh2_main_def_scourge_of_khaine', 'temperate island', 'Evershale'),
     380: settlementData('wh3_main_combi_region_scarpels_lair', 'regular', 15, 600, 'wh2_dlc16_skv_clan_gritus', 'mountain', "Scarpel's Lair"),
     381: settlementData('wh3_main_combi_region_shroktak_mount', 'regular', 57, 768, None, 'mountain', 'Shroktak Mount'),
     382: settlementData('wh3_main_combi_region_ssildra_tor', 'regular', 64, 535, 'wh2_main_def_ssildra_tor', 'frozen', "S'sildra Tor"),
     383: settlementData('wh3_main_combi_region_naglfari_plain', 'regular', 552, 838, 'wh_dlc08_nor_naglfarlings', 'frozen', 'Naglfari Plain'),
     384: settlementData('wh3_main_combi_region_tor_saroir', 'regular', 270, 601, 'wh2_main_def_scourge_of_khaine', 'temperate island', 'Tor Saroir'),
     385: settlementData('wh3_main_combi_region_dai_cheng', 'regular', 1371, 381, 'wh3_dlc21_nor_wyrmkins', 'temperate', 'Dai Cheng'),
     386: settlementData('wh3_main_combi_region_ice_rock_gorge', 'regular', 74, 645, None, 'mountain', 'Ice Rock Gorge'),
     387: settlementData('wh3_main_combi_region_bridge_of_heaven', 'regular', 1231, 497, 'wh3_dlc21_vmp_jiangshi_rebels', 'savannah', 'Bridge of Heaven'),
     388: settlementData('wh3_main_combi_region_marienburg', 'regular', 452, 657, 'wh_main_emp_marienburg', 'temperate', 'Marienburg'),
     389: settlementData('wh3_main_combi_region_ash_ridge_mountains', 'regular', 862, 459, 'wh2_dlc15_dwf_clan_helhein', 'mountain', 'Ash Ridge Mountains'),
     390: settlementData('wh3_main_combi_region_quenelles', 'regular', 481, 540, 'wh_main_brt_parravon', 'temperate', 'Quenelles'),
     391: settlementData('wh3_main_combi_region_axlotl', 'regular', 207, 231, 'wh2_main_lzd_xlanhuapec', 'jungle', 'Axlotl'),
     392: settlementData('wh3_main_combi_region_plesk', 'regular', 765, 754, 'wh3_main_ksl_ropsmenn_clan', 'frozen', 'Plesk'),
     393: settlementData('wh3_main_combi_region_the_witchwood', 'magical forest', 66, 660, 'wh2_dlc16_wef_sisters_of_twilight', 'magical forest', 'The Witchwood'),
     394: settlementData('wh3_main_combi_region_jungles_of_chian', 'magical forest', 1303, 386, 'wh3_dlc21_wef_spirits_of_shanlin', 'magical forest', "Chi'an"),
     395: settlementData('wh3_main_combi_region_golden_ziggurat', 'regular', 37, 282, 'wh2_main_lzd_sentinels_of_xeti', 'temperate island', 'Golden Ziggurat'),
     396: settlementData('wh3_main_combi_region_skeggi', 'regular', 126, 513, 'wh2_main_nor_skeggi', 'savannah', 'Skeggi'),
     397: settlementData('wh3_main_combi_region_the_moot', 'regular', 648, 601, 'wh_main_emp_stirland', 'temperate', 'The Moot'),
     398: settlementData('wh3_main_combi_region_har_ganeth', 'regular', 212, 827, 'wh2_main_def_har_ganeth', 'frozen', 'Har Ganeth'),
     399: settlementData('wh3_main_combi_region_karag_orrud', 'regular', 720, 309, 'wh2_main_grn_arachnos', 'mountain', 'Karag Orrud'),
     400: settlementData('wh3_main_combi_region_mount_athull', 'regular', 299, 36, 'wh3_main_kho_brazen_throne', 'chaotic wasteland', 'Mount Athull'),
     401: settlementData('wh3_main_combi_region_worlds_edge_archway', 'regular', 819, 563, 'wh_main_grn_bloody_spearz', '', ''),
     402: settlementData('wh3_main_combi_region_black_fortress', 'dark fortress', 950, 479, 'wh3_dlc23_chd_legion_of_azgorh', 'wasteland', 'Black Fortress'),
     403: settlementData('wh3_main_combi_region_port_reaver', 'regular', 98, 481, 'wh2_main_emp_new_world_colonies', 'savannah', 'Port Reaver'),
     404: settlementData('wh3_main_combi_region_chaqua', 'regular', 174, 273, 'wh3_dlc20_tze_apostles_of_change', 'jungle', 'Chaqua'),
     405: settlementData('wh3_main_combi_region_vitevo', 'regular', 709, 711, 'wh_main_nor_baersonling', 'temperate', 'Vitevo'),
     406: settlementData('wh3_main_combi_region_morgheim', 'regular', 685, 409, 'wh3_main_ie_vmp_sires_of_mourkain', 'wasteland', 'Morgheim'),
     407: settlementData('wh3_main_combi_region_kradtommen', 'regular', 747, 392, 'wh_main_grn_red_fangs', 'mountain', 'Kradtommen'),
     408: settlementData('wh3_main_combi_region_ekrund', 'regular', 634, 444, 'wh_main_grn_teef_snatchaz', 'wasteland', 'Ekrund'),
     409: settlementData('wh3_main_combi_region_khazid_bordkarag', 'regular', 687, 823, 'wh3_main_nur_maggoth_kin', 'mountain', 'Lair of the Troll King'),
     410: settlementData('wh3_main_combi_region_shang_yang', 'dark fortress', 1127, 554, 'wh3_main_cth_dissenter_lords_of_jinshen', 'desert', 'Shang Yang'),
     411: settlementData('wh3_main_combi_region_blacklight_tower', 'regular', 210, 793, 'wh2_main_def_karond_kar', 'frozen', 'Blacklight Tower'),
     412: settlementData('wh3_main_combi_region_the_howling_citadel', 'dark fortress', 790, 913, 'wh3_main_kho_bloody_sword', 'chaotic wasteland', 'The Howling Citadel'),
     413: settlementData('wh3_main_combi_region_monolith_of_bubonicus', 'regular', 853, 848, 'wh3_main_sla_exquisite_pain', 'chaotic wasteland', 'Monolith of Bubonicus'),
     414: settlementData('wh3_main_combi_region_statues_of_the_gods', 'regular', 545, 175, 'wh2_dlc12_grn_leaf_cutterz_tribe', 'jungle', 'Statues of The Gods'),
     415: settlementData('wh3_main_combi_region_infernius', 'regular', 430, 946, 'wh3_main_kho_crimson_skull', 'chaotic wasteland', 'Infernius'),
     416: settlementData('wh3_main_combi_region_subatuun', 'regular', 146, 201, 'wh2_main_skv_clan_pestilens', 'jungle', 'Subatuun'),
     417: settlementData('wh3_main_combi_region_novchozy', 'regular', 782, 768, 'wh3_main_ksl_ropsmenn_clan', 'frozen', 'Novchozy'),
     418: settlementData('wh3_main_combi_region_gorssel', 'regular', 460, 681, 'wh_main_emp_marienburg', 'temperate', 'Gorssel'),
     419: settlementData('wh3_main_combi_region_po_mei', 'regular', 1228, 649, 'wh3_main_cth_rebel_lords_of_nan_yang', 'temperate', 'Po Mei'),
     420: settlementData('wh3_main_combi_region_pahuax', 'regular', 92, 430, 'wh2_main_grn_blue_vipers', 'jungle', 'Pahuax'),
     421: settlementData('wh3_main_combi_region_karak_azgaraz', 'regular', 505, 592, None, 'mountain', 'Karak Azgaraz'),
     422: settlementData('wh3_main_combi_region_vauls_anvil_ulthuan', 'regular', 204, 511, 'wh2_main_hef_caledor', 'temperate island', "Vaul's Anvil (Ulthuan)"),
     423: settlementData('wh3_main_combi_region_the_gates_of_zharr', 'regular', 916, 564, 'wh3_dlc23_chd_minor_faction', 'wasteland', 'The Gates of Zharr'),
     424: settlementData('wh3_main_combi_region_ziggurat_of_dawn', 'regular', 92, 517, 'wh2_main_nor_skeggi', 'jungle', 'Ziggurat of Dawn'),
     425: settlementData('wh3_main_combi_region_karak_bhufdar', 'regular', 529, 499, 'wh_main_grn_broken_nose', 'mountain', 'Karak Bhufdar'),
     426: settlementData('wh3_main_combi_region_nonchang', 'regular', 1271, 493, 'wh3_main_cth_the_jade_custodians', 'temperate', 'Nonchang'),
     427: settlementData('wh3_main_combi_region_wissenburg', 'regular', 577, 586, 'wh3_dlc25_vmp_the_court_of_night', 'temperate', 'Wissenburg'),
     428: settlementData('wh3_main_combi_region_fortress_of_dawn', 'regular', 545, 68, 'wh2_main_hef_order_of_loremasters', 'temperate island', 'Fortress of Dawn'),
     429: settlementData('wh3_main_combi_region_fyrus', 'regular', 495, 350, 'wh2_main_vmp_strygos_empire', 'desert', 'Fyrus'),
     430: settlementData('wh3_main_combi_region_the_volary', 'dark fortress', 1111, 716, 'wh3_dlc23_chd_zhatan', 'chaotic wasteland', 'The Volary'),
     431: settlementData('wh3_main_combi_region_altar_of_the_horned_rat', 'regular', 245, 206, 'wh2_main_skv_clan_spittel', 'jungle', 'Altar of The Horned Rat'),
     432: settlementData('wh3_main_combi_region_cliff_of_beasts', 'regular', 527, 933, 'wh3_main_tze_broken_wheel', 'chaotic wasteland', 'Cliff of Beasts'),
     433: settlementData('wh3_main_combi_region_fallen_king_mountain', 'regular', 788, 627, 'wh_main_grn_red_eye', 'mountain', 'Fallen King Mountain'),
     434: settlementData('wh3_main_combi_region_forest_of_gloom', 'magical forest', 703, 549, 'wh2_dlc16_grn_creeping_death', 'magical forest', 'Forest of Gloom'),
     435: settlementData('wh3_main_combi_region_bilious_cliffs', 'regular', 608, 922, 'wh3_dlc25_nur_epidemius', 'chaotic wasteland', 'Bilious Cliffs'),
     436: settlementData('wh3_main_combi_region_baleful_hills', 'regular', 1190, 503, 'wh3_dlc21_vmp_jiangshi_rebels', 'savannah', 'Baleful Hills'),
     437: settlementData('wh3_main_combi_region_the_silvered_tower_of_sorcerers', 'dark fortress', 377, 937, 'wh3_main_kho_crimson_skull', 'chaotic wasteland', 'The Silvered Tower of Sorcerers'),
     438: settlementData('wh3_main_combi_region_silver_pinnacle', 'regular', 824, 660, 'wh3_main_vmp_lahmian_sisterhood', 'mountain', 'Silver Pinnacle'),
     439: settlementData('wh3_main_combi_region_konquata', 'dark fortress', 345, 745, 'wh3_dlc20_tze_the_sightless', 'jungle', 'Konquata'),
     440: settlementData('wh3_main_combi_region_castle_drakenhof', 'regular', 716, 612, 'wh_main_vmp_schwartzhafen', 'temperate', 'Castle Drakenhof'),
     441: settlementData('wh3_main_combi_region_hidden_landing', 'regular', 1373, 325, 'wh3_dlc27_sla_the_tormentors', 'jungle', 'Hidden Landing'),
     442: settlementData('wh3_main_combi_region_sabre_mountain', 'regular', 935, 700, 'wh3_main_ogr_sabreskin', 'mountain', 'Sabre Mountain'),
     443: settlementData('wh3_main_combi_region_bamboo_crossing', 'regular', 1262, 431, 'wh3_main_cth_burning_wind_nomads', 'temperate', 'Bamboo Crossing'),
     444: settlementData('wh3_main_combi_region_bilbali', 'regular', 399, 480, 'wh_main_teb_estalia', 'temperate', 'Bilbali'),
     445: settlementData('wh3_main_combi_region_pox_marsh', 'regular', 298, 283, 'wh2_dlc11_cst_vampire_coast_rebels', 'jungle', 'Pox Marsh'),
     446: settlementData('wh3_main_combi_region_floating_pyramid', 'regular', 104, 394, 'wh3_dlc24_cth_the_celestial_court', 'jungle', 'Floating Pyramid'),
     447: settlementData('wh3_main_combi_region_forest_of_arnheim', 'regular', 110, 601, 'wh2_main_def_bleak_holds', 'frozen', 'Forest of Arnheim'),
     448: settlementData('wh3_main_combi_region_kings_glade', 'magical forest', 512, 519, 'wh_dlc05_wef_wood_elves', 'magical forest', "King's Glade"),
     449: settlementData('wh3_main_combi_region_waili_village', 'regular', 1267, 383, 'wh3_main_cth_burning_wind_nomads', 'jungle', 'Wai-Li Village'),
     450: settlementData('wh3_main_combi_region_antoch', 'regular', 604, 219, 'wh2_dlc09_tmb_dune_kingdoms', 'desert', 'Antoch'),
     451: settlementData('wh3_main_combi_region_doom_glade', 'regular', 809, 282, 'wh2_main_vmp_the_silver_host', 'desert', 'Doom Glade'),
     452: settlementData('wh3_main_combi_region_valayas_sorrow', 'regular', 737, 446, 'wh_main_grn_necksnappers', 'wasteland', "Valaya's Sorrow"),
     453: settlementData('wh3_main_combi_region_the_forbidden_citadel', 'regular', 619, 849, 'wh_main_nor_aesling', 'mountain', 'The Forbidden Citadel'),
     454: settlementData('wh3_main_combi_region_shi_wu', 'regular', 1365, 417, 'wh3_main_cth_eastern_river_lords', 'mountain', 'Shi Wu'),
     455: settlementData('wh3_main_combi_region_karak_dum', 'dark fortress', 887, 764, 'wh3_main_ogr_lazarghs', 'mountain', 'Karak Dum'),
     456: settlementData('wh3_main_combi_region_springs_of_eternal_life', 'regular', 628, 268, 'wh2_main_vmp_necrarch_brotherhood', 'desert', 'Springs of Eternal Life'),
     457: settlementData('wh3_main_combi_region_spektazuma', 'regular', 87, 378, 'wh2_dlc12_skv_clan_mange', 'jungle', 'Spektazuma'),
     458: settlementData('wh3_main_combi_region_plain_of_dogs', 'regular', 40, 633, 'wh2_dlc16_skv_clan_gritus', 'mountain', 'Plain of Dogs'),
     459: settlementData('wh3_main_combi_region_bordeleaux', 'regular', 393, 580, 'wh3_main_brt_aquitaine', 'temperate', 'Bordeleaux'),
     460: settlementData('wh3_main_combi_region_lothern', 'regular', 254, 513, 'wh2_main_hef_eataine', 'temperate island', 'Lothern'),
     461: settlementData('wh3_main_combi_region_tower_of_ashung', 'regular', 1330, 366, 'wh3_dlc21_nor_wyrmkins', 'jungle', 'Tower of Ashung'),
     462: settlementData('wh3_main_combi_region_titans_notch', 'regular', 1047, 635, 'wh3_main_ogr_mountaineaters', 'mountain', "Titan's Notch"),
     463: settlementData('wh3_main_combi_region_averheim', 'regular', 615, 599, 'wh_main_emp_averland', 'temperate', 'Averheim'),
     464: settlementData('wh3_main_combi_region_temple_of_tlencan', 'regular', 215, 335, 'wh_main_brt_bordeleaux', 'jungle', 'Bregonne'),
     465: settlementData('wh3_main_combi_region_dragon_fang_mount', 'regular', 970, 350, 'wh3_main_nur_poxmakers_of_nurgle', 'jungle', 'Dragon Fang Mount'),
     466: settlementData('wh3_main_combi_region_karak_azgal', 'regular', 714, 395, 'wh_main_grn_red_fangs', 'mountain', 'Karak Azgal'),
     467: settlementData('wh3_main_combi_region_tlanxla', 'regular', 125, 331, 'wh2_main_lzd_tlaxtlan', 'jungle', 'Tlanxla'),
     468: settlementData('wh3_main_combi_region_lahmia', 'regular', 798, 347, 'wh2_main_vmp_the_silver_host', 'desert', 'Lahmia'),
     469: settlementData('wh3_main_combi_region_misty_mountain', 'regular', 782, 385, 'wh2_main_skv_clan_mors', 'mountain', 'Misty Mountain'),
     470: settlementData('wh3_main_combi_region_tralinia', 'regular', 344, 562, 'wh2_dlc15_grn_skull_crag', 'temperate island', 'Tralinia'),
     471: settlementData('wh3_main_combi_region_khazid_irkulaz', 'regular', 800, 676, 'wh2_dlc15_grn_bonerattlaz', 'mountain', 'Khazid Irkulaz'),
     472: settlementData('wh3_main_combi_region_sun_tree_glades', 'regular', 609, 180, 'wh2_dlc12_grn_leaf_cutterz_tribe', 'jungle', 'Sun-Tree Glades'),
     473: settlementData('wh3_main_combi_region_hag_graef', 'regular', 139, 787, 'wh2_main_def_naggarond', 'frozen', 'Hag Graef'),
     474: settlementData('wh3_main_combi_region_arnheim', 'regular', 147, 588, 'wh2_main_def_bleak_holds', 'frozen', 'Arnheim'),
     475: settlementData('wh3_main_combi_region_the_tower_of_khrakk', 'regular', 632, 821, 'wh3_main_ksl_brotherhood_of_the_bear', 'mountain', 'The Tower of Khrakk'),
     476: settlementData('wh3_main_combi_region_mount_arachnos', 'regular', 713, 267, 'wh2_main_grn_arachnos', 'mountain', 'Mount Arachnos'),
     477: settlementData('wh3_main_combi_region_the_sentinels', 'regular', 947, 510, 'wh3_main_grn_dark_land_orcs', 'wasteland', 'The Sentinels'),
     478: settlementData('wh3_main_combi_region_oreons_camp', 'magical forest', 641, 216, 'wh2_main_wef_bowmen_of_oreon', 'magical forest', "Oreon's Camp"),
     479: settlementData('wh3_main_combi_region_tor_anroc', 'regular', 178, 593, 'wh2_main_hef_tiranoc', 'temperate island', 'Tor Anroc'),
     480: settlementData('wh3_main_combi_region_nan_li', 'regular', 1143, 626, 'wh3_main_cth_rebel_lords_of_nan_yang', 'temperate', 'Nan Li'),
     481: settlementData('wh3_main_combi_region_whitepeak', 'regular', 171, 571, 'wh2_main_hef_tiranoc', 'temperate island', 'Whitepeak'),
     482: settlementData('wh3_main_combi_region_couronne', 'regular', 410, 675, 'wh_main_brt_bretonnia', 'temperate', 'Couronne'),
     483: settlementData('wh3_main_combi_region_mount_thug', 'regular', 1053, 461, 'wh3_main_skv_clan_treecherik', 'temperate', 'Shambletown'),
     484: settlementData('wh3_main_combi_region_the_challenge_stone', 'dark fortress', 1021, 726, 'wh3_main_ogr_fleshgreeders', 'chaotic wasteland', 'The Challenge Stone'),
     485: settlementData('wh3_main_combi_region_petrified_forest', 'regular', 77, 557, 'wh2_main_def_ssildra_tor', 'frozen', 'Petrified Forest'),
     486: settlementData('wh3_main_combi_region_ashrak', 'regular', 135, 862, 'wh2_main_def_ghrond', 'frozen', 'Ashrak'),
     487: settlementData('wh3_main_combi_region_mount_squighorn', 'regular', 779, 535, 'wh_main_grn_bloody_spearz', 'mountain', 'Mount Squighorn'),
     488: settlementData('wh3_main_combi_region_monolith_of_flesh', 'regular', 600, 894, 'wh_dlc08_nor_wintertooth', 'frozen', 'The Monolith of Flesh'),
     489: settlementData('wh3_main_combi_region_karak_ziflin', 'regular', 476, 608, 'wh_main_dwf_karak_ziflin', 'mountain', 'Karak Ziflin'),
     490: settlementData('wh3_main_combi_region_dawns_light', 'regular', 584, 57, 'wh3_main_tze_sarthoraels_watchers', 'savannah', "Dawn's Light"),
     491: settlementData('wh3_main_combi_region_myrmidens', 'regular', 572, 434, 'wh_main_teb_border_princes', 'temperate', 'Myrmidens'),
     492: settlementData('wh3_main_combi_region_kaiax', 'regular', 191, 118, 'wh3_main_skv_clan_skrat', 'savannah', 'Kaiax'),
     493: settlementData('wh3_main_combi_region_mount_gunbad', 'regular', 809, 588, 'wh_main_grn_crooked_moon', 'mountain', 'Mount Gunbad'),
     494: settlementData('wh3_main_combi_region_castle_von_rauken', 'regular', 646, 752, 'wh_main_emp_ostland', 'temperate', 'Castle Von Rauken'),
     495: settlementData('wh3_main_combi_region_temple_of_heimkel', 'regular', 788, 791, 'wh_dlc08_nor_goromadny_tribe', 'frozen', 'Temple of Heimkel'),
     496: settlementData('wh3_main_combi_region_isle_of_the_crimson_skull', 'regular', 62, 407, 'wh3_dlc24_cth_the_celestial_court', 'jungle', 'Isle of the Crimson Skull'),
     497: settlementData('wh3_main_combi_region_port_of_secrets', 'regular', 718, 900, 'wh3_main_tze_all_seeing_eye', 'chaotic wasteland', 'Port of Secrets'),
     498: settlementData('wh3_main_combi_region_galbaraz', 'regular', 624, 377, 'wh_main_grn_top_knotz', 'wasteland', 'Galbaraz'),
     499: settlementData('wh3_main_combi_region_the_tower_of_flies', 'regular', 684, 921, 'wh3_main_tze_all_seeing_eye', 'chaotic wasteland', 'Tower of Flies'),
     500: settlementData('wh3_main_combi_region_the_forest_of_decay', 'regular', 640, 939, 'wh3_dlc25_nur_epidemius', 'chaotic wasteland', 'The Forest of Decay'),
     501: settlementData('wh3_main_combi_region_monument_of_the_moon', 'regular', 145, 455, 'wh2_main_emp_new_world_colonies', 'jungle', 'Monument of The Moon'),
     502: settlementData('wh3_main_combi_region_magritta', 'regular', 417, 428, 'wh_main_teb_estalia', 'temperate', 'Magritta'),
     503: settlementData('wh3_main_combi_region_zarakzil', 'regular', 539, 451, 'wh_main_dwf_karak_izor', 'mountain', 'Zarakzil'),
     504: settlementData('wh3_main_combi_region_serpent_coast', 'regular', 795, 219, 'wh2_main_skv_clan_mordkin', 'jungle', 'Serpent Coast'),
     505: settlementData('wh3_main_combi_region_the_golden_colossus', 'regular', 86, 211, 'wh3_main_tmb_deserters_of_khatep', 'desert', 'The Golden Colossus'),
     506: settlementData('wh3_main_combi_region_icespewer', 'regular', 969, 713, 'wh3_main_grn_tusked_sunz', 'frozen', 'Icespewer'),
     507: settlementData('wh3_main_combi_region_waldenhof', 'regular', 720, 648, 'wh_main_vmp_rival_sylvanian_vamps', 'temperate', 'Waldenhof'),
     508: settlementData('wh3_main_combi_region_altar_of_ultimate_darkness', 'regular', 44, 842, 'wh2_main_skv_clan_septik', 'frozen', 'Altar of Ultimate Darkness'),
     509: settlementData('wh3_main_combi_region_stormhenge', 'regular', 568, 354, 'wh_main_grn_top_knotz', 'wasteland', 'Stormhenge'),
     510: settlementData('wh3_main_combi_region_tor_anlec', 'regular', 234, 650, 'wh2_main_def_scourge_of_khaine', 'wasteland', 'Tor Anlec'),
     511: settlementData('wh3_main_combi_region_fire_mouth', 'regular', 1007, 596, 'wh3_main_ogr_blood_guzzlers', 'mountain', 'Fire Mouth'),
     512: settlementData('wh3_main_combi_region_blizzardpeak', 'regular', 1016, 699, 'wh3_main_grn_tusked_sunz', 'frozen', 'Blizzardpeak'),
     513: settlementData('wh3_main_combi_region_iron_rock', 'regular', 728, 491, 'wh_main_grn_scabby_eye', 'wasteland', 'Iron Rock'),
     514: settlementData('wh3_main_combi_region_pigbarter', 'regular', 971, 458, 'wh3_main_ogr_thunderguts', 'wasteland', 'Pigbarter'),
     515: settlementData('wh3_main_combi_region_the_maw_gate', 'regular', 1065, 514, 'wh3_main_ogr_crossed_clubs', 'mountain', 'The Maw Gate'),
     516: settlementData('wh3_main_combi_region_temple_of_kara', 'regular', 152, 366, 'wh2_dlc13_emp_the_huntmarshals_expedition', 'jungle', 'Temple of Kara'),
     517: settlementData('wh3_dlc23_combi_region_fort_dorznye_vort', 'regular', 885, 692, 'wh3_main_grn_slaves_of_zharr', 'wasteland', 'Fort Dorznye-Vort'),
     518: settlementData('wh3_main_combi_region_sentinels_of_xeti', 'regular', 77, 243, 'wh2_main_lzd_sentinels_of_xeti', 'jungle', 'Sentinels of Xeti'),
     519: settlementData('wh3_main_combi_region_verdanos', 'regular', 557, 451, 'wh_main_teb_border_princes', 'temperate', 'Verdanos'),
     520: settlementData('wh3_main_combi_region_pfeildorf', 'regular', 588, 571, 'wh3_dlc25_vmp_the_court_of_night', 'temperate', 'Pfeildorf'),
     521: settlementData('wh3_main_combi_region_matorca', 'regular', 632, 505, 'wh_main_teb_border_princes', 'temperate', 'Matorca'),
     522: settlementData('wh3_main_combi_region_shrine_of_asuryan', 'regular', 258, 540, 'wh2_main_def_cult_of_excess', 'temperate island', 'Shrine of Asuryan'),
     523: settlementData('wh3_main_combi_region_iron_storm', 'regular', 1198, 710, 'wh3_main_chs_khazag', 'chaotic wasteland', 'Iron Storm'),
     524: settlementData('wh3_main_combi_region_nagrar', 'regular', 271, 836, 'wh3_main_grn_da_cage_breakaz', 'frozen', 'Nagrar'),
     525: settlementData('wh3_main_combi_region_hexoatl', 'regular', 69, 489, 'wh2_main_lzd_hexoatl', 'jungle', 'Hexoatl'),
     526: settlementData('wh3_main_combi_region_the_great_arena', 'regular', 155, 816, 'wh2_main_def_ghrond', 'frozen', 'The Great Arena'),
     527: settlementData('wh3_main_combi_region_castle_of_splendour', 'regular', 754, 48, 'wh3_main_sla_rapturous_excess', 'chaotic wasteland', 'Castle of Splendour'),
     528: settlementData('wh3_main_combi_region_shiyamas_rest', 'regular', 1269, 460, 'wh3_main_cth_the_jade_custodians', 'temperate', "Shiyama's Rest"),
     529: settlementData('wh3_main_combi_region_tor_sethai', 'regular', 206, 530, 'wh2_main_hef_caledor', 'temperate island', 'Tor Sethai'),
     530: settlementData('wh3_main_combi_region_grotrilexs_glare_lighthouse', 'regular', 412, 51, 'wh3_main_tze_flaming_scribes', 'chaotic wasteland', "Grotrilex's Glare Lighthouse"),
     531: settlementData('wh3_main_combi_region_castle_templehof', 'regular', 686, 628, 'wh_main_vmp_rival_sylvanian_vamps', 'temperate', 'Castle Waldenhof'),
     532: settlementData('wh3_main_combi_region_luccini', 'regular', 505, 410, 'wh_main_teb_tilea', 'temperate', 'Luccini'),
     533: settlementData('wh3_main_combi_region_grunburg', 'regular', 548, 623, 'wh_main_emp_empire_separatists', 'temperate', 'Grunurg'),
     534: settlementData('wh3_main_combi_region_brass_keep', 'regular', 592, 737, 'wh3_dlc20_chs_festus', 'mountain', 'Brass Keep'),
     535: settlementData('wh3_main_combi_region_tyrant_peak', 'regular', 21, 573, 'wh2_dlc16_skv_clan_gritus', 'mountain', 'Tyrant Peak'),
     536: settlementData('wh3_main_combi_region_pack_ice_bay', 'regular', 452, 759, 'wh_main_nor_skaeling', 'frozen', 'Pack Ice Bay'),
     537: settlementData('wh3_main_combi_region_sulpharets', 'regular', 22, 532, 'wh2_dlc16_skv_clan_gritus', 'mountain', 'Sulpharets'),
     538: settlementData('wh3_dlc23_combi_region_blasted_expanse', 'regular', 858, 634, 'wh3_main_grn_drippin_fangs', 'wasteland', 'The Blasted Expanse'),
     539: settlementData('wh3_main_combi_region_angerrial', 'regular', 269, 529, 'wh2_main_def_cult_of_excess', 'temperate island', 'Angerrial'),
     540: settlementData('wh3_main_combi_region_dagraks_end', 'dark fortress', 128, 909, 'wh2_main_def_ghrond', 'frozen', "Dagrak's End"),
     541: settlementData('wh3_main_combi_region_mount_grey_hag', 'regular', 879, 515, 'wh3_main_grn_moon_howlerz', 'mountain', 'Mount Grey Hag'),
     542: settlementData('wh3_main_combi_region_wreckers_point', 'regular', 474, 748, 'wh_dlc03_grn_black_pit', 'temperate', "Wrecker's Point"),
     543: settlementData('wh3_main_combi_region_sudenburg', 'regular', 550, 254, 'wh3_main_emp_cult_of_sigmar', 'desert', 'Sudenburg'),
     544: settlementData('wh3_main_combi_region_middenstag', 'regular', 568, 690, 'wh_main_emp_middenland', 'temperate', 'Middenstag'),
     545: settlementData('wh3_main_combi_region_crooked_fang_fort', 'regular', 731, 416, 'wh_main_grn_red_fangs', 'mountain', 'Crooked Fang Fort'),
     546: settlementData('wh3_main_combi_region_zhizhu', 'regular', 1321, 584, 'wh3_dlc21_cst_dead_flag_fleet', 'temperate', 'Zhizhu'),
     547: settlementData('wh3_main_combi_region_the_sinhall_monolith', 'regular', 369, 37, 'wh3_main_tze_flaming_scribes', 'chaotic wasteland', 'The Sinhall Monolith'),
     548: settlementData('wh3_main_combi_region_uzkulak', 'regular', 854, 723, 'wh3_dlc23_chd_astragoth', 'wasteland', 'Uzkulak'),
     549: settlementData('wh3_main_combi_region_gorger_rock', 'regular', 997, 678, 'wh3_main_ogr_fulg', 'mountain', 'Gorger Rock'),
     550: settlementData('wh3_main_combi_region_fu_chow', 'regular', 1354, 504, 'wh3_dlc21_cst_dead_flag_fleet', 'temperate', 'Fu Chow'),
     551: settlementData('wh3_main_combi_region_the_golden_tower', 'regular', 680, 198, 'wh2_main_lzd_last_defenders', 'jungle', 'The Golden Tower'),
     552: settlementData('wh3_main_combi_region_shi_long', 'regular', 1239, 460, 'wh3_dlc21_vmp_jiangshi_rebels', 'savannah', 'Shi Long'),
     553: settlementData('wh3_main_combi_region_the_high_place', 'regular', 795, 550, 'wh_main_grn_bloody_spearz', 'mountain', 'The High Place'),
     554: settlementData('wh3_main_combi_region_doomkeep', 'dark fortress', 514, 836, 'wh_dlc08_nor_naglfarlings', 'mountain', 'Doomkeep'),
     555: settlementData('wh3_main_combi_region_the_fetid_catacombs', 'regular', 441, 896, 'wh3_main_sla_subtle_torture', 'chaotic wasteland', 'The Fetid Catacombs'),
     556: settlementData('wh3_main_combi_region_varg_camp', 'regular', 514, 874, 'wh_main_nor_varg', 'frozen', 'Varg Camp'),
     557: settlementData('wh3_main_combi_region_circle_of_destruction', 'regular', 159, 757, 'wh2_main_def_clar_karond', 'frozen', 'Circle of Destruction'),
     558: settlementData('wh3_main_combi_region_the_twisted_glade', 'regular', 208, 692, 'wh2_dlc11_cst_the_drowned', 'frozen', 'The Twisted Glade'),
     559: settlementData('wh3_main_combi_region_ironfrost', 'regular', 40, 878, 'wh2_main_nor_mung', 'frozen', 'Ironfrost'),
     560: settlementData('wh3_main_combi_region_the_tower_of_torment', 'regular', 760, 858, 'wh3_main_kho_bloody_sword', 'frozen', 'The Tower of Torment'),
     561: settlementData('wh3_main_combi_region_black_crag', 'regular', 753, 483, 'wh3_dlc26_grn_gorbad_ironclaw', 'mountain', 'Black Crag'),
     562: settlementData('wh3_main_combi_region_karag_dron', 'regular', 752, 517, 'wh3_dlc26_grn_gorbad_ironclaw', 'mountain', 'Karag Dron'),
     563: settlementData('wh3_main_combi_region_great_turtle_isle', 'regular', 31, 250, 'wh2_twa03_def_rakarth', 'temperate island', 'Great Turtle Isle'),
     564: settlementData('wh3_main_combi_region_the_monoliths', 'regular', 203, 755, 'wh2_main_hef_nagarythe', 'frozen', 'The Monoliths'),
     565: settlementData('wh3_main_combi_region_dark_tower', 'regular', 1272, 725, 'wh3_dlc20_nor_dolgan', 'chaotic wasteland', 'Dark Tower'),
     566: settlementData('wh3_main_combi_region_broken_mount', 'regular', 1237, 740, 'wh3_dlc27_nor_avags', 'chaotic wasteland', 'Broken Mount'),
     567: settlementData('wh3_main_combi_region_desolation_ridge', 'regular', 1199, 728, 'wh3_dlc27_nor_avags', 'chaotic wasteland', 'Desolation Ridge'),
     568: settlementData('wh3_main_combi_region_rotten_stone', 'regular', 1164, 733, 'wh3_dlc27_nor_avags', 'chaotic wasteland', 'Rotten Stone')
}

# Return the distance between two settlements
def getDistance(s1: settlementData, s2: settlementData) -> int:
    return ((s1.x-s2.x)**2 + (s1.y-s2.y)**2)**0.5

class SettlementManager:

    def __init__(self, random, playerFaction, playerKey, startingSettlementCount):
        self.start = time.time()
        self.random = random
        self.playerFaction = playerFaction
        self.playerKey = playerKey
        self.startingSettlementCount = startingSettlementCount

        self.factionKeys: list[int] = list(factionDict.keys())
        random.shuffle(self.factionKeys)
        self.settlementKeys: list[int] = list(settlementDict.keys())
        random.shuffle(self.settlementKeys)

        self.shuffledFactionList: list[str] = []
        self.shuffledSettlementDict: dict[int, settlementData] = {}
        self.capitals: dict[str, str] = {}

        self.keysToRemove: list[int] = []

    def getSettlements(self):
        self.shuffledSettlementDict = settlementDict
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
        playerFaction = factionDict[self.playerKey]
        if playerFaction.name not in trueHordeList:
            # Assign player their first settlement
            if playerFaction.race == "woodElves":
                for i, sKey in enumerate(self.settlementKeys):
                    playerSettlement: settlementData = settlementDict[sKey]
                    if playerSettlement.type == "magical forest":
                        self.assignSettlement(sKey, playerSettlement, playerFaction)
                        break
            elif playerFaction.race[:5] == "chaos":
                for i, sKey in enumerate(self.settlementKeys):
                    playerSettlement: settlementData = settlementDict[sKey]
                    if playerSettlement.type == "dark fortress":
                        self.assignSettlement(sKey, playerSettlement, playerFaction)
                        break
            else:
                sKey = self.settlementKeys[0]
                playerSettlement: settlementData = settlementDict[sKey]
                self.assignSettlement(sKey, settlementDict[sKey], playerFaction)
            self.removeKeys()
            self.capitals.update({playerFaction.name: playerSettlement.name})


            # Assign the player 2 more settlements
            for i in range(self.startingSettlementCount - 1):
                distance: int = 10000
                for j, sKey in enumerate(self.settlementKeys):
                    settlement: settlementData = settlementDict[sKey]

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
            settlement: settlementData = settlementDict[sKey]
            if settlement.type == "magical forest":
                for i, fKey in enumerate(self.factionKeys):
                    faction: factionData = factionDict[fKey]
                    if faction.race == "woodElves" and faction.name not in self.shuffledFactionList:
                        self.assignSettlement(sKey, settlement, faction)
                        self.factionKeys.pop(i)
                        break
                self.capitals.update({faction.name: settlement.name})
        self.removeKeys() # Remove the magical forests that have been assigned.

    def randomiseChaos(self) -> None:
        # Assigns each chaos faction a magical forest
        for sKey in self.settlementKeys:
            settlement: settlementData = settlementDict[sKey]
            if settlement.type == "dark fortress":
                for i, fKey in enumerate(self.factionKeys):
                    faction: factionData = factionDict[fKey]
                    if faction.race[:5] == "chaos" and faction.name not in self.shuffledFactionList:
                        self.assignSettlement(sKey, settlement, faction)
                        self.factionKeys.pop(i)
                        break
                self.capitals.update({faction.name: settlement.name})
        self.removeKeys() # Remove the magical forests that have been assigned.


    # Assigns all other factions their first settlement (if they aren't a horde)
    def randomiseFirstSettlement(self) -> None:
        for sKey in self.settlementKeys:
            settlement: settlementData = settlementDict[sKey]

            for i, fKey in enumerate(self.factionKeys):
                faction: factionData = factionDict[fKey]
                if faction.name not in trueHordeList and faction.name not in self.shuffledFactionList:
                    self.assignSettlement(sKey, settlement, faction)
                    self.factionKeys.pop(i)
                    break
            self.capitals.update({faction.name: settlement.name})
        self.removeKeys() #Remove the settlements that have been assigned

    def randomiseRemainingSettlements(self) -> None:
        blackList: list[str] = []
        shuffledSettlementDict = self.shuffledSettlementDict
        shuffledSettlementList = list(shuffledSettlementDict.items())
        #print(shuffledSettlementList)
        #random.shuffle(shuffledSettlementList)
        #print(shuffledSettlementList)

        #Asign each faction new settlements, based on distance from their capital
        for i, sKey in enumerate(self.settlementKeys):
            settlement: settlementData = settlementDict[sKey]
            distance: int = 10000

            for aKey, assignedSettlement in shuffledSettlementList:
                faction: str = assignedSettlement.faction
                if faction in trueHordeList:
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
            faction = factionDict[fKey]
            if faction.name in trueHordeList:
                settlement = self.random.choice(settlementDict)
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

    def getRequiredDiploRange(self, sphereCount: int, sphereRadius: int) -> tuple[list[int], dict[str, int]]:
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
                settlementSpheres.append(sphereCount)
        return settlementSpheres, factionSpheres

    def debug(self):
        x = []
        for i, d in self.shuffledSettlementDict.items():
            x.append(d.faction)
        counter = Counter(x)

        print(counter)

        print(time.time() - self.start)

"""
for i in range(2):
    test = settlementRandomiser(random, 92) #92 = "wh_dlc05_wef_wood_elves"
    settlements = test.randomiseSettlements()
    hordes = test.randomiseHordes()
    factionSpheres = test.getRequiredDiploRange(5, 100)
    print(factionSpheres)
    test.debug()
"""