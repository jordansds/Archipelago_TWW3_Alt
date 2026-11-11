# Total War: Warhammer 3 Archipelago Alt.
This is an alternate implementation of the original TWW3 world which includes all features of the original mod as well
as an alternate mode that works better for syncs.

DO NOT USE THE "ARCHIPELAGO RANDOMIZER (BETA)" MOD FROM THE STEAM WORKSHOP.
[FAQ](FAQ.md)

## How does this work?
Upon starting a new game, all factions have their start positions randomised. Units, buildings, and technologies are
placed into the item pool meaning that you can't access them until the corresponding items are found in the multiworld.
The goal of this apworld is to find 9 keys that will unlock the end-times crisis (crisis can be disabled in the yaml if you're a coward).
To find keys, you must receive "map" items from other players in your multiworld which will tell you where the keys are and let you find them.

**If your lord does not spawn next to your city, type /teleport into your client**  

## Installation and setup  
 - Install the LATEST VERSION of the [Archipelago launcher](https://github.com/ArchipelagoMW/Archipelago/releases/latest)  
 - Download the .pack file and the .apworld from the [latest mod release](https://github.com/jordansds/Archipelago_TWW3_Alt/releases/latest)  
 - If you're not hosting the session, the host that is generating the multiworld will need the .apworld file, but not the .pack files.  
 - Move the .pack files to the Total War Warhammer data directory e.g. `SteamLibrary/steamapps/common/Total War WARHAMMER III/data/`  
 - Double click the .apworld and it will be installed to the Archipelago launcher.  

 - In the Archipelago launcher, run "Generate Template Options" and find the Total War Warhammer 3 template. Copy it up one directory to the players folder and edit the file.  
 - If you've never used a yaml before, refer to [this page](https://archipelago.gg/tutorial/Archipelago/advanced_settings_en) for an explanation of how
it works. For more detailed information on what the yaml settings do, check below.  
 - Once you have editted the file, run "Generate" in the Archipelago Launcher to create the .zip, then host the generated multiworld either locally using "Host" or on the [Archipelago website](https://archipelago.gg/uploads).  
 - Run the "Total War Warhammer" client from the Archipelago Launcher and select the folder where the Warhammer.exe file is saved when prompted.  
 - Connect to the multiworld and it will tell you which faction you have selected and which gamemode. If the multiworld is hosted on the Archipelago
website then in the connection field you will need to enter `archipelago.gg/` followed by the port number. The port will be
displayed on the lobby page for the multiworld.  

 - Launch Total War Warhammer 3 and in the mod launcher, enable the .pack file you downloaded.  
If the mods do not show up, try using [this mod manager](https://github.com/Shazbot/WH3-Mod-Manager/releases/tag/v2.16.14) instead (it's better).  
**.pack is the file format used by TWW3 mods and contains the code needed for the game modes to function. Make sure you *don't*
use the Archipelago mod found on the Steam workshop, it is for another dev's outdated APWorld.**  

 - Launch the game, select the correct faction, and start playing!  

## What the yaml do

**Many of these settings are outdated at this time, will be updated soonish**

**starting_faction**: Select the faction you're going to play as.

**faction_shuffle**: Randomize starting positions. Recommended to be on.

*It's recommended that you use the [No Climate Penalties mod](https://steamcommunity.com/sharedfiles/filedetails/?id=2789893460)
with this setting turned on.*

### Global settings

**max_range**: How far away settlements can be from each other during world generation.

**tech_shuffle**: Locks the tech tree behind multiworld items.

**progressive_technologies**: Requires tech_shuffle to be on. Every step further into your tech tree is a progressive item,
otherwise every tech is an individual item.

**building_shuffle**: Locks buildings behind multiworld items.

**progressive_buildings**: Requires building_shuffle to be on. Instead of finding every single building seperately find
progressive items unlocking the next building for each specific building chain. Setting this to progressive is recommended.

**unit_shuffle**: Locks units behind multiworld items.

**progressive_units**: Requires unit_shuffle to be on. Instead of unlocking every unit separately tiers 1-5 are
progressive items for each unit type (progressive infantry, progressive cavalry, progressive monsters etc.).

*Setting both buildings and units as non-progressive is **not** recommended.*

**starting_tier**: Start with buildings and units of this tier already unlocked.

**filler and traps**: Adjust the weights of traps and filler. Traps only trigger once so they don't softlock you if you need
to start over or load a save. Filler items include most legendary equipment items.

**randomize_personalities**: Give AI factions random personalities. Makes the game less predictable.

**ritual_shuffle**: Locks certain faction mechanics behind multiworld items.

**balance**: Forces unlocks to be near the start of the multiworld so you're guaranteed to get useful items early.
In a multiworld setting, 20 is probably the highest you'd want this. If you're not sure what to do with this option,
either set it to 10 or leave it off. For singleplayer games a value of at least 40 should guarantee a smooth early game.

**force_early**: Sets the max tiers that can be forced to generate early.
5 allows all tiers to generate, 0 disables early generation.

## Recommended mods: 

[No Climate Penalties](https://steamcommunity.com/sharedfiles/filedetails/?id=2789915966): Removes all climate penalties so your start position is not as bad as it seems.
