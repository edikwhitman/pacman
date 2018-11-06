#!/usr/bin/env python

import pygame
import sys

from game import Game


def main():
    pygame.init()  # Инициализация библиотеки
    pygame.font.init()  # Инициализация библиотеки для работы с текстом
    g = Game()
    g.main_loop()
    sys.exit()


if __name__ == "__main__":
    main()
