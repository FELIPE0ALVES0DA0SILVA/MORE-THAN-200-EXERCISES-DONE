from exercicios_4_USP.exerc_116 import fatir
import pytest


def Test_fatir1():
    assert fatir(1) == 1


def test_fatir2():
    assert fatir(2) == 2


def test_fatir0():
    assert fatir(0) == 1


def test_fatir5():
    assert fatir(5) == 120

pytest


