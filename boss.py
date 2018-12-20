from enemy import Enemy

class Boss(Enemy):
    """Boss enemy. Has 2 lives and chases the player with a 1 second delay. Loses lives by being jumped on"""
    def __init__(self, x, y=30):
        super().__init__(x,y)
        self.delay = 0
        self.pathL = 19
        self.delayVar = 0
        self.lives = 2
        self.x_init = self.x

    def draw(self, matrix, marioPos):
        diff = marioPos - 75
        try:
            if self.x-1-diff > 0:
                matrix[self.y-1][self.x-1-diff]='\033[40m' + "R"
                matrix[self.y-2][self.x-1-diff]='\033[40m' + "R"
            if self.x-diff > 0:
                matrix[self.y][self.x-diff]='\033[40m' + "R"
                matrix[self.y-3][self.x-diff]='\033[40m' + "M"
                matrix[self.y-1][self.x-diff]='\033[40m' + "E"
                matrix[self.y-2][self.x-diff]='\033[40m' + "A"
            if self.x+1-diff > 0:
                matrix[self.y][self.x+1-diff]='\033[40m' + "R" + '\033[46m'
                matrix[self.y-1][self.x+1-diff]='\033[40m' + "D"
                matrix[self.y-3][self.x+1-diff]='\033[40m' + "M" + '\033[46m'
                matrix[self.y-2][self.x+1-diff]='\033[40m' + "G"
            if self.x-2-diff > 0:
                matrix[self.y-1][self.x+2-diff]='\033[40m' + "Y" + '\033[46m'
                matrix[self.y-2][self.x+2-diff]='\033[40m' + "U" + '\033[46m'
        except:
            pass

    def coordList(self):
        bossList = [ [self.x,self.y], [self.x,self.y-1], [self.x,self.y-2],
        [self.x,self.y-3], [self.x+1,self.y], [self.x+1,self.y-1],
        [self.x+1,self.y-2], [self.x+1,self.y-3], [self.x-1, self.y-1],
        [self.x-1, self.y-2], [self.x+2, self.y-1], [self.x+2, self.y-2]]
        return bossList
