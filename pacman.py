from character import AnimatedCharacter


class Pacman(AnimatedCharacter):
    def __init__(self, x, y, width, height, time=1):
        super().__init__(x, y, "./images/entity/pacman_eat.png", 4, width, height, True, time)
        self.movement_direction = 0  # 0 - стоит на месте, 1 - движется вверх, 2 - вниз, 3 - влево, 4 - вправов
        self.movement_direction_queue = 0  # 0 - стоит на месте, 1 - движется вверх, 2 - вниз, 3 - влево, 4 - вправов
        self.animation_status = 0  # 0 - есть, 1 - анимация смерти, 2 - стоять

    def set_eat_animation(self):
        if not self.animation_status == 0:
            self.animation_status = 0
            self.set_animation("./images/entity/pacman_eat.png", 4, True, self.time*3)

    def set_death_animation(self):
        if not self.animation_status == 1:
            self.animation_status = 1
            self.set_animation("./images/entity/pacman_death.png", 11, False, self.time * 3)

    def set_stand_animation(self):
        self.animation_status = 2
        self.set_animation("./images/entity/pacman_stand.png", 1)


