from person import Person

class Mario(Person):
    """Player Object"""
    def __init__(self, x, y):
        super().__init__(x, y, 4, 3)
        self.isJumping = 0
        self.lives = 3
        self.invulnerable = 0
        self.jumpH = 5

    def jump(self):
        self.isJumping = 1

    def draw(self, matrix):
        try:
            if self.y > 0:
                matrix[self.y][75]="R"
                matrix[self.y][76]="R" + '\033[46m'
            if self.y-1 > 0:
                matrix[self.y-1][75]="O"
                matrix[self.y-1][76]="O"
                matrix[self.y-1][74]="I"
                matrix[self.y-1][77]="I" + '\033[46m'
            if self.y-2 > 0:
                matrix[self.y-2][75]="A"
                matrix[self.y-2][76]="A"
                matrix[self.y-2][74]="I"
                matrix[self.y-2][77]="I" + '\033[46m'
            if self.y-3 > 0:
                matrix[self.y-3][75]="M"
                matrix[self.y-3][76]="M" + '\033[46m'
        except:
            pass

    def coordList(self, xdisp = 0, ydisp = 0):
        """Optional xdisp and ydisp. Polymorphism"""
        marioList = [ [self.x+xdisp,self.y+ydisp], [self.x+xdisp,self.y-1+ydisp], [self.x+xdisp,self.y-2+ydisp],
        [self.x+xdisp,self.y-3+ydisp], [self.x+1+xdisp,self.y+ydisp], [self.x+1+xdisp,self.y-1+ydisp],
        [self.x+1+xdisp,self.y-2+ydisp], [self.x+1+xdisp,self.y-3+ydisp], [self.x-1+xdisp, self.y-1+ydisp],
        [self.x-1+xdisp, self.y-2+ydisp], [self.x+2+xdisp, self.y-1+ydisp], [self.x+2+xdisp, self.y-2+ydisp]]
        return marioList
