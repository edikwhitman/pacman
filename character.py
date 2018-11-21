import pygame


class Character():  # Статичный персонаж
    def __init__(self, x, y, img_src, width, height):  # x, y - координаты, img_src - спрайт
        self.x = x
        self.y = y
        self.object = pygame.image.load(img_src)
        self.object_rect = self.object.get_rect()
        self.width = width
        self.height = height
        self.angle = 0
        self.setPosition(self.x, self.y)

    def setX(self, x):  # Задать координату X
        self.x = x
        self.object_rect.x = self.x

    def setY(self, y):  # Задать координату Y
        self.y = y
        self.object_rect.y = self.y

    def setPosition(self, x, y):  # Задать координаты X и Y
        self.setX(x)
        self.setY(y)

    def setWidth(self, width):  # Задать ширину
        self.width = width
        self.setSize(self.width, self.height)

    def setHeight(self, height):  # Задать высоту
        self.height = height
        self.setSize(self.width, self.height)

    def setSize(self, width, height):  # Задать ширину и высоту
        self.width = width
        self.height = height
        self.object = pygame.transform.scale(self.object, (self.width, self.height))

    def setRotation(self, angle):  # Задать угол поворота (только 0, 90, 180, 270 градусов, ибо растровая картинка)
        self.object = pygame.transform.rotate(self.object, -self.angle)
        self.object = pygame.transform.rotate(self.object, -angle + self.angle)
        self.angle += angle - self.angle

    def getRotation(self):  # Вернуть угол поворота
        return self.angle

    def setImage(self, img_src, width=None, height=None):  # Задать изображение спрайта
        self.object = pygame.image.load(img_src)
        self.object_rect = self.object.get_rect()

    def draw(self, screen):  # Вывод на экран
        screen.blit(self.object, self.object_rect)


class AnimatedCharacter(Character):  # Анимированный персонаж
    def __init__(self, x, y, img_src, sprites_cnt, width, height, time=1,
                 loop=True):  # img_src - изображение с набором спрайтов (без отступов, в один ряд), sprites_cnt - количество спрайтов, loop - зацикливание анимации, time - время анимации
        self.x = x
        self.y = y
        self.img_src = pygame.image.load(img_src)
        self.sprite_width = self.img_src.get_rect().width // sprites_cnt
        self.sprite_height = self.img_src.get_rect().height
        self.sprites_cnt = sprites_cnt
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
        self.loop = loop
        self.end = False
        self.setPosition(self.x, self.y)

    def splitSprites(self, img_src, sprites_cnt = None, first_sprite = 0, last_sprite = -1):  # Разделение изображения img_src на спрайты
        if not sprites_cnt == None: self.sprites_cnt = sprites_cnt
        if last_sprite == -1: last_sprite = self.sprites_cnt

        sprites = []
        for c in range(first_sprite, last_sprite):
            sprites.append(img_src.subsurface((c * self.sprite_width, 0, self.sprite_width, self.sprite_height)))
        return sprites

    def update(self, dt):  # Обновление кадров анимации
        self.work_time += dt
        self.skip_frame = self.work_time // self.time
        if self.skip_frame > 0:
            self.work_time = self.work_time % self.time
            self.frame += self.skip_frame
            if self.frame >= len(self.sprites):
                if self.loop:
                    self.frame = 0
                else:
                    self.end = True

    def getSprite(self):  # Вернуть спрайт
        return self.sprites[self.frame]

    def setTime(self, time):  # Задать время для анимации
        self.time = time

    def setAnimation(self, img_src, sprites_cnt, time = 1, loop = True):  # Задать изображение со спрайтами
        self.img_src = pygame.image.load(img_src)
        self.sprite_width = self.img_src.get_rect().width // sprites_cnt
        self.sprite_height = self.img_src.get_rect().height
        self.sprites_cnt = sprites_cnt
        self.time = time
        self.work_time = 0
        self.skip_frame = 0
        self.frame = 0
        self.loop = loop
        self.sprites = self.splitSprites(self.img_src)

    def setSplitSpritesRange(self, first_sprite, last_sprite):  # Задать диапазон для разделения спрайтов
        self.sprites_cnt = last_sprite - first_sprite - 1
        self.sprites = self.splitSprites(self.img_src, self.sprites_cnt, first_sprite - 1, last_sprite)

    def draw(self, screen, upd_time = 1):  # Вывод на экран
        if not self.end:
            self.object = self.getSprite()
            self.update(upd_time)
            self.setRotation(self.angle)
            screen.blit(pygame.transform.scale(self.object, (self.width, self.height)), self.object_rect)