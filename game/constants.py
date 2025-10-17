import pygame
import math

pygame.init()

WIDTH = 900
HEIGHT = 950
FPS = 60
PI = math.pi

SCREEN_COLOR = 'black'
WALL_COLOR = 'blue'
DOT_COLOR = 'white'
POWERUP_COLOR = 'white'
PLAYER_SPEED = 2
GHOST_SPEEDS = [2, 2, 2, 2]
GHOST_SPEEDS_POWERUP = [1, 1, 1, 1]
GHOST_SPEEDS_EATEN = [2, 2, 2, 2]
GHOST_SPEEDS_DEAD = [4, 4, 4, 4]

PLAYER_START_X = 450
PLAYER_START_Y = 663
PLAYER_START_DIRECTION = 0

BLINKY_START_X = 56
BLINKY_START_Y = 58
BLINKY_START_DIRECTION = 0

INKY_START_X = 440
INKY_START_Y = 388
INKY_START_DIRECTION = 2

PINKY_START_X = 440
PINKY_START_Y = 438
PINKY_START_DIRECTION = 2

CLYDE_START_X = 440
CLYDE_START_Y = 438
CLYDE_START_DIRECTION = 2

LIVES_START = 3
SCORE_START = 0

POWERUP_DURATION = 600
STARTUP_DURATION = 180

ASSET_PATHS = {
    'player_images': 'assets/player_images/',
    'ghost_images': 'assets/ghost_images/',
    'font': 'freesansbold.ttf'
}

GHOST_IMAGES = {
    'blinky': 'red.png',
    'pinky': 'pink.png', 
    'inky': 'blue.png',
    'clyde': 'orange.png',
    'spooked': 'powerup.png',
    'dead': 'dead.png'
}
