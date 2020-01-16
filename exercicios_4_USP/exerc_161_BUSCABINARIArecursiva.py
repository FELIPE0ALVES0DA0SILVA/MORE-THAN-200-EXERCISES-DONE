def busca_binaria_recursiva(lista, elemento, min=0, max=None):
    if max == None:
        max = len(lista) - 1
    if max < min:
        return False
    else:
        meio = max + min // 2
    if lista[meio] > elemento:
        return busca_binaria_recursiva(lista, elemento, min, meio - 1)
    elif lista[meio] > elemento:
        return busca_binaria_recursiva(lista, elemento, meio + 1, max)
    else:
        return lista[meio]

