import pygame
import sys
from pacman import Pacman
from config import BLACK


class Game:
    def __init__(self, screen):
        self.screen = screen  # Плоскость отображения
        self.map_img = 0
        self.pacman_start_spawn = None
        self.fruit_spawn = None
        # self.image_pac = pygame.image.load('images/entity/pacman_stand.png')
        self.pacman = Pacman(0, 0, 32, 32, 3)
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
        self.score = 0

        self.hsp = 0  # Горизонтальная скорость
        self.vsp = 0  # Вертикальная скорость
        self.spd = 3  # Абсолютная скорость

    def main_loop(self):
        self.pacman.set_position(self.pacman_start_spawn[0], self.pacman_start_spawn[1])
        print('game loop run')
        game_loop_run = True
        while game_loop_run:  # Сцена меню
            self.__process_logic()
            if self.__check_event() == 1:
                game_loop_run = False
            self.__process_drawing()

            #pygame.draw.circle(self.screen, (0, 255, 0), ((self.pacman.x + 16) // 16 * 16, (self.pacman.y+54) // 16 * 16), 1)

            if self.pacman.movement_direction_queue == 3 and self.map[(self.pacman.y + 16 - 48) // 16][(self.pacman.x -2) // 16] != "0":
                self.pacman.movement_direction = 3

            if self.pacman.movement_direction_queue == 4 and self.map[(self.pacman.y + 16 - 48) // 16][(self.pacman.x + 34) // 16] != "0":
                self.pacman.movement_direction = 4

            if self.pacman.movement_direction_queue == 1 and self.map[(self.pacman.y - 34) // 16][(self.pacman.x + 16) // 16] != "0":
                self.pacman.movement_direction = 1

            if self.pacman.movement_direction_queue == 2 and self.map[(self.pacman.y - 30) // 16][(self.pacman.x + 16) // 16] != "0":
                self.pacman.movement_direction = 2

            # --------------------COLLISION---------------------
            if self.pacman.movement_direction == 3 and self.map[(self.pacman.y + 16 - 48) // 16][(self.pacman.x + 6) // 16] != "0":
                self.pacman.set_rotation(270)  # Поворот изображения до 270
                self.vsp = 0
                self.hsp = -self.spd
            elif self.pacman.movement_direction == 4 and self.map[(self.pacman.y + 16 - 48) // 16][(self.pacman.x + 26) // 16] != "0":
                self.pacman.set_rotation(90)  # Поворот изображения до 90
                self.vsp = 0
                self.hsp = self.spd
            elif self.pacman.movement_direction == 1 and self.map[(self.pacman.y - 42) // 16][(self.pacman.x + 16) // 16] != "0":
                self.pacman.set_rotation(0)  # Поворот изображения до 0
                self.vsp = -self.spd
                self.hsp = 0
            elif self.pacman.movement_direction == 2 and self.map[(self.pacman.y - 22) // 16][(self.pacman.x + 16) // 16] != "0":
                self.pacman.set_rotation(180)  # Поворот изображения до 180
                self.vsp = self.spd
                self.hsp = 0
            else:
                print("Collision")
                self.hsp = 0
                self.vsp = 0



            print((self.pacman.x) // 16, (self.pacman.y - 8) // 16, self.map[(self.pacman.y - 16) // 16][self.pacman.x // 16])



            pygame.display.flip()
            pygame.time.wait(10)
        print('game loop stop')

    def __process_logic(self):
        self.pacman.set_position(self.pacman.x + self.hsp, self.pacman.y + self.vsp)  # Изменение координат пакмана

    # Отрисовка не статичных объектов (кнопки)
    def __process_drawing(self):
        self.screen.fill(BLACK)
        # Очередь отрисовки:

        # 1. изображение карты map_img.png
        self.screen.blit(self.map_img, (0, 48))

        # 2. зерна и фрукты
        for i in range(31):
            for j in range(28):
                #pygame.draw.circle(self.screen, (255, 0, 0),  (j * 16, i * 16 + 48), 1) #  ------------------------------Отладка------------------------------
                if self.map[i][j] == '1':
                    self.screen.blit(self.grain_img, (j * 16, (i * 16) + 48))
                elif self.map[i][j] == '3':
                    self.screen.blit(self.big_grain_img, (j * 16, (i * 16) + 48))

        # 3. pac man
        self.pacman.draw(self.screen)

        # 4. ghosts
        # for ghost in self.ghosts:
        #     ghost.draw()git
        # 5. scores
        #

    # Обработка ивентов
    def __check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_v:  # Показать анимацию смерти пакмана
                    self.hsp = 0
                    self.vsp = 0
                    self.pacman.set_death_animation()
                elif event.key == pygame.K_w or event.key == pygame.K_UP:  # Идти вверх
                    self.pacman.movement_direction_queue = 1
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:  # Идти влево
                    self.pacman.movement_direction_queue = 3
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:  # Идти вниз
                    self.pacman.movement_direction_queue = 2
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:  # Идти вправо
                    self.pacman.movement_direction_queue = 4

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
                    self.pacman_start_spawn = (j*16 - 8 - 8, i*16 + 48 - 8)
                elif char == '6' and previous_char == '6':
                    self.fruit_spawn = (j*16 - 8, i*16 + 48)
                previous_char = self.map[i][j]
            previous_char = None

        if self.pacman_start_spawn is None:
            print('Error: No pacman start spawn point in map config file')
        if self.fruit_spawn is None:
            print('Error: No fruit spawn point in map config file')

        # установка остальных необходимых значений

    def get_score(self):
        return self.score
