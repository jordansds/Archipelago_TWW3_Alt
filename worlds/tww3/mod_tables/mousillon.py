from BaseClasses import ItemClassification as IC
from worlds.tww3.item_types import ItemType, ItemData
# @formatter:off

units: dict[int, ItemData] = {

}

"""
mixu_msl_mon_the_grey_men
mixu_msl_inf_bowmen
mixu_msl_inf_bowmen_balefire
mixu_msl_inf_bowmen_poison
mixu_msl_inf_men_at_arms_polearms
mixu_msl_inf_men_at_arms_sword
mixu_msl_art_trebuchet
mixu_msl_art_trebuchet_balefire
mixu_msl_cav_hellsteed_knights
mixu_msl_cav_black_knights_sword
mixu_msl_cav_black_knights_lance
mixu_msl_cav_black_grail_knights
mixu_msl_cav_black_grail_knights_summon
mixu_msl_ror_cantankerous_bellends
mixu_msl_ror_knights_of_bougar
mixu_msl_ror_the_rose_lances
mixu_msl_ror_ghosts_of_grismerie
mixu_msl_ror_barons_men
mixu_msl_inf_grave_guard_sword
mixu_msl_inf_grave_guard_great_weapons
mixu_msl_mon_dracoleech
mixu_msl_inf_brigands
mixu_msl_inf_mounted_brigands
mixu_msl_mon_giant_snail
"""

buildings: dict[int, ItemData] = {

}

"""
mixu_msl_barracks_1
mixu_msl_barracks_2
mixu_msl_wraiths_1
mixu_msl_wraiths_2
mixu_msl_wraiths_3
mixu_msl_binding_circle_1
mixu_msl_binding_circle_2
mixu_msl_binding_circle_3
mixu_msl_carpenter_1
mixu_msl_carpenter_2
mixu_msl_swampaire_camp_1
mixu_msl_swampaire_camp_2
mixu_msl_swampaire_camp_3
mixu_msl_tavern_1
mixu_msl_tavern_2
mixu_msl_tavern_3
mixu_msl_farm_1
mixu_msl_farm_2
mixu_msl_farm_3
mixu_msl_foreign_slot_discovery
mixu_msl_awakened_battlefield
mixu_msl_walls_1
mixu_msl_walls_2
mixu_msl_walls_3
mixu_msl_garrison_1
mixu_msl_garrison_2
mixu_msl_defence_norsca_1
mixu_msl_cemetary_1
mixu_msl_cemetary_2
mixu_msl_swamp_land_1
mixu_msl_swamp_land_2
mixu_msl_balefire_1
mixu_msl_balefire_2
mixu_msl_balefire_3
mixu_msl_port_1
mixu_msl_port_2
mixu_msl_port_3
mixu_msl_vampires_1
mixu_msl_vampires_2
mixu_msl_allied_outpost_1
mixu_msl_allied_outpost_2
mixu_msl_allied_outpost_3
mixu_msl_resource_animals_1
mixu_msl_resource_animals_2
mixu_msl_resource_animals_3
mixu_msl_resource_gemstones_1
mixu_msl_resource_gemstones_2
mixu_msl_resource_gemstones_3
mixu_msl_resource_medicine_1
mixu_msl_resource_medicine_2
mixu_msl_resource_medicine_3
mixu_msl_resource_obsidian_1
mixu_msl_resource_obsidian_2
mixu_msl_resource_obsidian_3
mixu_msl_resource_spices_1
mixu_msl_resource_spices_2
mixu_msl_resource_spices_3
mixu_msl_resource_ivory_1
mixu_msl_resource_ivory_2
mixu_msl_resource_ivory_3
mixu_msl_resource_dyes_1

mixu_special_settlement_altdorf_1_msl
mixu_special_settlement_altdorf_2_msl
mixu_special_settlement_altdorf_3_msl
mixu_special_settlement_altdorf_4_msl
mixu_special_settlement_altdorf_5_msl
mixu_special_settlement_castle_drakenhof_1_msl
mixu_special_settlement_castle_drakenhof_2_msl
mixu_special_settlement_castle_drakenhof_3_msl
mixu_special_settlement_castle_drakenhof_4_msl
mixu_special_settlement_castle_drakenhof_5_msl
mixu_special_settlement_couronne_1_msl
mixu_special_settlement_couronne_2_msl
mixu_special_settlement_couronne_3_msl
mixu_special_settlement_couronne_4_msl
mixu_special_settlement_couronne_5_msl
mixu_msl_settlement_major_1
mixu_msl_settlement_major_2
mixu_msl_settlement_major_3
mixu_msl_settlement_major_4
mixu_msl_settlement_major_5
mixu_msl_settlement_minor_1
mixu_msl_settlement_minor_2
mixu_msl_settlement_minor_3
mixu_special_settlement_mousillon_1_msl
mixu_special_settlement_mousillon_2_msl
mixu_special_settlement_mousillon_3_msl


mixu_msl_underground_pirates_grave
mixu_msl_lair_of_the_black_grail
mixu_msl_auction_house_1
mixu_msl_auction_house_2
"""

