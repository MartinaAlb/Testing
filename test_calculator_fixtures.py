import pytest
from calculator import Calc


@pytest.fixture
def kalkulacka1() -> Calc:
    k = Calc(5, 10)
    return k


@pytest.fixture
def kalkulacka2() -> Calc:
    k = Calc(20, 10)
    return k


def test_add(kalkulacka1, kalkulacka2):
    assert kalkulacka1.add() == 15
    assert kalkulacka2.add() == 30


def test_sub(kalkulacka1, kalkulacka2):
    assert kalkulacka1.sub() == -5
    assert kalkulacka2.sub() == 10


def test_sub_rev(kalkulacka1, kalkulacka2):
    assert kalkulacka1.sub(True) == 5
    assert kalkulacka2.sub(True) == -10


def test_mul(kalkulacka1, kalkulacka2):
    assert kalkulacka1.mul() == 50
    assert kalkulacka2.mul() == 200


def test_div(kalkulacka1, kalkulacka2):
    assert kalkulacka1.div() == 0.5
    assert kalkulacka2.div() == 2


def test_div_rev(kalkulacka1, kalkulacka2):
    assert kalkulacka1.div(True) == 2
    assert kalkulacka2.div(True) == 0.5