from character import AnimatedCharacter


class Ghost(AnimatedCharacter):
    def __init__(self, x, y, name, width=32, height=32, time=5):
        self.name = name
        super().__init__(x, y, "./images/entity/ghosts/" + self.name + "_moving.png", 8, width, height, True, time)
        self.set_moving_up_animation()
        self.movement_direction = 0  # 0 - стоит на месте, 1 - движется вверх, 2 - вниз, 3 - влево, 4 - вправо

    def set_moving_up_animation(self):
        self.movement_direction = 1
        self.set_split_sprites_range(5, 6)

    def set_moving_down_animation(self):
        self.movement_direction = 2
        self.set_split_sprites_range(7, 8)

    def set_moving_left_animation(self):
        self.movement_direction = 3
        self.set_split_sprites_range(3, 4)

    def set_moving_right_animation(self):
        self.movement_direction = 4
        self.set_split_sprites_range(1, 2)


class Blinky(Ghost):  # Красный
    def __init__(self, x, y):
        super().__init__(x, y, "blinky")


class Pinky(Ghost):  # Красный
    def __init__(self, x, y):
        super().__init__(x, y, "pinky")


class Inky(Ghost):  # Голубый
    def __init__(self, x, y):
        super().__init__(x, y, "inky")


class Clyde(Ghost):  # Оранжевый
    def __init__(self, x, y):
        super().__init__(x, y, "clyde")
