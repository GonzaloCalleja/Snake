

# All game sprites: Snake, Block, Apple

import pygame as pg
import random
from gym_snake.envs.settings import *
vec = pg.math.Vector2


class Spriteheet():
    # utitlity class for loading and parsing spritesheets
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert()

    def get_image(self, x, y, width, height):
        # get an image out of a larger sprisheet
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = pg.transform.scale(image, (SNAKE_HEIGHT, SNAKE_WIDTH))
        return image


class Snake(pg.sprite.Sprite):

    def __init__(self, spritesheet):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((SNAKE_WIDTH, SNAKE_HEIGHT))
        #self.image.fill(RED)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = SNAKE_PIXEL_SIZE // 2+1
        pg.draw.circle(self.image, DARK_GREEN, self.rect.center, self.radius)
        self.rect.topleft = INITIAL_POS

        self.spritesheet = spritesheet


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
        if keys[pg.K_SPACE]:
            self.next = vec(0, 0)

        if self.rect.left % SNAKE_WIDTH == 0 and self.rect.top % SNAKE_HEIGHT == 0 and self.next + self.vel != vec(0, 0):
            self.vel = self.next

        self.rect.left += self.vel.x
        self.rect.top += self.vel.y

        if not DIE_ON_EDGE:
            if self.rect.centerx < 0 + W_ADJUST:
                self.rect.centerx = WIDTH + W_ADJUST
            if self.rect.centerx > WIDTH + W_ADJUST:
                self.rect.centerx = 0 + W_ADJUST
            if self.rect.centery < 0 + H_ADJUST:
                self.rect.centery = HEIGHT + H_ADJUST
            if self.rect.centery > HEIGHT + H_ADJUST:
                self.rect.centery = 0 + H_ADJUST


class Block(pg.sprite.Sprite):

    def __init__(self, previous):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((BLOCK_WIDTH, BLOCK_HEIGHT))
        #self.image.fill(RED)
        self.previous = previous
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.radius = SNAKE_PIXEL_SIZE // 2
        pg.draw.circle(self.image, DARK_GREEN, self.rect.center, self.radius)

        self.objectives = []
        self.waiting = 0

        self.vel = self.previous.vel
        self.rect.x = self.previous.rect.x
        self.rect.y = self.previous.rect.y

    def update(self):
        self.vel = self.previous.vel

        if 0 <= self.waiting < SNAKE_PIXEL_SIZE//SNAKE_SPEED + SEP_CHOICE:
            self.waiting += 1
            self.objectives.append(vec(self.previous.rect.x, self.previous.rect.y))
            return
        self.waiting = -1
        if self.vel != vec(0, 0):

            self.objectives.append(vec(self.previous.rect.x, self.previous.rect.y))
            next = self.objectives.pop(0)
            self.rect.x = next.x
            self.rect.y = next.y


class Apple(pg.sprite.Sprite):

    def __init__(self, spritesheet,  *group_rects):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((APPLE_WIDTH, APPLE_HEIGHT))
        #self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.radius = SNAKE_PIXEL_SIZE // 2
        pg.draw.circle(self.image, RED, self.rect.center, self.radius)

        self.group_rects = group_rects
        self.move()
        self.time = None
        self.eating = False
        self.value = APPLE_VALUE

    def move(self):
        occupied = True
        count = 0
        while occupied:
            count += 1
            occupied = False
            x = random.choice(range(0, WIDTH, APPLE_WIDTH))
            y = random.choice(range(0, HEIGHT, APPLE_HEIGHT))

            if (x, y) == INITIAL_POS:
                occupied = True

            for a in self.group_rects:
                self.rect.topleft = (x, y)
                hits = pg.sprite.spritecollide(self, a, False)
                if hits:
                    occupied = True

            if count > ROWS*COLUMNS:
                return False
        self.rect.topleft = (x, y)
        return True

    def update(self):
        pass
