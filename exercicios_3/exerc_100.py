# Make a program that have a list called numeros and two function called sorteia()
# and somapar(). The first function will guess five numbers and will put them within of the list and the second function
# will show the sum between all the values pairs guesses for the function
from time import sleep
from random import randint


def sorteia(inicio, fim):
    print('Sorteando {} valores da lista: '.format(fim), end='')
    for lacos in range(inicio, fim):
        sorteado = randint(0, 9)
        sleep(0.5)
        print(sorteado, end=' ', flush=True)
        numeros.append(sorteado)
    print('PRONTO!')

# Core of the program
numeros = []
sorteia(0, 5)


def somapar(numeros):
    soma = 0
    for posicao, valor in enumerate(numeros):
        if valor % 2 == 0:
            soma += valor
    print('Somando os valores pares de {}, temos: {}.'.format(numeros, soma))


somapar(numeros)
