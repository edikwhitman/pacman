import pygame
from config import SIZE
from start_menu import StartMenu
from game_class import Game
from after_game_menu import Gameover


def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('PAC-MAN')
    response = None

    while True:
        menu = StartMenu(screen)
        game = Game(screen)
        if response != 1:
            menu.main_loop()  # Основной цикл меню

        game.set_start_params(menu.get_map_and_textures())  # Получение карты для игры из класса menu

        game.main_loop()  # Основной цикл игры

        after_game = Gameover(game.score, screen)  # Сцена послеигрового меню
        response = after_game.main_loop()


if __name__ == '__main__':
    main()
