import pytest
from exercicios_4_USP.exerc_144_AOCUBO import cubo

@pytest.mark.parametrize('entrada, valor_esperado', [
        (0, 0),
        (1, 1),
        (2,8),
        (-2,-8),
        (10, 1000)
])


def test_cubo(entrada, valor_esperado):
    assert cubo(entrada) == valor_esperado
