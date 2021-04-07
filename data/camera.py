from cfg.config import *


class Camera:
    IN = 'IN'
    OUT = 'OUT'
    ZOOM_MODE = {4: IN, 5: OUT}

    def __init__(self, pl_pos, map):
        self.size_x = WINDOW_SIZE_X
        self.size_y = WINDOW_SIZE_Y
        self.size_x_half = self.size_x // 2
        self.size_y_half = self.size_y // 2
        self.map = map

        self.zoom_counter = 0
        self.zoom = 1
        self.camera_update(pl_pos)

    def camera_update(self, pl_pos):
        pl_x, pl_y = pl_pos
        self.top_left_x = int(pl_x - self.size_x_half)
        self.top_left_y = int(pl_y - self.size_y_half)
        self.bot_right_x = self.top_left_x + self.size_x
        self.bot_right_y = self.top_left_y + self.size_y

        start_row = max(int(self.top_left_x / MAP_CELL_TILE), 0)
        start_col = max(int(self.top_left_y / MAP_CELL_TILE), 0)
        self.start_cell = (start_row, start_col)

        end_row = min(int(self.bot_right_x / MAP_CELL_TILE) + 1, ROWS)
        end_col = min(int(self.bot_right_y / MAP_CELL_TILE) + 1, COLS)
        self.end_cell = (end_row, end_col)

    def camera_zoom(self, mode):
        if mode == Camera.IN and self.zoom_counter < ZOOM_IN_LIMIT:
            self.zoom_counter += ZOOM_STEP
            self.zoom = 2 ** self.zoom_counter
            self.set_size_x(WINDOW_SIZE_X / self.zoom)
            self.set_size_y(WINDOW_SIZE_Y / self.zoom)
        elif mode == Camera.OUT and self.zoom_counter > ZOOM_OUT_LIMIT:
            self.zoom_counter -= ZOOM_STEP
            self.zoom = 2 ** self.zoom_counter
            self.set_size_x(WINDOW_SIZE_X / self.zoom)
            self.set_size_y(WINDOW_SIZE_Y / self.zoom)

    def set_size_x(self, value):
        self.size_x = int(value)
        self.size_x_half = value // 2

    def set_size_y(self, value):
        self.size_y = int(value)
        self.size_y_half = value // 2
