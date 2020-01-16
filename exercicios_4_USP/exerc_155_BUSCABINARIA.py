from random import randint

def busca_binaria( lista, x):
    primeiro = 0
    ultimo = len(lista) - 1
    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        if lista[meio] == x:
            return meio
        elif x < lista[meio]:
            ultimo = meio - 1
        else:
            primeiro = meio + 1
    return -1


a = [randint(-10000000, 1000000) for x in range(10000000)]
print(busca_binaria(a, 760))
