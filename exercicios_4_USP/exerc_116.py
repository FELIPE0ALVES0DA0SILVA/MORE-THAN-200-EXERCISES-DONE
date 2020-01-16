# Make a factorial function and implemented a automated testing.
import pytest


def fatir(valor=1):
    soma = 1
    for contagem in range(valor, 0, -1):
        soma *= contagem
    return soma


def binomial(n, k):
    binomio = fatir(n)/ (fatir(k)*fatir(n - k))
    return binomio


def numeral():
    while True:
        try:
            numeros = int(input('Quantos números tu tens: '))
        except:
            print('Valor inválido, digite um número inteiro.')
        else:
            return  numeros


def combinacoes():
    while True:
        try:
            combinar = int(input('Quantas combinação tu queres: '))
        except:
            print('Valor novamente inválido, digite um número inteiro.')
        else:
            return combinar
