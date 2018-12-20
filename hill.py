"""This module creates the hill background object"""

from obstacle import Obstacle

class Hill(Obstacle):
    """Hill background object"""
    def __init__(self, x, size):
        super().__init__(x, 30)
        self._size = size

    def draw(self, matrix, mario_pos):
        diff = mario_pos - 75
        try:
            for i in range(self._size):
                if self.x_coord+i-diff > 0:
                    matrix[self.y_coord-i][self.x_coord+i-diff] = '\033[43m' + '/'
                    for y_coord in range(self.y_coord-i+1, self.y_coord+1):
                        matrix[y_coord][self.x_coord+i-diff] = '\033[43m' + ' '
            for i in range(self._size):
                if self.x_coord+i+self._size-diff > 0:
                    matrix[self.y_coord-self._size+1+i][self.x_coord+i+self._size-diff] = '\\' + '\033[46m'
                    for y_coord in range(self.y_coord-self._size+i+2, self.y_coord+1):
                        matrix[y_coord][self.x_coord+i+self._size-diff] = '\033[43m' + ' '
        except:
            pass
