from obstacle import Obstacle

class Pipe(Obstacle):
    """Pipe Obstacle"""
    def __init__(self, x, height):
        super().__init__(x, 30)
        self.height = height

    def draw(self, matrix, marioPos):
        diff = marioPos - 75
        for i in range(self.height):
            try:
                if self.x-diff > 0:
                    matrix[self.y-i][self.x-diff] = '\033[42m' + '{'
                if self.x+1-diff > 0:
                    matrix[self.y-i][self.x+1-diff] = '\033[42m' + '}'
                if self.x+2-diff > 0:
                    matrix[self.y-i][self.x+2-diff] = '\033[42m' + ' '
                if self.x+3-diff > 0:
                    matrix[self.y-i][self.x+3-diff] = '\033[42m' + ' '
                if self.x+4-diff > 0:
                    matrix[self.y-i][self.x+4-diff] = '\033[42m' + '{'
                if self.x+5-diff > 0:
                    matrix[self.y-i][self.x+5-diff] = '\033[42m' + '}' + '\033[46m'
            except:
                pass
        try:
                if self.x+2-diff > 0:
                    matrix[self.y-self.height+1][self.x+2-diff] = '\033[42m' + '{'
                if self.x+3-diff > 0:
                    matrix[self.y-self.height+1][self.x+3-diff] = '\033[42m' + '}'
        except:
            pass

    def coordList(self):
        pipeList = list()
        for i in range(self.height):
            pipeList.append([self.x, self.y-i])
            pipeList.append([self.x+1, self.y-i])
            pipeList.append([self.x+4, self.y-i])
            pipeList.append([self.x+5, self.y-i])
        pipeList.append([self.x+2, self.y-self.height+1])
        pipeList.append([self.x+3, self.y-self.height+1])
        return pipeList
