from BaseClasses import ItemClassification as IC
from worlds.tww3.dataStructs import itemType, itemData, specialItemData
from worlds.tww3.faction_item_tables import tzeentch

# @formatter:off
units: dict[int, itemData] = tzeentch.units

buildings: dict[int, itemData] = {
    72400: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_caster_1', itemType.building, 0, 'Progressive tze_changeling_caster', "Changeling Building: Cult of Deceits"),
    72401: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_caster_2', itemType.building, 1, 'Progressive tze_changeling_caster', "Changeling Building: Cult of Lies"),
    72402: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_caster_3', itemType.building, 2, 'Progressive tze_changeling_caster', "Changeling Building: Cult of Change"),

    72403: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_horror_barracks_1', itemType.building, 0, 'Progressive tze_changeling_horror', "Changeling Building: Slither of Potential"),
    72404: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_horror_barracks_2', itemType.building, 1, 'Progressive tze_changeling_horror', "Changeling Building: Flicker of Potential"),
    72405: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_horror_barracks_3', itemType.building, 2, 'Progressive tze_changeling_horror', "Changeling Building: Moment of Potential"),

    72406: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_flamer_0', itemType.building, 0, 'Progressive tze_changeling_flamer', "Changeling Building: The Spark"),
    72407: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_flamer_1', itemType.building, 1, 'Progressive tze_changeling_flamer', "Changeling Building: Blue Bonfire"),
    72408: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_flamer_2', itemType.building, 2, 'Progressive tze_changeling_flamer', "Changeling Building: Pink Blaze"),
    72409: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_flamer_3', itemType.building, 3, 'Progressive tze_changeling_flamer', "Changeling Building: Iridescent Conflagration"),

    72410: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_monster_barracks_1', itemType.building, 0, 'Progressive tze_changeling_mortal', "Changeling Building: Many-Eyed Tribute"),
    72411: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_monster_barracks_2', itemType.building, 1, 'Progressive tze_changeling_mortal', "Changeling Building: Puzzle-Maker's Hovel"),
    72412: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_monster_barracks_3', itemType.building, 2, 'Progressive tze_changeling_mortal', "Changeling Building: Chapterhouse of Knowledge"),
    72413: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_monster_barracks_4', itemType.building, 3, 'Progressive tze_changeling_mortal', "Changeling Building: Doom's Hold"),

    72414: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_mounted_1', itemType.building, 0, 'Progressive tze_changeling_mounted', "Changeling Building: Transmogrification Locus"),
    72415: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_mounted_2', itemType.building, 1, 'Progressive tze_changeling_mounted', "Changeling Building: Inchoate Armoury"),
    72416: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_mounted_3', itemType.building, 2, 'Progressive tze_changeling_mounted', "Changeling Building: Inchoate Forge"),

    72417: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_plunder_1', itemType.building, 0, 'Progressive tze_changeling_plunder', "Changeling Building: Halls of Despoiling"),
    72418: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_plunder_2', itemType.building, 1, 'Progressive tze_changeling_plunder', "Changeling Building: Ravaging Host"),

    72419: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_diplomacy_symbiotic_1', itemType.building, 0, 'Progressive tze_changeling_sym_diplomacy', "Changeling Building: Court of Whispers"),
    72420: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_diplomacy_symbiotic_2', itemType.building, 1, 'Progressive tze_changeling_sym_diplomacy', "Changeling Building: Parliament of Lies"),

    72421: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_expansion_symbiotic_1', itemType.building, 0, 'Progressive tze_changeling_sym_expansion', "Changeling Building: Bird Box"),
    72422: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_expansion_symbiotic_2', itemType.building, 1, 'Progressive tze_changeling_sym_expansion', "Changeling Building: The Aviary"),
    72423: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_expansion_symbiotic_3', itemType.building, 2, 'Progressive tze_changeling_sym_expansion', "Changeling Building: Twisted Volary"),

    72424: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_growth_symbiotic_1', itemType.building, 0, 'Progressive tze_changeling_sym_growth', "Changeling Building: Agents' Hollow"),
    72425: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_growth_symbiotic_2', itemType.building, 1, 'Progressive tze_changeling_sym_growth', "Changeling Building: Occult Conspiracy"),
    72426: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_growth_symbiotic_3', itemType.building, 2, 'Progressive tze_changeling_sym_growth', "Changeling Building: Sanctum of Subterfuge"),

    72427: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_income_symbiotic_1', itemType.building, 0, 'Progressive tze_changeling_sym_income', "Changeling Building: Disguised Trade"),
    72428: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_income_symbiotic_2', itemType.building, 1, 'Progressive tze_changeling_sym_income', "Changeling Building: Shrouded Financier"),
    72429: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_income_symbiotic_3', itemType.building, 2, 'Progressive tze_changeling_sym_income', "Changeling Building: Mercantile Illusion"),

    72430: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_diplomacy_parasitic_1', itemType.building, 0, 'Progressive tze_changeling_para_diplomacy', "Changeling Building: Underground Temple"),
    72431: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_diplomacy_parasitic_2', itemType.building, 1, 'Progressive tze_changeling_para_diplomacy', "Changeling Building: Unholy Cathedral"),

    72432: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_expansion_parasitic_1', itemType.building, 0, 'Progressive tze_changeling_para_expansion', "Changeling Building: Enforcers' Abode"),
    72433: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_expansion_parasitic_2', itemType.building, 1, 'Progressive tze_changeling_para_expansion', "Changeling Building: Torturer's Shack"),
    72434: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_expansion_parasitic_3', itemType.building, 2, 'Progressive tze_changeling_para_expansion', "Changeling Building: Chamber of Agony"),

    72435: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_growth_parasitic_1', itemType.building, 0, 'Progressive tze_changeling_para_growth', "Changeling Building: Limb-breaker's Lair"),
    72436: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_growth_parasitic_2', itemType.building, 1, 'Progressive tze_changeling_para_growth', "Changeling Building: Marauders' Den"),
    72437: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_growth_parasitic_3', itemType.building, 2, 'Progressive tze_changeling_para_growth', "Changeling Building: House of Havoc"),

    72438: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_income_parasitic_1', itemType.building, 0, 'Progressive tze_changeling_para_income', "Changeling Building: Raiders' Bounty"),
    72439: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_income_parasitic_2', itemType.building, 1, 'Progressive tze_changeling_para_income', "Changeling Building: Hidden Storehouse"),
    72440: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_income_parasitic_3', itemType.building, 2, 'Progressive tze_changeling_para_income', "Changeling Building: Bloodied Vault"),

    72441: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_raise_army_parasitic_1', itemType.building, 0, 'Progressive tze_changeling_para_army', "Changeling Building: Occult Confluence"),
    72442: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_raise_army_parasitic_2', itemType.building, 1, 'Progressive tze_changeling_para_army', "Changeling Building: Reality Wound"),

    72443: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_raise_army_symbiotic_1', itemType.building, 0, 'Progressive tze_changeling_sym_army', "Changeling Building: Dark Ritual"),
    72444: itemData(IC.useful, 1, 'wh3_dlc24_tze_the_changeling_raise_army_symbiotic_2', itemType.building, 1, 'Progressive tze_changeling_sym_army', "Changeling Building: Legion of the Changeling"),
}

