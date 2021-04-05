import random
from data.entity import Entity
from cfg.config import *


class Food(Entity):
    food_obj_list = []
    food_obj_on_screen_list = []

    def __init__(self, pos, color, tile_size):
        Entity.__init__(self, pos[0], pos[1], color, tile_size)
        self.tile_size *= random.randrange(80, 300) / 100

    def is_food_on_screen(self, top_left_x, top_left_y, bottom_right_x, bottom_right_y):
        top_left_x -= self.tile_size
        top_left_y -= self.tile_size
        bottom_right_x += self.tile_size
        bottom_right_y += self.tile_size
        return top_left_x < self.x < bottom_right_x and top_left_y < self.y < bottom_right_y

    @staticmethod
    def food_list_creation(food_amount):
        for _ in range(food_amount):
            Food.food_create_new()

    @staticmethod
    def food_list_update(food_amount):
        if len(Food.food_obj_list) < food_amount:
            Food.food_create_new()

    @staticmethod
    def food_list_on_screen_update(camera_pos):
        Food.food_obj_on_screen_list = [food for food in Food.food_obj_list if food.is_food_on_screen(*camera_pos)]

    @staticmethod
    def food_create_new():
        x = random.randrange(0, ROWS * MAP_CELL_TILE, MAP_CELL_TILE) + MAP_CELL_TILE // 2
        y = random.randrange(0, COLS * MAP_CELL_TILE, MAP_CELL_TILE) + MAP_CELL_TILE // 2
        # while len(Food.food_obj_list) > 0 and [food for food in Food.food_obj_list if food.get_pos() == (x, y)]:
        #    x = random.randrange(0, ROWS * MAP_CELL_TILE, MAP_CELL_TILE) + MAP_CELL_TILE // 2
        #    y = random.randrange(0, COLS * MAP_CELL_TILE, MAP_CELL_TILE) + MAP_CELL_TILE // 2
        Food.food_obj_list.append(Food((x, y), FOOD_COLOR, FOOD_CELL_TILE_HALF))
