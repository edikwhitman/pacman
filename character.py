import pygame


class Character():  # Статичный персонаж
    def __init__(self, x, y, img_src, width=None, height=None):  # x, y - координаты, img_src - спрайт
        self.x = x
        self.y = y
        self.object = pygame.image.load(img_src)
        self.object_rect = self.object.get_rect()
        self.width = width
        self.height = height
        self.angle = 0

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
    def __init__(self, x, y, img_src, sprite_width, sprite_height, columns, width=None, height=None, time=1,
                 loop=True):  # img_src - изображение с набором спрайтов (без отступов, в одну строку), sprite_width и sprite_height - ширина и высота спрайтов соответственно, columns - количество спрайтов
        self.x = x
        self.y = y
        self.img_src = pygame.image.load(img_src)
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height
        self.columns = columns
        self.width = width
        self.height = height
        self.angle = 0
        self.sprites = self.splitSprites(self.img_src, self.columns, self.sprite_width, self.sprite_height)
        self.object = self.sprites[0]
        self.object_rect = self.sprites[0].get_rect()
        self.time = time
        self.work_time = 0
        self.skip_frame = 0
        self.frame = 0
        self.loop = loop
        self.end = False

    def splitSprites(self, img_src, columns, sprite_width, sprite_height):  # Разделение изображения img_src на спрайты
        sprites = []
        for c in range(columns):
            sprites.append(img_src.subsurface((c * sprite_width, 0, sprite_width, sprite_height)))
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
        self.object = self.sprites[self.frame]
        return self.sprites[self.frame]

    def setTime(self, time):  # Задать время для анимации
        self.time = time

    def setAnimation(self, img_src, sprite_width, sprite_height, columns, time,
                     loop):  # Задать изображение со спрайтами
        self.img_src = pygame.image.load(img_src)
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height
        self.columns = columns
        self.time = time
        self.work_time = 0
        self.skip_frame = 0
        self.frame = 0
        self.loop = loop
        self.sprites = self.splitSprites(self.img_src, columns, sprite_width, sprite_height)

    def draw(self, screen):  # Вывод на экран
        if self.end == False:
            self.object = self.getSprite()
            self.update(1)
            self.setRotation(self.angle)
            screen.blit(pygame.transform.scale(self.object, (self.width, self.height)), self.object_rect)
