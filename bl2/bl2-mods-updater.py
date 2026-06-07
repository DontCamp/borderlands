"""
Borderlands 2 Mod Updater
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
from pathlib import Path

# ── Configuration ─────────────────────────────────────────────────────────────
UPDATER_VERSION  = "0.0.1"
STEAM_APP_ID     = "49520"
GAME_FOLDER_NAME = "Borderlands 2"
VERSION_URL      = "https://github.com/dontcamp/borderlands/releases/latest/download/bl2-mods-dontcamp-version.txt"
MOD_ZIP_URL      = "https://github.com/dontcamp/borderlands/releases/latest/download/bl2-mods.zip"
VERSION_MARKER   = "bl2-mods-dontcamp-version.txt"
SDK_MODS_DIR     = "sdk_mods"
SETTINGS_DIR     = "sdk_mods/settings"
# ──────────────────────────────────────────────────────────────────────────────

DIVIDER = "─" * 52


def banner():
    print()
    print("  ╔══════════════════════════════════════════════════╗")
    print("  ║    DONTCAMP.COM BORDERLANDS 2  ·  MOD UPDATER    ║")
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

def fetch_remote_version() -> str | None:
    try:
        with urllib.request.urlopen(VERSION_URL, timeout=10) as r:
            return r.read().decode().strip()
    except Exception:
        return None


def read_local_version(game_dir: Path) -> str | None:
    marker = game_dir / VERSION_MARKER
    return marker.read_text(encoding="utf-8").strip() if marker.exists() else None


def save_local_version(game_dir: Path, ver: str):
    (game_dir / VERSION_MARKER).write_text(ver, encoding="utf-8")


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

def clear_sdk_mods(game_path: Path):
    """
    Delete everything inside sdk_mods/ except the settings subfolder.
    If settings/ doesn't exist this is a full wipe of sdk_mods/.
    """
    sdk_dir = game_path / SDK_MODS_DIR
    if not sdk_dir.exists():
        return

    settings_dir = (game_path / SETTINGS_DIR).resolve()
    preserve_settings = settings_dir.exists()

    for item in sdk_dir.iterdir():
        if preserve_settings and item.resolve() == settings_dir:
            continue  # leave settings folder alone
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()


def extract_zip(zip_path: Path, game_path: Path, first_install: bool):
    """
    Extract zip to game_path.
    On updates, skip any entries that land inside sdk_mods/settings/.
    """
    with zipfile.ZipFile(zip_path, "r") as zf:
        for entry in zf.infolist():
            # Normalise to forward slashes for comparison
            entry_path = entry.filename.replace("\\", "/")

            if not first_install and entry_path.startswith(SETTINGS_DIR):
                continue  # preserve user settings on updates

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
    import json
    config_path = game_path / SETTINGS_DIR / "text_mod_loader.json"
    if not config_path.exists():
        return

    correct_patch = str(game_path / "Binaries" / "patch.txt")

    config = json.loads(config_path.read_text(encoding="utf-8"))
    options = config.get("options", {})

    # Fix auto_enable list
    options["auto_enable"] = [
        correct_patch if Path(p).name == "patch.txt" else p
        for p in options.get("auto_enable", [])
    ]

    # Fix mod_info keys and any path values inside each entry
    old_mod_info = options.get("mod_info", {})
    new_mod_info = {}
    for key, val in old_mod_info.items():
        new_key = correct_patch if Path(key).name == "patch.txt" else key
        new_mod_info[new_key] = val
    options["mod_info"] = new_mod_info

    config_path.write_text(json.dumps(config, indent=4), encoding="utf-8")


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
    remote_ver = fetch_remote_version()
    if not remote_ver:
        err("Could not reach update server. Check your connection.")
        input("\n  Press Enter to exit.")
        sys.exit(1)

    local_ver = read_local_version(game_path)
    first_install = local_ver is None
    info(f"Installed : {local_ver or 'none'}")
    info(f"Latest    : {remote_ver}")
    rule()

    if local_ver == remote_ver:
        ok(f"Mods are already up to date (v{remote_ver})")
        auto_close(2)
        return

    # 3. Download to a temp file
    info(f"Downloading mods v{remote_ver}...")
    try:
        with tempfile.NamedTemporaryFile(suffix=".zip", delete=False) as tmp:
            tmp_path = Path(tmp.name)
        download(MOD_ZIP_URL, tmp_path)
    except urllib.error.URLError as e:
        err(f"Download failed: {e.reason}")
        input("\n  Press Enter to exit.")
        sys.exit(1)

    # 4. Clear sdk_mods/ (preserving settings/ on updates)
    if first_install:
        info("Installing mods...")
    else:
        info("Removing old mod files (preserving settings)...")
        clear_sdk_mods(game_path)

    # 5. Extract zip, skipping sdk_mods/settings/ on updates
    info("Extracting...")
    extract_zip(tmp_path, game_path, first_install)
    tmp_path.unlink(missing_ok=True)

    # 6. Fix text_mod_loader config paths on first install
    if first_install:
        info("Configuring text mod loader...")
        fix_text_mod_loader_config(game_path)

    # 7. Write version marker
    save_local_version(game_path, remote_ver)

    rule()
    ok(f"Mods {'installed' if first_install else 'updated'} to v{remote_ver} successfully!")
    if not first_install:
        info("User settings were preserved.")
    input("\n  Press Enter to exit. ")


if __name__ == "__main__":
    main()