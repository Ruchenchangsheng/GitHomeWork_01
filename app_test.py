from app import add


def test_app():
    assert add(1, 2) == 3
    assert add(-1,  1) == 0
    assert add(0,  0) == 0
