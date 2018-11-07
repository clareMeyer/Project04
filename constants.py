## @file constants.py
#  File containing game constants
#
#  Project: Gallaga Clone
#  Author: Py Five
#  Created: 10/18/19

from pygame.locals import *


# Frames Per Second
FPS = 1000

# Window Size
#SCREENRECT = Rect(0, 0, 640, 480)
SCREENRECT = Rect(0, 0, 1000, 650)

# Player Speed
PLAYER_SPEED = 12

# Enemy
ENEMY_SPEED = 4
ENEMY_ODDS = 48 #was 24
ENEMY_SIZE = (26, 26)
MAX_ENEMY_SHOTS = 1000
ENEMY_SHOT_ODDS = 50
MAX_ENEMIES = 300

# Shots
MAX_SHOTS = 5
SHOT_SPEED = 10
