
# class game contains the game logic to:
# - generate the pygame window
# - generate a new instance of the game
# - listen to events, update all sprites and update the display
# - store highscore in a text file and read it later - currently not working

import pygame as pg
import random
from os import path, environ
from settings import *
from sprites import *

class Game():
    def __init__(self):
        # initialize game window, etc
        environ['SDL_VIDEO_CENTERED'] = '1'
        # pg.mixer.pre_init(44100, -16, 2, 2048)
        pg.mixer.init()
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data()

    def load_data(self):
        self.dir = path.dirname(__file__)
        try:
            with open(path.join(self.dir, HS_FILE), 'r') as f:
                try:
                    self.highscore = int(f.read())
                except:
                    self.highscore = 0
        except:
            self.highscore = 0

        if HEIGHT % SNAKE_HEIGHT != 0 or WIDTH % SNAKE_WIDTH != 0 or SNAKE_HEIGHT % SNAKE_SPEED != 0 or SNAKE_WIDTH % SNAKE_SPEED != 0:
            self.screen.fill(BLACK)
            self.draw_text("Settings ERROR", 22, RED, WIDTH / 2, HEIGHT/4)
            self.draw_text("The following numbers should be ints: ", 22, RED, WIDTH / 2, HEIGHT *3/ 8 )
            self.draw_text("HEIGHT / SNAKE_HEIGHT, WIDTH / SNAKE_WIDTH,", 20, RED, WIDTH / 2, HEIGHT / 2 )
            self.draw_text("SNAKE_HEIGHT / SNAKE_SPEED, SNAKE_WIDTH / SNAKE_SPEED", 20, RED, WIDTH / 2, HEIGHT /2 +50)
            pg.display.flip()
            self.wait_for_key()

    def new(self):
        # Start a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.body = pg.sprite.Group()
        self.snake_g = pg.sprite.Group()
        self.apples = pg.sprite.Group()

        self.apple = Apple(self.body, self.snake_g)
        self.all_sprites.add(self.apple)
        self.apples.add(self.apple)
        self.snake = Snake()
        self.all_sprites.add(self.snake)
        self.snake_g.add(self.snake)
        self.neck = Block(self.snake)
        self.all_sprites.add(self.neck)
        self.snake_g.add(self.neck)

        # For debugging apple pos
        # for i in range(500):
        #     self.apple.move()
        #     print(self.apple.rect.topleft)

        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        # check if player hits apple
        hits = pg.sprite.spritecollide(self.snake, self.apples, False)
        for hit in hits:
            if not hit.eating:
                for i in range(hit.value):
                    b = Block(self.neck)
                    self.neck = b
                    self.all_sprites.add(b)
                    self.body.add(b)
                    self.apple.move()
                    self.score += 10

        # Die!
        hits = pg.sprite.spritecollide(self.snake, self.body, False)
        for hit in hits:
            if hit.waiting == -1:
                self.playing = False

        if DIE_ON_EDGE:
            if self.snake.rect.right > WIDTH or self.snake.rect.left < 0 or self.snake.rect.bottom > HEIGHT or self.snake.rect.top < 0:
                self.playing = False


    def events(self):
        # Game Loop - Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing= False
                self.running = False

    def draw(self):
        # Game Loop - Draw
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 22, WHITE, WIDTH/2, 15 )
        # after drawing - flip
        pg.display.flip()

    def show_start_screen(self):
        # game start/splash screen
        self.screen.fill(BGCOLOR)
        self.draw_text(TITLE, 48, WHITE, WIDTH/2, HEIGHT/4)
        self.draw_text("Arrows to move", 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press any key to play", 22, WHITE, WIDTH / 2, HEIGHT * 3/4)
        self.draw_text("High Score: " + str(self.highscore), 22, WHITE, WIDTH / 2, 15)
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        # game over/ continue screen
        if not self.running:
            return
        #self.screen.fill(BGCOLOR)
        self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press any key to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("NEW HIGH SCORE!", 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
            with open(path.join(self.dir, HS_FILE), 'w') as f:
                f.write(str(self.score))
        else:
            self.draw_text("High Score: " + str(self.highscore), 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    #if event.key == pg.K_RIGHT:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
