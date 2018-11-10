# Код для текста от Смирнова
# Тоже можно юзать или переписать с нуля

import pygame


class Text:
    def __init__(self, text, size, x=0, y=0, color=(255, 255, 255)):
        self.position = (x, y)
        self.text = text
        self.size = size
        self.color = color
        self.font = pygame.font.SysFont('Comic Sans MS', self.size, True)  # Шрифт Comic Sans MS, размер 15, полужирный
        self.surface = self.font.render(self.text, True, self.color)

    def update_text(self, new_text):
        self.text = new_text
        self.surface = self.font.render(self.text, True, self.color)

    def update_position(self, x, y):
        self.position = (x, y)

    def get_text_size(self):
        r = self.surface.get_rect()
        return [r.width, r.height]

    def draw(self, screen):
        screen.blit(self.surface, self.position)
