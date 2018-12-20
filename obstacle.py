"""This module creates the obstacles base class"""

class Obstacle:
    """Basic obstacle class from which pipe, platform, coin, hill and cloud inherit"""
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def draw(self, matrix, mario_pos):
        """Draw to the board's matrix"""
        pass

    def coord_list(self):
        """Returns list of coordinates occupied on the matrix by the object"""
        pass
