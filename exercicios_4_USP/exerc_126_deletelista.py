
def remove_repetidos(lista):
    lista.sort()
    for i, v in enumerate(lista):
        if lista[i - 1] == lista[i]:
            lista.remove(v)
    return lista


print(remove_repetidos([100, 89, 100, 2, 2, 35, 35]))
