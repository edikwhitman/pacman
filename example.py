import pygame
import sys
from pacman import Pacman


def window_creation():
    print("Нажмите D, чтобы показать анимацию смерти")
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pacman = Pacman(100, 100, 32, 32)
    pacman.set_rotation(90)  # Повернуть до 90
    hsp = 10  # Горизонтальная скорость
    vsp = 0  # Вертикальная скорость
    spd = 10  # Абсолютная скорость
    gameover = False
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_v:   # Показать анимацию смерти пакмана
                    hsp = 0
                    vsp = 0
                    pacman.set_death_animation()
                if event.key == pygame.K_w or event.key == pygame.K_UP:  # Идти вверх
                    pacman.set_rotation(0)  # Поворот изображения до 0
                    vsp = -spd
                    hsp = 0

                if event.key == pygame.K_a or event.key == pygame.K_LEFT:  # Идти влево
                    pacman.set_rotation(270)  # Поворот изображения до 270
                    vsp = 0
                    hsp = -spd

                if event.key == pygame.K_s or event.key == pygame.K_DOWN:  # Идти вниз
                    pacman.set_rotation(180)  # Поворот изображения до 180
                    vsp = spd
                    hsp = 0
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:  # Идти вправо
                    pacman.set_rotation(90)  # Поворот изображения до 90
                    vsp = 0
                    hsp = spd
        screen.fill((0, 0, 0))
        pacman.set_position(pacman.x + hsp, pacman.y + vsp)  # Изменение координат пакмана
        pacman.draw(screen)  # Вывод на экран
        pygame.display.flip()
        pygame.time.wait(50)
    sys.exit()


if __name__ == '__main__':
    window_creation()
