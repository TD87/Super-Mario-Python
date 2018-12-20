import pytest
import time
from mario import Mario
from main import Engine

def true_func():
    return True

def r_func():
    return 'r'

def test_lvl2_coins():
    engine = Engine()
    engine.load_lvl()
    engine.lvl_num = 1
    engine.load_lvl()
    assert len(engine.coins) == 0

def test_next_level():
    engine = Engine()
    engine.load_lvl()
    engine.boss.lives = 0
    engine.next_level()
    assert engine.lvl_num == 1

def test_game_over_lose():
    engine = Engine()
    engine.load_lvl()
    engine.key_press.keypress = true_func
    engine.key_press.getch = r_func
    engine.mario.lives = 1
    engine.mario.x_coord = engine.enemies[0].x_coord
    engine.collide_enemy()
    assert engine.mario.lives == 3

def test_game_over_win():
    engine = Engine()
    engine.load_lvl()
    engine.start_time = time.time() - 4
    engine.key_press.keypress = true_func
    engine.key_press.getch = r_func
    engine.boss.lives = 0
    engine.lvl_num = 1
    engine.next_level()
    assert engine.boss.lives == 2

def test_mario_fall_game_over():
    engine = Engine()
    engine.key_press.keypress = true_func
    engine.key_press.getch = r_func
    engine.lvl_num = 1
    engine.load_lvl()
    engine.mario.move_left()
    engine.auto_moves1()
    engine.auto_moves1()
    engine.auto_moves1()
    engine.auto_moves1()
    engine.next_level()
    assert engine.mario.x_coord == 75
