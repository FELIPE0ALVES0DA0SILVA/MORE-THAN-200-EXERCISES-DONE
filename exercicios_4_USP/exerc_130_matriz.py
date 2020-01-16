def cria_matriz(num_linhas, num_colunas, valor):
    '''
    -> cria matrizes de forma linear.
    ; param num_colunas: recebe a quantidade de colunas
    ; param num_linhas: recebe a quantidade de linhas
    ; param valor: recebe os valores de cada espaço da matriz.
    return: matriz
    '''
    matriz = []
    for linha in range(num_linhas):
        colunas = []
        for coluna in range(num_colunas):
            colunas.append(valor)
        matriz.append(colunas)
    return matriz


def ler_metriz(num_linhas, num_colunas, valor):
    '''
        -> cria matrizes de forma linear.
        ; param num_colunas: recebe a quantidade de colunas
        ; param num_linhas: recebe a quantidade de linhas
        ; param valor: recebe os valores de cada espaço da matriz.
        return: None
        '''
    vetor = cria_matriz(num_linhas, num_colunas, valor)
    for linha in (vetor):
        for cada in linha:
            print(cada, end='\t')
        print()


def tarefa(mat):
    dim = len(mat)
    for i in range(dim):
        print(mat[i][dim-1-i], end="  ")


def criar_matriz(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(0)
        matriz.append(linha)

    for i in range(num_colunas):
        for j in range(num_linhas):
            matriz[j][i] = int(input("Digite o elemento [" + str(j) + "][" + str(i) + "]: "))

    return matriz


