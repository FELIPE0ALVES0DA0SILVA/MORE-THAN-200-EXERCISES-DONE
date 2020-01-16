def soma_matrizes(matriz_1, matriz_2):
    lin = col = lin_2 = col_2 = 0
    for linha in matriz_1:
        lin += 1
        for coluna in linha:
            col += 1
    for linha_2 in matriz_2:
        lin_2 += 1
        for coluna_2 in linha_2:
            col_2 += 1
    if lin == lin_2 and col == col_2:
        matriz_resultante = []
        soma_matriz = []
        for posicao, linha in enumerate(matriz_1):
            for local, coluna in enumerate(linha):
                soma = matriz_1[posicao][local] + matriz_2[posicao][local]
                soma_matriz.append(soma)
            matriz_resultante.append(soma_matriz[:])
            soma_matriz.clear()
        return matriz_resultante
    else:
        return False
