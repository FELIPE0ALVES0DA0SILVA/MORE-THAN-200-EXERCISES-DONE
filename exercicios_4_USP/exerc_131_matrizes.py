def dimensoes(matriz):
    c_linha = c_coluna = 0
    for linha in matriz:
        c_linha += 1
        c_coluna = 0
        for coluna in linha:
            c_coluna += 1
    print('{}X{}'.format(c_linha, c_coluna))

