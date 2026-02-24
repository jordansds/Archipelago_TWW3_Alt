from __future__ import annotations
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from .TWW3Client import TWW3Context
    from .world import TWW3World

deathLinkFunctions: list[str] = ["", "", ""]
#deathLinkOptions: list[str] = []

#Pull the enabled deathlink functions chosen in the yaml
def createDeathLinkFunctions(world: TWW3World):
    deathLinkOptions: list[bool] = [*world.options.death_link_effect]
    return [func for index, func in enumerate(deathLinkFunctions) if deathLinkOptions[index]]

async def receiveDeathLink(ctx: 'CivVIContext', message: str):
    deathLinkOptions = ctx.slot_data["death_link_options"]

async def checkDeathLink(ctx: 'CivVIContext', message: str):
    if ctx.received_death_link:
        ctx.received_death_link = False
        await receiveDeathLink(ctx, ctx.death_link_message)

    result = await ctx.game_interface.get_deathlink()
    if ctx.death_link_just_changed:
        ctx.death_link_just_changed = False
        return

