def ordenada(lista):
    lista = lista
    ordena = sorted(lista)
    verdadeiro = 0
    comprimento = len(lista)
    for item in range(len(ordena)):
        for cada in range(len(lista)):
            if item == cada and lista[cada] == ordena[item]:
                verdadeiro += 1
                break
    if verdadeiro == comprimento:
        return True
    else:
        return False


a = [10,10000, 3000, 40000]
print(ordenada(a))
