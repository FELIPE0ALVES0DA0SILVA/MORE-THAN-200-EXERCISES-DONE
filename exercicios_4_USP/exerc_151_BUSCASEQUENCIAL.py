def busca(lista, elemento):
    for item in range(len(lista)):
        if lista[item] == elemento:
            return item
    return False


print(busca([12, 13, 14], 15))