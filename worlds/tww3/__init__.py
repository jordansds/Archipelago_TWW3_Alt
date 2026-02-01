from worlds.LauncherComponents import components, Component, launch_subprocess, Type
from .world import TWW3World as TWW3World

def launch_client():
    from .TWW3Client import launch
    launch_subprocess(launch, name="TWW3Client")

components.append(Component("TWW3 Client",
                            func=launch_client,
                            component_type=Type.CLIENT,
                            description="Launches the Total War Warhammer 3 client.",
                            icon=f"ap:{__name__}/tww3client.png"))
