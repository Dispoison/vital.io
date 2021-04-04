from config import *


class Camera:
    IN = 'IN'
    OUT = 'OUT'
    ZOOM_MODE = {4: IN, 5: OUT}

    def __init__(self, pl_pos):
        self.camera_update(pl_pos)

    def camera_update(self, pl_pos):
        pl_x, pl_y = pl_pos
        self.camera_top_left_pos_on_map_x = pl_x - CAMERA_SIZE_X_HALF
        self.camera_top_left_pos_on_map_y = pl_y - CAMERA_SIZE_Y_HALF

        start_row = max(int(pl_x - CAMERA_SIZE_X_HALF) // MAP_CELL_TILE, 0)
        start_col = max(int(pl_y - CAMERA_SIZE_Y_HALF) // MAP_CELL_TILE, 0)
        self.start_cell = (start_row, start_col)

        end_row = min(start_row + CAMERA_SIZE_X // MAP_CELL_TILE + 1, ROWS)
        end_col = min(start_col + CAMERA_SIZE_Y // MAP_CELL_TILE + 1, COLS)
        self.end_cell = (end_row, end_col)

    def camera_zoom(self, mode):
        import config
        if mode == Camera.IN and config.ZOOM < 3:
            config.ZOOM += 0.1
        elif mode == Camera.OUT and config.ZOOM > 0.5:
            config.ZOOM -= 0.1


