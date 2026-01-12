#!/usr/bin/env python3
"""
FFXIV NoAFK - Prevents character from going AFK in Final Fantasy XIV
Simulates realistic human-like actions to maintain active status
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
    from pynput.mouse import Controller as MouseController
    import win32gui
    import win32con
except ImportError as e:
    print(f"Error: Required library not found. Please run: pip install -r requirements.txt")
    print(f"Missing: {e}")
    sys.exit(1)

# Import configuration
from config import (
    GAME_WINDOW_TITLE, BASE_INTERVAL, VARIANCE_RANGE,
    PRIMARY_ACTIONS, SECONDARY_ACTIONS, SECONDARY_ACTION_PROBABILITY,
    DOUBLE_ACTION_PROBABILITY, LONG_BREAK_PROBABILITY, LONG_BREAK_DURATION,
    FOCUS_DELAY_MIN, FOCUS_DELAY_MAX, KEY_PRESS_MIN, KEY_PRESS_MAX,
    ACTION_DELAY_MIN, ACTION_DELAY_MAX, ENABLE_MOUSE_MOVEMENT,
    MOUSE_MOVE_PROBABILITY, LOG_FILE, ENABLE_CONSOLE_LOG, ENABLE_DETAILED_LOG
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

def perform_mouse_movement():
    """
    Perform subtle mouse movement to appear more human-like
    Moves mouse slightly within game window bounds
    """
    try:
        if not ENABLE_MOUSE_MOVEMENT or random.random() > MOUSE_MOVE_PROBABILITY:
            return
        
        mouse = MouseController()
        current_x, current_y = mouse.position
        
        # Move mouse by small amount (5-20 pixels)
        offset_x = random.randint(-20, 20)
        offset_y = random.randint(-20, 20)
        
        new_x = max(0, current_x + offset_x)
        new_y = max(0, current_y + offset_y)
        
        # Smooth movement over 0.2-0.5 seconds
        duration = random.uniform(0.2, 0.5)
        steps = 5
        step_time = duration / steps
        
        for i in range(steps):
            current_x_temp = current_x + (new_x - current_x) * (i / steps)
            current_y_temp = current_y + (new_y - current_y) * (i / steps)
            mouse.position = (current_x_temp, current_y_temp)
            time.sleep(step_time)
        
        if ENABLE_DETAILED_LOG:
            logger.debug(f"Mouse moved: ({current_x}, {current_y}) -> ({new_x}, {new_y})")
    
    except Exception as e:
        logger.debug(f"Mouse movement error (non-critical): {e}")

def simulate_action():
    """
    Simulate a human-like action
    Can be primary action (jump), secondary action (movement), or double action
    """
    try:
        keyboard = Controller()
        
        # Decide which type of action to perform
        if random.random() < SECONDARY_ACTION_PROBABILITY:
            # Perform secondary action (movement)
            action = random.choice(SECONDARY_ACTIONS)
            action_type = "movement"
        else:
            # Perform primary action (jump)
            action = random.choice(PRIMARY_ACTIONS)
            action_type = "jump"
        
        # Determine if double action
        is_double_action = random.random() < DOUBLE_ACTION_PROBABILITY
        
        # Perform mouse movement occasionally
        perform_mouse_movement()
        
        # Add delay before action
        time.sleep(random.uniform(0.1, 0.3))
        
        # Press key
        keyboard.press(action)
        
        # Variable key hold duration (more human-like)
        hold_time = random.uniform(KEY_PRESS_MIN, KEY_PRESS_MAX)
        time.sleep(hold_time)
        
        # Release key
        keyboard.release(action)
        
        action_log = f"{action_type.upper()} - Key: {action}"
        
        # Double action
        if is_double_action:
            time.sleep(random.uniform(0.1, 0.3))
            keyboard.press(action)
            time.sleep(random.uniform(KEY_PRESS_MIN, KEY_PRESS_MAX))
            keyboard.release(action)
            action_log += " (DOUBLE)"
        
        logger.info(f"Action executed: {action_log}")
        
        # Delay after action
        time.sleep(random.uniform(ACTION_DELAY_MIN, ACTION_DELAY_MAX))
        
        return True
    
    except Exception as e:
        logger.error(f"Error executing action: {e}")
        return False

def get_next_interval():
    """
    Calculate next interval with random variance
    Makes timing appear more human-like and unpredictable
    """
    # Check for occasional long break (simulates human AFK-like behavior)
    if random.random() < LONG_BREAK_PROBABILITY:
        long_break = random.uniform(LONG_BREAK_DURATION[0], LONG_BREAK_DURATION[1])
        logger.info(f"Long break scheduled: {long_break/60:.1f} minutes (human-like behavior)")
        return long_break
    
    # Normal variance
    variance = random.uniform(-VARIANCE_RANGE, VARIANCE_RANGE)
    next_interval = BASE_INTERVAL + variance
    
    return max(next_interval, 60)  # Minimum 60 seconds

def main():
    """
    Main loop for the NoAFK script
    """
    logger.info("=" * 70)
    logger.info("FFXIV NoAFK Script Started - Enhanced Human-like Behavior")
    logger.info(f"Game Window: {GAME_WINDOW_TITLE}")
    logger.info(f"Base Interval: {BASE_INTERVAL}s ({BASE_INTERVAL/60:.1f} minutes)")
    logger.info(f"Variance: ±{VARIANCE_RANGE}s (±{VARIANCE_RANGE/60:.1f} minutes)")
    logger.info(f"Double Action Chance: {DOUBLE_ACTION_PROBABILITY*100:.0f}%")
    logger.info(f"Secondary Action Chance: {SECONDARY_ACTION_PROBABILITY*100:.0f}%")
    logger.info(f"Long Break Chance: {LONG_BREAK_PROBABILITY*100:.0f}%")
    logger.info("=" * 70)
    
    action_count = 0
    session_start = datetime.now()
    
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
            minutes = next_interval / 60
            logger.info(f"Next action in {next_interval:.1f}s ({minutes:.2f} minutes)")
            
            # Wait for the calculated interval
            time.sleep(next_interval)
            
            # Focus game window
            if not focus_game_window(game_hwnd):
                logger.warning("Failed to focus game window")
                continue
            
            # Wait a bit after focusing (human-like)
            time.sleep(random.uniform(FOCUS_DELAY_MIN, FOCUS_DELAY_MAX))
            
            # Execute action(s)
            if simulate_action():
                action_count += 1
                elapsed = datetime.now() - session_start
                logger.info(f"Total actions: {action_count} | Session time: {elapsed}")
    
    except KeyboardInterrupt:
        logger.info("Script interrupted by user")
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
    finally:
        elapsed = datetime.now() - session_start
        logger.info("=" * 70)
        logger.info("FFXIV NoAFK Script Stopped")
        logger.info(f"Total actions executed: {action_count}")
        logger.info(f"Total session time: {elapsed}")
        logger.info("=" * 70)

if __name__ == "__main__":
    main()
