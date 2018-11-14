import pygame


class Button:
    def __init__(self, index, x, y, height=20, width=30, static_img='images/button.png', on_pressed_img='images'
                                                                                                        '/button.jpg'):
        self.index = index
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img_static = pygame.image.load(static_img)
        self.img_on_pressed = pygame.image.load(on_pressed_img)
        self.status = 0  # 0 - курсор вне кнопки, 1- курсор на кнопке

    def draw(self, screen):
        if self.status == 0:
            screen.blit(self.img_static, (self.x, self.y))
        elif self.status == 1:
            screen.blit(self.img_on_pressed, (self.x, self.y))

    def logic(self, cur_xy):
        cur_x, cur_y = cur_xy
        if (self.x <= cur_x <= self.x + self.width) and (self.y <= cur_y <= self.y + self.height):
            self.status = 1
        else:
            self.status = 0
