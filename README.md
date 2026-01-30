# Total War: Warhammer 3 Archipelago Alt.
##
You must download the pack file included in the latest release. Do not use the workshop mod or this alt will not work.
Include the mod in the pack file in the warhammer 3 data folder and enable it in your mod manager.

## How does this work?
Upon starting a new game, all factions have their start positions randomised. Units, buildings, and technologies are
shuffled into the item pool meaning that you can't access them until the corresponding items are found in the multiworld.
The goal of this apworld is to conquer a certain number of settlements simultaneously, configurable in the yaml.
Additionally, your checks are determined by the goal - if your goal is 50 settlements, every settlement from 5-49 will
grant checks (unless your faction doesn't start with a home region, in which case it's 1-49). The number of checks you
send per settlement can be modified in the yaml - this is to account for how slow TWW3 can be to play and allows you to
tailor the pacing of checks to match other games in the multiworld.

**Playing beastmen is not recommended at this time.**

## What the yaml do

**starting_faction**: Pick who you wanna play!

**faction_shuffle**: Randomize starting positions. Recommended to be on.

*It's recommended that you use the [No Climate Penalties mod](https://steamcommunity.com/sharedfiles/filedetails/?id=2789893460)
with this setting turned on.*

**number_of_locations**: How many settlements you need to own simultaneously to reach your goal and determines the base number
of checks. Decrease this for a shorter game, increase for a longer one.

**checks_per_location**: How many checks there are per settlement. Increase this to release more items per settlement, decrease this
to slow down the pace of your checks.

*Note that these two options, number_of_locations and checks_per_location, will need to be set appropriately for your faction -
some factions have a lot of items that need generating while other factions need less. If world generation fails due to running
out of locations and you don't want to increase the number of settlements needed to goal, try increasing checks_per_location
instead.*

**balance**: Holdover from the original apworld. Might not do anything.

**max_range**: How far away settlements can be from each other during randomization.

**tech_shuffle**: Locks the tech tree behind multiworld items.

**progressive_technologies**: Requires tech_shuffle to be on. Every step further into your tech tree is a progressive item,
otherwise every tech is an individual item.

*If you play with progressive tech off you can use the [Remove Tech Requirements submod](https://steamcommunity.com/workshop/filedetails/?id=3541110164)
to research tech out of order so you don't have to wait for the whole chain to be found.*

**building_shuffle**: Locks buildings behind multiworld items.

**progressive_buildings**: Requires building_shuffle to be on. Instead of finding every single building seperately find
progressive items unlocking the next building for each specific building chain. Setting this to progressive is recommended.

**unit_shuffle**: Locks units behind multiworld items.

**progressive_units**: Requires unit_shuffle to be on. Instead of unlocking every unit separately tiers 1-5 are
progressive items for each unit type (progressive infantry, progressive cavalry, progressive monsters etc.).

*Setting both buildings and units as non-progressive is **not** recommended.*

**starting_tier**: Start with buildings and units of this tier already unlocked.

**filler and traps**: Set to your own liking.
(you can reload a previous save, traps wont trigger twice). Filler items include all equipment items. The
[No Item Requirement submod](https://steamcommunity.com/sharedfiles/filedetails/?id=3540371601) is recommended to
make sure you can equip every item you get.

**RandomizePersonalities**: Give AI factions random personalities. Makes the game less predictable.

**ritual_shuffle**: Locks certain faction mechanics behind multiworld items. Possibly broken right now.

## Recommended mods: 

[Remove Tech Requirements](https://steamcommunity.com/sharedfiles/filedetails/?id=3541110164): Lets you research all tech in any order. This is specifically intended to be used when
using shuffled non-progressive tech so you can research them immediately.

[Remove Faction Mechanic Debuffs](https://steamcommunity.com/sharedfiles/filedetails/?id=3540418784): Removes debuffs from Avelorn, Empire factions, Clan Angrund, Skarsnik and
Oxyotl which are related to specific places on the map you probably can't reach.

[No Item Requirements](https://steamcommunity.com/sharedfiles/filedetails/?id=3540371601): Lets you equip all items, even if they are restricted to a different Legendary Lord.

[No Climate Penalties](https://steamcommunity.com/sharedfiles/filedetails/?id=2789893460): Removes all climate penalties so your start position is not as bad as it seems.

*The version of the main mod that enables this apworld to work correctly is currently not on the Steam workshop or available anywhere else.*
