from character import AnimatedCharacter
import pygame


class Pacman(AnimatedCharacter):

    def __init__(self, x, y, width, height, img_src, sprites_cnt, time=1):
        super().__init__(x, y, img_src, sprites_cnt, width, height, time)
        self.x = x
        self.y = y
        self.img_src = pygame.image.load("./images/entity/pacman/pacman_eat.png")
        self.sprites_cnt = 4
        self.sprite_width = self.img_src.get_rect().width // self.sprites_cnt
        self.sprite_height = self.img_src.get_rect().height
        self.width = width
        self.height = height
        self.angle = 0
        self.sprites = self.split_sprites(self.img_src)
        self.object = self.sprites[0]
        self.object_rect = self.sprites[0].get_rect()
        self.time = time
        self.work_time = 0
        self.skip_frame = 0
        self.frame = 0
        self.loop = True
        self.end = False
        self.set_position(self.x, self.y)
        self.animation_status = 0  # 0 - есть, 1 - анимация смерти, 2 - стоять

    def set_eat_animation(self):
        self.animation_status = 0
        self.set_animation("./images/entity/pacman/pacman_eat.png", 4)

    def set_death_animation(self):
        if not self.animation_status == 1:
            self.animation_status = 1
            self.set_animation("./images/entity/pacman/pacman_death.png", 11, 3, False)

    def set_stand_animation(self):
        self.animation_status = 2
        self.set_animation("./images/entity/pacman/pacman_stand.png", 1)
