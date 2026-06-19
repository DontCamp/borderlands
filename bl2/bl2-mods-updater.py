"""
Borderlands 2 Mod Updater
Console-based auto-updater. Zero external dependencies, no persistent storage.
"""

import os
import sys
import shutil
import zipfile
import winreg
import urllib.request
import urllib.error
import tempfile
import time
import re
import json
from pathlib import Path

# ── Configuration ─────────────────────────────────────────────────────────────
STEAM_APP_ID     = "49520"
GAME_FOLDER_NAME = "Borderlands 2"
VERSION_URL      = "https://github.com/dontcamp/borderlands/releases/latest/download/bl2-mods-dontcamp-version.txt"
MOD_ZIP_URL      = "https://github.com/dontcamp/borderlands/releases/latest/download/bl2-mods.zip"
VERSION_MARKER   = "bl2-mods-dontcamp-version.txt"
UPDATER_VERSION  = "1.1.0"
SDK_MODS_DIR     = "sdk_mods"
SETTINGS_DIR     = "sdk_mods/settings"
# ──────────────────────────────────────────────────────────────────────────────

DIVIDER = "─" * 52



def banner():
    print()
    print("  ╔══════════════════════════════════════════════════╗")
    print("  ║    donntcamp.com BORDERLANDS 2 · MOD UPDATER     ║")
    print("  ╚══════════════════════════════════════════════════╝")
    print(f"  version {UPDATER_VERSION}")
    print()


def info(msg): print(f"  {msg}")
def ok(msg):   print(f"  ✔  {msg}")
def err(msg):  print(f"  ✖  {msg}")
def rule():    print(f"  {DIVIDER}")


def auto_close(seconds: int = 2):
    """Count down and exit without waiting for input."""
    for i in range(seconds, 0, -1):
        print(f"\r  Closing in {i}s... ", end="", flush=True)
        time.sleep(1)
    print()


# ── Progress bar (built-in) ────────────────────────────────────────────────────

def print_progress(downloaded: int, total: int):
    width = 36
    if total:
        filled = int(width * downloaded / total)
        bar = "█" * filled + "░" * (width - filled)
        pct = downloaded / total * 100
        mb_done = downloaded / 1_048_576
        mb_total = total / 1_048_576
        print(f"\r  [{bar}] {pct:5.1f}%  {mb_done:.1f}/{mb_total:.1f} MB", end="", flush=True)
    else:
        mb = downloaded / 1_048_576
        print(f"\r  Downloading... {mb:.1f} MB", end="", flush=True)


# ── Steam detection ────────────────────────────────────────────────────────────

def get_steam_path() -> Path | None:
    for key_path in [r"SOFTWARE\WOW6432Node\Valve\Steam", r"SOFTWARE\Valve\Steam"]:
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as k:
                val, _ = winreg.QueryValueEx(k, "InstallPath")
                return Path(val)
        except OSError:
            continue
    return None


def get_library_folders(steam_path: Path) -> list[Path]:
    libraries = [steam_path]
    vdf = steam_path / "steamapps" / "libraryfolders.vdf"
    if vdf.exists():
        for match in re.finditer(r'"path"\s+"([^"]+)"', vdf.read_text(encoding="utf-8")):
            p = Path(match.group(1))
            if p.exists() and p not in libraries:
                libraries.append(p)
    return libraries


def find_game() -> Path | None:
    steam_path = get_steam_path()
    if not steam_path:
        return None
    for lib in get_library_folders(steam_path):
        manifest = lib / "steamapps" / f"appmanifest_{STEAM_APP_ID}.acf"
        game_dir = lib / "steamapps" / "common" / GAME_FOLDER_NAME
        if manifest.exists() and game_dir.exists():
            return game_dir
    return None


# ── Version helpers ────────────────────────────────────────────────────────────

def fetch_remote_versions() -> dict | None:
    """Fetch version.json from server. Returns dict with mod_version and settings_version."""
    try:
        with urllib.request.urlopen(VERSION_URL, timeout=10) as r:
            return json.loads(r.read().decode())
    except Exception:
        return None


