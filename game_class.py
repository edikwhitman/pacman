import pygame
import sys
import os
from button import Button
from config import WIDTH, BLUE


class Game:
    def __init__(self, screen):
        self.screen = screen  # Плоскость отображения
        self.map_img = 0
        self.pacman_start_spawn = None
        self.fruit_spawn = None
        self.grain_img = pygame.image.load('images/entity/grain.png')
        self.big_grain_img = pygame.image.load('images/entity/grain_big.png')
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
        self.screen.blit(self.map_img, (0, 48))

        # 2. зерна и фрукты
        for i in range(31):
            for j in range(28):
                if self.map[i][j] == '1':
                    self.screen.blit(self.grain_img, (j * 16, (i * 16) + 48))
                elif self.map[i][j] == '3':
                    self.screen.blit(self.big_grain_img, (j * 16, (i * 16) + 48))

        # 3. pac man
        # self.pacman.draw(self.screen)
        # 4. ghosts
        # for ghost in self.ghosts:
        #     ghost.draw()
        # 5. scores
        #
        pass

    # Обработка ивентов
    def __check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def __reset_grains(self):
        for i in range(31):
            for j in range(28):
                if self.map[i][j] == '2':
                    self.map[i][j] = '1'
                elif self.map[i][j] == '4':
                    self.map[i][j] = '3'

    def set_map(self, arguments):
        self.map, self.map_img = arguments
        print('loaded')

        self.pacman_start_spawn = None
        self.fruit_spawn = None
        # Установка точки спавна PacMan'а и других необходимых элементов
        previous_char = None
        for i in range(31):
            for j in range(28):
                char = self.map[i][j]
                if char == '9' and previous_char == '9':
                    self.pacman_start_spawn = (j*16 - 8, i*16 + 48)
                elif char == '6' and previous_char == '6':
                    self.fruit_spawn = (j*16 - 8, i*16 + 48)
                previous_char = self.map[i][j]
            previous_char = None

        if self.pacman_start_spawn is None:
            print('Error: No pacman start spawn point in map config file')
        if self.fruit_spawn is None:
            print('Error: No fruit spawn point in map config file')

        # установка остальных необходимых значений
