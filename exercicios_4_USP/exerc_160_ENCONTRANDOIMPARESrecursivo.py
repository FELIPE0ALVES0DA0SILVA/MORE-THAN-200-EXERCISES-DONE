def encontra_impares(lista):
    if len(lista) == 0:
        return []
    if lista[0] % 2 == 1:
        return [lista[0]] + encontra_impares(lista[1:])
    return encontra_impares(lista[1:])


a = [1, 2, 3, 4, 5]
print(encontra_impares(a))
