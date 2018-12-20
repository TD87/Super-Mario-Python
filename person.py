"""This module creates the person base class"""

class Person:
    """Basic person class from which enemy and mario inherit from"""
    def __init__(self, x, y, xdisp, ydisp):
        self.x_coord = x
        self.y_coord = y
        self.xdisp = xdisp
        self.ydisp = ydisp

    def move_left(self):
        """Move person left"""
        self.x_coord -= self.xdisp

    def move_right(self):
        """Move person right"""
        self.x_coord += self.xdisp

    def move_up(self):
        """Move person up"""
        self.y_coord -= self.ydisp

    def move_down(self):
        """Move person down"""
        self.y_coord += self.ydisp

    def draw(self, matrix):
        """Draw to the board's matrix"""
        pass

    def coord_list(self):
        """Returns list of coordinates occupied on the matrix by the object"""
        pass
