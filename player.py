from config import *
import math
from entity import Entity

class Player(Entity):
    def __init__(self, pos, color, tile_size):
        Entity.__init__(self, pos[0], pos[1], color, tile_size)
        self.movement_left = True
        self.movement_right = True
        self.movement_up = True
        self.movement_down = True

    def movement(self, pg, delta_fps):
        key = pg.key.get_pressed()
        movement_speed = 1 / float(delta_fps)
        x, y = 0, 0
        if key[pg.K_a]:
            x = -PLAYER_MOVEMENT_SPEED * movement_speed * self.movement_left
        if key[pg.K_d]:
            x = PLAYER_MOVEMENT_SPEED * movement_speed * self.movement_right
        if key[pg.K_w]:
            y = -PLAYER_MOVEMENT_SPEED * movement_speed * self.movement_up
        if key[pg.K_s]:
            y = PLAYER_MOVEMENT_SPEED * movement_speed * self.movement_down
        if x != 0 and y != 0:
            x *= math.cos(math.pi / 4)
            y *= math.cos(math.pi / 4)
        self.x += x
        self.y += y

    def collision(self, food_obj_list):
        self.food_collision(food_obj_list)
        self.wall_collision()

    def food_collision(self, food_obj_list):
        for food_obj in food_obj_list:
            if math.sqrt((self.x - food_obj.x)**2 + (self.y - food_obj.y)**2) < self.tile_size:
                #self.color = (random.randrange(256), random.randrange(256), random.randrange(256))
                food_obj_list.remove(food_obj)
                self.tile_size += 2

    def wall_collision(self):
        self.movement_left = not self.x - self.tile_size // 2 < 0
        self.movement_right = not self.x + self.tile_size // 2 >= MAP_SIZE_X
        self.movement_up = not self.y - self.tile_size // 2 < 0
        self.movement_down = not self.y + self.tile_size // 2 >= MAP_SIZE_Y
