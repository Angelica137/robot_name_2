from scripts.robot_name import *


def test_get_letters():
    assert len(get_letters()) == 676


def test_get_letters_has_YX():
    assert "YX" in get_letters()


def test_name_pool():
    assert len(name_pool()) == 676000


def test_name_pool_has_WS324():
    assert "WS324" in name_pool()
