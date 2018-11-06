import pygame

from text import Text
from constants import SIZE, BLACK


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SIZE)  # Установка размеров окна
        self.gameover = False
        self.objects = []
        self.prepare_scene()

    def prepare_scene(self):
        self.objects.append(Text(100, 100))

    def main_loop(self):
        while not self.gameover:  # Основной цикл
            self.process_events()
            self.process_logic()
            self.process_drawing()
            pygame.time.wait(10)  # Ожидание отрисовки

    def process_events(self):
        for event in pygame.event.get():  # Получение всех событий
            if event.type == pygame.QUIT:  # Событие выхода
                self.gameover = True

    def process_logic(self):
        for i in self.objects:
            i.shift()

    def process_drawing(self):
        self.screen.fill(BLACK)  # Заливка цветом
        for i in self.objects:
            i.draw(self.screen)
        pygame.display.flip()  # Double buffering
