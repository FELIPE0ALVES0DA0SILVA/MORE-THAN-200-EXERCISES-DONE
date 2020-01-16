from exercicios_4_USP.exerc_143_BHASKARApytest import Bhaskara
import pytest


class TestBhaskara:
    @pytest.fixture
    def b(self):
        return Bhaskara()
    def testa_uma_raiz(self, b):
        assert b.calcular(1, 0, 0) == (1, 0)
    def testa_duas_raiz(self, b):
        assert b.calcular(1, -5, 6) == (2, 3, 2)
    def testa_zero_raiz(self, b):
        assert b.calcular(10, 10, 10) == 0
    def testa_negativa_raiz(self, b):
        assert b.calcular(10, 20, 10) == (1, -10)
