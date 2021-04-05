import pygame as pg
from config import *


class Drawer:
    def __init__(self, camera):
        self.font = pg.font.Font('freesansbold.ttf', 32)
        self.camera = camera

    def draw(self, sc, food_obj_list, player):
        self.draw_grid(sc)
        self.draw_food(sc, food_obj_list)
        self.draw_player(sc, player)

    def draw_food(self, sc, food_obj_list):
        [pg.draw.circle(sc, food_obj.color, ((food_obj.x - self.camera.camera_top_left_x) * self.camera.zoom,
                                             (food_obj.y - self.camera.camera_top_left_y) * self.camera.zoom),
                        FOOD_CELL_TILE_HALF * self.camera.zoom)
         for food_obj in food_obj_list]

    def draw_grid(self, sc):
        start_row = self.camera.start_cell[0]
        start_col = self.camera.start_cell[1]
        end_row = self.camera.end_cell[0]
        end_col = self.camera.end_cell[1]

        [[pg.draw.rect(sc, (10, 10, 10),
                       ((((x * MAP_CELL_TILE) - self.camera.camera_top_left_x) * self.camera.zoom),
                        (((y * MAP_CELL_TILE) - self.camera.camera_top_left_y) * self.camera.zoom),
                        MAP_CELL_TILE * self.camera.zoom, MAP_CELL_TILE * self.camera.zoom),
                       1, border_radius=int(MAP_CELL_TILE_RADIUS * self.camera.zoom))
          for y in range(start_col, end_col)]
         for x in range(start_row, end_row)]

    def draw_player(self, sc, player):
        pg.draw.circle(sc, player.color, (((player.x - self.camera.camera_top_left_x) * self.camera.zoom),
                                          (player.y - self.camera.camera_top_left_y) * self.camera.zoom),
                       player.tile_size * self.camera.zoom)
        score = player.tile_size - PLAYER_START_TILE_HALF
        score = self.font.render(f'Score: {score}', True, (0, 127, 255))
        score_rect = score.get_rect()
        score_rect.center = (score_rect.width - 30, WINDOW_SIZE_Y - 40)
        sc.blit(score, score_rect)
