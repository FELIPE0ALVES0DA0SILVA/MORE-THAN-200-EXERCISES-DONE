from exercicios_4_USP import exerc_130_matriz, exerc_134_multiplicamatrizes


def multiplica(matriz_1, matriz_2):
    a, c = len(matriz_1), len(matriz_1[0])
    b, d = len(matriz_2), len(matriz_2[0])
    validacao_matrizes = exerc_134_multiplicamatrizes.sao_multiplicaveis(matriz_1, matriz_2)
    if validacao_matrizes:
        resultado = []
        for linha in range(a):
            resultado.append([])
            for colunas in range(d):
                resultado[linha].append(0)
                for k in range(c):
                    resultado[linha][colunas] += matriz_1[linha][k] * matriz_2[k][colunas]
        return resultado
    else:
        return 'As matrizes não são multiplicáveis.'


matriz_a = [[1, 2], [3, 4], [5, 6]]
matriz_b = [[1, 2, 3], [4, 5, 6]]
print(multiplica(matriz_a, matriz_b))
