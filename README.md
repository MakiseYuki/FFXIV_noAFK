# FFXIV NoAFK - Anti-AFK Script

A simple Python script that prevents your FFXIV character from going AFK by simulating periodic jump actions.

## Features

- ✅ Automatically detects the FFXIV game window
- ✅ Simulates jump actions at randomized intervals (~10 minutes)
- ✅ Random variance in timing to appear more human-like
- ✅ Detailed logging of all actions
- ✅ Easy to configure via `config.py`
- ✅ Works on Windows 10/11

## Installation

### Prerequisites
- Python 3.7 or higher
- Windows 10 or 11
- FFXIV game client

### Setup

1. Clone or download this repository
2. Install required dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage
```powershell
python ffxiv_noafk.py
```

### Quick Launch (Windows)
Double-click `run.bat` to start the script

## Configuration

Edit `config.py` to customize behavior:

```python
BASE_INTERVAL = 600          # Base interval in seconds (10 minutes)
VARIANCE_RANGE = 120         # Random variance ±2 minutes
JUMP_KEY = "space"           # Key to press for jump
GAME_WINDOW_TITLE = "FINAL FANTASY XIV"  # Game window title
```

## How It Works

1. **Detects Game Window**: Searches for the FFXIV window
2. **Calculates Random Interval**: Waits 10 minutes ±2 minutes
3. **Focuses Window**: Brings game window to front
4. **Simulates Jump**: Sends space key press (default jump action)
5. **Repeats**: Continues indefinitely

## Anti-Detection Features

- **Random Timing**: ±2 minutes variance around 10-minute base
- **Human-like Delays**: Slight pauses before/after key press
- **Discrete Input**: Uses direct keyboard input to appear more natural
- **Logging Only**: No screen manipulation or suspicious memory access

## Logs

The script logs all actions to `noafk.log`. Check this file to verify the script is working:
```
2026-01-12 15:30:45 - INFO - Jump action executed successfully
2026-01-12 15:40:52 - INFO - Actions executed: 1
```

## Stopping the Script

Press `Ctrl+C` in the terminal/command prompt to stop the script gracefully.

## Important Notes

- **Game Must Be Running**: Launch FFXIV before starting this script
- **Window Focus**: The script will occasionally bring the window to focus
- **Use Responsibly**: This is for your own character only - don't use on others' accounts
- **Check Game Terms**: Verify this complies with FFXIV Terms of Service

## Troubleshooting

### "Game window not found"
- Make sure FFXIV is running and the window is visible
- Check that `GAME_WINDOW_TITLE` in config.py matches your game window title

### "pyautogui/pynput not found"
- Run: `pip install -r requirements.txt`

### Script not executing jumps
- Check `noafk.log` for error messages
- Ensure the FFXIV window is in focus when script runs

## License

This project is provided as-is for personal use.
