from game import Game

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()