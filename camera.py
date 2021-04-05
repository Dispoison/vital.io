from config import *


class Camera:
    IN = 'IN'
    OUT = 'OUT'
    ZOOM_MODE = {4: IN, 5: OUT}

    def __init__(self, pl_pos):
        self.camera_size_x = WINDOW_SIZE_X
        self.camera_size_y = WINDOW_SIZE_Y
        self.camera_size_x_half = self.camera_size_x // 2
        self.camera_size_y_half = self.camera_size_y // 2

        self.zoom = 1
        self.camera_update(pl_pos)

    def camera_update(self, pl_pos):
        pl_x, pl_y = pl_pos
        self.camera_top_left_x = int(pl_x - self.camera_size_x_half)
        self.camera_top_left_y = int(pl_y - self.camera_size_y_half)

        start_row = max(int(self.camera_top_left_x / MAP_CELL_TILE), 0)
        start_col = max(int(self.camera_top_left_y / MAP_CELL_TILE), 0)
        self.start_cell = (start_row, start_col)

        end_row = min(int((self.camera_top_left_x + self.camera_size_x) / MAP_CELL_TILE) + 1, ROWS)
        end_col = min(int((self.camera_top_left_y + self.camera_size_y) / MAP_CELL_TILE) + 1, COLS)
        self.end_cell = (end_row, end_col)

    def camera_zoom(self, mode):
        if mode == Camera.IN and self.zoom < 2.99:
            self.zoom += 0.1
            self.set_camera_size_x(WINDOW_SIZE_X / self.zoom)
            self.set_camera_size_y(WINDOW_SIZE_Y / self.zoom)
        elif mode == Camera.OUT and self.zoom > 0.31:
            self.zoom -= 0.1
            self.set_camera_size_x(WINDOW_SIZE_X / self.zoom)
            self.set_camera_size_y(WINDOW_SIZE_Y / self.zoom)

    def set_camera_size_x(self, value):
        self.camera_size_x = int(value)
        self.camera_size_x_half = value // 2

    def set_camera_size_y(self, value):
        self.camera_size_y = int(value)
        self.camera_size_y_half = value // 2