techs: dict[int, itemData] = {
    72800: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_rift_1', itemType.tech, 1, 'Progressive tech_tze_changeling_rifts', "Changeling Tech: A Rift to All Mankind"),
    72801: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_rift_2', itemType.tech, 1, 'Progressive tech_tze_changeling_rifts', "Changeling Tech: Frozen Gateway"),
    72802: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_rift_3', itemType.tech, 1, 'Progressive tech_tze_changeling_rifts', "Changeling Tech: Key to the West"),
    72803: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_rift_4', itemType.tech, 1, 'Progressive tech_tze_changeling_rifts', "Changeling Tech: Doorway to the Dark Lands"),
    72804: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_rift_5', itemType.tech, 1, 'Progressive tech_tze_changeling_rifts', "Changeling Tech: Southern Hospitality"),
    72805: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_rift_6', itemType.tech, 1, 'Progressive tech_tze_changeling_rifts', "Changeling Tech: Bridge to Naggaroth"),
    72806: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_rift_7', itemType.tech, 1, 'Progressive tech_tze_changeling_rifts', "Changeling Tech: Doom of Ulthuan"),
    72807: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_rift_8', itemType.tech, 1, 'Progressive tech_tze_changeling_rifts', "Changeling Tech: Chasm of Cathay"),
    72808: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_rift_9', itemType.tech, 1, 'Progressive tech_tze_changeling_rifts', "Changeling Tech: Jaws of the Jungle"),

    72809: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_root', itemType.tech, 1, 'Progressive tech_tze_changeling_boons', "Changeling Tech: Way of the Trickster"),
    72810: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_gate_army', itemType.tech, 2, 'Progressive tech_tze_changeling_boons', "Changeling Tech: Warhost in Waiting"),
    72811: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_gate_units', itemType.tech, 2, 'Progressive tech_tze_changeling_boons', "Changeling Tech: Mastery of Scheming"),
    72812: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_architects_chosen', itemType.tech, 3, 'Progressive tech_tze_changeling_boons', "Changeling Tech:The Architect’s Chosen "),

    72813: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_gift_of_mutation', itemType.tech, 3, 'Progressive tech_tze_changeling_boons', "Changeling Tech: Gift of Mutation"),
    72814: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_greater_locus_of_change', itemType.tech, 3, 'Progressive tech_tze_changeling_boons', "Changeling Tech: Greater Locus of Change"),
    72815: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_warpflame_formulae', itemType.tech, 3, 'Progressive tech_tze_changeling_boons', "Changeling Tech: Warpflame Formulae"),
    72816: itemData(IC.useful, 1, 'wh3_main_tech_tze_1_8', itemType.tech, 3, 'Progressive tech_tze_changeling_boons', "Changeling Tech: Piercing Screams"),
    72817: itemData(IC.useful, 1, 'wh3_main_tech_tze_0_9', itemType.tech, 3, 'Progressive tech_tze_changeling_boons', "Changeling Tech: Locus of Transmogrification"),
    72818: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_locus_of_contrivance', itemType.tech, 4, 'Progressive tech_tze_changeling_boons', "Changeling Tech: Locus of Contrivance"),
    72819: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_disc_taming', itemType.tech, 4, 'Progressive tech_tze_changeling_boons', "Changeling Tech: Disc Taming"),
    72820: itemData(IC.useful, 1, 'wh3_main_tech_tze_3_4', itemType.tech, 4, 'Progressive tech_tze_changeling_boons', "Changeling Tech: Metallurgical Morphism"),
    72821: itemData(IC.useful, 1, 'wh3_main_tech_tze_2_8', itemType.tech, 4, 'Progressive tech_tze_changeling_boons', "Changeling Tech: Exalted Locus of Conjuration"),

    72823: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_awaken_the_sleeper', itemType.tech, 4, 'Progressive tech_tze_changeling_boons', "Changeling Tech: Awaken the Sleeper"),
    72824: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_blinding_iridescent', itemType.tech, 4, 'Progressive tech_tze_changeling_boons', "Changeling Tech: Blinding Iridescent"),
    72825: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_champions_of_change', itemType.tech, 4, 'Progressive tech_tze_changeling_boons', "Changeling Tech: Champions of Change"),
    72826: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_endless_mutation', itemType.tech, 4, 'Progressive tech_tze_changeling_boons', "Changeling Tech: Endless Mutation"),
    72827: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_scatter_loci', itemType.tech, 5, 'Progressive tech_tze_changeling_boons', "Changeling Tech: Scatter Loci"),
    72828: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_stannic_deviance', itemType.tech, 5, 'Progressive tech_tze_changeling_boons', "Changeling Tech: Stannic Deviance"),
    72829: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_teleport', itemType.tech, 5, 'Progressive tech_tze_changeling_boons', "Changeling Tech: Teleport"),
    72830: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_inscrutable_demagoguery', itemType.tech, 5, 'Progressive tech_tze_changeling_boons', "Changeling Tech: Inscrutable Demagoguery"),

    72831: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_cultist_1', itemType.tech, 1, 'Progressive tech_tze_changeling_cultists', "Changeling Tech: Imperial Subterfuge"),
    72832: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_cultist_2', itemType.tech, 1, 'Progressive tech_tze_changeling_cultists', "Changeling Tech: Northern Machinations"),
    72833: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_cultist_3', itemType.tech, 1, 'Progressive tech_tze_changeling_cultists', "Changeling Tech: Old World Blues"),
    72834: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_cultist_4', itemType.tech, 1, 'Progressive tech_tze_changeling_cultists', "Changeling Tech: Cult of Smoke & Ash"),
    72835: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_cultist_5', itemType.tech, 1, 'Progressive tech_tze_changeling_cultists', "Changeling Tech: Sins of the South"),
    72836: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_cultist_6', itemType.tech, 1, 'Progressive tech_tze_changeling_cultists', "Changeling Tech: Chilling Conspiracy"),
    72837: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_cultist_7', itemType.tech, 1, 'Progressive tech_tze_changeling_cultists', "Changeling Tech: Playing on Pomposity"),
    72838: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_cultist_8', itemType.tech, 1, 'Progressive tech_tze_changeling_cultists', "Changeling Tech: Deceiving the Dragon"),
    72839: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_cultist_9', itemType.tech, 1, 'Progressive tech_tze_changeling_cultists', "Changeling Tech: Lustrian Cabal"),

    72840: itemData(IC.useful, 1, 'wh3_main_tech_tze_0_1', itemType.tech, 1, 'Progressive tech_tze_changeling_winds', "Changeling Tech: Thaumatic Locus"),
    72841: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_fires_of_change', itemType.tech, 1, 'Progressive tech_tze_changeling_winds', "Changeling Tech: Fires of Change"),
    72842: itemData(IC.useful, 1, 'wh3_main_tech_tze_0_4', itemType.tech, 1, 'Progressive tech_tze_changeling_winds', "Changeling Tech: Arcane Surge"),
    72843: itemData(IC.useful, 1, 'wh3_main_tech_tze_3_2', itemType.tech, 2, 'Progressive tech_tze_changeling_winds', "Changeling Tech: Storm of Fire"),
    72844: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_glean_magic', itemType.tech, 2, 'Progressive tech_tze_changeling_winds', "Changeling Tech: Glean Magic"),
    72845: itemData(IC.useful, 1, 'wh3_main_tech_tze_2_4', itemType.tech, 2, 'Progressive tech_tze_changeling_winds', "Changeling Tech: Bolt of Change"),
    72846: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_infernal_gateway', itemType.tech, 3, 'Progressive tech_tze_changeling_winds', "Changeling Tech: Infernal Gateway"),
    72847: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_treason_of_tzeentch', itemType.tech, 3, 'Progressive tech_tze_changeling_winds', "Changeling Tech: Treason of Tzeentch"),
    72848: itemData(IC.useful, 1, 'wh3_dlc24_tech_the_changeling_tzeentch_firestorm', itemType.tech, 3, 'Progressive tech_tze_changeling_winds', "Changeling Tech: Tzeentch's Firestorm"),

    72849: itemData(IC.useful, 1, 'wh3_main_tech_tze_1_9', itemType.tech, 1, 'Progressive tech_tze_changeling_ways', "Changeling Tech: Way of Fate"),
    72850: itemData(IC.useful, 1, 'wh3_dlc24_tech_tze_1_1_changeling', itemType.tech, 1, 'Progressive tech_tze_changeling_ways', "Changeling Tech: Way of Scrying"),
    72851: itemData(IC.useful, 1, 'wh3_main_tech_tze_3_5', itemType.tech, 1, 'Progressive tech_tze_changeling_ways', "Changeling Tech: Way of Time"),
    72852: itemData(IC.useful, 1, 'wh3_main_tech_tze_0_8', itemType.tech, 2, 'Progressive tech_tze_changeling_ways', "Changeling Tech: Way of Deception"),
    72853: itemData(IC.useful, 1, 'wh3_main_tech_tze_2_9', itemType.tech, 2, 'Progressive tech_tze_changeling_ways', "Changeling Tech: Way of Deceit"),
    72854: itemData(IC.useful, 1, 'wh3_main_tech_tze_4_9', itemType.tech, 2, 'Progressive tech_tze_changeling_ways', "Changeling Tech: Way of Prognostication"),
    72855: itemData(IC.useful, 1, 'wh3_main_tech_tze_2_3', itemType.tech, 3, 'Progressive tech_tze_changeling_ways', "Changeling Tech: Way of War"),
    72856: itemData(IC.useful, 1, 'wh3_main_tech_tze_3_7', itemType.tech, 3, 'Progressive tech_tze_changeling_ways', "Changeling Tech: Way of Manipulation"),
    72857: itemData(IC.useful, 1, 'wh3_main_tech_tze_4_1', itemType.tech, 3, 'Progressive tech_tze_changeling_ways', "Changeling Tech: Temporal Switch"),
}

