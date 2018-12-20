from obstacle import Obstacle

class Platform(Obstacle):
    """Plaform Obstacle"""
    def __init__(self, x, y, length):
        super().__init__(x, y)
        self.length = length

    def draw(self, matrix, marioPos):
        diff = marioPos - 75
        for i in range(self.length):
            if i % 2 == 0:
                try:
                    if self.x+i-diff > 0:
                        matrix[self.y][self.x+i-diff] = '\033[41m' + "["
                        matrix[self.y+1][self.x+i-diff] = '\033[41m' + "["
                except:
                    pass
            else:
                try:
                    if self.x+i-diff > 0:
                        if i == self.length-1:
                            matrix[self.y][self.x+i-diff] = '\033[41m' + "]" + '\033[46m'
                            matrix[self.y+1][self.x+i-diff] = '\033[41m' + "]" + '\033[46m'
                        else:
                            matrix[self.y][self.x+i-diff] = '\033[41m' + "]"
                            matrix[self.y+1][self.x+i-diff] = '\033[41m' + "]"
                except:
                    pass

    def coordList(self):
        platformList = list()
        for i in range(self.length):
            platformList.append([self.x+i, self.y])
            platformList.append([self.x+i, self.y+1])
        return platformList
