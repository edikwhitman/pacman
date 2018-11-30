from character import AnimatedCharacter
import pygame


class Ghost(AnimatedCharacter):
    def __init__(self, x, y, name, scatter_point = (0, 0), width=32, height=32, time=5):
        self.name = name
        super().__init__(x, y, "./images/entity/ghosts/" + self.name + "_moving.png", 8, width, height, True, time)
        self.movement_direction = 0  # 0 - стоит на месте, 1 - движется вверх, 2 - вниз, 3 - влево, 4 - вправо
        self.movement_direction_queue = 0
        self.animation_status = 0  # 0 - есть, 1 - анимация смерти, 2 - стоять
        self.vertical_speed = 0
        self.horisontal_speed = 0
        self.absolute_speed = 3
        self.current_cell = list
        self.scatter_point = scatter_point

    def set_moving_animation(self, direction):
        if direction == 1:
            self.movement_direction = 1
            self.set_split_sprites_range(5, 6)
        if direction == 2:
            self.movement_direction = 2
            self.set_split_sprites_range(7, 8)
        if direction == 3:
            self.movement_direction = 3
            self.set_split_sprites_range(3, 4)
        if direction == 4:
            self.movement_direction = 4
            self.set_split_sprites_range(1, 2)

    def change_direction(self, map):  # Проверка на возможность поворота
        if self.movement_direction_queue == 3 and map[(self.y + 16 - 48) // 16][(self.x - 2) // 16] != "0":
            self.movement_direction = 3
            self.movement_direction_queue = 0
        elif self.movement_direction_queue == 4 and map[(self.y + 16 - 48) // 16][(self.x + 34) // 16] != "0":
            self.movement_direction = 4
            self.movement_direction_queue = 0
        elif self.movement_direction_queue == 1 and map[(self.y - 44) // 16][(self.x + 16) // 16] != "0":
            self.movement_direction = 1
            self.movement_direction_queue = 0
        elif self.movement_direction_queue == 2 and map[(self.y - 10) // 16][(self.x + 16) // 16] != "0":
            self.movement_direction = 2
            self.movement_direction_queue = 0

    def check_collision(self, map):  # Проверка на столкновение со стенами
        if self.movement_direction == 3 and map[(self.y + 16 - 48) // 16][(self.x+6) // 16] != "0":
            self.set_y(self.y // 16 * 16 + 8)
            self.vertical_speed = 0
            self.horisontal_speed = -self.absolute_speed
        elif self.movement_direction == 4 and map[(self.y + 16 - 48) // 16][(self.x + 26) // 16] != "0":
            self.set_y(self.y // 16 * 16 + 8)
            self.vertical_speed = 0
            self.horisontal_speed = self.absolute_speed
        elif self.movement_direction == 1 and map[(self.y - 42) // 16][(self.x + 16) // 16] != "0":
            self.set_x(self.x // 16 * 16 + 8)
            self.vertical_speed = -self.absolute_speed
            self.horisontal_speed = 0
        elif self.movement_direction == 2 and map[(self.y - 24) // 16][(self.x + 16) // 16] != "0":
            self.set_x(self.x // 16 * 16 + 8)
            self.vertical_speed = self.absolute_speed
            self.horisontal_speed = 0

    def check_event(self, event):  # Проверка событий
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:  # Идти вверх
                self.movement_direction = 1
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:  # Идти влево
                self.movement_direction = 3
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:  # Идти вниз
                self.movement_direction = 2
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:  # Идти вправо
                self.movement_direction = 4

    def position_logic(self):  # Изменение положения пакмана с учётом телепортов
        if self.x > 448:
            self.set_position(-self.width, self.y + self.vertical_speed)
        if self.x < -self.width:
            self.set_position(440, self.y + self.vertical_speed)
        elif self.movement_direction > 0:
            self.set_position(self.x + self.horisontal_speed, self.y + self.vertical_speed)

    def get_ghost_cell(self):
        return (self.x + 16) // 16, (self.y - 40) // 16

    def move(self, map):  # Движение
        try:
            self.change_direction(map)
        except IndexError:
            pass
        try:
            self.check_collision(map)
        except IndexError:
            pass
        self.position_logic()
        self.set_moving_animation(self.movement_direction)

    def set_chase_mode(self, map, target_position):
        try:
            pos = self.get_ghost_cell()
            minimum_distance = 1000
            direction = 0
            if map[pos[1]][pos[0]-1] != '0' and self.get_points_distance((target_position[1], target_position[0]), (pos[1], pos[0] - 1)) <= minimum_distance and self.movement_direction != 4 and self.current_cell != pos:
                direction = 3
                minimum_distance = self.get_points_distance((target_position[1], target_position[0]), (pos[1], pos[0] - 1))

            if map[pos[1]][pos[0]+1] != '0' and self.get_points_distance((target_position[1], target_position[0]), (pos[1], pos[0] + 1)) <= minimum_distance and self.movement_direction != 3 and self.current_cell != pos:
                direction = 4
                minimum_distance = self.get_points_distance((target_position[1], target_position[0]), (pos[1], pos[0] + 1))

            if map[pos[1]+1][pos[0]] != '0' and self.get_points_distance((target_position[1], target_position[0]), (pos[1] + 1, pos[0])) <= minimum_distance and self.movement_direction != 1 and self.current_cell != pos:
                direction = 2
                minimum_distance = self.get_points_distance((target_position[1], target_position[0]), (pos[1] + 1, pos[0]))

            if map[pos[1]-1][pos[0]] != '0' and self.get_points_distance((target_position[1], target_position[0]), (pos[1] - 1, pos[0])) <= minimum_distance and self.movement_direction != 2 and self.current_cell != pos:
                direction = 1
                minimum_distance = self.get_points_distance((target_position[1], target_position[0]), (pos[1] - 1, pos[0]))
            if direction > 0:
                self.current_cell = pos
                if self.movement_direction == 0:
                    self.movement_direction_queue = direction
                if self.movement_direction == 1 and direction != 2:
                    self.movement_direction_queue = direction
                if self.movement_direction == 2 and direction != 1:
                    self.movement_direction_queue = direction
                if self.movement_direction == 3 and direction != 4:
                    self.movement_direction_queue = direction
                if self.movement_direction == 4 and direction != 3:
                    self.movement_direction_queue = direction
        except IndexError:pass

    def set_scatter_mode(self, map):
        self.set_chase_mode(map, self.scatter_point)

    def get_points_distance(self, p1, p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

class Blinky(Ghost):  # Красный
    def __init__(self, x, y):
        super().__init__(x, y, "blinky", (30, -30))


class Pinky(Ghost):  # Розовый
    def __init__(self, x, y):
        super().__init__(x, y, "pinky", (0, 0))


class Inky(Ghost):  # Голубой
    def __init__(self, x, y):
        super().__init__(x, y, "inky", (30, 30))


class Clyde(Ghost):  # Оранжевый
    def __init__(self, x, y):
        super().__init__(x, y, "clyde", (0, 30))
