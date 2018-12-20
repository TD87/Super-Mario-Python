class Person:
    """Basic person class from which enemy and mario inherit from"""
    def __init__(self, x, y, xdisp, ydisp):
        self.x = x
        self.y = y
        self.xdisp = xdisp
        self.ydisp = ydisp

    def moveLeft(self):
        self.x -= self.xdisp

    def moveRight(self):
        self.x += self.xdisp

    def moveUp(self):
        self.y -= self.ydisp

    def moveDown(self):
        self.y += self.ydisp

    def draw(self, matrix):
        """Draw to the board's matrix"""
        pass

    def coordList(self):
        """Returns list of coordinates occupied on the matrix by the object"""
        pass
