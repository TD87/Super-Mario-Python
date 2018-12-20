import pytest
import time
from mario import Mario
from main import Engine

def empty_func():
    pass

def true_func():
    return True

def r_func():
    return 'r'

def test_collide_check_enemy():
    engine = Engine()
    engine.load_lvl()
    engine.mario.x_coord = engine.enemies[0].x_coord
    assert engine.collide_check(engine.enemies) == engine.enemies[0]

def test_collide_check_coin():
    engine = Engine()
    engine.load_lvl()
    engine.mario.x_coord = engine.coins[0].x_coord
    engine.mario.y_coord = engine.coins[0].y_coord
    assert engine.collide_check(engine.coins) == engine.coins[0]

def test_collide_check_obstacles():
    engine = Engine()
    engine.load_lvl()
    engine.mario.x_coord = engine.obstacles[0].x_coord
    engine.mario.y_coord = engine.obstacles[0].y_coord
    assert engine.collide_check(engine.obstacles) == 1

def test_collide_check_xdisp():
    engine = Engine()
    engine.load_lvl()
    engine.mario.x_coord = engine.enemies[0].x_coord - 4
    assert engine.collide_check(engine.enemies, 4) == engine.enemies[0]

def test_collide_check_ydisp():
    engine = Engine()
    engine.load_lvl()
    engine.mario.x_coord = engine.enemies[0].x_coord
    engine.mario.y_coord = engine.enemies[0].y_coord - 3
    assert engine.collide_check(engine.enemies, 0, 3) == engine.enemies[0]

def test_collide_enemy_lose_life():
    engine = Engine()
    engine.load_lvl()
    engine.game_over = empty_func
    init_lives = engine.mario.lives
    engine.mario.x_coord = engine.enemies[0].x_coord
    engine.collide_enemy()
    assert engine.mario.lives < init_lives

def test_collide_enemy_invulnerable():
    engine = Engine()
    engine.load_lvl()
    engine.game_over = empty_func
    init_lives = engine.mario.lives
    engine.mario.x_coord = engine.enemies[0].x_coord
    engine.mario.invulnerable = time.time() + 100
    engine.collide_enemy()
    assert engine.mario.lives == init_lives

def test_collide_coin():
    engine = Engine()
    engine.load_lvl()
    engine.game_over = empty_func
    init_score = engine.score
    engine.mario.x_coord = engine.coins[0].x_coord
    engine.mario.y_coord = engine.coins[0].y_coord
    engine.collide_enemy()
    assert engine.score == init_score + 10
