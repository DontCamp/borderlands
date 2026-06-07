# Build script for BL2 Mod Updater
# Creates a venv, installs PyInstaller, and builds the exe.
# to make a zip:  zip -r bl2-mods.zip Binaries sdk_mods -x "*.DS_Store"

$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "  Setting up virtual environment..." -ForegroundColor Cyan
python -m venv .venv

Write-Host "  Activating venv..." -ForegroundColor Cyan
& .\.venv\Scripts\Activate.ps1

Write-Host "  Installing PyInstaller..." -ForegroundColor Cyan
pip install pyinstaller --quiet

Write-Host "  Building exe..." -ForegroundColor Cyan
pyinstaller --onefile --name "bl2-mods-updater" bl2-mods-updater.py

Write-Host ""
Write-Host "  Done! Exe is at dist\file.exe" -ForegroundColor Green
Write-Host ""