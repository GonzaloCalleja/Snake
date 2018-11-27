
# All settings to control several game posibilities
# game options
TITLE = "Snake!"
WIDTH = 600
HEIGHT = 600
FPS = 60
FONT_NAME = 'arial'
HS_FILE = 'highscore.txt'
ROWS = 50
COLUMNS = 50

# Snake properties
INITIAL_POS = ((COLUMNS//2)*(WIDTH/COLUMNS),(ROWS//2)*(HEIGHT/ROWS))
SNAKE_SPEED = 6
LOOK = ["Joined", "Separated"]
DIE_ON_EDGE = True
#    1 - Joined  2 - Separated by one pixel
SEP_CHOICE = 1

# apple
APPLE_VALUE = 1


# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = LIGHTBLUE
