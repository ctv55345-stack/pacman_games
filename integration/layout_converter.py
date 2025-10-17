"""Convert between algorithm txt layout and game board."""

from typing import List, Tuple, Optional
import copy

class LayoutConverter:
    """Convert between txt format and game board format."""
    
    @staticmethod
    def txt_to_game_board(txt_lines: List[str]) -> Tuple[List[List[int]], dict]:
        """
        Convert txt layout → game board format.
        Returns: (board, metadata)
        """
        height = len(txt_lines)
        width = max(len(line) for line in txt_lines)
        
        board = []
        metadata = {
            'pacman_start': None,
            'ghost_starts': [],
            'exit_gate': None
        }
        
        for r, line in enumerate(txt_lines):
            row = []
            for c, char in enumerate(line.ljust(width)):
                pos = (r, c)
                
                if char == '%':  # Wall
                    row.append(3)
                elif char == '.':  # Dot/Food
                    row.append(1)
                elif char == 'O':  # Pie/Power pellet
                    row.append(2)
                elif char == 'P':  # Pacman start
                    row.append(0)
                    metadata['pacman_start'] = pos
                elif char == 'G':  # Ghost start
                    row.append(0)
                    metadata['ghost_starts'].append(pos)
                elif char == 'E':  # Exit gate
                    row.append(0)
                    metadata['exit_gate'] = pos
                else:  # Empty space
                    row.append(0)
            
            board.append(row)
        
        return board, metadata
    
    @staticmethod
    def game_board_to_txt(board: List[List[int]], 
                          pacman_pos: Tuple[int, int],
                          ghost_positions: List[Tuple[int, int]]) -> List[str]:
        """
        Convert game board → txt layout (for algorithm).
        Used to run AI hint in original game.
        """
        lines = []
        height = len(board)
        width = len(board[0]) if height > 0 else 0
        
        for r in range(height):
            row_chars = []
            for c in range(width):
                pos = (r, c)
                cell = board[r][c]
                
                if pos == pacman_pos:
                    row_chars.append('P')
                elif pos in ghost_positions:
                    row_chars.append('G')
                elif cell == 3 or cell == 4 or cell == 5 or cell == 6 or cell == 7 or cell == 8:
                    row_chars.append('%')  # Wall
                elif cell == 1:
                    row_chars.append('.')  # Dot
                elif cell == 2:
                    row_chars.append('O')  # Pie
                else:
                    row_chars.append(' ')  # Empty
            
            lines.append(''.join(row_chars))
        
        # Add exit gate temporarily (bottom right corner)
        if height > 0 and width > 0:
            lines[-1] = lines[-1][:-1] + 'E'
        
        return lines
