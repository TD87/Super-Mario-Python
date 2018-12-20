"""This module creates the platform obstacle"""

from obstacle import Obstacle

class Platform(Obstacle):
    """Plaform Obstacle"""
    def __init__(self, x, y, length):
        super().__init__(x, y)
        self._length = length

    def draw(self, matrix, mario_pos):
        diff = mario_pos - 75
        for i in range(self._length):
            if i % 2 == 0:
                try:
                    if self.x_coord+i-diff > 0:
                        matrix[self.y_coord][self.x_coord+i-diff] = '\033[41m' + "["
                        matrix[self.y_coord+1][self.x_coord+i-diff] = '\033[41m' + "["
                except:
                    pass
            else:
                try:
                    if self.x_coord+i-diff > 0:
                        if i == self._length-1:
                            matrix[self.y_coord][self.x_coord+i-diff] = '\033[41m' +"]"+ '\033[46m'
                            matrix[self.y_coord+1][self.x_coord+i-diff] = '\033[41m' +"]"+'\033[46m'
                        else:
                            matrix[self.y_coord][self.x_coord+i-diff] = '\033[41m' + "]"
                            matrix[self.y_coord+1][self.x_coord+i-diff] = '\033[41m' + "]"
                except:
                    pass

    def coord_list(self):
        platform_list = list()
        for i in range(self._length):
            platform_list.append([self.x_coord+i, self.y_coord])
            platform_list.append([self.x_coord+i, self.y_coord+1])
        return platform_list
