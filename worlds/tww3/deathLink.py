from __future__ import annotations
from typing import TYPE_CHECKING

deathLinkFunctionDict: dict[str, str] = {
    "10% Treasury" : "remove_treasury_percentage(10)",
    "25% Treasury": "remove_treasury_percentage(25)",
    "50% Treasury": "remove_treasury_percentage(50)",
    "Wound Hero": "wound_random_hero()",
    "Wound Lord": "wound_random_lord()",
    "Rebellion": "force_random_strong_rebellion_for_player()",
    "Raze Random Settlement": "raze_random_settlement()",
    "Disable Replenishment (2 turns)": "deathlink_disable_replenishment()"
}

#Pull the enabled deathlink functions chosen in the yaml
def createDeathLinkFunctions(deathLinkEffects):
    return {key: deathLinkFunctionDict[key] for key in deathLinkEffects}