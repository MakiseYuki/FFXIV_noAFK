# Configuration for FFXIV NoAFK Script

# Game window title (partial match is used)
GAME_WINDOW_TITLE = "FINAL FANTASY XIV"

# Base interval in seconds (10 minutes = 600 seconds)
BASE_INTERVAL = 600

# Variance range (±) in seconds to randomize the interval
# This makes it appear more human-like
VARIANCE_RANGE = 180  # ±3 minutes (larger variance for more randomness)

# Primary keys to press (will randomize between them)
PRIMARY_ACTIONS = ["space"]  # Jump
SECONDARY_ACTIONS = ["w", "a", "s", "d"]  # Movement keys

# Probability of secondary action instead of primary (0.0 to 1.0)
# 20% chance to move instead of jump
SECONDARY_ACTION_PROBABILITY = 0.2

# Probability of double action (pressing key twice)
# Simulates human behavior like pressing twice when excited
DOUBLE_ACTION_PROBABILITY = 0.15

# Probability of occasional long break (simulates AFK-like behavior but within safe limits)
LONG_BREAK_PROBABILITY = 0.1
LONG_BREAK_DURATION = (1200, 1800)  # 20-30 minutes

# Delay before pressing key after window focus (in seconds)
# Variable to appear more human-like
FOCUS_DELAY_MIN = 0.3
FOCUS_DELAY_MAX = 1.5

# Key press duration variance (in seconds)
KEY_PRESS_MIN = 0.05
KEY_PRESS_MAX = 0.25

# Delay between actions (in seconds)
ACTION_DELAY_MIN = 0.5
ACTION_DELAY_MAX = 3.0

# Mouse movement for realism
ENABLE_MOUSE_MOVEMENT = True
MOUSE_MOVE_PROBABILITY = 0.3  # 30% chance to move mouse slightly

# Logging
LOG_FILE = "noafk.log"
ENABLE_CONSOLE_LOG = True
ENABLE_DETAILED_LOG = True  # Log more details for human-like behavior
