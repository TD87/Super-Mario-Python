"""This module creates the cloud background object"""

from obstacle import Obstacle

class Cloud(Obstacle):
    """Cloud background object"""
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, matrix, mario_pos):
        diff = mario_pos - 75
        try:
            if self.x_coord-diff > 0:
                matrix[self.y_coord+1][self.x_coord-diff] = '\033[47m' + '('
                matrix[self.y_coord+2][self.x_coord-diff] = '\033[47m' + '('
            for i in range(1, 15):
                if self.x_coord+i-diff > 0:
                    if i == 14:
                        matrix[self.y_coord][self.x_coord+i-diff] = '\033[47m' + '_' + '\033[46m'
                        matrix[self.y_coord+3][self.x_coord+i-diff] = '\033[47m' + '_' + '\033[46m'
                    else:
                        matrix[self.y_coord][self.x_coord+i-diff] = '\033[47m' + '_'
                        matrix[self.y_coord+3][self.x_coord+i-diff] = '\033[47m' + '_'
                    matrix[self.y_coord+1][self.x_coord+i-diff] = '\033[47m' + ' '
                    matrix[self.y_coord+2][self.x_coord+i-diff] = '\033[47m' + ' '
            if self.x_coord+15-diff > 0:
                matrix[self.y_coord+1][self.x_coord+15-diff] = '\033[47m' + ')' + '\033[46m'
                matrix[self.y_coord+2][self.x_coord+15-diff] = '\033[47m' + ')' + '\033[46m'
        except:
            pass
