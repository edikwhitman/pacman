import pygame


class Button:
    def __init__(self, index, x, y, width, height, static_img, on_pressed_img):
        self.index = index
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__img_static = pygame.image.load(static_img)
        self.__img_on_pressed = pygame.image.load(on_pressed_img)
        self.__status = 0  # 0 - курсор вне кнопки, 1 - курсор на кнопке, 2 - кнопка нажата

    def draw(self, screen):
        if self.__status == 0:
            screen.blit(self.__img_static, (self.__x, self.__y))
        elif self.__status == 1 or self.__status == 2:
            screen.blit(self.__img_on_pressed, (self.__x, self.__y))

    def logic(self, cur_xy):
        cur_x, cur_y = cur_xy
        if (self.__x <= cur_x <= self.__x + self.__width) and (self.__y <= cur_y <= self.__y + self.__height):
            self.__status = 1
        else:
            self.__status = 0

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status
