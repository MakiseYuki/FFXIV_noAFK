#!/usr/bin/env python3
"""
FFXIV NoAFK - Prevents character from going AFK in Final Fantasy XIV
Simulates periodic jump actions to maintain active status
"""

import time
import random
import logging
from datetime import datetime
import sys
import os

# Try importing required libraries
try:
    import pyautogui
    import pynput
    from pynput.keyboard import Controller
    import win32gui
    import win32con
except ImportError as e:
    print(f"Error: Required library not found. Please run: pip install -r requirements.txt")
    print(f"Missing: {e}")
    sys.exit(1)

# Import configuration
from config import (
    GAME_WINDOW_TITLE, BASE_INTERVAL, VARIANCE_RANGE,
    JUMP_KEY, FOCUS_DELAY, LOG_FILE, ENABLE_CONSOLE_LOG
)

# Setup logging
def setup_logging():
    """Configure logging to file and console"""
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    
    # Create logger
    logger = logging.getLogger('FFXIVNoAFK')
    logger.setLevel(logging.INFO)
    
    # File handler
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(log_format))
    logger.addHandler(file_handler)
    
    # Console handler
    if ENABLE_CONSOLE_LOG:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter(log_format))
        logger.addHandler(console_handler)
    
    return logger

logger = setup_logging()

def find_game_window():
    """
    Find the FFXIV game window
    Returns window handle or None if not found
    """
    def enum_handler(hwnd, ctx):
        if GAME_WINDOW_TITLE.lower() in win32gui.GetWindowText(hwnd).lower():
            ctx.append(hwnd)
    
    windows = []
    win32gui.EnumWindows(enum_handler, windows)
    
    return windows[0] if windows else None

def focus_game_window(hwnd):
    """
    Bring the game window to focus
    Attempts to restore if minimized
    """
    try:
        # Check if window is minimized
        if win32gui.IsIconic(hwnd):
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        
        # Set foreground window
        win32gui.SetForegroundWindow(hwnd)
        
        # Add a small delay to ensure focus is set
        time.sleep(0.5)
        return True
    except Exception as e:
        logger.error(f"Error focusing window: {e}")
        return False

def simulate_jump():
    """
    Simulate a jump action by pressing space key
    Uses pynput for more discrete input
    """
    try:
        keyboard = Controller()
        
        # Add slight delay before pressing (more human-like)
        time.sleep(random.uniform(0.1, 0.3))
        
        # Press space key
        keyboard.press(' ')
        
        # Brief hold (human-like key press duration)
        time.sleep(random.uniform(0.05, 0.15))
        
        # Release key
        keyboard.release(' ')
        
        logger.info("Jump action executed successfully")
        return True
    except Exception as e:
        logger.error(f"Error executing jump action: {e}")
        return False

def get_next_interval():
    """
    Calculate next interval with random variance
    Makes timing appear more human-like
    """
    variance = random.uniform(-VARIANCE_RANGE, VARIANCE_RANGE)
    next_interval = BASE_INTERVAL + variance
    return max(next_interval, 60)  # Minimum 60 seconds

def main():
    """
    Main loop for the NoAFK script
    """
    logger.info("=" * 60)
    logger.info("FFXIV NoAFK Script Started")
    logger.info(f"Game Window: {GAME_WINDOW_TITLE}")
    logger.info(f"Base Interval: {BASE_INTERVAL}s ({BASE_INTERVAL/60:.1f} minutes)")
    logger.info(f"Variance: ±{VARIANCE_RANGE}s (±{VARIANCE_RANGE/60:.1f} minutes)")
    logger.info("=" * 60)
    
    action_count = 0
    
    try:
        while True:
            # Find game window
            game_hwnd = find_game_window()
            
            if game_hwnd is None:
                logger.warning(f"Game window '{GAME_WINDOW_TITLE}' not found. Retrying...")
                time.sleep(5)  # Wait before retrying
                continue
            
            # Calculate next action interval
            next_interval = get_next_interval()
            logger.info(f"Next jump in {next_interval:.1f}s ({next_interval/60:.2f} minutes)")
            
            # Wait for the calculated interval
            time.sleep(next_interval)
            
            # Focus game window
            if not focus_game_window(game_hwnd):
                logger.warning("Failed to focus game window")
                continue
            
            # Wait a bit after focusing (more human-like)
            time.sleep(FOCUS_DELAY)
            
            # Execute jump action
            if simulate_jump():
                action_count += 1
                logger.info(f"Actions executed: {action_count}")
            
            # Small random delay before next iteration (appears more natural)
            time.sleep(random.uniform(0.5, 1.5))
    
    except KeyboardInterrupt:
        logger.info("Script interrupted by user")
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
    finally:
        logger.info("FFXIV NoAFK Script Stopped")
        logger.info(f"Total actions executed: {action_count}")

if __name__ == "__main__":
    main()
