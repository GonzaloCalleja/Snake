import random
import time


class Snake(object):

    # yspeed, xspeed might be better

    # __directions__ = {"North": 1, "South": -1, "East": 1, "West": -1}
    __directions__ = ["North", "South", "East", "West"]

    def __init__(self, tile_number=10):

        self.direction = random.choice(self.__directions__)
        self.x = tile_number // 2
        self.y = tile_number // 2

    # method returns true if a tile is a snake
    def is_snake(self, x, y):
        if (x, y) == (self.x, self.y):
            return True
        return False

    def snake_pos(self):
        return self.x, self.y

    def change(self, direction):

        if direction in self.__directions__:
            self.direction = direction

    def move(self):

        if self.direction is self.__directions__[0]:
            time.sleep(5)
            self.y += 1
        elif self.direction is self.__directions__[1]:
            time.sleep(5)
            self.y -= 1
        elif self.direction is self.__directions__[2]:
            time.sleep(5)
            self.x += 1
        elif self.direction is self.__directions__[3]:
            time.sleep(5)
            self.x -= 1
