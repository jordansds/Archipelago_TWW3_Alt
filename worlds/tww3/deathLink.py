from __future__ import annotations
from typing import TYPE_CHECKING

deathLinkFunctionDict: dict[str, str] = {
    "10% Treasury" : "archipelago.remove_treasury_percentage(10)",
    "25% Treasury": "archipelago.remove_treasury_percentage(25)",
    "50% Treasury": "archipelago.remove_treasury_percentage(50)",
    "Wound Hero": 'archipelago.wound_random_unit("hero")',
    "Wound Lord": 'archipelago.wound_random_unit("lord")',
    "Rebellion": "archipelago.force_random_strong_rebellion_for_player()",
    "Raze Random Settlement": "archipelago.raze_random_settlement()",
    "Disable Replenishment (2 turns)": "archipelago.disable_replenishment()"
}

#Pull the enabled deathlink functions chosen in the yaml
def createDeathLinkFunctions(deathLinkEffects):
    return {key: deathLinkFunctionDict[key] for key in deathLinkEffects}