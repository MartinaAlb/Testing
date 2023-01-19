import pytest
from calculator import Calc


# sčítání
@pytest.mark.parametrize("prvni_hodnota, druha_hodnota, ocekavany_soucet", [
    (1, 2, 3), (1, 0, 1), (-1, -2, -3), (1.5, -5, -3.5), (0, -3, -3),
])
def test_add_parametrize(prvni_hodnota, druha_hodnota, ocekavany_soucet):
    moje_kalkulacka = Calc(prvni_hodnota, druha_hodnota)
    assert moje_kalkulacka.add() == ocekavany_soucet

# odčítání
@pytest.mark.parametrize("prvni_hodnota, druha_hodnota, ocekavany_rozdil", [
    (1, 2, -1), (1, 0, 1), (-1, -2, 1), (1.5, -5, 6.5), (0, -3, 3),
])
def test_sub_parametrize(prvni_hodnota, druha_hodnota, ocekavany_rozdil):
    moje_kalkulacka = Calc(prvni_hodnota, druha_hodnota)
    assert moje_kalkulacka.sub() == ocekavany_rozdil

# násobení
@pytest.mark.parametrize("prvni_hodnota, druha_hodnota, ocekavany_nasobek", [
    (1, 2, 2), (1, 0, 0), (-1, -2, 2), (1.5, -5, -7.5), (0, -3, 0),
])
def test_mul_parametrize(prvni_hodnota, druha_hodnota, ocekavany_nasobek):
    moje_kalkulacka = Calc(prvni_hodnota, druha_hodnota)
    assert moje_kalkulacka.mul() == ocekavany_nasobek

# dělení
@pytest.mark.parametrize("prvni_hodnota, druha_hodnota, ocekavany_podil", [
    (1, 2, 0.5), (1, 0.1, 10), (-1, -2, 0.5), (1.5, -5, -0.3), (0, -3, 0),
])
def test_div_parametrize(prvni_hodnota, druha_hodnota, ocekavany_podil):
    moje_kalkulacka = Calc(prvni_hodnota, druha_hodnota)
    assert moje_kalkulacka.div() == ocekavany_podil

def test_div_error():
    prvni_hodnota = 3
    druha_hodnota = 0
    moje_kalkulacka = Calc(prvni_hodnota, druha_hodnota)
    with pytest.raises(ZeroDivisionError):
        moje_kalkulacka.div()

def test_div_reverse():
    prvni_hodnota = 2
    druha_hodnota = -1
    moje_kalkulacka = Calc(prvni_hodnota, druha_hodnota)
    assert moje_kalkulacka.div(reversed) == -0.5

def test_sub_reverse():
    prvni_hodnota = 2
    druha_hodnota = -1
    moje_kalkulacka = Calc(prvni_hodnota, druha_hodnota)
    assert moje_kalkulacka.sub(reversed) == -3