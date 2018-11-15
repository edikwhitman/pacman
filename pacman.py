from character import AnimatedCharacter
from character import Character
import pygame

class Pacman(AnimatedCharacter):

    def __init__(self, x, y, width, height, time=1):
        self.x = x
        self.y = y
        self.img_src = pygame.image.load("./images/pacman_eat.png")
        self.sprites_cnt = 4
        self.sprite_width = self.img_src.get_rect().width // self.sprites_cnt
        self.sprite_height = self.img_src.get_rect().height
        self.width = width
        self.height = height
        self.angle = 0
        self.sprites = self.splitSprites(self.img_src)
        self.object = self.sprites[0]
        self.object_rect = self.sprites[0].get_rect()
        self.time = time
        self.work_time = 0
        self.skip_frame = 0
        self.frame = 0
        self.loop = True
        self.end = False
        self.setPosition(self.x, self.y)
        self.anim_status = 0  # 0 - есть, 1 - анимация смерти, 2 - стоять

    def setEatAnimation(self):
        self.anim_status = 0
        self.setAnimation("./images/pacman_eat.png", 4)

    def setDeathAnimation(self):
        if not self.anim_status == 1:
            self.anim_status = 1
            self.setAnimation("./images/pacman_death.png", 11, 3, False)

    def setStandAnimation(self):
        self.anim_status = 2
        self.setAnimation("./images/pacman_stand.png", 1)