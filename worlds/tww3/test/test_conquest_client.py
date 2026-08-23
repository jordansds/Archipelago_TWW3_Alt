import asyncio
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock, call, patch

from NetUtils import ClientStatus
from worlds.tww3 import TWW3World
from worlds.tww3.client import _get_conquest_admin_capacity, TWW3CommandProcessor, TWW3Context
from worlds.tww3.item_tables.progression_table import progressionDict


class TestConquestClientProgression(unittest.IsolatedAsyncioTestCase):
    @staticmethod
    def make_context(
        *,
        received_items: int = 1,
        admin_capacity: int = 5,
        max_empire_size: int = 6,
        settlement_count: int = 4,
    ) -> TWW3Context:
        context = object.__new__(TWW3Context)
        context.gameMode = "conquest"
        context.maxEmpireSize = max_empire_size
        context.adminCapacity = admin_capacity
        context.expansionItems = received_items
        context.maxExpansionItems = 1
        context.checksPerLocation = 5
        context.hardLogic = True
        context.settlementCount = settlement_count
        context.debugCapacityOverride = False
        context.postVictoryCapacityOverride = False
        context.missing_locations = set()
        context.send_msgs = AsyncMock()
        context.sendMessage = Mock()
        return context

    def test_admin_capacity_prefers_slot_data_and_falls_back_by_faction(self) -> None:
        with patch("worlds.tww3.client.logger.warning") as log_warning:
            self.assertEqual(1, _get_conquest_admin_capacity({"admin_capacity": 1}, "empire"))
            log_warning.assert_not_called()

            self.assertEqual(1, _get_conquest_admin_capacity({}, "beastmen"))
            self.assertEqual(5, _get_conquest_admin_capacity({}, "empire"))
            self.assertEqual(2, log_warning.call_count)

    async def test_goal_observation_backfills_checks_before_victory(self) -> None:
        context = self.make_context()
        expected_location_ids = {
            TWW3World.location_name_to_id[f"Empire Size {empire_size} ({check})"]
            for empire_size in (5, 6)
            for check in range(5)
        }
        context.missing_locations = expected_location_ids.copy()
        capacity_state = (context.expansionItems, context.maxExpansionItems, context.adminCapacity)

        await context.check("6")

        self.assertEqual(6, context.settlementCount)
        self.assertEqual(capacity_state, (context.expansionItems, context.maxExpansionItems, context.adminCapacity))
        self.assertTrue(context.postVictoryCapacityOverride)
        context.sendMessage.assert_called_once_with("archipelago.set_admin_capacity_mult(1000)")
        self.assertEqual(2, context.send_msgs.await_count)

        location_message = context.send_msgs.await_args_list[0].args[0][0]
        victory_message = context.send_msgs.await_args_list[1].args[0]
        self.assertEqual("LocationChecks", location_message["cmd"])
        self.assertSetEqual(expected_location_ids, set(location_message["locations"]))
        self.assertEqual([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}], victory_message)

        context.missing_locations.clear()
        await context.check("6")

        self.assertEqual(3, context.send_msgs.await_count)
        self.assertEqual(
            [{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}],
            context.send_msgs.await_args_list[2].args[0],
        )
        context.sendMessage.assert_called_once_with("archipelago.set_admin_capacity_mult(1000)")

    async def test_hard_logic_blocks_goal_and_final_checks_without_capacity(self) -> None:
        context = self.make_context(received_items=0)
        accessible_location_ids = {
            TWW3World.location_name_to_id[f"Empire Size 5 ({check})"]
            for check in range(5)
        }
        final_location_ids = {
            TWW3World.location_name_to_id[f"Empire Size 6 ({check})"]
            for check in range(5)
        }
        context.missing_locations = accessible_location_ids | final_location_ids

        await context.check("6")

        self.assertEqual(5, context.settlementCount)
        self.assertFalse(context.postVictoryCapacityOverride)
        context.sendMessage.assert_not_called()
        context.send_msgs.assert_awaited_once()
        location_message = context.send_msgs.await_args.args[0][0]
        self.assertEqual("LocationChecks", location_message["cmd"])
        self.assertSetEqual(accessible_location_ids, set(location_message["locations"]))
        self.assertTrue(final_location_ids.isdisjoint(location_message["locations"]))

    async def test_free_tier_allows_the_size_five_batch(self) -> None:
        context = self.make_context(received_items=0)
        expected_location_ids = {
            TWW3World.location_name_to_id[f"Empire Size 5 ({check})"]
            for check in range(5)
        }
        context.missing_locations = expected_location_ids.copy()

        await context.check("5")

        self.assertEqual(5, context.settlementCount)
        location_message = context.send_msgs.await_args.args[0][0]
        self.assertSetEqual(expected_location_ids, set(location_message["locations"]))
        context.sendMessage.assert_not_called()

    async def test_received_item_count_is_sent_while_logic_uses_the_free_tier(self) -> None:
        context = self.make_context(received_items=0)
        context.itemDict = {1000: progressionDict[1000]}
        context.itemArchive = {"items": []}
        context.messenger = Mock()
        context.receivedItems = []
        context.notificationPending = False
        context.initialized = False

        context.on_received_items({"items": [SimpleNamespace(item=1000)]})
        await asyncio.sleep(0)

        self.assertEqual(1, context.expansionItems)
        context.sendMessage.assert_called_once_with("archipelago.set_admin_capacity(1)")
        self.assertEqual(5, context.adminCapacity)

    async def test_resync_replays_raw_capacity_count_and_post_victory_override(self) -> None:
        context = self.make_context(received_items=3)
        context.postVictoryCapacityOverride = True
        context.messenger = Mock()
        context.itemDict = {}
        context.progressiveTechs = False
        context.progressiveBuildings = False
        context.progressiveUnits = False
        context.itemArchive = {"items": []}
        context.on_received_items = Mock()
        context.locationArchive = []

        await context.resync()

        self.assertEqual(0, context.expansionItems)
        self.assertEqual(
            [
                call("archipelago.set_admin_capacity(0)"),
                call("archipelago.set_admin_capacity_mult(1000)"),
            ],
            context.messenger.runTemp.call_args_list,
        )
        context.on_received_items.assert_called_once_with(context.itemArchive, True)

    def test_status_reports_actual_items_and_active_tiers(self) -> None:
        context = self.make_context(received_items=1)
        context.settlementCount = 6
        context.postVictoryCapacityOverride = True

        with patch("worlds.tww3.client.logger.info") as log_info:
            TWW3CommandProcessor(context)._cmd_ac()

        status_lines = [logged_call.args[0] for logged_call in log_info.call_args_list]
        self.assertIn("You have received 1/1 Administrative Capacity upgrades", status_lines)
        self.assertIn("You have 2 active Administrative Capacity tiers", status_lines)
        self.assertIn("Your Administrative Capacity upgrades provide capacity for 10 settlements", status_lines)
        self.assertIn("Post-victory settlement penalties are disabled", status_lines)
        self.assertIn("You currently control 6 settlements", status_lines)


if __name__ == "__main__":
    unittest.main()
