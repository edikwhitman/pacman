import pygame
from random import randint


class MovingObject:
    def ___init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.direction = randint(0, 4)  # 0 - left, 1 - up, 2 - right, 3 - down


class Ghost1(MovingObject):
    def ___init__(self, x=0, y=0):
        super().__init__(x, y)
        self.image = pygame.image.load("")
        self.rect = self.image.get_rect()

    def move(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Ghost2(MovingObject):
    def ___init__(self, x=0, y=0):
        super().__init__(x, y)
        self.image = pygame.image.load("")
        self.rect = self.image.get_rect()

    def move(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Ghost3(MovingObject):
    def ___init__(self, x=0, y=0):
        super().__init__(x, y)
        self.image = pygame.image.load("")
        self.rect = self.image.get_rect()

    def move(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Ghost4(MovingObject):
    def ___init__(self, x=0, y=0):
        super().__init__(x, y)
        self.image = pygame.image.load("")
        self.rect = self.image.get_rect()

    def move(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
