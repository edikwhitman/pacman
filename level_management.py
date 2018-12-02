import time
from pacman import Pacman
from ghosts import Blinky, Pinky, Inky, Clyde


class LevelManagement:
    def __init__(self):
        self.time = time.time()
        self.start_time = self.time
        self.waves = 1
        self.status = 1  # 0 - преследование, 1 - разбегание, 2 - страх
        self.level = 1
        self.scatter_time = 7  # время разбегания
        self.chase_time = 20   # время преследования

    def manage(self, map, pacman, ghosts, scores):
        if self.status == 0 and int(time.time() - self.time) >= self.chase_time:  # Разбегание
            self.time = time.time()
            self.status = (self.status + 1) % 2
        elif self.status == 1 and time.time() - self.time >= self.scatter_time:  # Преследование
            self.time = time.time()
            self.status = (self.status + 1) % 2
            self.waves += 1
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
        if self.status == 0:
            ghosts[0].set_chase_mode(map, pacman.get_pacman_cell())
            ghosts[0].move(map)
            ghosts[1].set_pinky_chase_mode(map, pacman.get_pacman_cell(), pacman.movement_direction)
            ghosts[1].move(map)
            if scores > 300:
                ghosts[2].set_inky_chase_mode(map, pacman.get_pacman_cell(), pacman.movement_direction,
                                              ghosts[0].get_ghost_cell())
                ghosts[2].move(map)
            else:
                if time.time() - self.start_time > 5:
                    ghosts[2].set_scatter_mode(map)
                    ghosts[2].move(map)
            if scores > 800:
                ghosts[3].set_clyde_chase_mode(map, pacman.get_pacman_cell())
                ghosts[3].move(map)
        elif self.status == 1:
            for ghost in ghosts:
                if ghost.name == "clyde" and scores < 800:
                    pass
                elif ghost.name == "inky" and time.time() - self.start_time < 5:
                    pass
                else:
                    ghost.set_scatter_mode(map)
                    ghost.move(map)




