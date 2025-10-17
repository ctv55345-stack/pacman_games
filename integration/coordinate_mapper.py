"""Map coordinates between algorithm and game."""

from typing import Tuple, Optional

class CoordinateMapper:
    """Convert between algorithm (row, col) and game (x, y) coordinates."""
    
    def __init__(self, game_width=900, game_height=900, grid_rows=33, grid_cols=30):
        self.game_width = game_width
        self.game_height = game_height
        self.grid_rows = grid_rows
        self.grid_cols = grid_cols
        
        self.cell_width = game_width / grid_cols
        self.cell_height = game_height / grid_rows
    
    def algo_to_game(self, row: int, col: int) -> Tuple[int, int]:
        """Convert (row, col) → (x, y) pixel."""
        x = int(col * self.cell_width + self.cell_width / 2)
        y = int(row * self.cell_height + self.cell_height / 2)
        return x, y
    
    def game_to_algo(self, x: int, y: int) -> Tuple[int, int]:
        """Convert (x, y) pixel → (row, col)."""
        col = int(x / self.cell_width)
        row = int(y / self.cell_height)
        return row, col
    
    def action_to_delta(self, action: str) -> Tuple[int, int]:
        """Convert action name to (dx, dy)."""
        deltas = {
            "Up": (0, -1),
            "Down": (0, 1),
            "Left": (-1, 0),
            "Right": (1, 0),
            "Stay": (0, 0),
            "Stop": (0, 0)
        }
        return deltas.get(action, (0, 0))
