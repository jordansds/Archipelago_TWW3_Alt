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

    def test_goal_batch_is_included(self) -> None:
        location_names = self.get_conquest_location_names()
        expected_location_names = {
            f"Empire Size {empire_size} ({check})"
            for empire_size in (5, 6)
            for check in range(5)
        }

        self.assertEqual(10, len(location_names))
        self.assertSetEqual(expected_location_names, location_names)
        self.assertFalse(any(name.startswith("Empire Size 4 (") for name in location_names))
        self.assertFalse(any(name.startswith("Empire Size 7 (") for name in location_names))


class TestChangelingConquestLocations(TWW3TestBase):
    options = CONQUEST_OPTIONS | {
        "starting_faction": 202,
        "faction_shuffle": False,
        "starting_settlements": 4,
        "checks_per_settlement": 3,
        "number_of_settlements": 5,
    }

    def test_special_start_keeps_the_goal_batch(self) -> None:
        location_names = self.get_conquest_location_names()
        expected_location_names = {
            f"Empire Size {empire_size} ({check})"
            for empire_size in (2, 3, 4, 5)
            for check in range(3)
        }

        self.assertEqual(12, len(location_names))
        self.assertSetEqual(expected_location_names, location_names)
        self.assertFalse(any(name.startswith("Empire Size 1 (") for name in location_names))
        self.assertFalse(any(name.startswith("Empire Size 6 (") for name in location_names))


class TestHordeConquestLocations(TWW3TestBase):
    options = CONQUEST_OPTIONS | {
        "starting_faction": 11,
        "faction_shuffle": False,
        "starting_settlements": 4,
        "checks_per_settlement": 2,
        "number_of_settlements": 5,
    }

    def test_horde_start_and_goal_batch_are_preserved(self) -> None:
        location_names = self.get_conquest_location_names()
        expected_location_names = {
            f"Empire Size {empire_size} ({check})"
            for empire_size in (1, 2, 3, 4, 5)
            for check in range(2)
        }

        self.assertEqual(10, len(location_names))
        self.assertSetEqual(expected_location_names, location_names)


class TestStartingAtGoalLocations(TWW3TestBase):
    options = CONQUEST_OPTIONS | {
        "starting_faction": 71,
        "faction_shuffle": True,
        "starting_settlements": 5,
        "checks_per_settlement": 3,
        "number_of_settlements": 5,
    }

    def test_starting_at_goal_still_creates_the_final_batch(self) -> None:
        location_names = self.get_conquest_location_names()
        expected_location_names = {f"Empire Size 5 ({check})" for check in range(3)}

        self.assertSetEqual(expected_location_names, location_names)
