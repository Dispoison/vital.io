from cfg.config import *


class Map:
    def __init__(self, food_obj_list, background_color=(0, 0, 0), grid_color=(20, 20, 20)):
        self.rows = ROWS
        self.cols = COLS
        self.food_obj_list = food_obj_list
        self.background_color = background_color
        self.grid_color = grid_color
