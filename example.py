import pygame
import sys
from pacman import Pacman

def windowCreation():
    print("Нажмите D, чтобы показать анимацию смерти")
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pacman = Pacman(100, 100, 32, 32)
    pacman.setRotation(90)  # Повернуть на 90
    gameover = False
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    pacman.setDeathAnimation()  # Показать анимацию смерти пакмена
        screen.fill((0, 0, 0))
        pacman.draw(screen)
        pygame.display.flip()
        pygame.time.wait(50)
    sys.exit()

if __name__ == '__main__':
    windowCreation()
