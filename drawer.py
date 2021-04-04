import pygame as pg
from config import *


class Drawer:
    def __init__(self, camera):
        self.font = pg.font.Font('freesansbold.ttf', 32)
        self.camera = camera

    def draw_food(self, sc, food_obj_list):
        [pg.draw.circle(sc, food_obj.color, ((food_obj.x - self.camera.camera_top_left_pos_on_map_x),
                                            (food_obj.y - self.camera.camera_top_left_pos_on_map_y)),
                                            FOOD_CELL_TILE_HALF)
         for food_obj in food_obj_list]

    def draw_grid(self, sc):
        start_row = self.camera.start_cell[0]
        start_col = self.camera.start_cell[1]
        end_row = self.camera.end_cell[0]
        end_col = self.camera.end_cell[1]

        [[pg.draw.rect(sc, (20, 20, 20),
                       ((x * MAP_CELL_TILE) - self.camera.camera_top_left_pos_on_map_x,
                        (y * MAP_CELL_TILE) - self.camera.camera_top_left_pos_on_map_y,
                        MAP_CELL_TILE, MAP_CELL_TILE),
                       1, border_radius=MAP_CELL_TILE_RADIUS)
          for y in range(start_col, end_col)]
         for x in range(start_row, end_row)]

    def draw_player(self, sc, player):
        pg.draw.circle(sc, player.color, (CAMERA_SIZE_X_HALF, CAMERA_SIZE_Y_HALF), player.tile_size)
        score = player.tile_size - PLAYER_START_TILE_HALF
        score = self.font.render(f'Score: {score}', True, (0, 127, 255))
        score_rect = score.get_rect()
        score_rect.center = (score_rect.width - 30, WINDOW_SIZE_Y - 40)
        sc.blit(score, score_rect)
