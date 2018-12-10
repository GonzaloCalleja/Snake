
# Snake Game main: Execute to run program
from gym_snake.envs.game import Game
def run():

    g = Game()
    g.show_start_screen()
    while g.running:
        g.new()
        g.show_go_screen()