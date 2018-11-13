import pygame
import sys
from button import Button


class StartMenu:
    def __init__(self, screen):
        self.scores = []
        self.buttons = []
        self.buttons.append(Button(1, 46, 300, 71, 356, 'images/start_button.png', 'images/start_button_pressed.png'))  # start game
        self.buttons.append(Button(2, 46, 400, 47, 166, 'images/scores_button.png', 'images/scores_button_pressed.png'))  # scores
        self.buttons.append(Button(3, 236, 400, 47, 166, 'images/exit_button.png', 'images/exit_button_pressed.png'))  # exit
        open('highscores.txt', 'a').close()  # Создает файл, если его нет
        self.start_menu_image = pygame.image.load("images/menu.png")

    def process_logic(self):
        for button in self.buttons:
            button.logic(pygame.mouse.get_pos())

    # Отрисовка не статичных объектов (кнопки)
    def process_drawing(self, screen):
        screen.blit(self.start_menu_image, (0, 0))
        for button in self.buttons:
            button.draw(screen)

    # Обработка ивентов
    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed_button = self.get_pressed_button()
            if pressed_button == 3:
                pygame.quit()
                sys.exit()
            elif pressed_button == 2:
                print('high scores menu run')
            elif pressed_button == 1:
                print('start game')

    def get_pressed_button(self):
        for but in self.buttons:
            if but.status == 1:
                print(but.index)
                return but.index
        return None

    ###### работа с рекордами #######

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
