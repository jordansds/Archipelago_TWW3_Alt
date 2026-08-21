from .bases import TWW3TestBase


CONQUEST_OPTIONS = {
    "game_mode": "conquest",
    "sanity": False,
    "ritual_sanity": False,
    "battle_sanity": False,
    "despoiler_sanity": False,
    "tech_shuffle": False,
    "building_shuffle": False,
    "unit_shuffle": False,
    "ritual_shuffle": False,
    "filler": 100,
}


class TestSettledConquestLocations(TWW3TestBase):
    options = CONQUEST_OPTIONS | {
        "starting_faction": 81,
        "faction_shuffle": True,
        "starting_settlements": 4,
        "checks_per_settlement": 5,
        "number_of_settlements": 6,
    }

    def test_goal_boundary(self) -> None:
        location_names = self.get_conquest_location_names()
        last_valid_batch = {f"Empire Size 5 ({check})" for check in range(5)}

        self.assertEqual(5, len(location_names))
        self.assertSetEqual(last_valid_batch, location_names)
        self.assertFalse(any(name.startswith("Empire Size 6 (") for name in location_names))
        self.assertFalse(any(name.startswith("Empire Size 4 (") for name in location_names))


class TestChangelingConquestLocations(TWW3TestBase):
    options = CONQUEST_OPTIONS | {
        "starting_faction": 202,
        "faction_shuffle": False,
        "starting_settlements": 4,
        "checks_per_settlement": 3,
        "number_of_settlements": 5,
    }

    def test_special_start_and_goal_boundary(self) -> None:
        location_names = self.get_conquest_location_names()
        expected_location_names = {
            f"Empire Size {empire_size} ({check})"
            for empire_size in (2, 3, 4)
            for check in range(3)
        }
        first_valid_batch = {f"Empire Size 2 ({check})" for check in range(3)}
        last_valid_batch = {f"Empire Size 4 ({check})" for check in range(3)}

        self.assertEqual(9, len(location_names))
        self.assertSetEqual(expected_location_names, location_names)
        self.assertTrue(first_valid_batch.issubset(location_names))
        self.assertTrue(last_valid_batch.issubset(location_names))
        self.assertFalse(any(name.startswith("Empire Size 5 (") for name in location_names))
        self.assertFalse(any(name.startswith("Empire Size 1 (") for name in location_names))
