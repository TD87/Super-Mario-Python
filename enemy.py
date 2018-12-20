from person import Person

class Enemy(Person):
    """Enemy object. Moves back and forth on a fixed path. Can kill mario. Is killed by being jumped on."""
    def __init__(self, x, y=30):
        super().__init__(x, y, 4, 0)
        self.pathPos = 0
        self.dir = 1
        self.pathL = 9

    def draw(self, matrix, marioPos):
        diff = marioPos - 75
        try:
            if self.x-diff > 0:
                matrix[30][self.x-diff] = '\033[40m' + '<'
            if self.x-diff+1 > 0:
                matrix[30][self.x+1-diff] = '\033[40m' + 'T'
                matrix[29][self.x+1-diff] = '\033[40m' + 'A'
            if self.x-diff+2 > 0:
                matrix[30][self.x+2-diff] = '\033[40m' + 'T' + '\033[46m'
                matrix[29][self.x+2-diff] = '\033[40m' + 'A' + '\033[46m'
            if self.x-diff+3 > 0:
                matrix[30][self.x+3-diff] = '\033[40m' + '>' + '\033[46m'
        except:
            pass

    def coordList(self):
        enemyList = [ [self.x, self.y], [self.x+1, self.y], [self.x+1, self.y-1], [self.x+2, self.y],
        [self.x+2, self.y-1], [self.x+3, self.y] ]
        return enemyList
