import pygame
import sys
from pacman import Pacman
from config import BLACK, WHITE
from ghosts import Blinky, Pinky, Inky, Clyde


class Game:
    def __init__(self, screen):
        self.game_loop_run = True
        self.screen = screen  # Плоскость отображения
        self.pacman_start_spawn = None
        self.fruit_spawn = None
        self.pacman = None
        self.ghosts = list()
        self.ghosts.append(Blinky(13 * 16, 11 * 16 + 48 - 8))
        self.ghosts.append(Pinky(13 * 16, 14 * 16 + 48 - 8))
        self.ghosts.append(Inky(11 * 16, 14 * 16 + 48 - 8))
        self.ghosts.append(Clyde(15 * 16, 14 * 16 + 48 - 8))
        self.grain_img = None
        self.big_grain_img = None
        self.big_grain_draw = True  # Отображаем большое зерно или нет. Чтобы мигание делать
        self.counter = 1  # Счетчик прохода по game_loop, нужен как таймер
        self.map = None  # Экземпляр класса карты, map.data - карта в виде символов (31 строка по 28 символов):
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
        self.texturepack = None  # Текущий текстурпак (экземпляр класса Texturepack)
        self.lives = 3

    def main_loop(self):
        print('game loop run')
        while self.game_loop_run:
            if self.__check_event() == 1:
                self.game_loop_run = False
            self.__process_drawing()
            self.__process_logic()

            pygame.display.flip()
            pygame.time.wait(10)
        # После конца игры
        self.map.add_new_score(self.score)
        self.map.write_scores()
        print('game loop stop')

    def __process_logic(self):
        self.pacman.move(self.map.data)
        self.check_eaten_grains()
        if self.counter % 10 == 0:  # Типа таймера, чтобы мигали не сильно часто
            if self.big_grain_draw:
                self.big_grain_draw = False
            else:
                self.big_grain_draw = True
        self.counter += 1
        if self.counter == 100:
            self.counter = 0
        if self.lives == 0:
            self.game_loop_run = False

    # Отрисовка не статичных объектов
    def __process_drawing(self):
        self.screen.fill(BLACK)
        # Очередь отрисовки:

        # 1. изображение карты map_img.png
        self.screen.blit(self.map.img, (0, 48))

        # 2. зерна и фрукты
        for i in range(31):
            for j in range(28):
                if self.map.data[i][j] == '1':
                    self.screen.blit(self.grain_img, (j * 16, (i * 16) + 48))
                elif self.map.data[i][j] == '3' and self.big_grain_draw:
                    self.screen.blit(self.big_grain_img, (j * 16, (i * 16) + 48))

        # 3. pac man
        self.pacman.draw(self.screen)

        # 4. ghosts
        for ghost in self.ghosts:
            ghost.draw(self.screen)

        # 5. scores
        font = pygame.font.Font('font.ttf', 25)

        up = font.render('1UP', True, WHITE)  # Надпись над текущим счетом
        up_rect = up.get_rect(topleft=(16*2, 0))
        self.screen.blit(up, up_rect)

        score_now = font.render(str(self.score), True, WHITE)  # Текущий счет
        sc_rect = score_now.get_rect(topleft=(16*3, 20))
        self.screen.blit(score_now, sc_rect)

        hs_txt = font.render('HIGH SCORE', True, WHITE)  # Надпись над наибольшим счетом
        hs_txt_rect = hs_txt.get_rect(topleft=(16*9, 0))
        self.screen.blit(hs_txt, hs_txt_rect)
        if not self.map.scores:
            hs = font.render(str(self.score), True, WHITE)  # Наибольший счет
        else:
            hs = font.render(str(self.map.scores[0]) if self.map.scores[0] > self.score else str(self.score),
                             True, WHITE)  # Наибольший счет
        hs_rect = hs.get_rect(topleft=(16*14, 20))
        self.screen.blit(hs, hs_rect)

        # Жизни
        live_pacman = pygame.image.load('./texturepacks/{}/pacman/pacman_stand.png'.format(self.texturepack.name))
        live_pacman = pygame.transform.rotate(live_pacman, 90)
        for i in range(self.lives):
            self.screen.blit(live_pacman, (16 * 2*(i+1) + 5*i, 34 * 16))

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
                if self.map.data[i][j] == '2':
                    self.map.data[i][j] = '1'
                elif self.map.data[i][j] == '4':
                    self.map.data[i][j] = '3'

    def set_start_params(self, arguments):
        self.map, self.texturepack = arguments
        print('loaded')

        self.pacman = Pacman(0, 0, 32, 32, 3, 3,
                             start_img_path='texturepacks/{}/pacman/pacman_stand.png'.format(self.texturepack.name))

        self.pacman_start_spawn = None
        self.fruit_spawn = None
        # Установка точки спавна PacMan'а и других необходимых элементов
        previous_char = None
        for i in range(31):
            for j in range(28):
                char = self.map.data[i][j]
                if char == '9' and previous_char == '9':
                    self.pacman_start_spawn = (j * 16 - 16, i * 16 + 40)
                elif char == '6' and previous_char == '6':
                    self.fruit_spawn = (j * 16 - 8, i * 16 + 48)
                previous_char = self.map.data[i][j]
            previous_char = None

        if self.pacman_start_spawn is None:
            print('Error: No pacman start spawn point in map config file')
        if self.fruit_spawn is None:
            print('Error: No fruit spawn point in map config file')

        # Установка текстурок из текстурпака
        self.__set_textures()
        # Установка стартовой позиции пакмана
        self.pacman.set_position(self.pacman_start_spawn[0], self.pacman_start_spawn[1])

        # установка остальных необходимых значений
        self.map.load_scores()

    def get_pacman_cell(self):  # Возвращает клетку, в которой находится пакман сейчас в виде колонка, строка
        return (self.pacman.x + 16) // 16, (self.pacman.y - 40) // 16

    def check_eaten_grains(self):
        for i in range(31):
            for j in range(28):
                char = self.map.data[i][j]
                if (char == '1' or char == '3') and self.get_pacman_cell()[0] == j and self.get_pacman_cell()[1] == i:
                    if char == '1':
                        self.map.data[i][j] = '2'
                        self.score += 10
                    elif char == '3':
                        self.map.data[i][j] = '4'

    def __set_textures(self):
        # grains
        self.grain_img = pygame.image.load('texturepacks/{}/grains/grain.png'.format(self.texturepack.name))
        self.big_grain_img = pygame.image.load('texturepacks/{}/grains/grain_big.png'.format(self.texturepack.name))
        # pacman
        self.pacman.texture_stand = 'texturepacks/{}/pacman/pacman_stand.png'.format(self.texturepack.name)
        self.pacman.texture_death = 'texturepacks/{}/pacman/pacman_death.png'.format(self.texturepack.name)
        self.pacman.texture_eat = 'texturepacks/{}/pacman/pacman_eat.png'.format(self.texturepack.name)