def read_local_versions(game_dir: Path) -> dict:
    """
    Read local marker file. Returns dict with mod_version and settings_version.
    Handles legacy plain-text version files by treating them as old mod_version
    with no settings_version, which will trigger a settings wipe prompt.
    """
    marker = game_dir / VERSION_MARKER
    if marker.exists():
        content = marker.read_text(encoding="utf-8").strip()
        try:
            data = json.loads(content)
            if isinstance(data, dict):
                return {
                    "mod_version": data.get("mod_version"),
                    "settings_version": data.get("settings_version"),
                }
            # Legacy format: json parsed but was a bare number e.g. 1
            return {"mod_version": str(data), "settings_version": None}
        except json.JSONDecodeError:
            # Legacy plain-text format — treat as old mod version, no settings version
            return {"mod_version": content, "settings_version": None}
    return {"mod_version": None, "settings_version": None}


def save_local_versions(game_dir: Path, mod_ver: str, settings_ver: str):
    (game_dir / VERSION_MARKER).write_text(
        json.dumps({"mod_version": mod_ver, "settings_version": settings_ver}, indent=4),
        encoding="utf-8"
    )


# ── Download ───────────────────────────────────────────────────────────────────

def download(url: str, dest: Path):
    with urllib.request.urlopen(url, timeout=30) as resp:
        total = int(resp.headers.get("Content-Length", 0))
        downloaded = 0
        with open(dest, "wb") as f:
            while chunk := resp.read(65536):
                f.write(chunk)
                downloaded += len(chunk)
                print_progress(downloaded, total)
    print()  # newline after progress bar


# ── Mod install helpers ────────────────────────────────────────────────────────

def clear_sdk_mods(game_path: Path, wipe_settings: bool = False):
    """
    Delete everything inside sdk_mods/ except the settings subfolder
    (unless wipe_settings is True).
    Requires __main__.py to exist in sdk_mods/ as a safety check.
    """
    sdk_dir = game_path / SDK_MODS_DIR
    if not sdk_dir.exists():
        return

    if not (sdk_dir / "__main__.py").exists():
        err("Safety check failed: __main__.py not found in sdk_mods/.")
        err("Refusing to delete — this may not be a valid mods directory.")
        input("\n  Press Enter to exit.")
        sys.exit(1)

    settings_dir = (game_path / SETTINGS_DIR).resolve()
    preserve_settings = settings_dir.exists() and not wipe_settings

    for item in sdk_dir.iterdir():
        if preserve_settings and item.resolve() == settings_dir:
            continue
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()


def clear_settings(game_path: Path):
    """
    Delete everything inside sdk_mods/settings/.
    Requires python-sdk.json to exist as a safety check.
    Called only when wipe_settings is True.
    """
    settings_dir = game_path / SETTINGS_DIR
    if not settings_dir.exists():
        return

    if not (settings_dir / "python-sdk.json").exists():
        err("Safety check failed: python-sdk.json not found in sdk_mods/settings/.")
        err("Refusing to delete — this may not be a valid settings directory.")
        input("\n  Press Enter to exit.")
        sys.exit(1)

    shutil.rmtree(settings_dir)
    settings_dir.mkdir()


def extract_zip(zip_path: Path, game_path: Path, first_install: bool, wipe_settings: bool = False):
    """
    Extract zip to game_path.
    On updates, skip entries inside sdk_mods/settings/ unless wipe_settings is True.
    """
    with zipfile.ZipFile(zip_path, "r") as zf:
        for entry in zf.infolist():
            entry_path = entry.filename.replace("\\", "/")

            if not first_install and not wipe_settings and entry_path.startswith(SETTINGS_DIR):
                continue

            target = game_path / entry.filename
            if entry.is_dir():
                target.mkdir(parents=True, exist_ok=True)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                with zf.open(entry) as src, open(target, "wb") as dst:
                    shutil.copyfileobj(src, dst)


def fix_text_mod_loader_config(game_path: Path):
    """
    After extraction, patch text_mod_loader.json in place by replacing
    any path values pointing to patch.txt with the correct local path.
    Only the path strings are changed; all other content is preserved.
    """
    config_path = game_path / SETTINGS_DIR / "text_mod_loader.json"
    if not config_path.exists():
        return

    correct_patch = str(game_path / "Binaries" / "patch.txt")
    config = json.loads(config_path.read_text(encoding="utf-8"))
    options = config.get("options", {})

    options["auto_enable"] = [
        correct_patch if Path(p).name == "patch.txt" else p
        for p in options.get("auto_enable", [])
    ]

    old_mod_info = options.get("mod_info", {})
    new_mod_info = {}
    for key, val in old_mod_info.items():
        new_key = correct_patch if Path(key).name == "patch.txt" else key
        new_mod_info[new_key] = val
    options["mod_info"] = new_mod_info

    config_path.write_text(json.dumps(config, indent=4), encoding="utf-8")


