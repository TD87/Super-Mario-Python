class Obstacle:
    """Basic obstacle class from which pipe, platform, coin, hill and cloud inherit"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, matrix, marioPos):
        """Draw to the board's matrix"""
        pass

    def coordList(self):
        """Returns list of coordinates occupied on the matrix by the object"""
        pass
