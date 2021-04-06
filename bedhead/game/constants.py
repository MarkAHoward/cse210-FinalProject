import os

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Bedhead"

CHARACTER_SCALING = 2
TILE_SCALING = 3
COIN_SCALING = 3
SPRITE_PIXEL_SIZE = 16
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * TILE_SCALING)

PLAYER_MOVEMENT_SPEED = 5

# Gravity
GRAVITY = 1800

# Damping - Amount of speed lost per second
DEFAULT_DAMPING = 1.0
PLAYER_DAMPING = 0.9

# Friction between objects
PLAYER_FRICTION = 10.0
WALL_FRICTION = 1.0
DYNAMIC_ITEM_FRICTION = 0.6

# Mass (defaults to 1)
PLAYER_MASS = 2.1

# Keep player from going too fast
PLAYER_MAX_HORIZONTAL_SPEED = 500
PLAYER_MAX_VERTICAL_SPEED = 1200

# Player move speed on ground
PLAYER_MOVE_FORCE_ON_GROUND = 5000

# Force applied when moving left/right in the air
PLAYER_MOVE_FORCE_IN_AIR = 3000

# Strength of a jump
PLAYER_JUMP_IMPULSE = 1800
PLAYER_JUMP_SPEED = 15

LEFT_VIEWPORT_MARGIN = 400
RIGHT_VIEWPORT_MARGIN = 400
BOTTOM_VIEWPORT_MARGIN = 100
TOP_VIEWPORT_MARGIN = 200

# Close enough to not-moving to have the animation go to idle.
DEAD_ZONE = 0.1

# Constants used to track if the player is facing left or right
RIGHT_FACING = 0
LEFT_FACING = 1

# How many pixels to move before we change the texture in the walking animation
DISTANCE_TO_CHANGE_TEXTURE = 20

CHARACTER_IMAGE = "cse210-FinalProject/bedhead/assets/adventurer-idle-00.png"