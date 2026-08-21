import unittest

from BaseClasses import CollectionState, ItemClassification as IC
from Fill import distribute_items_restrictive
from worlds.AutoWorld import call_all
from worlds.tww3.conquest import capacity_tiers, required_capacity_items, settlement_capacity

from .bases import TWW3TestBase


FIXED_SEED = 2608212026

BASE_CAPACITY_OPTIONS = {
    "accessibility": "items",
    "progression_balancing": 0,
    "starting_faction": 81,
    "game_mode": "conquest",
    "faction_shuffle": True,
    "randomize_personalities": False,
    "sanity": False,
    "ritual_sanity": False,
    "battle_sanity": False,
    "despoiler_sanity": False,
    "tech_shuffle": False,
    "progressive_technologies": False,
    "building_shuffle": False,
    "progressive_buildings": True,
    "unit_shuffle": False,
    "progressive_units": False,
    "ritual_shuffle": False,
    "filler": 100,
    "death_link": False,
    "death_link_effects": [],
    "starting_tier": 1,
    "balance": 0,
    "hard_logic": True,
    "fast_research": False,
    "reveal_hints": False,
    "mod_list": [],
    "filler_blacklist": [],
    "trap_blacklist": [],
}


class TestCapacityHelpers(unittest.TestCase):
    def test_required_capacity_items_step_five_table(self) -> None:
        expected_items = {
            0: 0,
            1: 0,
            5: 0,
            6: 1,
            10: 1,
            11: 2,
            49: 9,
            50: 9,
            51: 10,
        }

        for settlement_count, expected in expected_items.items():
            with self.subTest(settlement_count=settlement_count, capacity_step=5):
                self.assertEqual(expected, required_capacity_items(settlement_count, 5))

    def test_required_capacity_items_beastmen_step_one_table(self) -> None:
        expected_items = {
            0: 0,
            1: 0,
            2: 1,
            5: 4,
        }

        for settlement_count, expected in expected_items.items():
            with self.subTest(settlement_count=settlement_count, capacity_step=1):
                self.assertEqual(expected, required_capacity_items(settlement_count, 1))

    def test_received_items_to_client_capacity(self) -> None:
        expected_mappings = (
            (0, 5, 1, 5),
            (1, 5, 2, 10),
            (9, 5, 10, 50),
        )

        for received_items, capacity_step, expected_tiers, expected_capacity in expected_mappings:
            with self.subTest(received_items=received_items, capacity_step=capacity_step):
                self.assertEqual(expected_tiers, capacity_tiers(received_items))
                self.assertEqual(expected_capacity, settlement_capacity(received_items, capacity_step))

    def test_invalid_inputs(self) -> None:
        invalid_calls = (
            (required_capacity_items, (-1, 5)),
            (required_capacity_items, (5, 0)),
            (required_capacity_items, (5, -1)),
            (capacity_tiers, (-1,)),
            (settlement_capacity, (-1, 5)),
            (settlement_capacity, (0, 0)),
            (settlement_capacity, (0, -1)),
        )

        for helper, arguments in invalid_calls:
            with self.subTest(helper=helper.__name__, arguments=arguments):
                with self.assertRaises(ValueError):
                    helper(*arguments)


class _FixedSeedTWW3TestBase(TWW3TestBase):
    def setUp(self) -> None:
        self.world_setup(seed=FIXED_SEED)

    def state_with_capacity_items(self, count: int) -> CollectionState:
        capacity_items = self.get_items_by_name("Administrative Capacity")
        self.assertGreaterEqual(len(capacity_items), count)

        state = CollectionState(self.multiworld)
        for item in capacity_items[:count]:
            state.collect(item)
        return state


class TestConquestCapacityRules(_FixedSeedTWW3TestBase):
    options = BASE_CAPACITY_OPTIONS | {
        "starting_settlements": 4,
        "checks_per_settlement": 1,
        "number_of_settlements": 11,
    }

    def test_capacity_item_and_access_rule_agreement(self) -> None:
        capacity_items = self.get_items_by_name("Administrative Capacity")

        self.assertEqual(2, self.world.adminItems)
        self.assertEqual(2, len(capacity_items))
        self.assertEqual(2, self.world.fill_slot_data()["max_expansion_items"])

        no_capacity_items = self.state_with_capacity_items(0)
        one_capacity_item = self.state_with_capacity_items(1)
        two_capacity_items = self.state_with_capacity_items(2)

        self.assertTrue(self.multiworld.get_location("Empire Size 5 (0)", self.player).can_reach(no_capacity_items))
        self.assertFalse(self.multiworld.get_location("Empire Size 6 (0)", self.player).can_reach(no_capacity_items))
        self.assertFalse(self.multiworld.get_location("Empire Size 10 (0)", self.player).can_reach(no_capacity_items))
        self.assertTrue(self.multiworld.get_location("Empire Size 6 (0)", self.player).can_reach(one_capacity_item))
        self.assertTrue(self.multiworld.get_location("Empire Size 10 (0)", self.player).can_reach(one_capacity_item))

        victory = self.multiworld.get_location("Victory", self.player)
        self.assertFalse(victory.can_reach(no_capacity_items))
        self.assertFalse(victory.can_reach(one_capacity_item))
        self.assertTrue(victory.can_reach(two_capacity_items))


