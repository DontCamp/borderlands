# Patches!
Community Patch and Mods Collection for the DontCamp.com community

All credits to the [original authors](https://github.com/BLCM/BLCMods).  This repository serves as a way for DontCamp.com community members to more easily stay up to date with our latest patch set distribution.

## Configuration

1. Run [Borderlands-Hex-Multitool](https://github.com/c0dycode/Borderlands-Hex-Multitool)

2. In the program, select the appropriate game (BL2|TPS) via the icon at top left.

3. Ensure the **Console and Set Command** option is enabled.  Configure the key you wish to bind the console to.

4. Select **Apply**. You may now close the program.

5. Save our customized **Patch.txt** ([BL2](https://raw.githubusercontent.com/DontCamp/borderlands/master/bl2/Patch.txt)|[TPS](https://raw.githubusercontent.com/DontCamp/borderlands/master/tps/Patch.txt)) for the appropriate game to 

```%HOMEPATH%\Documents\My Games\Borderlands 2\Binaries\Patch.txt```

OR

```%HOMEPATH%\Documents\My Games\Borderlands The Pre-Sequel\Binaries\Patch.txt```

6. Run the game, and at the main menu screen, bring up the console and run **exec patch.txt**. This must be done each time you run the game. Note that the doskey history persists between runs.

## Automatic Updates

Our distribution of the patch changes sometimes.  In order to keep all players current, automation is provided that will update **Patch.txt** when the game is launched.

Notable downsides of this automation are that the file is re-downloaded every time, due to limitations of the built-in Windows **Invoke-WebRequest** (aliased to **wget**) PowerShell cmdlet, and if your **cmd.exe** binary is somehow not on your **C:** drive, then you are pretty silly.  This was intended as a way to avoid having to install Cygwin or Windows Subsystem for Linux, but for nerds who have that stuff installed, an alternate method using a proper **wget** binary which can avoid re-downloading unchanged files would be cool.

1.  Save the appropriate dlpatch.bat ([BL2](https://raw.githubusercontent.com/DontCamp/borderlands/master/bl2/dlpatch.bat)|[TPS](https://raw.githubusercontent.com/DontCamp/borderlands/master/tps/dlpatch.bat)) for your game to 

```%HOMEPATH%\Documents\My Games\Borderlands 2\Binaries\dlpatch.bat```

OR

```%HOMEPATH%\Documents\My Games\Borderlands The Pre-Sequel\Binaries\dlpatch.bat```

2.  In the Steam launch options, set the following for the appropriate game:

BL2

```C:\Windows\System32\cmd.exe /c %HOMEPATH%\Documents\"My Games"\"Borderlands 2"\Binaries\dlpatch.bat & %command% -nostartupmovies -NoLauncher```

TPS

```C:\Windows\System32\cmd.exe /c %HOMEPATH%\Documents\"My Games"\"Borderlands The Pre-Sequel"\Binaries\dlpatch.bat & %command% -NoLauncher```

## Mod List
### BL2
[Commnity Patch Changelog](https://raw.githubusercontent.com/BLCM/BLCMods/master/Borderlands 2 mods/Community Patch Team/Full UCP Changelog.txt)
* [#MakeVendorsGreatAgain2017](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/Jim Raven/%23MakeVendorsGreatAgain2017)
* [BetterVehicles](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/Teratorn43906/Better Vehicles (SLAG IMMUNITY! NO%2C I'M NOT JOKING)/BetterVehicles.txt)
* [BL2 No Wasted COMs](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/Apocalyptech/BL2 No Wasted COMs/BL2 No Wasted COMs.txt)
* [ButtStallion](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/EmpireScum/ButtStallion.txt)
* [CarAnywhere](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/FromDarkHell/Car Changes/CarAnywhere.txt)
* [MoreVehicles](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/OurLordAndSaviorGabeNewell/MoreVehicles.blcm)
* [Golden Chest is Free](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/Naarin/Golden Chest is Free (FilterTool))
* [Item lvl Fix](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/VexilleSerra/Item lvl Fix)
* ~[More Loot Midget Containers](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/Apocalyptech/More Loot Midget Containers/More Loot Midget Containers.txt)~
* [No Respec Cost](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/AngrierPat/Quality of life changes/No Respec Cost)
* [NoMuzzleflashes](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/Sommer/QUALITY OF LIFE/NoMuzzleflashes.txt)
* [second chances](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/Ethel/Second Chances/second chances.txt)
* [Speedier Sandskiffs](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/Apocalyptech/Speedier Sandskiffs/Speedier Sandskiffs.txt)
* ~[STV no self dmg](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/Ethel/STV no self dmg/STV no self dmg.txt)~
* [ToggleGaige](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/soze/Experimental/Toggle Skills (hotfix)/ToggleGaige.txt)
* [TurretRecall(hotfix)](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/theNocturni/Axton/TurretRecall(hotfix).txt)
* ~[PartNotifier](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/FromDarkHell/Quality of Life/PartNotifier.txt)~
* [LessClutteringParticles](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/Sommer/QUALITY OF LIFE/LessClutteringParticles.txt)
* [Rarity Color Fix](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/Koby/Single Mods/Quality of Life and Fixes/Rarity Color Fix.txt)
* ~[VarkidOverhaul](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/LightChaosman/VarkidOverhaul.txt)~
* [RepeatDon'tCopyThatFloppy](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/LollosaurusRex/Make Don-t Copy That Floppy Repeatable/RepeatDon'tCopyThatFloppy.blcm)
* [BL2 Container TimeSaver XL](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/Apocalyptech/BL2 Container TimeSaver XL/BL2 Container TimeSaver XL.blcm)
* [No Crushers in Lair of Infinite Agony](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/Apocalyptech/No Crushers in Lair of Infinite Agony/No Crushers in Lair of Infinite Agony.blcm)
* [BetterProgressionInDigistructPeak](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/OurLordAndSaviorGabeNewell/BetterProgressionInDigistructPeak.blcm)
* [Elemental Melee](https://www.nexusmods.com/borderlands2/mods/87)
* [GunlessUniqueDropSoundNotifier](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/OurLordAndSaviorGabeNewell/GunlessUniqueDropSoundNotifier.blcm)
* [NO_MORE_ORDERS](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/Exotek/QOL/NO_MORE_ORDERS.blcm)
* [OPTIONAL_OBJECTIVES+_](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/Exotek/QOL/OPTIONAL_OBJECTIVES%2B_.blcm)
* ~[PhaselockTweaks](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/55tumbl/Skill Changes/PhaselockTweaks.blcm)~
* [Vanilla Enhanced](https://www.nexusmods.com/borderlands2/mods/88)
* [AutoTrashOrFavorite](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/OurLordAndSaviorGabeNewell/AutoTrashOrFavorite.blcm)
* [Fast Travel - Bank - Stash - Quick Change From Anywhere](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/OurLordAndSaviorGabeNewell/Fast Travel - Bank - Stash - Quick Change From Anywhere.blcm)
* [LargerMidgetContainers](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/OurLordAndSaviorGabeNewell/LargerMidgetContainers.blcm)
* [UncappedPauseMenuSettings](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/OurLordAndSaviorGabeNewell/UncappedPauseMenuSettings.blcm)
* [FreeRaidCost](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/Freya/QUALITY OF LIFE/FreeRaidCost.blcm)
* [LessDumbVisuals](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/Freya/QUALITY OF LIFE/LessDumbVisuals.blcm)
* ~[ARPGStyleLootBeams](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/OurLordAndSaviorGabeNewell/ARPGStyleLootBeams.blcm)~
* [BlockingDoorRemoval](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/OurLordAndSaviorGabeNewell/BlockingDoorRemoval.blcm)
* ~[HeadAndSkinUsabilityUnlocker](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/OurLordAndSaviorGabeNewell/HeadAndSkinUsabilityUnlocker.blcm)~
* [RespawningLoot](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/OurLordAndSaviorGabeNewell/RespawningLoot.blcm)
* [RespawningEnemiesAndAllies](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/OurLordAndSaviorGabeNewell/RespawningEnemiesAndAllies.blcm)
* ~[Teleport](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/OurLordAndSaviorGabeNewell/Teleport.txt)~
* [TheBestPartyI'veEverThrown](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/OurLordAndSaviorGabeNewell/TheBestPartyI'veEverThrown.CL4P-TP)
* [AnemoneFastTravels](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/apple1417/AnemoneFastTravels.blcm)
* [LootDespawner](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/OurLordAndSaviorGabeNewell/LootDespawner.blcm)
* [EZAmmoVendors](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/Ethel/EZ Ammo Vendors/EZAmmoVendors.txt)
* [Firing Range Vendors](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/Ethel/Firing Range Vendors/Firing Range Vendors.blcm)
* [BL2 Configurable Slot Machines](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/Apocalyptech/BL2 Configurable Slot Machines/BL2 Configurable Slot Machines.blcm)
* [Cheaper Black Market](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/Coleby/Cheaper Black Market)
* [GrogNozzleMissionReward](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/Jim Raven/GrogNozzleMissionReward)
* [More Rare Midgets](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/Hemaxhu/Spawn Rates/More Rare Midgets)
* [World Spawn Loot Midgets](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/Hemaxhu/Spawn Rates/World Spawn Loot Midgets)
* [LootMidgetWorld](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/mopioid/LootMidgetWorld.blcm)
* [BL2 Better Loot Mod](https://github.com/BLCM/BLCMods/tree/master/Borderlands 2 mods/Apocalyptech/BL2 Better Loot Mod)
* [Better Quests](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/Hemaxhu/Quest Rewards/Better Quests)
* [More Chests on Pandora](https://www.nexusmods.com/borderlands2/mods/99)
* [DerpTrap](https://github.com/BLCM/BLCMods/tree/master/Borderlands 2 mods/Ethel/DerpTrap)
* [Exp++](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/Jim Raven/Exp%2B%2B)
* [More Chubbies](https://github.com/BLCM/BLCMods/blob/master/Borderlands 2 mods/Hemaxhu/Spawn Rates/More Chubbies)
* [Guaranteed Omnd-Omnd-Ohk](https://github.com/BLCM/BLCMods/tree/master/Borderlands%202%20mods/Apocalyptech/Guaranteed%20Omnd-Omnd-Ohk)
* [Guaranteed Varkid Evolution](https://github.com/BLCM/BLCMods/tree/master/Borderlands%202%20mods/Apocalyptech/Guaranteed%20Varkid%20Evolution)
* [SniperZoom](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/WarMocK/Small%20stuff/SniperZoom.txt)
* [ZoomedOutSights](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/TheDerpOfGames/ZoomedOutSights.txt)
* [OPWeaponVendors](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Greem/OP%20Shit/OPWeaponVendors.txt)
* ~[CryoElement](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Aaron0000/Overhauls/CryoElement.txt)~
* [Phaselock(hotfix) v2.1](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/theNocturni/Phaselock/Phaselock(hotfix)%20v2.1.txt)
* [MoxxiStash](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/CzRSpecV/MoxxiStash.txt)
* [No Death Cost](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/AngrierPat/Quality%20of%20life%20changes/No%20Death%20Cost)
* [More Muscles](https://github.com/BLCM/BLCMods/tree/master/Borderlands%202%20mods/Apocalyptech/More%20Muscles)

### TPS
[Commnity Patch Changelog](https://raw.githubusercontent.com/BLCM/BLCMods/master/Pre Sequel Mods/Community Patch/Community Patch 2.2/Full Changelog)
* [Speedier Moon Buggies](https://github.com/BLCM/BLCMods/blob/master/Pre Sequel Mods/Apocalyptech/Speedier Moon Buggies/Speedier Moon Buggies.blcm)
* [Speedier Stingrays](https://github.com/BLCM/BLCMods/blob/master/Pre Sequel Mods/Apocalyptech/Speedier Stingrays/Speedier Stingrays.blcm)
* [CarAnywhere](https://github.com/BLCM/BLCMods/blob/master/Pre Sequel Mods/FromDarkHell/Car Changes/CarAnywhere.txt)
* [TPS Rarity Color Fix](https://github.com/BLCM/BLCMods/blob/master/Pre Sequel Mods/Koby/TPS Rarity Color Fix.txt)
* [BuggyReplace](https://github.com/BLCM/BLCMods/blob/master/Pre Sequel Mods/Laxlife/BuggyReplace.txt)
* [No Respec Cost](https://github.com/BLCM/BLCMods/blob/master/Pre Sequel Mods/AngrierPat/Quality of life changes/No Respec Cost.blcm)
* [Item lvl Fix](https://github.com/BLCM/BLCMods/blob/master/Pre Sequel Mods/VexilleSerra/Item lvl Fix.blcm)
* [TPS Container TimeSaver XL](https://github.com/BLCM/BLCMods/blob/master/Pre Sequel Mods/Apocalyptech/TPS Container TimeSaver XL/TPS Container TimeSaver XL.blcm)
* [Infinite Air Boosts](https://github.com/BLCM/BLCMods/blob/master/Pre Sequel Mods/Apocalyptech/Infinite Air Boosts/Infinite Air Boosts.blcm)
* [TPSUncappedPauseMenuSettings](https://github.com/BLCM/BLCMods/blob/master/Pre Sequel Mods/OurLordAndSaviorGabeNewell/TPSUncappedPauseMenuSettings.blcm)
* [Weapon View Offset Code](https://github.com/BLCM/BLCMods/blob/master/Pre Sequel Mods/iNSANE990/Weapon View Offset Code.blcm)
* [Double Quest Rewards](https://github.com/BLCM/BLCMods/blob/master/Pre Sequel Mods/Astor/Quests Improvement/Double Quest Rewards/Double Quest Rewards v1.0.0.blcm)
* [FastTravelHelper](https://github.com/BLCM/BLCMods/blob/master/Pre Sequel Mods/apple1417/FastTravelHelper.blcm)
