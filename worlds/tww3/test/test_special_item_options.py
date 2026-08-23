import unittest
from types import SimpleNamespace
from unittest.mock import patch

from BaseClasses import ItemClassification as IC
from worlds.tww3 import items
from worlds.tww3.dataStructs import itemType, specialItemData


def make_special_item(
    name: str,
    item_type: itemType,
    *,
    count: int = 1,
    tier: int = 2,
    spc_logic: bool = False,
    progressive: bool = False,
) -> specialItemData:
    return specialItemData(
        IC.useful,
        count,
        ["test_faction"],
        name,
        item_type,
        tier,
        "test_progression_group",
        spc_logic,
        progressive,
        name,
    )


class DummyWorld:
    def __init__(self, *, building_shuffle: bool, unit_shuffle: bool, tech_shuffle: bool) -> None:
        self.options = SimpleNamespace(
            building_shuffle=building_shuffle,
            unit_shuffle=unit_shuffle,
            tech_shuffle=tech_shuffle,
            starting_tier=1,
        )
        self.itemKeys: list[int] = []
        self.precollected: list[str] = []

    @staticmethod
    def create_item(name: str) -> str:
        return name

    def push_precollected(self, item: str) -> None:
        self.precollected.append(item)


class SpecialItemOptionTests(unittest.TestCase):
    special_items = [
        (100, make_special_item("Special Building", itemType.building, count=2)),
        (101, make_special_item("Special Unit", itemType.unit)),
        (102, make_special_item("Special Technology", itemType.tech, tier=0)),
        (103, make_special_item("Starting Building", itemType.building, tier=0)),
        (104, make_special_item("Starting Unit", itemType.unit, tier=1)),
        (105, make_special_item("Logic Item", itemType.building, spc_logic=True, progressive=True)),
    ]

    def generate(self, *, building: bool = False, unit: bool = False, tech: bool = False):
        world = DummyWorld(building_shuffle=building, unit_shuffle=unit, tech_shuffle=tech)
        with patch.object(items.factionItemManager, "getSpecial", return_value=self.special_items):
            pool = items.generateSpecialItems(world, [])
        return world, pool

    def test_disabled_shuffles_exclude_special_items_but_keep_logic_precollection(self) -> None:
        world, pool = self.generate()

        self.assertEqual([], pool)
        self.assertEqual([], world.itemKeys)
        self.assertEqual(["Logic Item"], world.precollected)

    def test_each_shuffle_only_adds_its_matching_special_item_type(self) -> None:
        expectations = (
            ({"building": True}, ["Special Building", "Special Building", "Logic Item"], [100, 100]),
            ({"unit": True}, ["Special Unit"], [101]),
            ({"tech": True}, ["Special Technology"], [102]),
        )

        for enabled_options, expected_pool, expected_keys in expectations:
            with self.subTest(enabled_options=enabled_options):
                world, pool = self.generate(**enabled_options)
                self.assertEqual(expected_pool, pool)
                self.assertEqual(expected_keys, world.itemKeys)
                self.assertEqual(["Logic Item"], world.precollected)

    def test_tier_thresholds_and_progressive_key_handling_are_preserved(self) -> None:
        world, pool = self.generate(building=True, unit=True, tech=True)

        self.assertNotIn("Starting Building", pool)
        self.assertNotIn("Starting Unit", pool)
        self.assertNotIn(105, world.itemKeys)
        self.assertEqual(
            ["Special Building", "Special Building", "Special Unit", "Special Technology", "Logic Item"],
            pool,
        )


if __name__ == "__main__":
    unittest.main()
