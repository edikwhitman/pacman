import pygame
import sys
import os
from button import Button
from config import WIDTH, BLUE


class Game:
    def __init__(self, screen):
        self.screen = screen  # Плоскость отображения
        self.map_img = 0
        self.map = []  # карта в виде символов (31 строка по 28 символов):
        # 0 - стена
        # 1 - малое зерно
        # 2 - съеденное малое зерно
        # 3 - большое зерно
        # 4 - съеденное большое зерно
        # 5 - вишенка
        # 6 - съеденная вишенка
        # 7 - одна из 18 клеток комнаты спавна приведений
        # 8 - пустая клетка

    def main_loop(self):
        print('game loop run')
        game_loop_run = True
        while game_loop_run:  # Сцена меню
            self.__process_logic()
            if self.__check_event() == 1:
                game_loop_run = False
            self.__process_drawing()

            pygame.display.flip()
            pygame.time.wait(10)
        print('game loop stop')

    def __process_logic(self):
        pass

    # Отрисовка не статичных объектов (кнопки)
    def __process_drawing(self):
        # Очередь отрисовки:
        # 1. изображение карты map_img.png
        # 2. зерна и фрукты
        # 3. pac man
        # 4. ghosts
        # 5. scores
        pass

    # Обработка ивентов
    def __check_event(self):
        response = None
        for event in pygame.event.get():
            pass
        return 1

    def set_map(self, arguments):
        self.map, self.map_img = arguments
        print('loaded')
        # self.map_i, self.map_img = arguments
        # установка остальных необходимых значений
