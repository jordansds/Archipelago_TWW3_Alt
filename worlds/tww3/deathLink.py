from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .world import TWW3World

#deathLinkFunctions: list[str] = ["remove_treasury_percentage(10)", "remove_treasury_percentage(25)", "remove_treasury_percentage(50)"]
deathLinkFunctionDict: dict[str, str] = {
    "10% Treasury" : "remove_treasury_percentage(10)",
    "25% Treasury": "remove_treasury_percentage(25)",
    "50% Treasury": "remove_treasury_percentage(50)",
    "Wound Hero": "wound_random_hero()",
    "Wound Lord": "wound_random_lord()",
    "Rebellion": "force_random_strong_rebellion_for_player()",
    "Raze Random Settlement": "raze_random_settlement()"
}
#deathLinkOptions: list[str] = []

#Pull the enabled deathlink functions chosen in the yaml
def createDeathLinkFunctions(deathLinkEffects):
    return [deathLinkFunctionDict[key] for key in deathLinkEffects]
    #deathLinkOptions: list[bool] = [*world.options.death_link_effect]
    #return [func for key, func in enumerate(deathLinkFunctions) if deathLinkOptions[index]]