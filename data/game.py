import pygame as pg
from data.camera import *
from data.drawer import Drawer
from data.food import Food
from data.player import Player
from data.map import Map
from data.menu import *


class Game:
    def __init__(self):
        pg.init()
        self.running, self.playing = True, True
        self.display = pg.Surface([WINDOW_SIZE_X, WINDOW_SIZE_Y])
        self.window = pg.display.set_mode([WINDOW_SIZE_X, WINDOW_SIZE_Y])
        self.clock = pg.time.Clock()
        self.player = Player(PLAYER_START_POS, PLAYER_COLOR, PLAYER_START_TILE_HALF)
        self.food = Food(FOOD_AMOUNT)
        self.map_ = Map(self.food.obj_list)
        self.camera = Camera(self.player.get_pos(), self.map_)
        self.drawer = Drawer(pg, self.camera)
        self.delta_fps = None
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.current_menu = self.main_menu
        self.keys = {'return': False, 'backspace': False, 'down': False, 'up': False}

    def game_loop(self):
        while self.playing:
            self.check_events()
            self.display.fill(self.map_.background_color)

            self.camera.update(*self.player.get_pos())
            self.food.list_update(FOOD_AMOUNT)
            self.food.list_on_screen_update((self.camera.top_left_x, self.camera.top_left_y,
                                             self.camera.bot_right_x, self.camera.bot_right_y))

            self.drawer.draw(self.display, self.map_, self.food.obj_on_screen_list, self.player)

            self.window.blit(self.display, (0, 0))
            pg.display.update()
            self.delta_fps = self.clock.tick(FPS)
            self.player.update(pg, self.delta_fps, self.food.obj_list, self.food.obj_on_screen_list)
            self.camera.zoom_update()

            pg.display.set_caption(f'{WINDOW_TITLE} - {"%.0f" % self.clock.get_fps()}')
            self.reset_keys()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running, self.playing = False, False
                self.current_menu.run_display = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 4 or event.button == 5:
                    self.camera.zoom(Camera.ZOOM_MODE[event.button], 1000 / self.delta_fps)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.keys['return'] = True
                if event.key == pygame.K_BACKSPACE:
                    self.keys['backspace'] = True
                if event.key == pygame.K_DOWN:
                    self.keys['down'] = True
                if event.key == pygame.K_UP:
                    self.keys['up'] = True


    def reset_keys(self):
        self.keys = dict.fromkeys(self.keys, False)

