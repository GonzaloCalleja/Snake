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
        with open(path.join(self.dir, HS_FILE), 'w') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0

        if HEIGHT/ROWS != HEIGHT//ROWS or WIDTH/COLUMNS != WIDTH//COLUMNS:
            self.screen.fill(BLACK)
            self.draw_text("Settings for Rows or Columns not in accordance with screen size!",
                           22, RED, WIDTH / 2, HEIGHT/4)
            self.draw_text("( "+str(HEIGHT / ROWS) + ", " + str(WIDTH / COLUMNS) + ") is not a valid grid size",
                           22, RED, WIDTH / 2, HEIGHT / 4 + 30)
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
        if hits:
            if not self.apple.eating:
                for i in range(APPLE_VALUE):
                    b = Block(self.neck)
                    self.neck = b
                    self.all_sprites.add(b)
                    self.body.add(b)
                    self.apple.move()
                    self.score += 10

        # Die!
        hits = pg.sprite.spritecollide(self.snake, self.body, False)
        if hits:
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
