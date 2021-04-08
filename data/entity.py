class Entity:
    def __init__(self, x, y, color, tile_size):
        self.x = x
        self.y = y
        self.color = color
        self.tile_size = tile_size

    def get_pos(self):
        return self.x, self.y
