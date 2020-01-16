from exercicios_4_USP.exerc_143_BHASKARApytest import Bhaskara
import pytest

@pytest.mark.parametrize('a, b, c, resultado', [(10, 20, 10, (1, -10))])


class Test_Bhaskara:
    def testa_uma_raiz(self, a, b, c, resultado):
        bhas = Bhaskara()
        assert bhas.calcular(a, b, c) == resultado
