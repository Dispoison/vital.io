from cfg.config import *
from collections import deque


class Camera:
    IN = 'IN'
    OUT = 'OUT'
    ZOOM_MODE = {4: IN, 5: OUT}
    ZOOM_QUEUE = deque(maxlen=50)
    ZOOM_LAST_MODE = IN

    def __init__(self, pl_pos, map):
        self.size_x = WINDOW_SIZE_X
        self.size_y = WINDOW_SIZE_Y
        self.size_x_half = self.size_x / 2
        self.size_y_half = self.size_y / 2
        self.map = map

        self.zoom_counter = 0
        self.zoom = 1
        self.camera_update(*pl_pos)

    def camera_update(self, pl_x, pl_y):
        self.top_left_x = pl_x - self.size_x_half
        self.top_left_y = pl_y - self.size_y_half
        self.bot_right_x = self.top_left_x + self.size_x
        self.bot_right_y = self.top_left_y + self.size_y

        start_row = max(int(self.top_left_x / self.map.tile_size), 0)
        start_col = max(int(self.top_left_y / self.map.tile_size), 0)
        self.start_cell = (start_row, start_col)

        end_row = min(int(self.bot_right_x / self.map.tile_size) + 1, self.map.rows)
        end_col = min(int(self.bot_right_y / self.map.tile_size) + 1, self.map.cols)
        self.end_cell = (end_row, end_col)

    def camera_zoom(self, mode, fps):
        if mode == Camera.IN and self.zoom_counter < ZOOM_IN_LIMIT:
            if Camera.ZOOM_LAST_MODE == Camera.OUT:
                Camera.ZOOM_QUEUE.clear()
            zoom_frames = round(fps / 10)
            Camera.ZOOM_QUEUE.extend([ZOOM_STEP / zoom_frames] * zoom_frames)
            Camera.ZOOM_LAST_MODE = Camera.IN
        elif mode == Camera.OUT and self.zoom_counter > ZOOM_OUT_LIMIT:
            if Camera.ZOOM_LAST_MODE == Camera.IN:
                Camera.ZOOM_QUEUE.clear()
            zoom_frames = round(fps / 10)
            Camera.ZOOM_QUEUE.extend([-ZOOM_STEP / zoom_frames] * zoom_frames)
            Camera.ZOOM_LAST_MODE = Camera.OUT

    def zoom_update(self):
        if Camera.ZOOM_QUEUE:
            if self.zoom_counter > ZOOM_IN_LIMIT or self.zoom_counter < ZOOM_OUT_LIMIT:
                Camera.ZOOM_QUEUE.clear()
                self.zoom_counter = round(self.zoom_counter)
            else:
                zoom_diff = Camera.ZOOM_QUEUE.popleft()
                self.zoom_counter += zoom_diff
                self.zoom = 2 ** self.zoom_counter
                zoom_rounded = 2 ** round(self.zoom_counter)
                self.set_size_x(WINDOW_SIZE_X / self.zoom)
                self.set_size_y(WINDOW_SIZE_Y / self.zoom)
                self.map.tile_size = int(MAP_CELL_TILE / zoom_rounded)
                self.map.rows = MAP_SIZE_X // self.map.tile_size
                self.map.cols = MAP_SIZE_Y // self.map.tile_size

    def set_size_x(self, value):
        self.size_x = int(value)
        self.size_x_half = value // 2

    def set_size_y(self, value):
        self.size_y = int(value)
        self.size_y_half = value // 2
