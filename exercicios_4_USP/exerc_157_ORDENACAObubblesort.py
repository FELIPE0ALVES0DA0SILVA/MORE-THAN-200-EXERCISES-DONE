def bubble_sort(lista):
    fim = len(lista)
    for cada in range(fim-1, 0, -1):
        for item in range(cada):
            if lista[item] > lista[item + 1]:
                lista[item], lista[item + 1] = lista[item + 1], lista[item]
                print(lista)
    return lista


