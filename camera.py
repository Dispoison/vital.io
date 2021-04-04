from config import *


class Camera:
    IN = 'IN'
    OUT = 'OUT'
    ZOOM_MODE = {4: IN, 5: OUT}

    def __init__(self, pl_pos):
        self.camera_update(pl_pos)

    def camera_update(self, pl_pos):
        pl_x, pl_y = pl_pos
        self.camera_top_left_pos_on_map_x = pl_x - WINDOW_SIZE_X_HALF
        self.camera_top_left_pos_on_map_y = pl_y - WINDOW_SIZE_Y_HALF
        camera_bottom_right_pos_on_map_x = pl_x + WINDOW_SIZE_X_HALF
        camera_bottom_right_pos_on_map_y = pl_y + WINDOW_SIZE_Y_HALF

        self.reserve_top_left_x = self.camera_top_left_pos_on_map_x // MAP_CELL_TILE * MAP_CELL_TILE \
                                    if self.camera_top_left_pos_on_map_x > 0 else 0 # floor
        self.reserve_top_left_y = self.camera_top_left_pos_on_map_y // MAP_CELL_TILE * MAP_CELL_TILE \
                                    if self.camera_top_left_pos_on_map_y > 0 else 0 # floor

        self.reserve_bottom_right_x = -(-camera_bottom_right_pos_on_map_x // MAP_CELL_TILE) * MAP_CELL_TILE  # ceil
        self.reserve_bottom_right_y = -(-camera_bottom_right_pos_on_map_y // MAP_CELL_TILE) * MAP_CELL_TILE  # ceil

        self.grid_bias = ((self.reserve_top_left_x - self.camera_top_left_pos_on_map_x),
                          (self.reserve_top_left_y - self.camera_top_left_pos_on_map_y))

        if camera_bottom_right_pos_on_map_x <= MAP_SIZE_X:
            drawable_cells_x = MAP_CELLS_ON_SCREEN_X + 1
        else:
            drawable_cells_x = min(int((MAP_SIZE_X - self.camera_top_left_pos_on_map_x) // MAP_CELL_TILE) + 1, ROWS)
        if camera_bottom_right_pos_on_map_y <= MAP_SIZE_Y:
            drawable_cells_y = MAP_CELLS_ON_SCREEN_Y + 1
        else:
            drawable_cells_y = min(int((MAP_SIZE_Y - self.camera_top_left_pos_on_map_y) // MAP_CELL_TILE) + 1, COLS)

        self.drawable_cells_amount = (drawable_cells_x, drawable_cells_y)

    def camera_zoom(self, mode):
        import config
        if mode == Camera.IN and config.ZOOM < 3:
            config.ZOOM += 0.1
        elif mode == Camera.OUT and config.ZOOM > 0.5:
            config.ZOOM -= 0.1

