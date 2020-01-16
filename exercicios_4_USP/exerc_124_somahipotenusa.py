# We say that a number is a hypotenuses of a integer triangle if there's a
# rectangular triangle with integer sides that hypotenuses is equal to this number. In other words,
# n is a hypotenuse if exist integer numbers, such as: n^2 = i^2 + j^2

# Write a function soma_hipotenusas that receive like a parameter a positive integer number n
# and output the sum of all the integers between 1 and n that are
# length of the hypotenuses of some rectangular triangle with integers collars.

from math import sqrt


def e_hipotenusa(valor):
    n = 0
    numeros = []
    while n < valor:
        for contagem in range(1, valor + 1):
            for contar in range(1, valor + 1):
                n = sqrt((contar*contar) + (contagem*contagem))
                if n % 1 == 0 and n <= valor:
                    if n not in numeros:
                        numeros.append(n)
    return numeros


def soma_hipotenusas(valor):
    soma = 0
    numeros = e_hipotenusa(valor)
    for posicao, valor in enumerate(numeros):
        soma += valor
    return soma
