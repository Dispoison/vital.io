from cfg.config import *


class Drawer:
    def __init__(self, pg, camera):
        self.pg = pg
        self.camera = camera
        self.font = pg.font.Font('freesansbold.ttf', 32)

    def draw(self, sc, map, food_obj_list, player):
        self.draw_grid(sc, map)
        self.draw_food(sc, food_obj_list)
        self.draw_player(sc, player)
        self.draw_player_score(sc, player)

    def draw_grid(self, sc, map):
        start_row = self.camera.start_cell[0]
        start_col = self.camera.start_cell[1]
        end_row = self.camera.end_cell[0]
        end_col = self.camera.end_cell[1]

        for x in range(start_row, end_row):
            for y in range(start_col, end_col):
                rect_x = (x * map.grid_size - self.camera.top_left_x) * self.camera.zoom
                rect_y = (y * map.grid_size - self.camera.top_left_y) * self.camera.zoom
                rect_size = map.grid_size * self.camera.zoom
                rect = rect_x, rect_y, rect_size, rect_size
                border_radius = int(MAP_CELL_TILE_RADIUS * self.camera.zoom)

                self.pg.draw.rect(sc, map.grid_color, rect, MAP_CELL_WIDTH, border_radius=border_radius)

    def draw_food(self, sc, food_obj_list):
        for food in food_obj_list:
            circle_x = (food.x - self.camera.top_left_x) * self.camera.zoom
            circle_y = (food.y - self.camera.top_left_y) * self.camera.zoom
            circle = circle_x, circle_y
            circle_radius = food.tile_size * self.camera.zoom

            self.pg.draw.circle(sc, food.color, circle, circle_radius)

    def draw_player(self, sc, player):
        circle_x = (player.x - self.camera.top_left_x) * self.camera.zoom
        circle_y = (player.y - self.camera.top_left_y) * self.camera.zoom
        circle = circle_x, circle_y
        circle_radius = player.tile_size * self.camera.zoom

        self.pg.draw.circle(sc, player.color, circle, circle_radius)

    def draw_player_score(self, sc, player):
        score = player.tile_size - PLAYER_START_TILE_HALF
        score = self.font.render(f'Score: {"%.1f" % score}', True, SCORE_TEXT_COLOR)
        score_rect = score.get_rect()
        score_rect.center = (score_rect.width - 30, WINDOW_SIZE_Y - 40)
        sc.blit(score, score_rect)
