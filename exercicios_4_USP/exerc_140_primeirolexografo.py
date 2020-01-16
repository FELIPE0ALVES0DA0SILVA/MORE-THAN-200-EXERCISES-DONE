def primeiro_lex(list):
    dict = {}
    lista = []
    for cada in list:
        dict[cada] = cada
    for local, valor in dict.items():
        converter = ord(valor[0])
        lista.append(converter)
        dict[valor] = converter
    lista.sort()
    a = sorted(dict.items())
    for local, valor in a:
        for posicao, cada in enumerate(lista):
            if cada == valor:
                lista[posicao] = local
                break
    return lista[0]
