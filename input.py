"""This module takes input from the player"""

# import os
# import fcntl
# import tty
import sys
import termios
import atexit
from select import select

class Keypress:
    """Keypress object to take input on keypress"""
    def __init__(self):
        # Save terminal settings
        self.filedesc = sys.stdin.fileno()
        self.prev_terminal = termios.tcgetattr(self.filedesc)
        self.cur_terminal = termios.tcgetattr(self.filedesc)

        # Terminal reset when exit
        atexit.register(self.reset_normal)

        # Setting new terminal to unbuffered
        self.cur_terminal[3] = (self.cur_terminal[3] & ~termios.ICANON &
                                ~termios.ECHO)
        termios.tcsetattr(self.filedesc, termios.TCSAFLUSH, self.cur_terminal)

    def reset_normal(self):
        """Resets terminal"""
        termios.tcsetattr(self.filedesc, termios.TCSAFLUSH, self.prev_terminal)

    def getch(self):
        """Returns character from keypress"""
        return sys.stdin.read(1)

    def keypress(self):
        """True if keypress and false if not. Has 0.2 seconds timeout"""
        dr_var, _, _ = select([sys.stdin], [], [], 0.2)
        return dr_var != []
