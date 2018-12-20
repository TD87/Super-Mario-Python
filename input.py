import sys
import os
import termios
import fcntl
import tty
import atexit
from select import select

class Keypress:
    """Keypress object to take input on keypress"""
    def __init__(self):
        # Save terminal settings
        self.filedesc = sys.stdin.fileno()
        self.prevTerminal = termios.tcgetattr(self.filedesc)
        self.curTerminal = termios.tcgetattr(self.filedesc)

        # Terminal reset when exit
        atexit.register(self.reset_normal)

        # Setting new terminal to unbuffered
        self.curTerminal[3] = (self.curTerminal[3] & ~termios.ICANON &
                                   ~termios.ECHO)
        termios.tcsetattr(self.filedesc, termios.TCSAFLUSH, self.curTerminal)

    def reset_normal(self):
        """Resets terminal"""
        termios.tcsetattr(self.filedesc, termios.TCSAFLUSH, self.prevTerminal)

    def getch(self):
        """Returns character from keypress"""
        return sys.stdin.read(1)

    def keypress(self):
        """True if keypress and false if not. Has 0.2 seconds timeout"""
        dr, dw, de = select([sys.stdin], [], [], 0.2)
        return dr != []
