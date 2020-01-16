matriz = [[0,0,0],[0,0,0],[0,0,0]]

for contagem in range(0,3):
    for valores in range(0,3):
        matriz[contagem][valores] = int(input('Digite uo valor {} X {}: '.format(contagem, valores)))
for contagem in range(0, 3):
    for valores in range(0, 3):
        print('[{:^5}]'.format(matriz[contagem][valores]), end='')
    print()


