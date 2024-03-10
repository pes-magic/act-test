import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import src.lib as lib

def test_add():

    assert lib.add(1, 2) == 3
    assert lib.add(0, 0) == 0
    assert lib.add(-1, 1) == 0
    assert lib.add(1, -1) == 0
    assert lib.add(-1, -1) == -2
    assert lib.add(1, 1) == 2
    assert lib.add(1, 0) == 1
    assert lib.add(0, 1) == 1
    assert lib.add(0, -1) == -1
    assert lib.add(-1, 0) == -1
    assert lib.add(0, 0) == 0