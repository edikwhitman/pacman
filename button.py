import pygame
from text import Text


class Button:
    def __init__(self, w, h, screen, x=0, y=0, color=(255, 255, 255), b_text='', text_color=(0, 0, 0), size=20):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.screen = screen
        self.color = color
        self.size = size
        self.text = Text(int(self.x), int(self.y), b_text, 'Comic Sans MS', self.size, text_color, True, False)
        pygame.font.init()

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.w, self.h))
        self.text.draw(self.screen)
        # font = pygame.font.SysFont('comic Sans MS', 40, True)
        # ts = font.render(self.text.text, True, self.text.color)
        # self.screen.blit(ts, ((self.x+self.w//2)-self.text.rect.w//2, (self.y+self.h//2)-self.text.rect.h//2))

    def is_clicked(self, x, y):
        if (self.x <= x <= self.x + self.w) and (self.y <= y <= self.y + self.h):
            return True
        else:
            return False
