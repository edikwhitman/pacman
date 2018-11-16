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
        self.map_num = 0
        self.scores = []
        self.buttons = []
        self.font = pygame.font.SysFont('arial', 40)

        # Start button
        self.buttons.append(
            Button(1, 46, 350, 356, 71, 'images/ui/button_start_static.png', 'images/ui/button_start_pressed.png'))
        # Scores button
        self.buttons.append(
            Button(2, 46, 450, 166, 47, 'images/ui/button_scores_static.png', 'images/ui/button_scores_pressed.png'))
        # Exit button
        self.buttons.append(
            Button(3, 236, 450, 166, 47, 'images/ui/button_exit_static.png', 'images/ui/button_exit_pressed.png'))
        # Left arrow
        self.buttons.append(
            Button(4, 100, 230, 31, 51, 'images/ui/arrow_left_static.png', 'images/ui/arrow_left_pressed.png'))
        # Right arrow
        self.buttons.append(
            Button(5, 320, 230, 31, 51, 'images/ui/arrow_right_static.png', 'images/ui/arrow_right_pressed.png'))
        open('highscores.txt', 'a').close()  # Создает файл, если его нет (пока не надо)
        self.start_menu_image = pygame.image.load("images/ui/main_menu.png")

    def process_logic(self):
        for button in self.buttons:
            button.logic(pygame.mouse.get_pos())

    # Отрисовка не статичных объектов (кнопки)
    def process_drawing(self):
        self.screen.fill((200, 200, 200))

        self.screen.blit(self.maps[self.map_num].preview_img, (168, 200))  # отрисовка превью картинки

        self.screen.blit(self.start_menu_image, (0, 0))  # отрисовка картинки менюшки

        for button in self.buttons:  # отрисовка кнопок
            button.draw(self.screen)

        text = self.font.render(self.maps[self.map_num].name, True, (200, 200, 200))
        text_rect = text.get_rect(center=(WIDTH / 2, 165))
        self.screen.blit(text, text_rect)

    # Обработка ивентов
    def check_event(self):
        response = None
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed_button = self.get_pressed_button()
                if pressed_button is not None:
                    if pressed_button == 3:
                        pygame.quit()
                        sys.exit()
                    elif pressed_button == 2:
                        print('high scores menu run')
                    elif pressed_button == 1:
                        response = 1
                    elif pressed_button == 4:
                        self.map_num = (self.map_num - 1) % len(self.maps)
                    elif pressed_button == 5:
                        self.map_num = (self.map_num + 1) % len(self.maps)
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        return response

    def get_pressed_button(self):
        for button in self.buttons:
            if button.status == 1:
                print(button.index)
                return button.index
        return None

    ##### Табота с картами #

    def load_maps(self):
        files = os.listdir('maps')
        for map_ in files:
            self.maps.append(Map(map_))

    ##### работа с рекордами #

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
