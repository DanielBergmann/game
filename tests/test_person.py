"""
======================
game.tests.test_person
======================
"""
from models.things import Thing
from models.utils import calculate_weight


def test_calculate_weight():
    thing = Thing(name="test", weight=1.5)
    container = thing * 4
    assert calculate_weight(container) == 6.0


def test_calculate_weight_empty():
    assert calculate_weight([]) == 0.0


def test_calculate_weight_wrong_value():
    container = [Thing(name="test2", weight="a")]
    try:
        calculate_weight(container)
    except TypeError:
        assert True
