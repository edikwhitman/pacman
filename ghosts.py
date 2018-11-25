from character import AnimatedCharacter


class Ghost(AnimatedCharacter):
    def __init__(self, x, y, width=16, height=16, time=1):
        super().__init__(x, y, "", 2, width, height, True, time)
        self.movement_direction = 0  # 0 - стоит на месте, 1 - движется вверх, 2 - вниз, 3 - влево, 4 - вправов
        self.movement_direction_queue = 0  # 0 - стоит на месте, 1 - движется вверх, 2 - вниз, 3 - влево, 4 - вправов

    def set_dir_animation(self, name):  # Поставить нужную картинку в зависимости от направления движения
        if self.movement_direction == 1:
            self.set_animation("./images/entity/ghosts/{}_moving_up".format(name), 2, True, self.time*3)
        elif self.movement_direction == 2:
            self.set_animation("./images/entity/ghosts/{}_moving_down".format(name), 2, True, self.time*3)
        elif self.movement_direction == 3:
            self.set_animation("./images/entity/ghosts/{}_moving_left".format(name), 2, True, self.time*3)
        elif self.movement_direction == 4:
            self.set_animation("./images/entity/ghosts/{}_moving_right".format(name), 2, True, self.time*3)


class Blinky(Ghost):  # Красный
    def ___init__(self, x, y):
        super().__init__(x, y)
        super().set_image("./images/entity/ghosts/blinky_moving_left")


class Pinky(Ghost):  # Красный
    def ___init__(self, x, y):
        super().__init__(x, y)
        super().set_image("./images/entity/ghosts/pinky_moving_down")


class Inky(Ghost):  # Голубый
    def ___init__(self, x, y):
        super().__init__(x, y)
        super().set_image("./images/entity/ghosts/inky_moving_up")


class Clyde(Ghost):  # Оранжевый
    def ___init__(self, x, y):
        super().__init__(x, y)
        super().set_image("./images/entity/ghosts/clyde_moving_up")
