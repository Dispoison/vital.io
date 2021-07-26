import random
from cfg.config import *
from data.food_unit import FoodUnit


class Food:
    def __init__(self, food_amount):
        self.obj_list = []
        self.obj_on_screen_list = []
        self.list_creation(food_amount)

    def list_creation(self, food_amount):
        for _ in range(food_amount):
            self.create_new()

    def list_update(self, food_amount):
        if len(self.obj_list) < food_amount:
            self.create_new()

    def list_on_screen_update(self, camera_pos):
        self.obj_on_screen_list = [food_unit for food_unit in self.obj_list if food_unit.is_on_screen(*camera_pos)]

    def create_new(self):
        x = random.randrange(0, ROWS * MAP_CELL_TILE, MAP_CELL_TILE) + MAP_CELL_TILE // 2
        y = random.randrange(0, COLS * MAP_CELL_TILE, MAP_CELL_TILE) + MAP_CELL_TILE // 2
        # while len(Food.food_obj_list) > 0 and [food for food in Food.food_obj_list if food.get_pos() == (x, y)]:
        #    x = random.randrange(0, ROWS * MAP_CELL_TILE, MAP_CELL_TILE) + MAP_CELL_TILE // 2
        #    y = random.randrange(0, COLS * MAP_CELL_TILE, MAP_CELL_TILE) + MAP_CELL_TILE // 2
        self.obj_list.append(FoodUnit((x, y), FOOD_COLOR, FOOD_CELL_TILE_HALF))
