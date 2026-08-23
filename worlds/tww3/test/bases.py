from test.bases import WorldTestBase


class TWW3TestBase(WorldTestBase):
    game = "Total War Warhammer III"
    run_default_tests = False

    def get_conquest_location_names(self) -> set[str]:
        return {
            location.name
            for location in self.multiworld.get_locations(self.player)
            if location.name.startswith("Empire Size ")
        }
