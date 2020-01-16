from exercicios_4_USP.exerc_161_BUSCABINARIArecursiva import busca_binaria_recursiva
from pytest import mark
from random import randrange

@mark.parametrize('lis, elemento, esperado', [([1, 2, 5, 450, 600], 450 , 450),
                                               ([randrange(-900, 10)], -901, False),
                                               ([x for x in range(11)], 3, 3),
                                               ([x for x in range(10001)], 10000, 10000)])


class Test_BUSCArecursiva:
    def test_BUSCABINARIA(self, lis, elemento, esperado):
        assert busca_binaria_recursiva(lis, elemento) == esperado

