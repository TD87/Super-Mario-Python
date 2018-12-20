"""This is the main module that contains the game engine"""

import sys
import time
from os import system
from math import floor, ceil
from pipe import Pipe
from mario import Mario
from platforms import Platform
from enemy import Enemy
from boss import Boss
from coin import Coin
from cloud import Cloud
from hill import Hill
from input import Keypress
from board import Board

class Engine:
    """Main game logic"""
    def __init__(self):
        self.board = Board()
        self.mario = Mario(75, 30)
        self.boss = Boss(195)
        self.enemies = list()
        self.obstacles = list()
        self.coins = list()
        self.backgrounds = list()
        self.key_press = Keypress()
        self.start_time = time.time()
        self.lvl_num = 0
        self.floor = 30
        self.score = 0

    def run(self):
        """Run the game"""
        self.load_lvl()
        self.start_time = time.time()
        while True:
            self.board.create_mat(self.mario, [self.enemies, self.obstacles,
                                               self.coins, self.backgrounds], self.lvl_num)
            self.board.render(self.mario.lives, self.score, floor(time.time()-self.start_time), 0)
            if self.key_press.keypress() and self.take_input() == 1:
                continue
            self.auto_moves1()
            self.auto_moves2()
            self.collide_enemy()
            self.next_level()

    def next_level(self):
        if self.boss.lives == 0:
            if self.lvl_num == 0:
                self.lvl_num = 1
                self.load_lvl()          #Load lvl 2
            else:
                #Calc final score at end of lvl 2
                self.score += ceil(1 / floor(time.time() - self.start_time)
                                   * 10000)
                self.game_over(1)
        if self.mario.y_coord == 36:
            self.game_over(0)             #When mario falls of platform in lvl 2

    def take_input(self):
        """Take input and move mario accordingly"""
        input_key = self.key_press.getch()
        if input_key == 'd' and (self.lvl_num == 1 or self.mario.x_coord < 287):
            if self.collide_check(xdisp=self.mario.xdisp, collide_list=self.obstacles) == 0:
                self.mario.move_right()
        elif input_key == 'a' and self.mario.x_coord > 43:
            if self.collide_check(xdisp=-self.mario.xdisp, collide_list=self.obstacles) == 0:
                self.mario.move_left()
        elif input_key == 'w':
            if (self.mario.y_coord == self.floor or
                    self.collide_check(ydisp=self.mario.ydisp, collide_list=
                                       self.obstacles) == 1) and self.mario.is_jumping == 0:
                self.mario.jump()
                if self.mario.y_coord == 30:
                    self.audio("jump_small")
                else:
                    self.audio("jump_super")
        elif input_key == 'q':
            sys.exit()
        elif input_key == 'r':
            self.load_lvl()
            return 1
        if input_key == 'a' or input_key == 'd':
            self.audio("move")
        return 0

    def game_over(self, won):
        """Print game over and wait for user input"""
        self.board.create_mat(self.mario, [self.enemies, self.obstacles,
                                           self.coins, self.backgrounds], self.lvl_num)
        self.board.render(self.mario.lives, self.score, floor(time.time()-self.start_time), 1 + won)
        if won:
            self.audio("win")
        else:
            self.audio("die")
        while True:
            if self.key_press.keypress():
                input_key = self.key_press.getch()
            else:
                input_key = None
            if input_key == 'q':
                sys.exit()
            elif input_key == 'r':
                self.load_lvl()
                return

    def collide_check(self, collide_list, xdisp=0, ydisp=0):
        """Generic collide check between mario and an object in the collide_list.
            disp variables for mario can be specified to predict collisions
            before they actually happen"""
        mario_list = self.mario.coord_list(xdisp=xdisp, ydisp=ydisp)
        for item in collide_list:
            item_list = item.coord_list()
            #Actually we are taking intersection of their coordinate sets
            union = [x for x in mario_list if x in item_list]
            if union != []:
                if collide_list == self.enemies or collide_list == self.coins:
                    return item
                else:
                    return 1
        return 0

    def collide_enemy(self):
        """Check for collisions between mario and enemies & coins. Mario is unvulnerable
            to collision with enemies for 2 seconds after losing a life"""
        if time.time() - self.mario.invulnerable < 2:
            return
        if self.collide_check(collide_list=self.enemies) != 0:
            self.mario.lives -= 1
            self.mario.invulnerable = time.time()
        item = self.collide_check(collide_list=self.coins)
        if item != 0:
            self.coins.remove(item)
            self.score += 10
            self.audio("coin")
        if self.mario.lives < 1:
            self.game_over(0)

    def load_lvl(self):
        """Load all objects and variables of corresponding level"""
        if self.lvl_num == 0:
            self.score = 0
            self.floor = 30
            self.mario.__init__(75, 30)
            self.boss.__init__(195)
            self.enemies = [Enemy(91), Enemy(147), self.boss]
            self.obstacles = [Pipe(131, 6), Platform(91, 19, 22), Platform(147, 13, 22),
                              Pipe(187, 15)]
            self.coins = [Coin(95, 18), Coin(99, 18), Coin(103, 18), Coin(107, 18),
                          Coin(151, 12), Coin(155, 12), Coin(159, 12), Coin(163, 12)]
            self.backgrounds = [Cloud(120, 3), Cloud(40, 8), Cloud(220, 6), Cloud(270, 5),
                                Hill(10, 15), Hill(155, 10), Hill(260, 20)]

        if self.lvl_num == 1:
            self.floor = 36
            self.boss.__init__(247, 18)
            self.mario.__init__(75, 24)
            self.obstacles = [Platform(75, 25, 22), Platform(115, 19, 22), Platform(155, 13, 22),
                              Platform(195, 7, 22), Platform(247, 19, 82)]
            self.enemies = [self.boss]
            self.backgrounds = [Cloud(40, 15), Cloud(80, 4), Cloud(130, 6), Cloud(160, 24),
                                Cloud(200, 16), Cloud(240, 25), Cloud(270, 3), Cloud(360, 3),
                                Cloud(350, 25)]
            self.coins = list()

    def auto_moves1(self):
        """Manages Mario's jumping: gravity and automatic move up. Also checks for
            jumping on enemies and killing them"""
        if (self.mario.is_jumping == 0 and self.mario.y_coord != self.floor and
                self.collide_check(ydisp=self.mario.ydisp, collide_list=self.obstacles) == 0):
            #This might not work
            item = self.collide_check(collide_list=self.enemies, ydisp=self.mario.ydisp)
            if item != 0:
                if item == self.boss and item.lives == 2:
                    item.lives -= 1
                    self.mario.invulnerable = time.time()
                elif item == self.boss and time.time() - self.mario.invulnerable > 2:
                    item.lives -= 1
                    self.enemies.remove(item)
                    self.score += 200
                elif item != self.boss:
                    self.enemies.remove(item)
                    self.score += 100
            self.mario.move_down()
        elif (self.mario.is_jumping > 0 and self.mario.is_jumping < self.mario.jump_h and
              self.collide_check(ydisp=-self.mario.ydisp, collide_list=self.obstacles) == 0):
            self.mario.move_up()
            self.mario.is_jumping += 1
        else:
            self.mario.is_jumping = 0

    def auto_moves2(self):
        """Following mechanic of boss"""
        for enemy in self.enemies:
            if enemy == self.boss and self.mario.x_coord >= enemy.x_init:
                if enemy.delay_var == 0:
                    if ((self.mario.x_coord < enemy.x_coord and enemy.dir == 1) or
                            (self.mario.x_coord >= enemy.x_coord and enemy.dir == 0)):
                        enemy.delay_var = 1
                        enemy.delay = time.time()
                elif enemy.delay_var == 1 and time.time() - enemy.delay > 1.5:
                    if self.mario.x_coord < enemy.x_coord:
                        enemy.dir = 0
                    else:
                        enemy.dir = 1
                    enemy.delay_var = 0
            self.auto_moves3(enemy)

    def auto_moves3(self, enemy):
        """Automatic movement of enemies"""
        if enemy.dir == 1 and enemy.path_pos < enemy.path_l:
            enemy.path_pos += 1
            enemy.move_right()
        elif enemy.dir == 1:
            enemy.path_pos -= 1
            enemy.dir = 0
            enemy.move_left()
        elif enemy.dir == 0 and enemy.path_pos > 0:
            enemy.path_pos -= 1
            enemy.move_left()
        else:
            enemy.path_pos += 1
            enemy.dir = 1
            enemy.move_right()

    def audio(self, sound):
        """Audio function. Uses aplay"""
        try:
            if sound == "jump_small":
                system("aplay -q ./sounds/smb_jump-small.wav &")
            elif sound == "jump_super":
                system("aplay -q ./sounds/smb_jump-super.wav &")
            elif sound == "move":
                system("aplay -q ./sounds/smb_fireball.wav &")
            elif sound == "win":
                system("aplay -q ./sounds/smb_stage_clear.wav")
            elif sound == "die":
                system("aplay -q ./sounds/smb_bowserfalls.wav &")
            elif sound == "coin":
                system("aplay -q ./sounds/smb_coin.wav &")
        except:
            pass

if __name__ == "__main__":
    GAME_ENGINE = Engine()
    GAME_ENGINE.run()
