"""Configuration for integrated Pacman game."""

# Game modes
MODE_MANUAL = "manual"
MODE_AI = "ai"
MODE_HYBRID = "hybrid"

# UI Layout
GAME_PANEL_WIDTH = 900
GAME_PANEL_HEIGHT = 950
CONTROL_PANEL_WIDTH = 300
STATS_PANEL_HEIGHT = 200

TOTAL_WIDTH = GAME_PANEL_WIDTH + CONTROL_PANEL_WIDTH
TOTAL_HEIGHT = GAME_PANEL_HEIGHT

# Colors
COLOR_BG = (20, 20, 30)
COLOR_PANEL = (40, 40, 50)
COLOR_TEXT = (255, 255, 255)
COLOR_BUTTON = (60, 60, 80)
COLOR_BUTTON_HOVER = (80, 80, 100)
COLOR_PATH = (0, 255, 0, 128)        # Green semi-transparent
COLOR_EXPLORED = (255, 0, 0, 50)     # Red semi-transparent
COLOR_FRONTIER = (0, 0, 255, 50)     # Blue semi-transparent
COLOR_HINT = (255, 255, 0)           # Yellow

# AI Settings
AI_SPEED_MIN = 1
AI_SPEED_MAX = 60
AI_SPEED_DEFAULT = 10

# Algorithm settings
HEURISTICS = [
    ("Auto", "auto"),
    ("PieAware", "pie"),
    ("FoodMST", "mst"),
    ("ExactDistance", "exact-dist"),
    ("ExactMST ⭐", "exact-mst"),
    ("Combined", "combo")
]

LAYOUTS = [
    ("Classic (Game)", None),
    ("Small Basic", "layouts/small_basic.txt"),
    ("Medium Twists", "layouts/medium_twists.txt"),
    ("Large Multi-Pie", "layouts/large_multi_pie.txt"),
    ("Maze", "layouts/maze.txt")
]

# FPS
FPS = 60
