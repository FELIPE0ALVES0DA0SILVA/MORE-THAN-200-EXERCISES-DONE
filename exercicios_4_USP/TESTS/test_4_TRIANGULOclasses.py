from exercicios_4_USP.exerc_145_TRIANGULOclasses import Triangulo
import pytest


@pytest.mark.parametrize('foo, doo, coo, bar', [(1, 1, 1, 3), (2, 1, 2, 5), (3, 2, 1, 6), (5, 10, 19, 34), (0, 0, 0, 0)])

class Test_triangulo:
    def test_triangulo(self, foo, doo, coo, bar):
        t = Triangulo(foo, doo, coo)
        assert t.perimetro() == bar
    def test_a(self, foo, doo, coo, bar):
        t = Triangulo(foo, doo, coo)
        assert t.a == foo
    def test_b(self, foo, doo, coo, bar):
        t = Triangulo(foo, doo, coo)
        assert t.b == doo
    def test_c(self, foo, doo, coo, bar):
        t = Triangulo(foo, doo, coo)
        assert t.c == coo
