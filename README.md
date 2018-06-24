# Patches!
Community Patch ([changelog](https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Shadowevil/Full%20UCP%20Changelog.txt)) and Mods Collection for the DontCamp.com community

All credits to the [original authors](https://github.com/BLCM/BLCMods).  This repository serves as a way for DontCamp.com community members to more easily stay up to date with our latest patch set distribution.

## Configuration

1. Save [BorderlandsPatcher.exe](https://github.com/bugworm/BorderlandsPatcher/releases/) to any directory you wish.

2. Run the program. It will auto-detect your Steam-provided binary for Borderlands 2 (BL2) and Borderlands The Pre-Sequel (TPS).

3. In the program, select the appropriate game (BL2|TPS) via the first drop-down menu. Then, select **Patch (BL2|TPS).exe** and wait for the action to complete.

4. Select **Add Console Hotkey**. Do not select **Download Patch**, since the DontCamp.com patch is customized beyond the defaults. You may now close **BorderlandsPatcher.exe**

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