class TestConquestSanityScaling(_FixedSeedTWW3TestBase):
    options = BASE_CAPACITY_OPTIONS | {
        "starting_settlements": 2,
        "checks_per_settlement": 3,
        "number_of_settlements": 50,
        "battle_sanity": True,
        "despoiler_sanity": True,
    }

    def test_sanity_and_victory_require_no_more_than_generated_items(self) -> None:
        capacity_items = self.get_items_by_name("Administrative Capacity")

        self.assertEqual(9, self.world.adminItems)
        self.assertEqual(9, len(capacity_items))
        self.assertEqual(9, self.world.fill_slot_data()["max_expansion_items"])

        eight_capacity_items = self.state_with_capacity_items(8)
        nine_capacity_items = self.state_with_capacity_items(9)
        final_sanity_locations = (
            "Won 100 Battles",
            "Sacked 40 Settlements",
            "Razed 40 Settlements",
        )

        for location_name in final_sanity_locations:
            location = self.multiworld.get_location(location_name, self.player)
            with self.subTest(location=location_name):
                self.assertFalse(location.can_reach(eight_capacity_items))
                self.assertTrue(location.can_reach(nine_capacity_items))

        sanity_locations = [
            location
            for location in self.multiworld.get_locations(self.player)
            if location.parent_region.name in {"Battles", "Despoiler"}
        ]
        self.assertEqual(60, len(sanity_locations))
        self.assertTrue(all(location.can_reach(nine_capacity_items) for location in sanity_locations))

        victory = self.multiworld.get_location("Victory", self.player)
        self.assertFalse(victory.can_reach(eight_capacity_items))
        self.assertTrue(victory.can_reach(nine_capacity_items))


class TestMinimalKarlFranzCapacityFill(_FixedSeedTWW3TestBase):
    options = BASE_CAPACITY_OPTIONS | {
        "starting_settlements": 4,
        "checks_per_settlement": 5,
        "number_of_settlements": 6,
    }

    def test_fixed_minimal_fill_reproducer(self) -> None:
        expected_location_names = {f"Empire Size 5 ({check})" for check in range(5)}
        location_names = self.get_conquest_location_names()
        capacity_items = self.get_items_by_name("Administrative Capacity")
        filler_items = [item for item in self.multiworld.itempool if item.classification == IC.filler]

        self.assertSetEqual(expected_location_names, location_names)
        self.assertFalse(any(name.startswith("Empire Size 6 (") for name in location_names))
        self.assertEqual(1, self.world.adminItems)
        self.assertEqual(1, len(capacity_items))
        self.assertEqual(1, self.world.fill_slot_data()["max_expansion_items"])

        with self.subTest("minimal item pool"):
            self.assertEqual(4, len(filler_items))
            self.assertEqual(5, len(self.multiworld.itempool))

        initial_state = CollectionState(self.multiworld)
        self.assertTrue(
            all(
                self.multiworld.get_location(location_name, self.player).can_reach(initial_state)
                for location_name in expected_location_names
            )
        )

        distribute_items_restrictive(self.multiworld)
        call_all(self.multiworld, "post_fill")
        call_all(self.multiworld, "finalize_multiworld")

        placed_items = [
            self.multiworld.get_location(location_name, self.player).item
            for location_name in expected_location_names
        ]
        with self.subTest("minimal placed items"):
            self.assertEqual(1, sum(item.name == "Administrative Capacity" for item in placed_items))
            self.assertEqual(4, sum(item.classification == IC.filler for item in placed_items))

        placed_code_items = [
            location.item
            for location in self.multiworld.get_locations(self.player)
            if location.item and location.item.code
        ]
        with self.subTest("all generated items placed"):
            self.assertEqual(len(self.multiworld.itempool), len(placed_code_items))

        state = CollectionState(self.multiworld)
        for location_name in expected_location_names:
            location = self.multiworld.get_location(location_name, self.player)
            self.assertTrue(location.can_reach(state))
            state.collect(location.item, True, location)

        victory = self.multiworld.get_location("Victory", self.player)
        self.assertTrue(victory.can_reach(state))
        state.collect(victory.item, True, victory)
        self.assertTrue(self.multiworld.has_beaten_game(state, self.player))
