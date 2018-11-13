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

    #menu_image = pygame.image.load("images/menu.png")

    while not gameover:  # Основной цикл программы
        for event in pygame.event.get():  # Цикл обработки событий
            if event.type == pygame.QUIT:  # Проверка на событие выхода
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)  # Заливка черным цветом

        # ВСЕ РИСОВАНИЕ ЗДЕСЬ!!!!1111
        a.process_logic()
        for event in pygame.event.get():
            a.check_event(event)
        a.process_drawing(screen)
        #screen.blit(menu_image, (0, 0))
        pygame.display.flip()

        pygame.time.wait(1)  # Ожидание 10 мсек

    sys.exit()


if __name__ == '__main__':
    main()
