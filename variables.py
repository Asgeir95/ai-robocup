# All variables are in this file
from vector2d import Vec2d
import random
# Screen variables
SCREEN_X    = 1200
SCREEN_Y    = 900
SCREEN_SIZE = (SCREEN_X, SCREEN_Y)
FPS         = 60

# Field variables
HORISONTAL  = 0
VERTICAL    = 1
DISTANCE_FROM_SCREEN = 50
FIELD_V = SCREEN_Y - 2 * DISTANCE_FROM_SCREEN
FIELD_H = SCREEN_X - 2 * DISTANCE_FROM_SCREEN
HORISONTAL_TO_GOAL = 160
PENTALTY_HORISONTAL = 160
PENTALTY_VERTICAL = 400
GOAL = 80
GOAL_H = 20

# Player Variables
PLAYER_RADIUS = 10
PLAYER_SPEED = 2
PLAYER_MAXSPEED = 2

BALL_MAXSPEED = 10

VIEW_DISTANCE = 1000
SHOOT_DISTANCE = 300
PLAYER_DISTANCE = 5


#Team 
RED = 1
BLUE = 2

# Default pos
KEEPER_RED_POS = Vec2d(DISTANCE_FROM_SCREEN, SCREEN_Y/2)
RED_PLAYER2 = Vec2d(SCREEN_X / 2 - 400, SCREEN_Y/2 - 100)
RED_PLAYER3 = Vec2d(SCREEN_X / 2 - 400, SCREEN_Y/2 + 100)
RED_PLAYER4 = Vec2d(SCREEN_X / 2 - 200, SCREEN_Y/2)
KEEPER_BLUE_POS = Vec2d(SCREEN_X - DISTANCE_FROM_SCREEN, SCREEN_Y/2)
BLUE_PLAYER2 = Vec2d(SCREEN_X / 2 + 400, SCREEN_Y/2 - 100)
BLUE_PLAYER3 = Vec2d(SCREEN_X / 2 + 400, SCREEN_Y/2 + 100)
BLUE_PLAYER4 = Vec2d(SCREEN_X / 2 + 200, SCREEN_Y/2)
BALL_POS = Vec2d(SCREEN_X/2,SCREEN_Y/2)