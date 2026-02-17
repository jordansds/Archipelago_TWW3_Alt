from worlds.LauncherComponents import components, Component, launch, Type, icon_paths
from .world import TWW3World as TWW3World

def runClient(*args: str) -> None:
    from .TWW3Client import launchClient
    launch(launchClient, name="TWW3 Client", args=args)

components.append(Component("TWW3 Client",
                            game_name="Total War Warhammer 3",
                            func=runClient,
                            component_type=Type.CLIENT,
                            supports_uri=True,
                            description="Launches the Total War Warhammer 3 client.",
                            icon="TWW3"))
icon_paths["TWW3"] = f"ap:{__name__}/tww3client.png"