def prompt_wipe_settings() -> bool:
    """
    Ask the user whether to wipe settings.
    Returns True if confirmed, False otherwise.
    """
    print()
    print("  ⚠  A new settings version is available.")
    print("  There is a new co-op mod settings configuration.")
    print("  You will need to re-configure your keybinds and")
    print("  mod settings after this update.")
    answer = input("  Wipe settings? (y/N): ").strip().lower()
    return answer == "y"


def launch_game():
    """Launch Borderlands 2 via Steam protocol URL."""
    info("Launching Borderlands 2...")
    os.startfile(f"steam://rungameid/{STEAM_APP_ID}")


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    banner()

    # 1. Find game
    info("Locating Borderlands 2...")
    game_path = find_game()
    if not game_path:
        err("Could not find Borderlands 2 via Steam.")
        err("Make sure the game is installed, then re-run.")
        input("\n  Press Enter to exit.")
        sys.exit(1)
    ok(f"Found: {game_path}")
    rule()

    # 2. Check versions
    info("Checking for updates...")
    remote = fetch_remote_versions()
    if not remote:
        err("Could not reach update server. Check your connection.")
        input("\n  Press Enter to exit.")
        sys.exit(1)

    remote_mod_ver      = remote.get("mod_version")
    remote_settings_ver = remote.get("settings_version")

    local               = read_local_versions(game_path)
    local_mod_ver       = local.get("mod_version")
    local_settings_ver  = local.get("settings_version")

    first_install       = local_mod_ver is None

    info(f"Mods      — installed: {local_mod_ver or 'none':>6}   latest: {remote_mod_ver}")
    info(f"Settings  — installed: {local_settings_ver or 'none':>6}   latest: {remote_settings_ver}")
    rule()

    # 3. Determine if settings wipe is needed and prompt user
    settings_outdated = local_settings_ver != remote_settings_ver
    wipe_settings = False
    settings_exist = (game_path / SETTINGS_DIR).exists()
    if not first_install and settings_outdated and settings_exist:
        wipe_settings = prompt_wipe_settings()
        if wipe_settings:
            ok("Settings will be wiped.")
        else:
            info("Keeping existing settings.")
        rule()

    # 4. If mods are up to date, launch and exit
    if local_mod_ver == remote_mod_ver and not wipe_settings:
        ok("Mods are already up to date.")
        launch_game()
        return

    # 5. Download zip
    info(f"Downloading mods v{remote_mod_ver}...")
    try:
        with tempfile.NamedTemporaryFile(suffix=".zip", delete=False) as tmp:
            tmp_path = Path(tmp.name)
        download(MOD_ZIP_URL, tmp_path)
    except urllib.error.URLError as e:
        err(f"Download failed: {e.reason}")
        input("\n  Press Enter to exit.")
        sys.exit(1)

    # 6. Clear sdk_mods/
    if first_install:
        info("Installing mods...")
    else:
        info("Removing old mod files" + (" and settings..." if wipe_settings else " (preserving settings)..."))
        if wipe_settings:
            clear_settings(game_path)
        clear_sdk_mods(game_path, wipe_settings=False)

    # 7. Extract
    info("Extracting...")
    extract_zip(tmp_path, game_path, first_install, wipe_settings)
    tmp_path.unlink(missing_ok=True)

    # 8. Fix text_mod_loader config on first install or settings wipe
    if first_install or wipe_settings:
        info("Configuring text mod loader...")
        fix_text_mod_loader_config(game_path)

    # 9. Save version marker
    # If user declined the wipe, keep their local settings version unchanged
    saved_settings_ver = remote_settings_ver if (first_install or wipe_settings) else local_settings_ver
    save_local_versions(game_path, remote_mod_ver, saved_settings_ver)

    rule()
    ok(f"Mods {'installed' if first_install else 'updated'} to v{remote_mod_ver} successfully!")
    if wipe_settings:
        info("Settings updated to v{}.".format(remote_settings_ver))
    elif not first_install:
        info("User settings were preserved.")
    auto_close(2)
    launch_game()


if __name__ == "__main__":
    main()
