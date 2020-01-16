from exercicios_4_USP.exerc_146_TRIANGULOTIPOclasses import Triangulo
import pytest


@pytest.mark.parametrize('foo, doo, coo, tipo', [(10, 10, 10, 'equilátero'), (1, 3, 5, 'escaleno'), (4, 2, 4, 'isósceles'), (30, 30, 30, 'equilátero'), (12, 234, 3, 'escaleno'), (400, 400, 4, 'isósceles')])

class Test_triangulo_tipo:
    def test_escaleno(self, foo, doo, coo, tipo):
        t = Triangulo(foo, doo, coo)
        assert t.tipo_lado() == tipo
