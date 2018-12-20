# from colorama import Fore, Back, Style
from os import system

class Board:
    """Creates and renders the matrix every frame"""
    def __init__(self):
        self.matrix = list()
        self.__width = 34
        self.__length = 150

    def createMat(self, mario, enemies, obstacles, coins, backgrounds, lvl):
        """Call draw method of mario,coins,enemys,obstacles,backgrounds and hardcode borders,ground"""
        self.matrix = [ [' '] * self.__length for x in range(self.__width) ]
        for i in range(self.__width):
            self.matrix[i][1]='\033[46m'+ ' '

        for background in backgrounds:
            background.draw(self.matrix, mario.x)
        for enemy in enemies:
            enemy.draw(self.matrix, mario.x)
        for obstacle in obstacles:
            obstacle.draw(self.matrix, mario.x)
        for coin in coins:
            coin.draw(self.matrix, mario.x)
        mario.draw(self.matrix)
        for i in range(self.__length):
            self.matrix[0][i] = '\033[47m' + '_'
            self.matrix[self.__width-1][i] = '\033[47m' + '_'
            if i % 2 == 0 and lvl == 0:
                self.matrix[self.__width-2][i] = '\033[41m' + '['
                self.matrix[self.__width-3][i] = '\033[41m' + '['
            elif lvl == 0:
                self.matrix[self.__width-2][i] = '\033[41m' + ']'
                self.matrix[self.__width-3][i] = '\033[41m' + ']'
        for i in range(self.__width):
            self.matrix[i][0] = '\033[47m' + '|'
            self.matrix[i][self.__length-1] = '\033[47m' + '|'

    def render(self, lives, score, curTime, gameOver = False, won = False):
        """Convert matrix to string and print"""
        stringBoard = ""
        for x in range(0, self.__width):
            for y in range(0, self.__length):
                stringBoard += self.matrix[x][y]
            stringBoard += '\n'
        stringBoard+='\033[0m'
        if won:
            stringBoard += "YOU WON\n"
        elif gameOver:
            stringBoard += "GAME OVER\n"
        stringBoard += "LIVES: " + str(lives) + "\n"
        stringBoard += "SCORE: " + str(score) + "\n"
        stringBoard += "TIME: " + str(curTime) + "\n"
        stringBoard += "Press 'q' to exit\n"
        stringBoard += "Press 'r' to restart\n"
        system("clear")
        print(stringBoard)
