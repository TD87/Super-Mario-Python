"""This module creates the coin object"""

from obstacle import Obstacle

class Coin(Obstacle):
    """Coin object. Can be collected by player"""
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, matrix, mario_pos):
        diff = mario_pos - 75
        try:
            if self.x_coord-diff > 0:
                matrix[self.y_coord][self.x_coord-diff] = '\033[35m' + 'O' + '\033[39m'
        except:
            pass

    def coord_list(self):
        coin_list = list()
        coin_list.append([self.x_coord, self.y_coord])
        return coin_list
