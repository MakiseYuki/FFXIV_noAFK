@echo off
REM FFXIV NoAFK Script Launcher
REM This batch file automatically installs dependencies and runs the script

echo.
echo ===== FFXIV NoAFK Script =====
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://www.python.org/
    pause
    exit /b 1
)

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Starting FFXIV NoAFK Script...
echo Press Ctrl+C to stop the script
echo.

python ffxiv_noafk.py

pause
