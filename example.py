import pygame
import sys
from start_menu import StartMenu


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    a = StartMenu(screen)
    a.start_draw()
    a.draw()
    pygame.display.flip()
    pygame.time.wait(5000)
    sys.exit()


if __name__ == '__main__':
    main()