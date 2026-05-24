# Total War: Warhammer 3 Archipelago Alt.
This is an alternate implementation of the original TWW3 world which includes all features of the original mod as well
as an alternate mode that works better for syncs.

DO NOT ENABLE BOTH THE SPHERES AND CONQUEST MODS AT THE SAME TIME. ONLY ENABLE THE GAMEMODE YOU SELECT IN THE YAML.
DO NOT USE THE "ARCHIPELAGO RANDOMIZER (BETA)" MOD FROM THE STEAM WORKSHOP.

## How does this work?
Upon starting a new game, all factions have their start positions randomised. Units, buildings, and technologies are
placed into the item pool meaning that you can't access them until the corresponding items are found in the multiworld.
The goal of this apworld is to conquer a certain number of settlements simultaneously, configurable in the yaml.

Additionally, your checks are determined by the selected game mode - in conquest mode if your goal is 50 settlements,
every settlement after your starting settlements until settlement 49 will grant checks (unless your faction doesn't 
start with a home region, in which case it's 1-49). The number of checks you send per settlement can be modified in the 
yaml - this is to account for how slow TWW3 can be to play and allows you to tailor the pacing of checks to match other 
games in the multiworld.

In sphere mode every unique settlement in the world can be a check, though only a certain amount will be active based
on your current diplomatic radius. IF YOU PLAN TO PLAY SPHERES MODE, SCROLL DOWN AND DOWNLOAD THE RECOMMENDED MODS TO
PREVENT POTENTIAL SOFTLOCK.

**If your lord does not spawn next to your city, type /teleport into your client**  

## Installation and setup  
 - Install the [Archipelago launcher](https://github.com/ArchipelagoMW/Archipelago/releases/latest)  
 - Download all .pack files and the .apworld from the [latest mod release](https://github.com/jordansds/Archipelago_TWW3_Alt/releases/latest)  
 - If you're not hosting the session, the host that is generating the multiworld will need the .apworld file, but not the .pack files.  
 - Move the .pack files to the Total War Warhammer data directory e.g. `SteamLibrary/steamapps/common/Total War WARHAMMER III/data/`  
 - Double click the .apworld and it will be installed to the Archipelago launcher.  

 - In the Archipelago launcher, run "Generate Template Options" and find the Total War Warhammer 3 template. Copy it up one directory to the players folder and edit the file.  
 - If you've never used a yaml before, refer to [this page](https://archipelago.gg/tutorial/Archipelago/advanced_settings_en) for an explanation of how
it works. For more detailed information on what the yaml settings do, check below.  
 - Once you have editted the file, run "Generate" in the Archipelago Launcher to create the .zip, then host the generated multiworld either locally using "Host" or on the [Archipelago website](https://archipelago.gg/uploads).  
 - Run the "Total War Warhammer" from the Archipelago Launcher and select the folder where the Warhammer.exe file is saved when prompted.  
 - Connect to the multiworld and it will tell you which faction you have selected and which gamemode. If the multiworld is hosted on the Archipelago
website then in the connection field you will need to enter `archipelago.gg/` followed by the port number. The port will be
displayed on the lobby page for the multiworld.  

 - Launch Total War Warhammer 3 and in the mod launcher, enable the QOL.pack along with either the spheres or conquest .pack file you downloaded (depending on which gamemode the Archipelago Launcher says).  
(If the mods do not show up, try using [this mod manager](https://github.com/Shazbot/WH3-Mod-Manager/releases/tag/v2.16.14) instead (it's better).  
**.pack is the file format used by TWW3 mods and contains the code needed for the game modes to function. Make sure you *don't*
use the Archipelago mod found on the Steam workshop, it is for another dev's outdated APWorld.**  

 - Launch the game, select the correct faction, and start playing!  

## What the yaml do

**Many of these settings are outdated at this time, will be updated soonish**

**starting_faction**: Select the faction you're going to play as.

**faction_shuffle**: Randomize starting positions. Recommended to be on.

*It's recommended that you use the [No Climate Penalties mod](https://steamcommunity.com/sharedfiles/filedetails/?id=2789893460)
with this setting turned on.*

**game_mode**: `conquest` is the new mode offered by this implementation and consists of owning a certain number of settlements
to win. The number of settlements needed is determined by `number_of_locations`. Checks are granted as your empire size grows.
This lends itself to faster paced games and plays better in synchronous multiworlds.

`spheres` is the old game mode originally developed by SinthorasRage. This mode starts with a limited radius in which you can interact with other factions, which
grows as you collect **Diplomatic Radius** upgrades. Along the way **Orbs of Domination** are also collected - upon collecting enough,
you win. Every settlement on the map is a unique check. This is a *much* slower paced game than conquest.
Additionally this mode is prone to causing softlocks, as AI factions can claim razed settlements causing them to become 
out of logic and impossible to collect items from. If this happens you will have to release the location manually.

**checks_per_settlement**: How many checks there are per settlement. Increase this to release more items per settlement, decrease this
to slow down the pace of your checks. This is designed to allow smaller values for "number_of_settlements" whilst still generating
enough locations for all your items. If you set this to an absurd number, you'll end up with far too much filler items and traps.

### Conquest settings
**number_of_settlements**: How many settlements you need to own simultaneously to reach your goal and determines the base number
of checks. Decrease this for a shorter game, increase for a longer one.

*Note that these two options, number_of_locations and checks_per_location, will need to be set appropriately for your faction -
some factions have a lot of items that need generating while other factions need less. If world generation fails due to running
out of locations and you don't want to increase the number of settlements needed to win, try increasing checks_per_location
instead!*

### Spheres settings

**spheres_count**: How many diplomatic radius upgrades are needed to have access to every location. Doesn't necessarily cover the
entire map unless you configure `sphere_radius` to do so.

### Global settings

**max_range**: How far away settlements can be from each other during world generation.

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

**filler and traps**: Adjust the weights of traps and filler. Traps only trigger once so they don't softlock you if you need
to start over or load a save. Filler items include all equipment items.
The [No Item Requirement submod](https://steamcommunity.com/sharedfiles/filedetails/?id=3540371601)
is recommended to make sure you can equip every item you get.

**randomize_personalities**: Give AI factions random personalities. Makes the game less predictable.

**ritual_shuffle**: Locks certain faction mechanics behind multiworld items.

**balance**: Forces unlocks to be near the start of the multiworld so you're guaranteed to get useful items early.
In a multiworld setting, 20 is probably the highest you'd want this. If you're not sure what to do with this option,
either set it to 10 or leave it off. For singleplayer games a value of at least 40 should guarantee a smooth early game.

**force_early**: Sets the max tiers that can be forced to generate early.
5 allows all tiers to generate, 0 disables early generation.

## Recommended mods: 

[Ruins Settling Cooldown](https://steamcommunity.com/workshop/filedetails/?id=2937367689): PREVENTS SOFTLOCKING in spheres gamemeode if you set min and max to 100 turn cooldown and enable for AI (not player). HIGHLY RECOMMENDED FOR SPHERES.

[Mod Configuration Tool](https://steamcommunity.com/workshop/filedetails/?id=2927955021): Allows configuration of the above mod. HIGHLY RECOMMENDED FOR SPHERES.

[No Item Requirements](https://steamcommunity.com/sharedfiles/filedetails/?id=3540371601): Lets you equip all items, even if they are restricted to a different Legendary Lord.

[No Climate Penalties](https://steamcommunity.com/sharedfiles/filedetails/?id=2789915966): Removes all climate penalties so your start position is not as bad as it seems.

[Sea Lord Aislinn – Infinite Colonies](https://steamcommunity.com/workshop/filedetails/?id=3626519982): Allows Aislinn to conquer any city as an elven colony.
