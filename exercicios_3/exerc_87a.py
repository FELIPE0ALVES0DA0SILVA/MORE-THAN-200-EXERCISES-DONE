matriz = [[0,0,0], [0,0,0], [0,0,0]]

for contagem in range(0, 3):
    for valores in range(0,3):
        matriz[contagem][valores] = int(input('Digite o valor {} X {}: '.format(contagem, valores)))
maior = cont = soma = 0
for contagem in range(0, 3):
    for valores in range(0,3):
        print('[{}]'.format(matriz[contagem][valores]), end='')
        if matriz[contagem][valores] % 2 == 0:
            soma += matriz[contagem][valores]
    print()
print(soma)

