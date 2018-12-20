import pytest
import time
from mario import Mario
from main import Engine

def test_create_mat():
    engine = Engine()
    engine.load_lvl()
    engine.start_time = time.time()
    engine.board.create_mat(engine.mario, [engine.enemies, engine.obstacles,
                          engine.coins, engine.backgrounds], engine.lvl_num)
    assert len(engine.board.matrix) > 0
