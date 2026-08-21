import unittest
from unittest.mock import AsyncMock, Mock, patch

from NetUtils import ClientStatus
from worlds.tww3 import TWW3World
from worlds.tww3.client import TWW3CommandProcessor, TWW3Context


class TestConquestClientProgression(unittest.IsolatedAsyncioTestCase):
    async def test_goal_observation_records_settlements_without_a_goal_check_batch(self) -> None:
        context = object.__new__(TWW3Context)
        context.gameMode = "conquest"
        context.maxEmpireSize = 6
        context.adminCapacity = 5
        context.expansionItems = 1
        context.maxExpansionItems = 1
        context.checksPerLocation = 5
        context.hardLogic = True
        context.settlementCount = 4
        context.postVictoryCapacityOverride = False
        expected_location_ids = [
            TWW3World.location_name_to_id[f"Empire Size 5 ({check})"]
            for check in range(5)
        ]
        context.missing_locations = set(expected_location_ids)
        context.send_msgs = AsyncMock()
        context.sendMessage = Mock()

        capacity_state = (context.expansionItems, context.maxExpansionItems, context.adminCapacity)

        await context.check("5")

        location_messages = [
            call.args[0][0]
            for call in context.send_msgs.await_args_list
            if call.args[0][0]["cmd"] == "LocationChecks"
        ]
        checked_locations = [
            location
            for message in location_messages
            for location in message["locations"]
        ]
        self.assertEqual(expected_location_ids, checked_locations)
        self.assertEqual(5, context.settlementCount)

        await context.check("6")

        self.assertEqual(6, context.settlementCount)
        self.assertEqual(capacity_state, (context.expansionItems, context.maxExpansionItems, context.adminCapacity))
        context.sendMessage.assert_called_once_with("archipelago.set_admin_capacity_mult(1000)")
        context.send_msgs.assert_any_await(
            [{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}]
        )
        await context.check("6")

        self.assertEqual(6, context.settlementCount)
        self.assertEqual(capacity_state, (context.expansionItems, context.maxExpansionItems, context.adminCapacity))
        context.sendMessage.assert_called_once_with("archipelago.set_admin_capacity_mult(1000)")
        all_location_messages = [
            call.args[0][0]
            for call in context.send_msgs.await_args_list
            if call.args[0][0]["cmd"] == "LocationChecks"
        ]
        self.assertEqual(location_messages, all_location_messages)

        with patch("worlds.tww3.client.logger.info") as log_info:
            TWW3CommandProcessor(context)._cmd_ac()

        status_lines = [call.args[0] for call in log_info.call_args_list]
        self.assertIn("You have received 1/1 Administrative Capacity upgrades", status_lines)
        self.assertIn("You have 2 active Administrative Capacity tiers", status_lines)
        self.assertIn("Your Administrative Capacity upgrades provide capacity for 10 settlements", status_lines)
        self.assertIn("Post-victory settlement penalties are disabled", status_lines)
        self.assertIn("You currently control 6 settlements", status_lines)
