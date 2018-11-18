import pygame
from config import SIZE
from start_menu import StartMenu


def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('PAC-MAN')

    menu = StartMenu(screen)

    menu.load_maps()
    # Выгрузка рекордов всех карт

    while True:
        main_menu_loop_run = True

        while main_menu_loop_run:  # Сцена меню
            menu.process_logic()
            if menu.check_event() == 1:
                main_menu_loop_run = False
            menu.process_drawing()

            pygame.display.flip()
            pygame.time.wait(10)

        # game_loop_run = True
        # Получение карты для игры из класса menu

        # Сцена игры

        # Получение счета из класса игры
        # Добавление счета и выгрузка в файл
        #

        # Сцена послеигрового меню


if __name__ == '__main__':
    main()
