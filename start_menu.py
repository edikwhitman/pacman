import pygame
import sys

from config import BLACK


class StartMenu:
    def __init__(self, screen):
        self.scores = []
        self.screen = screen
        open('highscores.txt', 'a').close()  # Создает файл, если его нет

# Возвращает номер кнопки на которую наведен курсор: 0-new game; 1-highscores menu; 2-exit или None
    def cur_in_button(self, mouse_x, mouse_my):
        return None

# Отрисовка не статичных объектов (кнопки)
    def draw(self, surface):
        pass

# Стартовая отрисовка меню (отрисовка статичных объектов)
    def start_draw(self, surface):
        self.screen.fill(BLACK)

# Обработка ивентов
    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            num = self.cur_in_button(pygame.mouse.get_pos())
            if num == 0: # новая игра
                pass
            elif num == 1: # меню рекордов
                pass
            elif num == 2: # выход из игры
                pygame.quit()
                sys.exit()

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
