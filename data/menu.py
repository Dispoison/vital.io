import pygame
from cfg.config import *
from data.text import Text


class Menu:
    def __init__(self, game):
        self.game = game
        self.run_display = True
        self.offset = - 100
        self.font_name = 'fonts/muller-extrabold.ttf'
        self.state = 'Start'

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()

    def check_mouse_input(self, texts):
        for text in texts:
            if text.is_selectable:
                text.is_mouse_over = text.text_rect.collidepoint(pygame.mouse.get_pos())
                if pygame.mouse.get_pressed()[0]:
                    self.state = text.state
                    self.state_routing()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.main_menu_text_x, self.main_menu_text_y = WINDOW_SIZE_X_HALF, WINDOW_SIZE_Y_HALF - 70
        self.start_text_x, self.start_text_y = WINDOW_SIZE_X_HALF, WINDOW_SIZE_Y_HALF + 30
        self.options_text_x, self.options_text_y = WINDOW_SIZE_X_HALF, WINDOW_SIZE_Y_HALF + 70
        self.credits_text_x, self.credits_text_y = WINDOW_SIZE_X_HALF, WINDOW_SIZE_Y_HALF + 110
        self.quit_text_x, self.quit_text_y = WINDOW_SIZE_X_HALF, WINDOW_SIZE_Y_HALF + 150

        self.main_menu_text = Text(game.display, 'Main Menu', 40, self.font_name, SCORE_TEXT_COLOR,
                                   self.main_menu_text_x, self.main_menu_text_y, None, False)
        self.start_game_text = Text(game.display, 'Start Game', 40, self.font_name, SCORE_TEXT_COLOR,
                                    self.start_text_x, self.start_text_y, 'Start')
        self.options_text = Text(game.display, 'Options', 40, self.font_name, SCORE_TEXT_COLOR,
                                 self.options_text_x, self.options_text_y, 'Options')
        self.credits_text = Text(game.display, 'Credits', 40, self.font_name, SCORE_TEXT_COLOR,
                                 self.credits_text_x, self.credits_text_y, 'Credits')
        self.quit_text = Text(game.display, 'Quit', 40, self.font_name, SCORE_TEXT_COLOR,
                              self.quit_text_x, self.quit_text_y, 'Quit')
        self.texts = [self.main_menu_text, self.start_game_text, self.options_text, self.credits_text, self.quit_text]

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_keys_input()
            self.check_mouse_input(self.texts)
            self.game.display.fill((0, 0, 0))
            self.main_menu_text.draw()
            self.start_game_text.draw()
            self.options_text.draw()
            self.credits_text.draw()
            self.quit_text.draw()
            self.blit_screen()

    def check_keys_input(self):
        if self.game.keys['return']:
            self.state_routing()

    def state_routing(self):
        if self.state == 'Start':
            self.game.playing = True
        elif self.state == 'Options':
            self.game.curr_menu = self.game.options
        elif self.state == 'Credits':
            self.game.curr_menu = self.game.credits
        self.run_display = False


class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.options_text_x, self.options_text_y = WINDOW_SIZE_X_HALF, WINDOW_SIZE_Y_HALF - 30
        self.volume_text_x, self.volume_text_y = WINDOW_SIZE_X_HALF, WINDOW_SIZE_Y_HALF + 20
        self.controls_text_x, self.controls_text_y = WINDOW_SIZE_X_HALF, WINDOW_SIZE_Y_HALF + 40

        self.options_text = Text(game.display, 'Options', 20, self.font_name, SCORE_TEXT_COLOR,
                                 self.options_text_x, self.options_text_y)
        self.volume_text = Text(game.display, 'Volume', 20, self.font_name, SCORE_TEXT_COLOR,
                                self.volume_text_x, self.volume_text_y)
        self.controls_text = Text(game.display, 'Controls', 20, self.font_name, SCORE_TEXT_COLOR,
                                  self.controls_text_x, self.controls_text_y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.options_text.draw()
            self.volume_text.draw()
            self.controls_text.draw()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
            elif self.state == 'Controls':
                self.state = 'Volume'
        elif self.game.START_KEY:
            # TO-DO: Create a Volume Menu and a Controls Menu
            pass


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.credits_text_x, self.credits_text_y = WINDOW_SIZE_X_HALF, WINDOW_SIZE_Y_HALF - 20
        self.info_text_x, self.info_text_y = WINDOW_SIZE_X_HALF, WINDOW_SIZE_Y_HALF + 10

        self.credits_text = Text(game.display, 'Credits', 20, self.font_name, SCORE_TEXT_COLOR,
                                 self.credits_text_x, self.credits_text_y)
        self.info_text = Text(game.display, 'Made by Dispoison', 20, self.font_name, SCORE_TEXT_COLOR,
                              self.info_text_x, self.info_text_y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.credits_text.draw()
            self.info_text.draw()
            self.blit_screen()
