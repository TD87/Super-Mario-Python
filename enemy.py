"""This module creates the standard enemy"""

from person import Person

class Enemy(Person):
    """Enemy object. Moves back and forth on a fixed path.
       Can kill mario. Is killed by being jumped on."""
    def __init__(self, x, y=30):
        super().__init__(x, y, 4, 0)
        self.path_pos = 0
        self.dir = 1
        self.path_l = 9

    def draw(self, matrix, mario_pos):
        diff = mario_pos - 75
        try:
            if self.x_coord-diff > 0:
                matrix[30][self.x_coord-diff] = '\033[40m' + '<'
            if self.x_coord-diff+1 > 0:
                matrix[30][self.x_coord+1-diff] = '\033[40m' + 'T'
                matrix[29][self.x_coord+1-diff] = '\033[40m' + 'A'
            if self.x_coord-diff+2 > 0:
                matrix[30][self.x_coord+2-diff] = '\033[40m' + 'T' + '\033[46m'
                matrix[29][self.x_coord+2-diff] = '\033[40m' + 'A' + '\033[46m'
            if self.x_coord-diff+3 > 0:
                matrix[30][self.x_coord+3-diff] = '\033[40m' + '>' + '\033[46m'
        except:
            pass

    def coord_list(self):
        enemy_list = [[self.x_coord, self.y_coord], [self.x_coord+1, self.y_coord],
                      [self.x_coord+1, self.y_coord-1], [self.x_coord+2, self.y_coord],
                      [self.x_coord+2, self.y_coord-1], [self.x_coord+3, self.y_coord]]
        return enemy_list
