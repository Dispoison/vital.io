import pygame


class Text:
    def __init__(self, display, text, size, font, color, x, y, state=None, is_selectable=True):
        self.display = display
        self.text = text
        self.size = size
        self.font = font
        self.color = color
        self.x = x
        self.y = y
        self.state = state
        self.is_mouse_over = False
        self.is_selectable = is_selectable

        self._font = pygame.font.Font(self.font, self.size)
        self._text = self._font.render(self.text, True, self.color)
        self._temp_surface = pygame.Surface(self._text.get_size())
        self.text_rect = self._text.get_rect()

    def draw(self):
        if self.is_mouse_over:
            self._temp_surface.fill((160, 160, 120))
        else:
            self._temp_surface.fill((0, 0, 0))
        self._temp_surface.blit(self._text, (0, 0))
        self.text_rect.center = (self.x, self.y)
        self.display.blit(self._temp_surface, self.text_rect)
