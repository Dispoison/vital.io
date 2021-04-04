from drawer import *
from food import *
from player import *
from map import *
from camera import *


pg.init()
pg.display.set_caption('vital.io')
sc = pg.display.set_mode([WINDOW_SIZE_X, WINDOW_SIZE_Y])
clock = pg.time.Clock()
player = Player(PLAYER_START_POS, PLAYER_COLOR, PLAYER_START_TILE_HALF)

food_obj_list = Food.food_list_creation(FOOD_AMOUNT)
map = Map(food_obj_list)
camera = Camera(player.get_pos())
drawer = Drawer(camera)

while True:
    sc.fill('black')
    camera.camera_update(player.get_pos())
    drawer.draw_grid(sc)
    drawer.draw_food(sc, food_obj_list)
    drawer.draw_player(sc, player)

    pg.display.flip()
    delta_fps = clock.tick(FPS)

    player.movement(pg, delta_fps)
    player.collision(food_obj_list)
    Food.food_list_update(food_obj_list, FOOD_AMOUNT)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 4 or event.button == 5:
                camera.camera_zoom(Camera.ZOOM_MODE[event.button])