progUnits: dict[int, itemData] = tzeentch.progUnits

progBuildings: dict[int, itemData] = {
    73300: itemData(IC.useful, 3, 'Progressive tze_changeling_caster', itemType.building, 3, None, "Progressive Changeling Building: Secret Society"),
    73301: itemData(IC.useful, 3, 'Progressive tze_changeling_horror', itemType.building, 3, None, "Progressive Changeling Building: Servants"),
    73302: itemData(IC.useful, 4, 'Progressive tze_changeling_flamer', itemType.building, 4, None, "Progressive Changeling Building: Fiery Servants"),
    73303: itemData(IC.useful, 4, 'Progressive tze_changeling_mortal', itemType.building, 4, None, "Progressive Changeling Building: Mortal Servants"),
    73304: itemData(IC.useful, 3, 'Progressive tze_changeling_mounted', itemType.building, 3, None, "Progressive Changeling Building: Forges of Change"),
    73305: itemData(IC.useful, 2, 'Progressive tze_changeling_plunder', itemType.building, 2, None, "Progressive Changeling Building: Loot"),
    73306: itemData(IC.useful, 2, 'Progressive tze_changeling_sym_diplomacy', itemType.building, 2, None, "Progressive Changeling Building: Symbiotic Diplomacy"),
    73307: itemData(IC.useful, 3, 'Progressive tze_changeling_sym_expansion', itemType.building, 3, None, "Progressive Changeling Building: Symbiotic Expansion"),
    73308: itemData(IC.useful, 3, 'Progressive tze_changeling_sym_growth', itemType.building, 3, None, "Progressive Changeling Building: Symbiotic Infrastructure"),
    73309: itemData(IC.useful, 3, 'Progressive tze_changeling_sym_income', itemType.building, 3, None, "Progressive Changeling Building: Symbiotic Income"),
    73310: itemData(IC.useful, 2, 'Progressive tze_changeling_sym_army', itemType.building, 2, None, "Progressive Changeling Building: Symbiotic Raise Army"),
    73311: itemData(IC.useful, 2, 'Progressive tze_changeling_para_diplomacy', itemType.building, 2, None, "Progressive Changeling Building: Parasitic Diplomacy"),
    73312: itemData(IC.useful, 3, 'Progressive tze_changeling_para_expansion', itemType.building, 3, None, "Progressive Changeling Building: Parasitic Expansion"),
    73313: itemData(IC.useful, 3, 'Progressive tze_changeling_para_growth', itemType.building, 3, None, "Progressive Changeling Building: Parasitic Infrastructure"),
    73314: itemData(IC.useful, 3, 'Progressive tze_changeling_para_income', itemType.building, 3, None, "Progressive Changeling Building: Parasitic Income"),
    73315: itemData(IC.useful, 2, 'Progressive tze_changeling_para_army', itemType.building, 2, None, "Progressive Changeling Building: Parasitic Raise Army"),
}

progTechs: dict[int, itemData] = {
    73400: itemData(IC.useful, 3, 'Progressive tech_tze_changeling_boons', itemType.tech, 5, None, "Progressive Changeling Tech: Boons"),
    73401: itemData(IC.useful, 3, 'Progressive tech_tze_changeling_ways', itemType.tech, 3, None, "Progressive Changeling Tech: Changing of the Ways"),
    73402: itemData(IC.useful, 3, 'Progressive tech_tze_changeling_winds', itemType.tech, 3, None, "Progressive Changeling Tech: Winds of Magic"),
    73403: itemData(IC.useful, 3, 'Progressive tech_tze_changeling_rifts', itemType.tech, 1, None, "Progressive Changeling Tech: Trickster Rifts"),
    73404: itemData(IC.useful, 3, 'Progressive tech_tze_changeling_cultists', itemType.tech, 1, None, "Progressive Changeling Tech: Trickster Cultists"),
}

special: dict[int, specialItemData] = {

}

rituals: dict[int, specialItemData] = {

}
