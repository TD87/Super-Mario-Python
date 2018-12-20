from obstacle import Obstacle

class Coin(Obstacle):
    """Coin object. Can be collected by player"""
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, matrix, marioPos):
        diff = marioPos - 75
        try:
            if self.x-diff > 0:
                matrix[self.y][self.x-diff] = '\033[35m' + 'O' + '\033[39m'
        except:
            pass

    def coordList(self):
        coinList = list()
        coinList.append([self.x, self.y])
        return coinList
