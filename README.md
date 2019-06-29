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
[Commnity Patch Changelog](https://raw.githubusercontent.com/BLCM/BLCMods/master/Borderlands%202%20mods/Community%20Patch%20Team/Full%20UCP%20Changelog.txt)
* [#MakeVendorsGreatAgain2017](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Jim%20Raven/%23MakeVendorsGreatAgain2017)
* [BetterVehicles](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Teratorn43906/Better%20Vehicles%20(SLAG%20IMMUNITY!%20NO%2C%20I'M%20NOT%20JOKING)/BetterVehicles.txt)
* [BL2 No Wasted COMs](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Apocalyptech/BL2%20No%20Wasted%20COMs/BL2%20No%20Wasted%20COMs.txt)
* [ButtStallion](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/EmpireScum/ButtStallion.txt)
* [CarAnywhere](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/FromDarkHell/Car%20Changes/CarAnywhere.txt)
* [MoreVehicles](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/OurLordAndSaviorGabeNewell/MoreVehicles.blcm)
* [Golden Chest is Free](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Naarin/Golden%20Chest%20is%20Free%20(FilterTool))
* [Item lvl Fix](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/VexilleSerra/Item%20lvl%20Fix)
* ~[More Loot Midget Containers](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Apocalyptech/More%20Loot%20Midget%20Containers/More%20Loot%20Midget%20Containers.txt)~
* [No Respec Cost](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/AngrierPat/Quality%20of%20life%20changes/No%20Respec%20Cost)
* [NoMuzzleflashes](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Sommer/QUALITY%20OF%20LIFE/NoMuzzleflashes.txt)
* [second chances](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Ethel/Second%20Chances/second%20chances.txt)
* [Speedier Sandskiffs](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Apocalyptech/Speedier%20Sandskiffs/Speedier%20Sandskiffs.txt)
* ~[STV no self dmg](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Ethel/STV%20no%20self%20dmg/STV%20no%20self%20dmg.txt)~
* [ToggleGaige](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/soze/Experimental/Toggle%20Skills%20(hotfix)/ToggleGaige.txt)
* [TurretRecall(hotfix)](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/theNocturni/Axton/TurretRecall(hotfix).txt)
* ~[PartNotifier](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/FromDarkHell/Quality%20of%20Life/PartNotifier.txt)~
* [LessClutteringParticles](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Sommer/QUALITY%20OF%20LIFE/LessClutteringParticles.txt)
* [Rarity Color Fix](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Koby/Single%20Mods/Quality%20of%20Life%20and%20Fixes/Rarity%20Color%20Fix.txt)
* ~[VarkidOverhaul](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/LightChaosman/VarkidOverhaul.txt)~
* [RepeatDon'tCopyThatFloppy](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/LollosaurusRex/Make%20Don-t%20Copy%20That%20Floppy%20Repeatable/RepeatDon'tCopyThatFloppy.blcm)
* [BL2 Container TimeSaver XL](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Apocalyptech/BL2%20Container%20TimeSaver%20XL/BL2%20Container%20TimeSaver%20XL.blcm)
* [No Crushers in Lair of Infinite Agony](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Apocalyptech/No%20Crushers%20in%20Lair%20of%20Infinite%20Agony/No%20Crushers%20in%20Lair%20of%20Infinite%20Agony.blcm)
* [BetterProgressionInDigistructPeak](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/OurLordAndSaviorGabeNewell/BetterProgressionInDigistructPeak.blcm)
* [Elemental Melee](https://www.nexusmods.com/borderlands2/mods/87)
* [GunlessUniqueDropSoundNotifier](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/OurLordAndSaviorGabeNewell/GunlessUniqueDropSoundNotifier.blcm)
* [NO_MORE_ORDERS](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Exotek/QOL/NO_MORE_ORDERS.blcm)
* [OPTIONAL_OBJECTIVES+_](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Exotek/QOL/OPTIONAL_OBJECTIVES%2B_.blcm)
* ~[PhaselockTweaks](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/55tumbl/Skill%20Changes/PhaselockTweaks.blcm)~
* [Vanilla Enhanced](https://www.nexusmods.com/borderlands2/mods/88)
* [AutoTrashOrFavorite](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/OurLordAndSaviorGabeNewell/AutoTrashOrFavorite.blcm)
* [Fast Travel - Bank - Stash - Quick Change From Anywhere](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/OurLordAndSaviorGabeNewell/Fast%20Travel%20-%20Bank%20-%20Stash%20-%20Quick%20Change%20From%20Anywhere.blcm)
* [LargerMidgetContainers](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/OurLordAndSaviorGabeNewell/LargerMidgetContainers.blcm)
* [UncappedPauseMenuSettings](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/OurLordAndSaviorGabeNewell/UncappedPauseMenuSettings.blcm)
* [FreeRaidCost](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Freya/QUALITY%20OF%20LIFE/FreeRaidCost.blcm)
* [LessDumbVisuals](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Freya/QUALITY%20OF%20LIFE/LessDumbVisuals.blcm)
* ~[ARPGStyleLootBeams](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/OurLordAndSaviorGabeNewell/ARPGStyleLootBeams.blcm)~
* [BlockingDoorRemoval](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/OurLordAndSaviorGabeNewell/BlockingDoorRemoval.blcm)
* ~[HeadAndSkinUsabilityUnlocker](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/OurLordAndSaviorGabeNewell/HeadAndSkinUsabilityUnlocker.blcm)~
* [RespawningLoot](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/OurLordAndSaviorGabeNewell/RespawningLoot.blcm)
* [RespawningEnemiesAndAllies](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/OurLordAndSaviorGabeNewell/RespawningEnemiesAndAllies.blcm)
* ~[Teleport](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/OurLordAndSaviorGabeNewell/Teleport.txt)~
* [TheBestPartyI'veEverThrown](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/OurLordAndSaviorGabeNewell/TheBestPartyI'veEverThrown.CL4P-TP)
* [AnemoneFastTravels](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/apple1417/AnemoneFastTravels.blcm)
* [LootDespawner](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/OurLordAndSaviorGabeNewell/LootDespawner.blcm)
* [EZAmmoVendors](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Ethel/EZ%20Ammo%20Vendors/EZAmmoVendors.txt)
* [Firing Range Vendors](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Ethel/Firing%20Range%20Vendors/Firing%20Range%20Vendors.blcm)
* [BL2 Configurable Slot Machines](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Apocalyptech/BL2%20Configurable%20Slot%20Machines/BL2%20Configurable%20Slot%20Machines.blcm)
* [Cheaper Black Market](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Coleby/Cheaper%20Black%20Market)
* [GrogNozzleMissionReward](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Jim%20Raven/GrogNozzleMissionReward)
* [More Rare Midgets](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Hemaxhu/Spawn%20Rates/More%20Rare%20Midgets)
* [World Spawn Loot Midgets](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Hemaxhu/Spawn%20Rates/World%20Spawn%20Loot%20Midgets)
* [LootMidgetWorld](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/mopioid/LootMidgetWorld.blcm)
* [BL2 Better Loot Mod](https://github.com/BLCM/BLCMods/tree/master/Borderlands%202%20mods/Apocalyptech/BL2%20Better%20Loot%20Mod)
* [Better Quests](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Hemaxhu/Quest%20Rewards/Better%20Quests)
* [More Chests on Pandora](https://www.nexusmods.com/borderlands2/mods/99)
* [DerpTrap](https://github.com/BLCM/BLCMods/tree/master/Borderlands%202%20mods/Ethel/DerpTrap)
* [Exp++](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Jim%20Raven/Exp%2B%2B)
* [More Chubbies](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Hemaxhu/Spawn%20Rates/More%20Chubbies)
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
* [AlwaysElementalSandhawk](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Alex/AlwaysElementalSandhawk)
* [Seeker](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Greem/OP%20Shit/Seeker.txt)
* [ToggleSal](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/soze/Experimental/Toggle%20Skills%20(hotfix)/ToggleSal.txt)

### TPS
[Commnity Patch Changelog](https://raw.githubusercontent.com/BLCM/BLCMods/master/Pre%20Sequel%20Mods/Community%20Patch/Full%20Changelog%202.2)
* [Speedier Moon Buggies](https://github.com/BLCM/BLCMods/blob/master/Pre%20Sequel%20Mods/Apocalyptech/Speedier%20Moon%20Buggies/Speedier%20Moon%20Buggies.blcm)
* [Speedier Stingrays](https://github.com/BLCM/BLCMods/blob/master/Pre%20Sequel%20Mods/Apocalyptech/Speedier%20Stingrays/Speedier%20Stingrays.blcm)
* [CarAnywhere](https://github.com/BLCM/BLCMods/blob/master/Pre%20Sequel%20Mods/FromDarkHell/Car%20Changes/CarAnywhere.txt)
* [TPS Rarity Color Fix](https://github.com/BLCM/BLCMods/blob/master/Pre%20Sequel%20Mods/Koby/TPS%20Rarity%20Color%20Fix.txt)
* [BuggyReplace](https://github.com/BLCM/BLCMods/blob/master/Pre%20Sequel%20Mods/Laxlife/BuggyReplace.txt)
* [No Respec Cost](https://github.com/BLCM/BLCMods/blob/master/Pre%20Sequel%20Mods/AngrierPat/Quality%20of%20life%20changes/No%20Respec%20Cost.blcm)
* [Item lvl Fix](https://github.com/BLCM/BLCMods/blob/master/Pre%20Sequel%20Mods/VexilleSerra/Item%20lvl%20Fix.blcm)
* [TPS Container TimeSaver XL](https://github.com/BLCM/BLCMods/blob/master/Pre%20Sequel%20Mods/Apocalyptech/TPS%20Container%20TimeSaver%20XL/TPS%20Container%20TimeSaver%20XL.blcm)
* [Infinite Air Boosts](https://github.com/BLCM/BLCMods/blob/master/Pre%20Sequel%20Mods/Apocalyptech/Infinite%20Air%20Boosts/Infinite%20Air%20Boosts.blcm)
* [TPSUncappedPauseMenuSettings](https://github.com/BLCM/BLCMods/blob/master/Pre%20Sequel%20Mods/OurLordAndSaviorGabeNewell/TPSUncappedPauseMenuSettings.blcm)
* [Weapon View Offset Code](https://github.com/BLCM/BLCMods/blob/master/Pre%20Sequel%20Mods/iNSANE990/Weapon%20View%20Offset%20Code.blcm)
* [Double Quest Rewards](https://github.com/BLCM/BLCMods/blob/master/Pre%20Sequel%20Mods/Astor/Quests%20Improvement/Double%20Quest%20Rewards/Double%20Quest%20Rewards%20v1.0.0.blcm)
* [FastTravelHelper](https://github.com/BLCM/BLCMods/blob/master/Pre%20Sequel%20Mods/apple1417/FastTravelHelper.blcm)
* [TPS Configurable Slot Machines](https://github.com/BLCM/BLCMods/blob/master/Pre%20Sequel%20Mods/Apocalyptech/TPS%20Configurable%20Slot%20Machines/TPS%20Configurable%20Slot%20Machines.blcm)
* [TPS Better Loot Mod](https://github.com/BLCM/BLCMods/blob/master/Pre%20Sequel%20Mods/Apocalyptech/TPS%20Better%20Loot%20Mod/TPS%20Better%20Loot%20Mod.blcm)
* [Moonstone Grind No Longer Costs Moonstone](https://www.nexusmods.com/borderlandspresequel/mods/21)
* [Shorter Fast Travel Waiting Time v1.0.0](https://github.com/BLCM/BLCMods/blob/master/Pre%20Sequel%20Mods/Astor/Quality%20of%20Life/Shorter%20Fast%20Travel%20Waiting%20Time/Shorter%20Fast%20Travel%20Waiting%20Time%20v1.0.0.blcm)
* [No More Reload Messages v1.0.0](https://github.com/BLCM/BLCMods/blob/master/Pre%20Sequel%20Mods/Astor/Quality%20of%20Life/No%20More%20Reload%20Message/No%20More%20Reload%20Messages%20v1.0.0.blcm)
* [No More Fast Travel Animation v1.0.0](https://github.com/BLCM/BLCMods/blob/master/Pre%20Sequel%20Mods/Astor/Quality%20of%20Life/No%20More%20Fast%20Travel%20Animation/No%20More%20Fast%20Travel%20Animation%20v1.0.0.blcm)
* [More Pick-Up Radius v1.0.0](https://github.com/BLCM/BLCMods/blob/master/Pre%20Sequel%20Mods/Astor/Quality%20of%20Life/More%20Pick-Up%20Radius/More%20Pick-Up%20Radius%20v1.0.0.blcm)
* [TPSRespawningLoot](https://github.com/BLCM/BLCMods/blob/master/Pre%20Sequel%20Mods/OurLordAndSaviorGabeNewell/TPSRespawningLoot.blcm)
* [TPSRespawningEnemiesAndAllies](https://github.com/BLCM/BLCMods/blob/master/Pre%20Sequel%20Mods/OurLordAndSaviorGabeNewell/TPSRespawningEnemiesAndAllies.blcm)
* [EXP+](https://github.com/BLCM/BLCMods/blob/master/Pre%20Sequel%20Mods/Jim%20Raven/EXP%2B)
* [RespawnableExcalibastard](https://github.com/BLCM/BLCMods/blob/master/Pre%20Sequel%20Mods/Freya/QUALITY%20OF%20LIFE/RespawnableExcalibastard.blcm)
* [BetterHandlingBuggies](https://github.com/BLCM/BLCMods/blob/master/Pre%20Sequel%20Mods/Freya/QUALITY%20OF%20LIFE/BetterHandlingBuggies.blcm)

