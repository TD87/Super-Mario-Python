import pytest
import time
from mario import Mario
from main import Engine

def mario_move(engine):
    engine.auto_moves1()
    y_coord = engine.mario.y_coord
    return y_coord

def test_jump_simple():
    engine = Engine()
    engine.load_lvl()
    engine.mario.jump()
    init_y = engine.mario.y_coord
    final_y = mario_move(engine)
    assert final_y < init_y

def test_jump_top():
    engine = Engine()
    engine.load_lvl()
    engine.mario.jump()
    y1 = engine.mario.y_coord
    y2 = mario_move(engine)
    while y2 < y1:
        y1 = y2
        y2 = mario_move(engine)
    assert y1 == 18

def test_jump_gravity():
    engine = Engine()
    engine.load_lvl()
    engine.mario.jump()
    y1 = engine.mario.y_coord
    y2 = mario_move(engine)
    while y2 <= y1:
        y1 = y2
        y2 = mario_move(engine)
    assert y2 == 21

def test_jump_bot():
    engine = Engine()
    engine.load_lvl()
    engine.mario.jump()
    y1 = engine.mario.y_coord
    y2 = mario_move(engine)
    while y1 != y2 or y1 == 18:
        y1 = y2
        y2 = mario_move(engine)
    assert y1 == 30

def test_jump_land_platform():
    engine = Engine()
    engine.load_lvl()
    engine.mario.x_coord = 95
    engine.mario.y_coord = 0
    y1 = engine.mario.y_coord
    y2 = mario_move(engine)
    while y1 != y2:
        y1 = y2
        y2 = mario_move(engine)
    assert y1 == 18

def test_fall_enemy():
    engine = Engine()
    engine.load_lvl()
    engine.mario.x_coord = engine.enemies[0].x_coord
    engine.mario.y_coord = engine.enemies[0].y_coord - 3
    enemy = engine.enemies[0]
    engine.auto_moves1()
    assert enemy not in engine.enemies

def test_fall_boss():
    engine = Engine()
    engine.load_lvl()
    engine.mario.x_coord = engine.boss.x_coord
    engine.mario.y_coord = engine.boss.y_coord - 3
    boss = engine.boss
    engine.auto_moves1()
    assert boss.lives == 1

def test_fall_boss_kill():
    engine = Engine()
    engine.load_lvl()
    engine.mario.x_coord = engine.boss.x_coord
    engine.mario.y_coord = engine.boss.y_coord - 3
    engine.boss.lives = 1
    boss = engine.boss
    engine.auto_moves1()
    assert boss not in engine.enemies

def test_fall_boss_bug():
    engine = Engine()
    engine.load_lvl()
    engine.mario.x_coord = engine.boss.x_coord
    engine.mario.y_coord = engine.boss.y_coord - 6
    boss = engine.boss
    engine.auto_moves1()
    time.sleep(1)
    engine.auto_moves1()
    assert boss in engine.enemies
