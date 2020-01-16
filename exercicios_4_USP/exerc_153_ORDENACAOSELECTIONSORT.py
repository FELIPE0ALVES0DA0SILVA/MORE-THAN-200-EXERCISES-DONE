def ordena(lista):
    fim = len(lista)
    for minimo_inicial in range(fim - 1):
        posicao_minimo = minimo_inicial
        for cada in range(minimo_inicial + 1, fim):
            if lista[cada] < lista[posicao_minimo]:
                posicao_minimo = cada
        lista[minimo_inicial], lista[posicao_minimo] = lista[posicao_minimo], lista[minimo_inicial]
    return lista


a = [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(ordena(a))