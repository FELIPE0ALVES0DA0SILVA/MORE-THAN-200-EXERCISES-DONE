def sao_multiplicaveis(matriz_1, matriz_2):
    l_matriz_2 = c_matriz_1 = 0
    for linha in matriz_1:
        for coluna in linha:
            c_matriz_1 += 1
        break
    for linha in matriz_2:
        l_matriz_2 += 1
    if l_matriz_2 == c_matriz_1:
        return True
    else:
        return False
