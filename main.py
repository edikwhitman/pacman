import pygame
from config import SIZE
from start_menu import StartMenu
from game_class import Game


def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('PAC-MAN')

    menu = StartMenu(screen)
    game = Game(screen)

    while True:
        menu.main_loop()  # Основной цикл меню

        game.set_start_params(menu.get_map_and_textures())  # Получение карты для игры из класса menu

        game.main_loop()  # Основной цикл игры

        # Получение счета из класса игры
        # Добавление счета и выгрузка в файл
        #

        # Сцена послеигрового меню


if __name__ == '__main__':
    main()
