

# All game sprites: Snake, Block, Apple

import pygame as pg
import random
from settings import *
vec = pg.math.Vector2

class Snake(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((WIDTH / COLUMNS, HEIGHT / ROWS))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.topleft = INITIAL_POS

        self.vel = vec(0,0)
        self.next = vec(0,0)

    def update(self):

        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.next = vec(-SNAKE_SPEED, 0)
        if keys[pg.K_RIGHT]:
            self.next = vec(SNAKE_SPEED, 0)
        if keys[pg.K_UP]:
            self.next = vec(0, -SNAKE_SPEED)
        if keys[pg.K_DOWN]:
            self.next = vec(0, SNAKE_SPEED)

        if self.rect.left % (WIDTH/COLUMNS) == 0 and self.rect.top % (HEIGHT/ROWS) == 0 and self.next + self.vel != vec(0,0):
            self.vel = self.next

        self.rect.left += self.vel.x
        self.rect.top += self.vel.y

        if not DIE_ON_EDGE:
            if self.rect.centerx < 0:
                self.rect.centerx = WIDTH
            if self.rect.centerx > WIDTH:
                self.rect.centerx = 0
            if self.rect.centery < 0:
                self.rect.centery = HEIGHT
            if self.rect.centery > HEIGHT:
                self.rect.centery = 0



class Block(pg.sprite.Sprite):

    def __init__(self, previous):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((WIDTH / COLUMNS, HEIGHT / ROWS))
        self.image.fill(RED)
        self.previous = previous
        self.rect = self.image.get_rect()

        self.objectives = []
        self.wait = 0

        self.rect.x = self.previous.rect.x
        self.rect.y = self.previous.rect.y

    def update(self):
        # So the new block "slides of the previous one
        self.wait += 1
        if self.wait < WIDTH//COLUMNS//SNAKE_SPEED + SEP_CHOICE:
            self.objectives.append(vec(self.previous.rect.x, self.previous.rect.y))
            return

        self.objectives.append(vec(self.previous.rect.x, self.previous.rect.y))

        next = self.objectives.pop(0)
        self.rect.x = next.x
        self.rect.y = next.y


class Apple(pg.sprite.Sprite):

    def __init__(self, *group_rects):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((WIDTH / COLUMNS, HEIGHT / ROWS))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.group_rects = group_rects
        self.move()
        self.time = None
        self.eating = False

    def move(self):
        occupied = True
        while occupied:
            occupied = False
            x = random.choice(range(0, WIDTH, WIDTH // COLUMNS))
            y = random.choice(range(0, HEIGHT, HEIGHT // ROWS))

            if (x, y) == INITIAL_POS:
                occupied = True

            for a in self.group_rects:
                for b in a:
                    if (x, y) == b.rect.topleft:
                        occupied = True
        self.rect.topleft = (x, y)

    def update(self):
        pass
