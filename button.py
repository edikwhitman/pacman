# Нашел у себя класс с игры, добавил тебе прост посмотреть,
# можем и использовать, если хочешь
# Если будем юзать, то все равно надо дописать апдейты например

import pygame


class Button:
    def __init__(self, w, h, screen, x=0, y=0, color=(0, 0, 0), text='', text_color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.screen = screen
        self.color = color
        self.text = text
        self.text_color = text_color
        pygame.font.init()

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.w, self.h))
        font = pygame.font.SysFont('comic Sans MS', 20, True)
        ts = font.render(self.text, True, self.text_color)
        self.screen.blit(ts, (self.x, self.y))

    def is_clicked(self, x, y):
        if (self.x <= x <= self.x + self.w) and (self.y <= y <= self.y + self.h):
            return True
        else:
            return False
