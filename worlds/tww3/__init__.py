from worlds.LauncherComponents import components, Component, launch, Type, icon_paths
from .world import TWW3World as TWW3World

def runClient(*args: str) -> None:
    from .client import launchClient
    launch(launchClient, name="Total War Warhammer III Client", args=args)

components.append(Component("Total War Warhammer III Client",
                            game_name="Total War Warhammer III",
                            func=runClient,
                            component_type=Type.CLIENT,
                            supports_uri=True,
                            description="Launches the Total War Warhammer III client.",
                            icon="TWW3"))
icon_paths["TWW3"] = f"ap:{__name__}/tww3client.png"