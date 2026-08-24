from unittest.mock import patch

from BaseClasses import CollectionState, ItemClassification as IC
from Fill import distribute_items_restrictive
from worlds.AutoWorld import call_all

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

    def test_free_tier_is_limited_to_empire_size_progression(self) -> None:
        capacity_items = self.get_items_by_name("Administrative Capacity")

        self.assertEqual(2, self.world.adminItems)
        self.assertEqual(2, len(capacity_items))
        slot_data = self.world.fill_slot_data()
        self.assertEqual(5, slot_data["admin_capacity"])
        self.assertEqual(2, slot_data["max_expansion_items"])

        no_capacity_items = self.state_with_capacity_items(0)
        one_capacity_item = self.state_with_capacity_items(1)
        two_capacity_items = self.state_with_capacity_items(2)

        expected_requirements = {
            "Empire Size 5 (0)": (True, True, True),
            "Empire Size 6 (0)": (False, True, True),
            "Empire Size 10 (0)": (False, True, True),
            "Empire Size 11 (0)": (False, False, True),
        }
        states = (no_capacity_items, one_capacity_item, two_capacity_items)
        for location_name, expected_reachability in expected_requirements.items():
            location = self.multiworld.get_location(location_name, self.player)
            with self.subTest(location=location_name):
                self.assertEqual(
                    expected_reachability,
                    tuple(location.can_reach(state) for state in states),
                )

        victory = self.multiworld.get_location("Victory", self.player)
        self.assertFalse(victory.can_reach(one_capacity_item))
        self.assertTrue(victory.can_reach(two_capacity_items))


class TestBeastmenCapacityRules(_FixedSeedTWW3TestBase):
    options = BASE_CAPACITY_OPTIONS | {
        "starting_faction": 11,
        "faction_shuffle": False,
        "starting_settlements": 4,
        "checks_per_settlement": 1,
        "number_of_settlements": 5,
    }

    def test_step_one_free_tier_boundaries(self) -> None:
        self.assertEqual(1, self.world.adminCapacity)
        self.assertEqual(5, self.world.adminItems)
        slot_data = self.world.fill_slot_data()
        self.assertEqual(1, slot_data["admin_capacity"])
        self.assertEqual(5, slot_data["max_expansion_items"])

        zero_items = self.state_with_capacity_items(0)
        one_item = self.state_with_capacity_items(1)
        four_items = self.state_with_capacity_items(4)

        self.assertTrue(self.multiworld.get_location("Empire Size 1 (0)", self.player).can_reach(zero_items))
        self.assertFalse(self.multiworld.get_location("Empire Size 2 (0)", self.player).can_reach(zero_items))
        self.assertTrue(self.multiworld.get_location("Empire Size 2 (0)", self.player).can_reach(one_item))
        self.assertTrue(self.multiworld.get_location("Empire Size 5 (0)", self.player).can_reach(four_items))


class TestConquestSanityScaling(_FixedSeedTWW3TestBase):
    options = BASE_CAPACITY_OPTIONS | {
        "starting_settlements": 2,
        "checks_per_settlement": 3,
        "number_of_settlements": 50,
        "battle_sanity": True,
        "despoiler_sanity": True,
    }

    def test_generic_sanity_uses_all_generated_items(self) -> None:
        capacity_items = self.get_items_by_name("Administrative Capacity")

        self.assertEqual(10, self.world.adminItems)
        self.assertEqual(10, len(capacity_items))
        self.assertEqual(10, self.world.fill_slot_data()["max_expansion_items"])

        nine_capacity_items = self.state_with_capacity_items(9)
        ten_capacity_items = self.state_with_capacity_items(10)
        final_sanity_locations = (
            "Won 100 Battles",
            "Sacked 40 Settlements",
            "Razed 40 Settlements",
        )

        for location_name in final_sanity_locations:
            location = self.multiworld.get_location(location_name, self.player)
            with self.subTest(location=location_name):
                self.assertFalse(location.can_reach(nine_capacity_items))
                self.assertTrue(location.can_reach(ten_capacity_items))

        final_empire_location = self.multiworld.get_location("Empire Size 50 (0)", self.player)
        victory = self.multiworld.get_location("Victory", self.player)
        self.assertTrue(final_empire_location.can_reach(nine_capacity_items))
        self.assertTrue(victory.can_reach(nine_capacity_items))


class TestMinimalKarlFranzCapacityFill(_FixedSeedTWW3TestBase):
    options = BASE_CAPACITY_OPTIONS | {
        "starting_settlements": 4,
        "checks_per_settlement": 5,
        "number_of_settlements": 6,
    }

    def setUp(self) -> None:
        # Special-item option gating is intentionally covered by its own follow-up branch.
        with patch("worlds.tww3.factionItemManager.getSpecial", return_value=[]):
            self.world_setup(seed=FIXED_SEED)

    def test_fixed_minimal_fill_reproducer(self) -> None:
        size_five_locations = {f"Empire Size 5 ({check})" for check in range(5)}
        size_six_locations = {f"Empire Size 6 ({check})" for check in range(5)}
        location_names = self.get_conquest_location_names()
        capacity_items = self.get_items_by_name("Administrative Capacity")
        filler_items = [item for item in self.multiworld.itempool if item.classification == IC.filler]

        self.assertSetEqual(size_five_locations | size_six_locations, location_names)
        self.assertEqual(1, self.world.adminItems)
        self.assertEqual(1, len(capacity_items))
        slot_data = self.world.fill_slot_data()
        self.assertEqual(5, slot_data["admin_capacity"])
        self.assertEqual(1, slot_data["max_expansion_items"])
        self.assertEqual(9, len(filler_items))
        self.assertEqual(10, len(self.multiworld.itempool))

        initial_state = CollectionState(self.multiworld)
        self.assertTrue(
            all(
                self.multiworld.get_location(location_name, self.player).can_reach(initial_state)
                for location_name in size_five_locations
            )
        )
        self.assertFalse(
            any(
                self.multiworld.get_location(location_name, self.player).can_reach(initial_state)
                for location_name in size_six_locations
            )
        )

        distribute_items_restrictive(self.multiworld)
        call_all(self.multiworld, "post_fill")
        call_all(self.multiworld, "finalize_multiworld")

        size_five_items = [
            self.multiworld.get_location(location_name, self.player).item
            for location_name in size_five_locations
        ]
        self.assertEqual(1, sum(item.name == "Administrative Capacity" for item in size_five_items))

        state = CollectionState(self.multiworld)
        for location_name in size_five_locations:
            location = self.multiworld.get_location(location_name, self.player)
            self.assertTrue(location.can_reach(state))
            state.collect(location.item, True, location)

        self.assertTrue(
            all(
                self.multiworld.get_location(location_name, self.player).can_reach(state)
                for location_name in size_six_locations
            )
        )
        for location_name in size_six_locations:
            location = self.multiworld.get_location(location_name, self.player)
            state.collect(location.item, True, location)

        victory = self.multiworld.get_location("Victory", self.player)
        self.assertTrue(victory.can_reach(state))
        state.collect(victory.item, True, victory)
        self.assertTrue(self.multiworld.has_beaten_game(state, self.player))