techs: dict[int, ItemData] = {
    102800: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_cursed_land', ItemType.tech, 1, 'Progressive tech_msl_undead', 'Msl Tech: Cursed Land'),
    102801: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_raise_newly_dead', ItemType.tech, 2, 'Progressive tech_msl_undead', 'Msl Tech: '),
    102802: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_defiler_of_the_ancient_barrows', ItemType.tech, 2, 'Progressive tech_msl_undead', 'Msl Tech: '),
    102803: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_rotten_gift', ItemType.tech, 2, 'Progressive tech_msl_undead', 'Msl Tech: '),
    102804: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_bonds_of_flesh', ItemType.tech, 2, 'Progressive tech_msl_undead', 'Msl Tech: '),
    102805: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_dread_animator', ItemType.tech, 2, 'Progressive tech_msl_undead', 'Msl Tech: '),
    102806: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_spirit_shackles', ItemType.tech, 2, 'Progressive tech_msl_undead', 'Msl Tech: '),
    102807: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_unearth_cursed_blades', ItemType.tech, 2, 'Progressive tech_msl_undead', 'Msl Tech: '),
    102808: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_cannibalistic_rituals', ItemType.tech, 2, 'Progressive tech_msl_undead', 'Msl Tech: '),
    102809: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_enshrine_ancient_lords', ItemType.tech, 2, 'Progressive tech_msl_undead', 'Msl Tech: '),
    102810: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_infuse_the_tireless_hordes', ItemType.tech, 2, 'Progressive tech_msl_undead', 'Msl Tech: '),
    102811: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_soulbinder', ItemType.tech, 2, 'Progressive tech_msl_undead', 'Msl Tech: '),
    102812: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_undead_nightmarish_reaping', ItemType.tech, 2, 'Progressive tech_msl_undead', 'Msl Tech: '),

    102813: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_living_rally_the_peasants', ItemType.tech, 1, 'Progressive tech_msl_living', 'Msl Tech: Rally the Peasants'),
    102814: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_living_disgraced_and_damned', ItemType.tech, 2, 'Progressive tech_msl_living', 'Msl Tech: '),
    102815: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_living_embrace_the_darkness', ItemType.tech, 2, 'Progressive tech_msl_living', 'Msl Tech: '),
    102816: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_living_steel_furnaces', ItemType.tech, 2, 'Progressive tech_msl_living', 'Msl Tech: '),
    102817: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_living_master_swordsmiths', ItemType.tech, 2, 'Progressive tech_msl_living', 'Msl Tech: '),
    102818: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_living_professional_fletchers', ItemType.tech, 2, 'Progressive tech_msl_living', 'Msl Tech: '),
    102819: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_living_siege_engineering', ItemType.tech, 2, 'Progressive tech_msl_living', 'Msl Tech: '),
    102820: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_living_serve_in_life_or_in_death', ItemType.tech, 2, 'Progressive tech_msl_living', 'Msl Tech: '),
    102821: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_living_charity', ItemType.tech, 2, 'Progressive tech_msl_living', 'Msl Tech: '),
    102822: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_living_registered_draft', ItemType.tech, 2, 'Progressive tech_msl_living', 'Msl Tech: '),
    102823: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_living_bigger_shovels', ItemType.tech, 2, 'Progressive tech_msl_living', 'Msl Tech: '),
    102824: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_living_subsidised_tools', ItemType.tech, 2, 'Progressive tech_msl_living', 'Msl Tech: '),
    102825: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_living_improved_construction', ItemType.tech, 2, 'Progressive tech_msl_living', 'Msl Tech: '),

    102826: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_cavalry_regular_tournaments', ItemType.tech, 1, 'Progressive tech_msl_knights', 'Msl Tech: Regular Tournaments'),
    102827: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_cavalry_dark_deeds', ItemType.tech, 1, 'Progressive tech_msl_knights', 'Msl Tech: '),
    102828: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_cavalry_unholy_strength', ItemType.tech, 1, 'Progressive tech_msl_knights', 'Msl Tech: '),

    102829: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_swamps_horrors_of_the_bog', ItemType.tech, 1, 'Progressive tech_msl_swamp', 'Msl Tech: Horrors of the Bog'),
    102830: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_swamps_swampaire_training', ItemType.tech, 1, 'Progressive tech_msl_swamp', 'Msl Tech: '),
    102831: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_swamps_support_the_frogwives', ItemType.tech, 1, 'Progressive tech_msl_swamp', 'Msl Tech: '),

    102832: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_nobels_of_mousillon', ItemType.tech, 1, 'Progressive tech_msl_nobility', 'Msl Tech: Nobles of Mousillon'),
    102833: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_blood_is_power', ItemType.tech, 2, 'Progressive tech_msl_nobility', 'Msl Tech: '),
    102834: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_hexensnacht_sacrifices', ItemType.tech, 2, 'Progressive tech_msl_nobility', 'Msl Tech: '),
    102835: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_blasphemous_disciples', ItemType.tech, 2, 'Progressive tech_msl_nobility', 'Msl Tech: '),
    102836: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_spread_vampire_covens', ItemType.tech, 2, 'Progressive tech_msl_nobility', 'Msl Tech: '),
    102837: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_turning_knights_of_the_realm', ItemType.tech, 2, 'Progressive tech_msl_nobility', 'Msl Tech: '),
    102838: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_delusions_of_grandeur', ItemType.tech, 2, 'Progressive tech_msl_nobility', 'Msl Tech: '),
    102839: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_puppet_master', ItemType.tech, 2, 'Progressive tech_msl_nobility', 'Msl Tech: '),
    102840: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_infiltrate_noble_houses', ItemType.tech, 2, 'Progressive tech_msl_nobility', 'Msl Tech: '),
    102841: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_baleful_rituals', ItemType.tech, 2, 'Progressive tech_msl_nobility', 'Msl Tech: '),
    102842: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_vampiric_revivification', ItemType.tech, 2, 'Progressive tech_msl_nobility', 'Msl Tech: '),
    102843: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_traditions_of_hospitality', ItemType.tech, 2, 'Progressive tech_msl_nobility', 'Msl Tech: '),
    102844: ItemData(IC.useful, 1, 'mixu_msl_mallobaude_nobility_code_of_conduct', ItemType.tech, 2, 'Progressive tech_msl_nobility', 'Msl Tech: '),
}

progUnits: dict[int, ItemData] = {}

progBuildings: dict[int, ItemData] = {}

progTechs: dict[int, ItemData] = {}

special: dict[int, ItemData] = {}