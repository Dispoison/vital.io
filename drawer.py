import pygame as pg
from config import *
import config


class Drawer:
    def __init__(self):
        self.font = pg.font.Font('freesansbold.ttf', 32)

    def draw_food(self, sc, food_obj_list, camera_pos_x, camera_pos_y):
        [pg.draw.circle(sc, food_obj.color, ((food_obj.x - camera_pos_x) * config.ZOOM,
                                            (food_obj.y - camera_pos_y) * config.ZOOM),
                                            FOOD_CELL_TILE_HALF * config.ZOOM)
         for food_obj in food_obj_list]

    def draw_grid(self, sc, grid_bias, drawable_cells_amount):
        start_x, start_y = grid_bias
        drawable_cells_in_row, drawable_cells_in_col = drawable_cells_amount[0], drawable_cells_amount[1]

        [[pg.draw.rect(sc, (20, 20, 20),
                       ((start_x + x * MAP_CELL_TILE) * config.ZOOM, (start_y + y * MAP_CELL_TILE* config.ZOOM) ,
                        MAP_CELL_TILE * config.ZOOM, MAP_CELL_TILE * config.ZOOM),
                       1, border_radius=MAP_CELL_TILE_RADIUS)
          for y in range(drawable_cells_in_col)]
         for x in range(drawable_cells_in_row)]

    def draw_player(self, sc, player):
        pg.draw.circle(sc, player.color, (WINDOW_SIZE_X_HALF, WINDOW_SIZE_Y_HALF), player.tile_size * config.ZOOM)
        score = player.tile_size - PLAYER_START_TILE_HALF
        score = self.font.render(f'Score: {score}', True, (0, 127, 255))
        score_rect = score.get_rect()
        score_rect.center = (score_rect.width - 30, WINDOW_SIZE_Y - 40)
        sc.blit(score, score_rect)
