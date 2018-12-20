from obstacle import Obstacle

class Cloud(Obstacle):
    """Cloud background object"""
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, matrix, marioPos):
        diff = marioPos - 75
        try:
            if self.x-diff > 0:
                matrix[self.y+1][self.x-diff] = '\033[47m' + '('
                matrix[self.y+2][self.x-diff] = '\033[47m' + '('
            for i in range(1,15):
                if self.x+i-diff > 0:
                    if i == 14:
                        matrix[self.y][self.x+i-diff] = '\033[47m' + '_' + '\033[46m'
                        matrix[self.y+3][self.x+i-diff] = '\033[47m' + '_' + '\033[46m'
                    else:
                        matrix[self.y][self.x+i-diff] = '\033[47m' + '_'
                        matrix[self.y+3][self.x+i-diff] = '\033[47m' + '_'
                    matrix[self.y+1][self.x+i-diff] = '\033[47m' + ' '
                    matrix[self.y+2][self.x+i-diff] = '\033[47m' + ' '
            if self.x+15-diff > 0:
                matrix[self.y+1][self.x+15-diff] = '\033[47m' + ')' + '\033[46m'
                matrix[self.y+2][self.x+15-diff] = '\033[47m' + ')' + '\033[46m'
        except:
            pass
