"""Main entry point for running the Pacman game."""

import pygame
import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(__file__))

from game.game import Game

def main():
    """Run the Pacman game."""
    try:
        game = Game()
        game.run()
    except Exception as e:
        print(f"Error running game: {e}")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
