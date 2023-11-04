"""
======================
game.tests.test_person
======================
"""
from models.person import calculate_weight, Thing


def test_calculate_weight():
    thing = Thing(name='test', weight=1.5)
    container = thing*4
    assert calculate_weight(container) == 6.0
