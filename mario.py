"""This module create the player character, mario"""

from person import Person

class Mario(Person):
    """Player Object"""
    def __init__(self, x, y):
        super().__init__(x, y, 4, 3)
        self.is_jumping = 0
        self.lives = 3
        self.invulnerable = 0
        self.jump_h = 5

    def jump(self):
        """Sets mario to jumping state"""
        self.is_jumping = 1

    def draw(self, matrix):
        try:
            if self.y_coord > 0:
                matrix[self.y_coord][75] = "R"
                matrix[self.y_coord][76] = "R" + '\033[46m'
            if self.y_coord-1 > 0:
                matrix[self.y_coord-1][75] = "O"
                matrix[self.y_coord-1][76] = "O"
                matrix[self.y_coord-1][74] = "I"
                matrix[self.y_coord-1][77] = "I" + '\033[46m'
            if self.y_coord-2 > 0:
                matrix[self.y_coord-2][75] = "A"
                matrix[self.y_coord-2][76] = "A"
                matrix[self.y_coord-2][74] = "I"
                matrix[self.y_coord-2][77] = "I" + '\033[46m'
            if self.y_coord-3 > 0:
                matrix[self.y_coord-3][75] = "M"
                matrix[self.y_coord-3][76] = "M" + '\033[46m'
        except:
            pass

    def coord_list(self, xdisp=0, ydisp=0):
        """Optional xdisp and ydisp. Polymorphism"""
        mario_list = [[self.x_coord+xdisp, self.y_coord+ydisp],
                      [self.x_coord+xdisp, self.y_coord-1+ydisp],
                      [self.x_coord+xdisp, self.y_coord-2+ydisp],
                      [self.x_coord+xdisp, self.y_coord-3+ydisp],
                      [self.x_coord+1+xdisp, self.y_coord+ydisp],
                      [self.x_coord+1+xdisp, self.y_coord-1+ydisp],
                      [self.x_coord+1+xdisp, self.y_coord-2+ydisp],
                      [self.x_coord+1+xdisp, self.y_coord-3+ydisp],
                      [self.x_coord-1+xdisp, self.y_coord-1+ydisp],
                      [self.x_coord-1+xdisp, self.y_coord-2+ydisp],
                      [self.x_coord+2+xdisp, self.y_coord-1+ydisp],
                      [self.x_coord+2+xdisp, self.y_coord-2+ydisp]]
        return mario_list
