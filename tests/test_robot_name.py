from scripts.robot_name import get_letters


def test_get_letters():
    assert len(get_letters()) == 676
