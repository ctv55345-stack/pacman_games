"""AI module - Algorithm and heuristics for Pacman AI."""

from .environment import PacmanEnvironment, PacmanProblem
from .heuristics import *
from .auto import run_auto_mode

__all__ = ['PacmanEnvironment', 'PacmanProblem', 'run_auto_mode']
