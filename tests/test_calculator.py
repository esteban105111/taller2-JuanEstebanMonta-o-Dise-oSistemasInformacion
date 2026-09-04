import pytest

from app.calculator import add, divide, multiply, subtract


def test_sumar_numeros_positivos():
    assert add(5, 3) == 8


def test_sumar_numeros_negativos():
    assert add(-5, -3) == -8


def test_sumar_con_cero():
    assert add(0, 7) == 7


def test_restar_numeros_positivos():
    assert subtract(10, 4) == 6


def test_restar_numeros_negativos():
    assert subtract(-10, -4) == -6


def test_restar_con_cero():
    assert subtract(0, 5) == -5


def test_multiplicar_numeros_positivos():
    assert multiply(6, 7) == 42


def test_multiplicar_numeros_negativos():
    assert multiply(-6, -7) == 42


def test_multiplicar_por_cero():
    assert multiply(9, 0) == 0


def test_dividir_numeros_positivos():
    assert divide(20, 5) == 4


def test_dividir_numeros_negativos():
    assert divide(-20, -5) == 4


def test_dividir_con_resultado_decimal():
    assert divide(5, 2) == 2.5


def test_dividir_entre_cero():
    with pytest.raises(ValueError, match="No se puede dividir entre cero"):
        divide(10, 0)
