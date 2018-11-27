import pygame
import sys
from pacman import Pacman
from config import BLACK
from ghosts import Blinky, Pinky, Inky, Clyde


class Game:
    def __init__(self, screen):
        self.screen = screen  # Плоскость отображения
        self.map_img = 0
        self.pacman_start_spawn = None
        self.fruit_spawn = None
        self.pacman = Pacman(0, 0, 32, 32, 3, 3)
        self.ghosts = list()
        self.ghosts.append(Blinky(13*16, 11*16 + 48 - 8))
        self.ghosts.append(Pinky(13*16, 14*16 + 48 - 8))
        self.ghosts.append(Inky(11*16, 14*16 + 48 - 8))
        self.ghosts.append(Clyde(15*16, 14*16 + 48 - 8))
        self.grain_img = pygame.image.load('images/entity/grains/grain.png')
        self.big_grain_img = pygame.image.load('images/entity/grains/grain_big.png')
        self.big_grain_draw = True  # Отображаем большое зерно или нет. Чтобы мигание делать
        self.counter = 1  # Счетчик прохода по game_loop, нужен как таймер
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
        self.score = 0

    def main_loop(self):
        self.pacman.set_position(self.pacman_start_spawn[0], self.pacman_start_spawn[1])
        print('game loop run')
        game_loop_run = True
        while game_loop_run:
            if self.__check_event() == 1:
                game_loop_run = False
            self.__process_drawing()
            self.__process_logic()

            pygame.display.flip()
            pygame.time.wait(10)
        print('game loop stop')

    def __process_logic(self):
        self.pacman.move(self.map)
        self.check_eaten_grains()
        if self.counter % 10 == 0:  # Типа таймера, чтобы мигали не сильно часто
            if self.big_grain_draw:
                self.big_grain_draw = False
            else:
                self.big_grain_draw = True
        self.counter += 1
        if self.counter == 100:
            self.counter = 0

    # Отрисовка не статичных объектов
    def __process_drawing(self):
        self.screen.fill(BLACK)
        # Очередь отрисовки:

        # 1. изображение карты map_img.png
        self.screen.blit(self.map_img, (0, 48))

        # 2. зерна и фрукты
        for i in range(31):
            for j in range(28):
                if self.map[i][j] == '1':
                    self.screen.blit(self.grain_img, (j * 16, (i * 16) + 48))
                elif self.map[i][j] == '3' and self.big_grain_draw:
                    self.screen.blit(self.big_grain_img, (j * 16, (i * 16) + 48))

        # 3. pac man
        self.pacman.draw(self.screen)
        # 4. ghosts
        for ghost in self.ghosts:
            ghost.draw(self.screen)
        # 5. scores
        #

    # Обработка ивентов
    def __check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.pacman.check_event(event)

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
                    self.pacman_start_spawn = (j*16 - 16, i*16 + 40)
                elif char == '6' and previous_char == '6':
                    self.fruit_spawn = (j*16 - 8, i*16 + 48)
                previous_char = self.map[i][j]
            previous_char = None

        if self.pacman_start_spawn is None:
            print('Error: No pacman start spawn point in map config file')
        if self.fruit_spawn is None:
            print('Error: No fruit spawn point in map config file')

        # установка остальных необходимых значений

#    def get_score(self): На будущее
#        return self.score

    def get_pacman_cell(self):  # Возвращает клетку, в которой находится пакман сейчас в виде колонка, строка
        return (self.pacman.x+16) // 16, (self.pacman.y-40) // 16

    def check_eaten_grains(self):
        for i in range(31):
            for j in range(28):
                char = self.map[i][j]
                if (char == '1' or char == '3') and self.get_pacman_cell()[0] == j and self.get_pacman_cell()[1] == i:
                    if char == '1':
                        self.map[i][j] = '2'
                    elif char == '3':
                        self.map[i][j] = '4'
