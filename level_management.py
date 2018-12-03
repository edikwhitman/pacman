import time
from pacman import Pacman
from ghosts import Blinky, Pinky, Inky, Clyde

class LevelManagement:
    def __init__(self):
        self.time = time.time()
        self.start_time = self.time
        self.waves = 1
        self.status = 1 # 0 - преследование, 1 - разбегание, 2 - страх
        self.level = 1
        self.scatter_time = 7 # время разбегания
        self.chase_time = 20 # время преследования
        self.frightened_time = 8 # время испуга
        self.ghosts_blinking_time = 3
        self.ghosts_blinking = False


    def manage(self, map, pacman, ghosts, scores):
        if self.status == 0 and int(time.time() - self.time) >= self.chase_time:  # Разбегание
            self.time = time.time()
            self.status = (self.status + 1) % 2
        elif self.status == 1 and time.time() - self.time >= self.scatter_time:  # Преследование
            self.time = time.time()
            self.status = (self.status + 1) % 2
            self.waves += 1
        elif self.status == 2 and time.time() - self.time >= self.frightened_time:
            self.time = time.time()
            self.status = 0
            for ghost in ghosts:
                if ghost.ghost_status != 3:
                    ghost.set_scatter_img()
                    ghost.absolute_speed = ghost.normal_speed
                    if ghost.inside_ghost_house :
                        ghost.set_moving_animation(1)
        if self.status == 2 and time.time() - self.time >= self.frightened_time - self.ghosts_blinking_time:
            self.ghosts_blinking = True
        self.move(map, pacman, ghosts, scores)

    def level_control(self):
        if self.level == 0:
            if self.waves < 3:
                self.chase_time = 20
                self.scatter_time = 7
            elif self.waves == 3:
                self.scatter_time = 5
            elif self.waves > 3:
                self.chase_time = time.time() + 1

    def move(self, map, pacman, ghosts, scores):

        for ghost in ghosts:
            if self.status != 1:
                if ghost.ghost_status != 3:
                    if ghost.name == "blinky":
                        ghost.set_chase_mode(map, pacman.get_pacman_cell())
                        ghost.move(map)
                    if ghost.name == "pinky":
                        ghost.set_pinky_chase_mode(map, pacman.get_pacman_cell(), pacman.movement_direction)
                        ghost.move(map)
                    if ghost.name == "inky":
                        if scores > 300:
                            ghost.set_inky_chase_mode(map, pacman.get_pacman_cell(), pacman.movement_direction, ghosts[0].get_ghost_cell())
                            ghost.move(map)
                        elif time.time() - self.start_time > 5:
                            ghost.set_scatter_mode(map)
                            ghost.move(map)
                    if ghost.name == "clyde" and scores > 800:
                        ghost.set_clyde_chase_mode(map, pacman.get_pacman_cell())
                        ghost.move(map)
            if self.status == 1 and ghost.ghost_status != 3 :
                if ghost.name == "clyde" and scores < 800: pass
                elif ghost.name == "inky" and time.time() - self.start_time < 5: pass
                else:
                    ghost.set_scatter_mode(map)
                    ghost.move(map)
            if ghost.ghost_status == 3:
                ghost.return_to_ghost_room(map)
                ghost.move(map)
            elif self.status == 2 and ghost.ghost_status == 2:
                ghost.set_frightened_mode(map, self.ghosts_blinking)




    def frightened(self, map, pacman, ghosts, scores):
        self.ghosts_blinking = False
        for ghost in ghosts:
            if ghost.ghost_status != 3:
                ghost.set_frightened_mode(map)
                ghost.absolute_speed = ghost.frightened_speed
        self.status = 2
        self.time = time.time()


