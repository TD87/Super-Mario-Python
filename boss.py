"""This module creates the boss enemy"""

from enemy import Enemy

class Boss(Enemy):
    """Boss enemy. Has 2 lives and chases the player with a 1
       second delay. Loses lives by being jumped on"""
    def __init__(self, x, y=30):
        super().__init__(x, y)
        self.delay = 0
        self.path_l = 19
        self.delay_var = 0
        self.lives = 2
        self.x_init = self.x_coord

    def draw(self, matrix, mario_pos):
        diff = mario_pos - 75
        try:
            if self.x_coord-1-diff > 0:
                matrix[self.y_coord-1][self.x_coord-1-diff] = '\033[40m' + "R"
                matrix[self.y_coord-2][self.x_coord-1-diff] = '\033[40m' + "R"
            if self.x_coord-diff > 0:
                matrix[self.y_coord][self.x_coord-diff] = '\033[40m' + "R"
                matrix[self.y_coord-3][self.x_coord-diff] = '\033[40m' + "M"
                matrix[self.y_coord-1][self.x_coord-diff] = '\033[40m' + "E"
                matrix[self.y_coord-2][self.x_coord-diff] = '\033[40m' + "A"
            if self.x_coord+1-diff > 0:
                matrix[self.y_coord][self.x_coord+1-diff] = '\033[40m' + "R" + '\033[46m'
                matrix[self.y_coord-1][self.x_coord+1-diff] = '\033[40m' + "D"
                matrix[self.y_coord-3][self.x_coord+1-diff] = '\033[40m' + "M" + '\033[46m'
                matrix[self.y_coord-2][self.x_coord+1-diff] = '\033[40m' + "G"
            if self.x_coord-2-diff > 0:
                matrix[self.y_coord-1][self.x_coord+2-diff] = '\033[40m' + "Y" + '\033[46m'
                matrix[self.y_coord-2][self.x_coord+2-diff] = '\033[40m' + "U" + '\033[46m'
        except:
            pass

    def coord_list(self):
        boss_list = [[self.x_coord, self.y_coord], [self.x_coord, self.y_coord-1],
                     [self.x_coord, self.y_coord-2], [self.x_coord, self.y_coord-3],
                     [self.x_coord+1, self.y_coord], [self.x_coord+1, self.y_coord-1],
                     [self.x_coord+1, self.y_coord-2], [self.x_coord+1, self.y_coord-3],
                     [self.x_coord-1, self.y_coord-1], [self.x_coord-1, self.y_coord-2],
                     [self.x_coord+2, self.y_coord-1], [self.x_coord+2, self.y_coord-2]]
        return boss_list
