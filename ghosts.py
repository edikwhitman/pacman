from character import AnimatedCharacter


class Ghost(AnimatedCharacter):
    def __init__(self, x, y, img, width=32, height=32, time=5):
        super().__init__(x, y, img, 2, width, height, True, time)
        self.movement_direction = 0  # 0 - стоит на месте, 1 - движется вверх, 2 - вниз, 3 - влево, 4 - вправов
        self.movement_direction_queue = 0  # 0 - стоит на месте, 1 - движется вверх, 2 - вниз, 3 - влево, 4 - вправов

    def set_dir_animation(self, name):  # Поставить нужную картинку в зависимости от направления движения
        if self.movement_direction == 1:
            self.set_animation("./images/entity/ghosts/{}_moving_up.png".format(name), 2, True, self.time*3)
        elif self.movement_direction == 2:
            self.set_animation("./images/entity/ghosts/{}_moving_down.png".format(name), 2, True, self.time*3)
        elif self.movement_direction == 3:
            self.set_animation("./images/entity/ghosts/{}_moving_left.png".format(name), 2, True, self.time*3)
        elif self.movement_direction == 4:
            self.set_animation("./images/entity/ghosts/{}_moving_right.png".format(name), 2, True, self.time*3)


class Blinky(Ghost):  # Красный
    def __init__(self, x, y, img="./images/entity/ghosts/blinky_moving_left.png"):
        super().__init__(x, y, img)


class Pinky(Ghost):  # Красный
    def __init__(self, x, y):
        super().__init__(x, y, "./images/entity/ghosts/pinky_moving_down.png")


class Inky(Ghost):  # Голубый
    def __init__(self, x, y):
        super().__init__(x, y, "./images/entity/ghosts/inky_moving_up.png")


class Clyde(Ghost):  # Оранжевый
    def __init__(self, x, y):
        super().__init__(x, y, "./images/entity/ghosts/clyde_moving_up.png")
