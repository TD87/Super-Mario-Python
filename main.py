from pipe import Pipe
from mario import Mario
from platform import Platform
from enemy import Enemy
from boss import Boss
from coin import Coin
from cloud import Cloud
from hill import Hill
from input import Keypress
from board import Board
from os import system
import sys
import time
from math import floor, ceil

class Engine:
    """Main game logic"""
    def __init__(self):
        self.board = Board()
        self.mario = Mario(75,30)
        self.boss = Boss(195)
        self.enemies = list()
        self.obstacles = list()
        self.coins = list()
        self.backgrounds = list()
        self.kp = Keypress()
        self.startTime = time.time()
        self.lvlNum = 0
        self.floor = 30
        self.score = 0

    def run(self):
        """Run the game"""
        self.loadLvl()
        self.startTime = time.time()
        while True:
            self.board.createMat(self.mario, self.enemies, self.obstacles, self.coins, self.backgrounds, self.lvlNum)
            self.board.render(self.mario.lives, self.score, floor(time.time()-self.startTime))
            if self.kp.keypress() and self.takeInput() == 1:
                    continue
            self.autoMoves1()
            self.autoMoves2()
            self.collideEnemy()
            if self.boss.lives == 0:
                if self.lvlNum == 0:
                    self.lvlNum = 1
                    self.loadLvl()          #Load lvl 2
                else:
                    self.score += ceil(1 / floor(time.time()-self.startTime) * 10000)   #Calc final score at end of lvl 2
                    self.gameOver(won = True)
            if self.mario.y == 36:
                self.gameOver()             #When mario falls of platform in lvl 2

    def takeInput(self):
        """Take input and move mario accordingly"""
        input = self.kp.getch()
        if input == 'd' and (self.lvlNum == 1 or self.mario.x < 287):
            if self.collideCheck(xdisp = self.mario.xdisp, collideList = self.obstacles) == 0:
                self.mario.moveRight()
        elif input == 'a' and self.mario.x > 43:
            if self.collideCheck(xdisp = -self.mario.xdisp, collideList = self.obstacles) == 0:
                self.mario.moveLeft()
        elif input == 'w':
            if self.mario.isJumping == 0 and (self.mario.y == self.floor or self.collideCheck(ydisp = self.mario.ydisp, collideList = self.obstacles) == 1):
                self.mario.jump()
                if self.mario.y == 30:
                    self.audio("jump_small")
                else:
                    self.audio("jump_super")
        elif input == 'q':
            sys.exit()
        elif input == 'r':
            self.loadLvl()
            return 1
        if input == 'a' or input == 'd':
            self.audio("move")
        return 0

    def gameOver(self, won = False):
        """Print game over and wait for user input"""
        self.board.createMat(self.mario, self.enemies, self.obstacles, self.coins, self.backgrounds, self.lvlNum)
        self.board.render(self.mario.lives, self.score, floor(time.time()-self.startTime), gameOver = True, won = won)
        if won:
            self.audio("win")
        else:
            self.audio("die")
        while True:
            if self.kp.keypress():
                input = self.kp.getch()
            else:
                input = None
            if input == 'q':
                sys.exit()
            elif input == 'r':
                self.loadLvl()
                return

    def collideCheck(self, collideList, xdisp = 0, ydisp = 0):
        """Generic collide check between mario and an object in the collideList.
            disp variables for mario can be specified to predict collisions before they actually happen"""
        marioList = self.mario.coordList(xdisp = xdisp, ydisp = ydisp)
        for item in collideList:
            itemList = item.coordList()
            union = [x for x in marioList if x in itemList]         #Actually we are taking intersection of their coordinate sets
            if union != []:
                if collideList == self.enemies or collideList == self.coins:
                    return item
                else:
                    return 1
        return 0

    def collideEnemy(self):
        """Check for collisions between mario and enemies & coins. Mario is unvulnerable
            to collision with enemies for 2 seconds after losing a life"""
        if time.time() - self.mario.invulnerable < 2:
            return
        if self.collideCheck(collideList = self.enemies) != 0:
            self.mario.lives -= 1
            self.mario.invulnerable = time.time()
        item = self.collideCheck(collideList = self.coins)
        if item != 0:
            self.coins.remove(item)
            self.score += 10
            self.audio("coin")
        if self.mario.lives < 1:
            self.gameOver()

    def loadLvl(self):
        """Load all objects and variables of corresponding level"""
        if self.lvlNum == 0:
            self.score = 0
            self.floor = 30
            self.mario.__init__(75,30)
            self.boss.__init__(195)
            self.enemies = [Enemy(91), Enemy(147), self.boss]
            self.obstacles = [Pipe(131,6), Platform(91,19,22), Platform(147,13,22), Pipe(187,15)]
            self.coins = [Coin(95, 18), Coin(99, 18), Coin(103, 18), Coin(107, 18), Coin(151, 12), Coin(155, 12), Coin(159, 12), Coin(163, 12)]
            self.backgrounds = [Cloud(120, 3), Cloud(40, 8), Cloud(220, 6), Cloud(270, 5), Hill(10, 15), Hill(155, 10), Hill(260, 20)]

        if self.lvlNum == 1:
            self.floor = 36
            self.boss.__init__(247,18)
            self.mario.__init__(75,24)
            self.obstacles = [Platform(75,25,22), Platform(115,19,22), Platform(155,13,22), Platform(195,7,22), Platform(247,19,82)]
            self.enemies = [self.boss]
            self.backgrounds = [Cloud(40, 15), Cloud(80, 4), Cloud(130, 6), Cloud(160, 24), Cloud(200, 16), Cloud(240, 25),
                                Cloud(270, 3), Cloud(360, 3), Cloud(350, 25)]

    def autoMoves1(self):
        """Manages Mario's jumping: gravity and automatic move up. Also checks for
            jumping on enemies and killing them"""
        if self.mario.isJumping == 0 and self.mario.y != self.floor and self.collideCheck(ydisp = self.mario.ydisp, collideList = self.obstacles) == 0:
            item = self.collideCheck(collideList = self.enemies, ydisp = self.mario.ydisp)  #This might not work
            if item != 0:
                if item == self.boss and item.lives == 2:
                    item.lives -= 1
                    self.mario.invulnerable = time.time()
                elif item == self.boss and time.time() - self.mario.invulnerable > 1:
                    item.lives -= 1
                    self.enemies.remove(item)
                    self.score += 200
                elif item != self.boss:
                    self.enemies.remove(item)
                    self.score += 100
            self.mario.moveDown()
        elif self.mario.isJumping > 0 and self.mario.isJumping < self.mario.jumpH and self.collideCheck(ydisp = -self.mario.ydisp, collideList = self.obstacles) == 0:
            self.mario.moveUp()
            self.mario.isJumping += 1
        else:
            self.mario.isJumping = 0

    def autoMoves2(self):
        """Automatic movement of enemies and following mechanic of boss"""
        for enemy in self.enemies:
            if enemy == self.boss and self.mario.x >= enemy.x_init:
                if enemy.delayVar == 0 and ((self.mario.x < enemy.x and enemy.dir == 1) or (self.mario.x >= enemy.x and enemy.dir == 0)):
                    enemy.delayVar = 1
                    enemy.delay = time.time()
                elif enemy.delayVar == 1 and time.time() - enemy.delay > 1:
                    if self.mario.x < enemy.x:
                        enemy.dir = 0
                    else:
                        enemy.dir = 1
                    enemy.delayVar = 0

            if enemy.dir == 1 and enemy.pathPos < enemy.pathL:
                enemy.pathPos += 1
                enemy.moveRight()
            elif enemy.dir == 1:
                enemy.pathPos -= 1
                enemy.dir = 0
                enemy.moveLeft()
            elif enemy.dir == 0 and enemy.pathPos > 0:
                enemy.pathPos -= 1
                enemy.moveLeft()
            else:
                enemy.pathPos += 1
                enemy.dir = 1
                enemy.moveRight()

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
    engine = Engine()
    engine.run()
