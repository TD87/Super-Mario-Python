from obstacle import Obstacle

class Hill(Obstacle):
    """Hill background object"""
    def __init__(self, x, size):
        super().__init__(x, 30)
        self.size = size

    def draw(self, matrix, marioPos):
        diff = marioPos - 75
        try:
            for i in range(self.size):
                if self.x+i-diff > 0:
                    matrix[self.y-i][self.x+i-diff] = '\033[43m' + '/'
                    for y in range(self.y-i+1,self.y+1):
                        matrix[y][self.x+i-diff] = '\033[43m' + ' '
            for i in range(self.size):
                if self.x+i+self.size-diff > 0:
                    matrix[self.y-self.size+1+i][self.x+i+self.size-diff] = '\\' + '\033[46m'
                    for y in range(self.y-self.size+i+2,self.y+1):
                        matrix[y][self.x+i+self.size-diff] = '\033[43m' + ' '
        except:
            pass
