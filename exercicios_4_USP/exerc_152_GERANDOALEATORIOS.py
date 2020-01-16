from random import randint


def lista_grande(n):
    lista = []
    for conta in range(n):
        gerou = randint(-n, n)
        lista.append(gerou)
    return lista


print(lista_grande(20))