import pygame
import sys
from start_menu import StartMenu
from config import BLACK, WIDTH, HEIGHT, SIZE


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('PAC-MAN')
    a = StartMenu(screen)
    gameover = False

    while not gameover:  # Основной цикл программы
        for event in pygame.event.get():  # Цикл обработки событий
            if event.type == pygame.QUIT:  # Проверка на событие выхода
                pygame.quit()
                sys.exit()
            a.check_event(event)

        screen.fill(BLACK)  # Заливка черным цветом

        # ВСЕ РИСОВАНИЕ ЗДЕСЬ!!!!1111
        a.process_logic()
        a.process_drawing()

        pygame.display.flip()

        pygame.time.wait(10)  # Ожидание 10 мсек

    sys.exit()


if __name__ == '__main__':
    main()
