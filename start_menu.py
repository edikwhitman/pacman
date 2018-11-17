import pygame
import sys
import os
from button import Button
from map_class import Map
from config import HEIGHT, WIDTH


class StartMenu:
    def __init__(self, screen):
        self.screen = screen
        self.maps = []
        self.__number_of_maps = 0
        self.__map_num = 0
        self.scores = []
        self.__buttons = []
        self.__font = pygame.font.SysFont('arial', 40)

        # Start button
        self.__buttons.append(
            Button(1, 46, 350, 356, 71, 'images/ui/button_start_static.png', 'images/ui/button_start_pressed.png'))
        # Scores button
        self.__buttons.append(
            Button(2, 46, 450, 166, 47, 'images/ui/button_scores_static.png', 'images/ui/button_scores_pressed.png'))
        # Exit button
        self.__buttons.append(
            Button(3, 236, 450, 166, 47, 'images/ui/button_exit_static.png', 'images/ui/button_exit_pressed.png'))
        # Left arrow
        self.__buttons.append(
            Button(4, 100, 230, 31, 51, 'images/ui/arrow_left_static.png', 'images/ui/arrow_left_pressed.png'))
        # Right arrow
        self.__buttons.append(
            Button(5, 320, 230, 31, 51, 'images/ui/arrow_right_static.png', 'images/ui/arrow_right_pressed.png'))
        open('highscores.txt', 'a').close()  # Создает файл, если его нет (пока не надо)
        self.start_menu_image = pygame.image.load("images/ui/main_menu.png")

    def process_logic(self):
        for button in self.__buttons:
            button.logic(pygame.mouse.get_pos())

    # Отрисовка не статичных объектов (кнопки)
    def process_drawing(self):
        self.screen.fill((200, 200, 200))

        self.screen.blit(self.maps[self.__map_num].preview_img, (168, 200))  # отрисовка превью картинки

        self.screen.blit(self.start_menu_image, (0, 0))  # отрисовка картинки менюшки

        for button in self.__buttons:  # отрисовка кнопок
            button.draw(self.screen)

        text = self.__font.render(self.maps[self.__map_num].name, True, (60, 60, 255))
        text_rect = text.get_rect(center=(WIDTH / 2, 165))
        self.screen.blit(text, text_rect)

    # Обработка ивентов
    def check_event(self):
        response = None
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed_button = self.__get_pressed_button()
                if pressed_button is not None:
                    # Выход из игры
                    if pressed_button == 3:
                        pygame.quit()
                        sys.exit()
                    # Вызов меню рекордов
                    elif pressed_button == 2:
                        print('high scores menu run')
                    # Старт игры
                    elif pressed_button == 1:
                        response = 1
                    # Смена карты
                    elif pressed_button == 4:
                        self.__switch_map(-1)
                    elif pressed_button == 5:
                        self.__switch_map(1)
            elif event.type == pygame.KEYDOWN:
                # Смена карты
                if event.key == pygame.K_LEFT:
                    self.__switch_map(-1)
                elif event.key == pygame.K_RIGHT:
                    self.__switch_map(1)
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        return response

    def __get_pressed_button(self):
        for button in self.__buttons:
            if button.get_status() == 1:
                # print(button.index)
                return button.index
        return None

    """
    Работа с картами
    """

    def load_maps(self):
        files = os.listdir('maps')
        for map_ in files:
            self.maps.append(Map(map_))
        self.__number_of_maps = len(self.maps)

    def __switch_map(self, num):
        self.__map_num = (self.__map_num + num) % self.__number_of_maps

    """
    Работа с рекордами
    """

    # Выгрузка рекордов из файла в память
    def load_scores(self):
        with open('highscores.txt', 'r') as f:
            for line in f:
                self.scores.append(int(line))
        # print('loaded ', self.scores)

    # Добавление нового рекорда (только в память)
    def add_new_score(self, num):
        self.scores.append(num)
        # print('add/ added ', self.scores)
        self.scores.sort(reverse=True)
        self.scores = self.scores[:-1]
        # print('add/ sorted ', self.scores)

    # Запись всех рекодов из памяти в файл
    def write_scores(self):
        with open('highscores.txt', 'w') as f:
            for i in range(10):
                f.write('{}\n'.format(self.scores[i]))
        # print('written to file ', self.scores)
