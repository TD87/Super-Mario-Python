"""This module creates the pipe obstacle"""

from obstacle import Obstacle

class Pipe(Obstacle):
    """Pipe Obstacle"""
    def __init__(self, x, height):
        super().__init__(x, 30)
        self._height = height

    def draw(self, matrix, mario_pos):
        diff = mario_pos - 75
        for i in range(self._height):
            try:
                if self.x_coord-diff > 0:
                    matrix[self.y_coord-i][self.x_coord-diff] = '\033[42m' + '{'
                if self.x_coord+1-diff > 0:
                    matrix[self.y_coord-i][self.x_coord+1-diff] = '\033[42m' + '}'
                if self.x_coord+2-diff > 0:
                    matrix[self.y_coord-i][self.x_coord+2-diff] = '\033[42m' + ' '
                if self.x_coord+3-diff > 0:
                    matrix[self.y_coord-i][self.x_coord+3-diff] = '\033[42m' + ' '
                if self.x_coord+4-diff > 0:
                    matrix[self.y_coord-i][self.x_coord+4-diff] = '\033[42m' + '{'
                if self.x_coord+5-diff > 0:
                    matrix[self.y_coord-i][self.x_coord+5-diff] = '\033[42m' + '}' + '\033[46m'
            except:
                pass
        try:
            if self.x_coord+2-diff > 0:
                matrix[self.y_coord-self._height+1][self.x_coord+2-diff] = '\033[42m' + '{'
            if self.x_coord+3-diff > 0:
                matrix[self.y_coord-self._height+1][self.x_coord+3-diff] = '\033[42m' + '}'
        except:
            pass

    def coord_list(self):
        pipe_list = list()
        for i in range(self._height):
            pipe_list.append([self.x_coord, self.y_coord-i])
            pipe_list.append([self.x_coord+1, self.y_coord-i])
            pipe_list.append([self.x_coord+4, self.y_coord-i])
            pipe_list.append([self.x_coord+5, self.y_coord-i])
        pipe_list.append([self.x_coord+2, self.y_coord-self._height+1])
        pipe_list.append([self.x_coord+3, self.y_coord-self._height+1])
        return pipe_list
