import random
from data.entity import Entity


class FoodUnit(Entity):

    def __init__(self, pos, color, tile_size):
        Entity.__init__(self, pos[0], pos[1], color, tile_size)
        self.tile_size *= random.randrange(80, 130) / 100

    def is_on_screen(self, top_left_x, top_left_y, bottom_right_x, bottom_right_y):
        top_left_x -= self.tile_size
        top_left_y -= self.tile_size
        bottom_right_x += self.tile_size
        bottom_right_y += self.tile_size
        return top_left_x < self.x < bottom_right_x and top_left_y < self.y < bottom_right_y
