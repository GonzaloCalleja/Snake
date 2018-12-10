
# All settings to control several game posibilities
# game options
TITLE = "Snake!"
WIDTH = 600
HEIGHT = 600
FPS = 60
FONT_NAME = 'arial'
HS_FILE = 'highscore.txt'
SPRITESHEET = "grass_background.jpg"


# Snake properties
SNAKE_PIXEL_SIZE = 15
SNAKE_HEIGHT = SNAKE_PIXEL_SIZE
SNAKE_WIDTH = SNAKE_PIXEL_SIZE
ROWS = HEIGHT // SNAKE_HEIGHT
COLUMNS = WIDTH // SNAKE_WIDTH
INITIAL_POS = ((COLUMNS//2)*SNAKE_WIDTH,(ROWS//2)*SNAKE_HEIGHT)
SNAKE_SPEED = 3

# If the speed divided by half the length is not 0,
# when going through an edge the speed will not place the snake in a
# correct position by itself

W_ADJUST = (SNAKE_WIDTH /2)%SNAKE_SPEED
H_ADJUST = (SNAKE_HEIGHT /2)%SNAKE_SPEED

DIE_ON_EDGE = False
# LOOK = ["Joined", "Separated"]
#    0 - Joined  1 - Separated by one pixel
SEP_CHOICE = 0

# apple
APPLE_VALUE = 50
APPLE_HEIGHT = SNAKE_PIXEL_SIZE
APPLE_WIDTH = SNAKE_PIXEL_SIZE

#block
BLOCK_HEIGHT = SNAKE_PIXEL_SIZE
BLOCK_WIDTH = SNAKE_PIXEL_SIZE


# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = LIGHTBLUE
PURPLE = (75,0,130)
DARK_GREEN = (0,100,0)
BORDER_RED = (61, 26, 26)
