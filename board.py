"""This module creates the board that the player sees"""

from os import system

class Board:
    """Creates and renders the matrix every frame"""
    def __init__(self):
        self.matrix = list()
        self.__width = 34
        self.__length = 150

    def create_mat(self, mario, draw_lists, lvl):
        """Call draw method of mario,coins,enemys,obstacles,
           backgrounds and hardcode borders,ground"""
        self.matrix = [[' '] * self.__length for x in range(self.__width)]
        for i in range(self.__width):
            self.matrix[i][1] = '\033[46m'+ ' '

        for enemies_obstacles in draw_lists:
            for item in enemies_obstacles:
                item.draw(self.matrix, mario.x_coord)
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

    def render(self, lives, score, cur_time, status):
        """Convert matrix to string and print"""
        string_board = ""
        for x_coord in range(0, self.__width):
            for y_coord in range(0, self.__length):
                string_board += self.matrix[x_coord][y_coord]
            string_board += '\n'
        string_board += '\033[0m'
        if status == 2:
            string_board += "YOU WON\n"
        elif status == 1:
            string_board += "GAME OVER\n"
        string_board += "LIVES: " + str(lives) + "\n"
        string_board += "SCORE: " + str(score) + "\n"
        string_board += "TIME: " + str(cur_time) + "\n"
        string_board += "Press 'q' to exit\n"
        string_board += "Press 'r' to restart\n"
        system("clear")
        print(string_board)
