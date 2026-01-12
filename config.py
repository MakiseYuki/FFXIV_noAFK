# Configuration for FFXIV NoAFK Script

# Game window title (partial match is used)
GAME_WINDOW_TITLE = "FINAL FANTASY XIV"

# Base interval in seconds (10 minutes = 600 seconds)
BASE_INTERVAL = 600

# Variance range (±) in seconds to randomize the interval
# This makes it appear more human-like
VARIANCE_RANGE = 120  # ±2 minutes

# Key to press for jump action
JUMP_KEY = "space"

# Delay before pressing key after window focus (in seconds)
# This adds a small human-like delay
FOCUS_DELAY = 0.5

# Logging
LOG_FILE = "noafk.log"
ENABLE_CONSOLE_LOG = True
