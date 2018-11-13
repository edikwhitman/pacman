import pygame
import sys
from start_menu import StartMenu
from config import BLACK


def main():
    pygame.init()
    SIZE = WIDTH, HEIGHT = 448, 576
    screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
    a = StartMenu(screen)
    gameover = False

    while not gameover:                       # Основной цикл программы
        for event in pygame.event.get():      # Цикл обработки событий
            if event.type == pygame.QUIT:     # Проверка на событие выхода
                gameover = True
            elif event.type == pygame.VIDEORESIZE:
                SIZE = WIDTH, HEIGHT = event.w, event.h
                screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)

        screen.fill(BLACK)                    # Заливка черным цветом

        # ВСЕ РИСОВАНИЕ ЗДЕСЬ!!!!1111
        a.draw()
        pygame.display.flip()

        pygame.time.wait(10)                  # Ожидание 10 мсек

    sys.exit()


if __name__ == '__main__':
    main()
