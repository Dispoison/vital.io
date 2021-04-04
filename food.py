import random
from entity import Entity
from config import *


class Food(Entity):
    def __init__(self, pos, color, tile_size):
        Entity.__init__(self, pos[0], pos[1], color, tile_size)

    @staticmethod
    def food_list_creation(food_amount):
        food_obj_list = []
        for iter in range(food_amount):
            Food.food_create_new(food_obj_list)
        return food_obj_list

    @staticmethod
    def food_list_update(food_obj_list, food_amount):
        if len(food_obj_list) < food_amount:
            Food.food_create_new(food_obj_list)


    @staticmethod
    def food_create_new(food_obj_list):
        x = random.randrange(0, ROWS * MAP_CELL_TILE, MAP_CELL_TILE) + FOOD_CELL_TILE_HALF
        y = random.randrange(0, COLS * MAP_CELL_TILE, MAP_CELL_TILE) + FOOD_CELL_TILE_HALF
        while len(food_obj_list) > 0 and [food_obj for food_obj in food_obj_list if food_obj.get_pos() == (x, y)]:
            x = random.randrange(0, ROWS * MAP_CELL_TILE, MAP_CELL_TILE) + FOOD_CELL_TILE_HALF
            y = random.randrange(0, COLS * MAP_CELL_TILE, MAP_CELL_TILE) + FOOD_CELL_TILE_HALF
        food_obj_list.append(Food((x, y), FOOD_COLOR, FOOD_CELL_TILE_HALF))