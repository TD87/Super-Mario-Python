import pytest
import time
from mario import Mario
from main import Engine

def enemy_move(engine):
    engine.auto_moves2()
    x_coord = engine.enemies[0].x_coord
    return x_coord

def test_enemy_move():
    engine = Engine()
    engine.load_lvl()
    x_init = engine.enemies[0].x_coord
    engine.auto_moves2()
    assert engine.enemies[0].x_coord > x_init

def test_move_max():
    engine = Engine()
    engine.load_lvl()
    x_init = engine.enemies[0].x_coord
    x1 = engine.enemies[0].x_coord
    x2 = enemy_move(engine)
    while x2 > x1:
        x1 = x2
        x2 = enemy_move(engine)
    assert x1 == x_init + engine.enemies[0].path_l * engine.enemies[0].xdisp

def test_move_reverse():
    engine = Engine()
    engine.load_lvl()
    x_init = engine.enemies[0].x_coord
    x1 = engine.enemies[0].x_coord
    x2 = enemy_move(engine)
    while x2 >= x1 and x2 != x_init + engine.enemies[0].path_l * engine.enemies[0].xdisp:
        x1 = x2
        x2 = enemy_move(engine)
    assert x1 == x_init + (engine.enemies[0].path_l - 1) * engine.enemies[0].xdisp

def test_move_return():
    engine = Engine()
    engine.load_lvl()
    x_init = engine.enemies[0].x_coord
    x1 = -1
    x2 = enemy_move(engine)
    while x1 != x_init:
        x1 = x2
        x2 = enemy_move(engine)
    assert x1 == x_init

def test_boss_follow_delay():
    engine = Engine()
    engine.load_lvl()
    engine.auto_moves2()
    engine.mario.x_coord = engine.boss.x_init
    engine.auto_moves2()
    assert engine.boss.delay_var == 1

def test_boss_follow():
    engine = Engine()
    engine.load_lvl()
    engine.auto_moves2()
    init_dir = engine.boss.dir
    engine.mario.x_coord = engine.boss.x_init
    engine.boss.delay = time.time() - 100
    engine.boss.delay_var = 1
    engine.auto_moves2()
    assert engine.boss.dir != init_dir
