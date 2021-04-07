import pygame as pg
from data.drawer import *
from data.food import *
from data.player import *
from data.map import *
from data.camera import *

pg.init()
pg.display.set_caption(WINDOW_TITLE)
sc = pg.display.set_mode([WINDOW_SIZE_X, WINDOW_SIZE_Y])
clock = pg.time.Clock()
player = Player(PLAYER_START_POS, PLAYER_COLOR, PLAYER_START_TILE_HALF)

Food.food_list_creation(FOOD_AMOUNT)
map = Map(Food.food_obj_list)
camera = Camera(player.get_pos(), map)
drawer = Drawer(pg, camera)

while True:
    sc.fill(map.background_color)

    camera.camera_update(player.get_pos())
    Food.food_list_update(FOOD_AMOUNT)
    Food.food_list_on_screen_update((camera.top_left_x, camera.top_left_y, camera.bot_right_x, camera.bot_right_y))

    drawer.draw(sc, map, Food.food_obj_on_screen_list, player)

    pg.display.flip()
    delta_fps = clock.tick(FPS)
    player.update(pg, delta_fps, Food.food_obj_list, Food.food_obj_on_screen_list)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 4 or event.button == 5:
                camera.camera_zoom(Camera.ZOOM_MODE[event.button])
    pg.display.set_caption(f'{WINDOW_TITLE} - {"%.0f" % clock.get_fps()}')

