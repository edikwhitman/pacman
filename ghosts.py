import random

from character import AnimatedCharacter
import pygame


class Ghost(AnimatedCharacter):
    def __init__(self, x, y, name, scatter_point=(0, 0), width=32, height=32, ghost_room_exit_point=(13, 14), time=8):
        self.name = name
        self.img = "./images/entity/ghosts/" + self.name + "_moving.png"
        self.frightened_img = "./images/entity/ghosts/fear_moving.png"

        super().__init__(x, y, self.img, self.get_image_parts(self.img), width, height, True, time)
        self.start_x = x
        self.start_y = y
        self.returning_room = False
        self.movement_direction = 0  # 0 - стоит на месте, 1 - движется вверх, 2 - вниз, 3 - влево, 4 - вправо
        self.movement_direction_queue = 0
        self.animation_status = 0  # 0 - есть, 1 - анимация смерти, 2 - стоять
        self.vertical_speed = 0
        self.horisontal_speed = 0
        self.normal_speed = 2
        self.frightened_speed = 1
        self.absolute_speed = self.normal_speed
        self.returning_speed = 4
        self.current_cell = list
        self.ghost_room_exit_point = ghost_room_exit_point
        self.ghost_status = 0  # 0 - режим преследования, 1 - режим разбегания, 2 - режим страха, 3 - режим возвращения домой
        self.set_split_sprites_range(5, 6)
        self.inside_ghost_house = True
        self.scatter_point = scatter_point

    def set_moving_animation(self, direction):
        if self.ghost_status < 2:
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

        if self.ghost_status == 3:
            if direction == 1:
                self.set_split_sprites_range(3, 3)
            if direction == 2:
                self.movement_direction = 2
                self.set_split_sprites_range(4, 4)
            if direction == 3:
                self.movement_direction = 3
                self.set_split_sprites_range(2, 2)
            if direction == 4:
                self.movement_direction = 4
                self.set_split_sprites_range(1, 1)

    def change_direction(self, map):  # Проверка на возможность поворота
        if self.movement_direction_queue == 3 and map[(self.y + 8 - 48) // 16][(self.x - 2) // 16] != "0":
            self.movement_direction = 3
            self.movement_direction_queue = 0
        elif self.movement_direction_queue == 4 and map[(self.y + 8 - 48) // 16][(self.x + 34) // 16] != "0":
            self.movement_direction = 4
            self.movement_direction_queue = 0
        elif self.movement_direction_queue == 1 and \
                ((map[(self.y - 44) // 16][(self.x + 8) // 16] != "0" and self.movement_direction == 4)
                 or (map[(self.y - 44) // 16][(self.x + 22) // 16] != "0" and self.movement_direction == 3)):
            self.movement_direction = 1
            self.movement_direction_queue = 0
        elif self.movement_direction_queue == 2 and \
                ((map[(self.y - 10) // 16][(self.x + 8) // 16] != "0" and self.movement_direction == 4)
                 or (map[(self.y - 10) // 16][(self.x + 22) // 16] != "0" and self.movement_direction == 3)):
            self.movement_direction = 2
            self.movement_direction_queue = 0

    def check_collision(self, map):  # Проверка на столкновение со стенами
        if self.movement_direction == 3 and map[(self.y + 16 - 48) // 16][(self.x + 6) // 16] != "0":
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
        if self.ghost_status == 0:
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
        if not self.inside_ghost_house:
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
        else:
            self.ghost_room_exit(map)

    def set_chase_mode(self, map, target_position):
        try:
            pos = self.get_ghost_cell()
            minimum_distance = 1000
            direction = 0
            if map[pos[1]][pos[0] - 1] != '0' and self.get_points_distance((target_position[1], target_position[0]), (
            pos[1], pos[0] - 1)) <= minimum_distance and self.movement_direction != 4 and self.current_cell != pos:
                direction = 3
                minimum_distance = self.get_points_distance((target_position[1], target_position[0]),
                                                            (pos[1], pos[0] - 1))

            if map[pos[1]][pos[0] + 1] != '0' and self.get_points_distance((target_position[1], target_position[0]), (
            pos[1], pos[0] + 1)) <= minimum_distance and self.movement_direction != 3 and self.current_cell != pos:
                direction = 4
                minimum_distance = self.get_points_distance((target_position[1], target_position[0]),
                                                            (pos[1], pos[0] + 1))

            if map[pos[1] + 1][pos[0]] != '0' and self.get_points_distance((target_position[1], target_position[0]), (
            pos[1] + 1, pos[0])) <= minimum_distance and self.movement_direction != 1 and self.current_cell != pos:
                direction = 2
                minimum_distance = self.get_points_distance((target_position[1], target_position[0]),
                                                            (pos[1] + 1, pos[0]))

            if map[pos[1] - 1][pos[0]] != '0' and self.get_points_distance((target_position[1], target_position[0]), (
            pos[1] - 1, pos[0])) <= minimum_distance and self.movement_direction != 2 and self.current_cell != pos:
                direction = 1
                minimum_distance = self.get_points_distance((target_position[1], target_position[0]),
                                                            (pos[1] - 1, pos[0]))
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
        except IndexError:
            pass

    def ghost_room_exit(self, map):
        if self.inside_ghost_house:
            pos = self.get_ghost_cell()
            if abs((self.ghost_room_exit_point[0] * 16) - self.x) >= self.absolute_speed:
                direct = ((self.ghost_room_exit_point[0] * 16) - self.x) / abs(
                    (self.ghost_room_exit_point[0] * 16) - self.x)
                self.set_x(int(self.x + direct * self.absolute_speed))
                if direct > 0:
                    self.set_moving_animation(4)
                else:
                    self.set_moving_animation(3)
            elif self.y > (self.ghost_room_exit_point[1] - 1) * 16 + 10:
                self.set_y(self.y - self.absolute_speed)
                self.set_x((self.ghost_room_exit_point[0] * 16))
                self.set_moving_animation(1)
            else:
                self.inside_ghost_house = False
                self.movement_direction = 1
                if self.ghost_status == 2:
                    self.movement_direction = 1
                    self.set_frightened_mode(map)

    def ghost_room_enter(self, map):
        pos = self.get_ghost_cell()
        if self.y < self.start_y:
            self.set_y(self.y + self.absolute_speed)
            self.set_x((self.ghost_room_exit_point[0] * 16))
            self.set_moving_animation(2)
        elif abs(self.start_x - self.x) >= self.absolute_speed:
            direct = (self.start_x - self.x) / abs(self.start_x - self.x)
            self.set_x(int(self.x + direct * self.absolute_speed))
            if direct > 0:
                self.set_moving_animation(4)
            else:
                self.set_moving_animation(3)
        else:
            self.inside_ghost_house = True
            self.returning_room = False
            self.set_scatter_img()
            self.ghost_status = 1
            self.move(map)
            self.movement_direction == 1

    def set_scatter_mode(self, map):
        self.set_chase_mode(map, self.scatter_point)

    def set_frightened_mode(self, map, blink = False):
        self.set_frightened_img(blink)
        self.set_chase_mode(map, (random.randint(0, 50), random.randint(0, 50)))

    def set_frightened_img(self, blink=False):
        if self.ghost_status < 2:
            self.set_animation(self.frightened_img, self.get_image_parts(self.frightened_img), True, self.time)
        if blink:
            self.set_split_sprites_range(5, 8)
        else:
            self.set_split_sprites_range(5, 6)
        self.ghost_status = 2

    def set_scatter_img(self):
        if self.ghost_status > 1:
            self.set_animation(self.img, self.get_image_parts(self.img), True, self.time)
            self.ghost_status = 0

    def get_points_distance(self, p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

    def return_to_ghost_room(self, map):
        self.absolute_speed = self.returning_speed
        if self.returning_room:
            self.absolute_speed = self.normal_speed
            self.movement_direction = 0
            self.ghost_room_enter(map)

        else:
            self.set_chase_mode(map, self.ghost_room_exit_point)
            if self.ghost_status != 3:
                self.set_frightened_img()
            self.ghost_status = 3
            if self.y == 216 and abs(self.x - 208) < self.absolute_speed:
                self.returning_room = True



class Blinky(Ghost):  # Красный
    def __init__(self, x, y):
        super().__init__(x, y, "blinky", (30, -30))
        self.inside_ghost_house = False


class Pinky(Ghost):  # Розовый
    def __init__(self, x, y):
        super().__init__(x, y, "pinky", (0, 0))

    def set_pinky_chase_mode(self, map, target_position, target_direction):
        if target_direction == 1:
            self.set_chase_mode(map, (target_position[0], target_position[1] - 4))
        elif target_direction == 2:
            self.set_chase_mode(map, (target_position[0], target_position[1] + 4))
        elif target_direction == 3:
            self.set_chase_mode(map, (target_position[0] - 4, target_position[1]))
        elif target_direction == 4:
            self.set_chase_mode(map, (target_position[0] + 4, target_position[1]))
        elif target_direction == 0:
            self.set_chase_mode(map, (target_position[0], target_position[1]))


class Inky(Ghost):  # Голубой
    def __init__(self, x, y):
        super().__init__(x, y, "inky", (30, 30))

    def set_inky_chase_mode(self, map, target_position, target_direction, blinky_position):
        if target_direction == 1:
            target = (target_position[0], target_position[1] - 2)
        elif target_direction == 2:
            target = (target_position[0], target_position[1] + 2)
        elif target_direction == 3:
            target = (target_position[0] - 2, target_position[1])
        elif target_direction == 4:
            target = (target_position[0] + 2, target_position[1])
        elif target_direction == 0:
            target = (target_position[0], target_position[1])

        target = (blinky_position[0] + (target_position[0] - blinky_position[0]) * 2,
                  blinky_position[1] + (target_position[1] - blinky_position[1]) * 2)
        self.set_chase_mode(map, (target[0], target[1]))


class Clyde(Ghost):  # Оранжевый
    def __init__(self, x, y):
        super().__init__(x, y, "clyde", (0, 30))

    def set_clyde_chase_mode(self, map, target_position):
        if self.get_points_distance(self.get_ghost_cell(), target_position) > 8:
            self.set_chase_mode(map, target_position)
        else:
            self.set_scatter_mode(map)

