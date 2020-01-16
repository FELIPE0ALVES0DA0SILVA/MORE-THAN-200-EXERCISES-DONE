# Create a program taht create a array of 3X3 dimension and fullfil with values readied for the keyboard.
# In the end, show the array in the screen, with the correct formation.
# improve the last challenge, showing in the end:

# A) The sum of all the pair values entered.
# B) The sum of the values of the third column.
# C) The major values of the second line.

matriz = [[], [], []]
i = c = soma = soma_3 = maior = 0
for contagem in range(1, 10):
    numeros = int(input('Digite o {} valor da matriz 3X3: '.format(contagem)))
    if contagem <= 3:
        matriz[0].append(numeros)
    if 6 >= contagem > 3:
        matriz[1].append(numeros)
    if 9 >= contagem > 6:
        matriz[2].append(numeros)
print('~O~'*7)
print('[ {} ]'.format(matriz[0][0]), end='   ')
print('[ {} ]'.format(matriz[0][1]), end='   ')
print('[ {} ]\n'.format(matriz[0][2]))
print('[ {} ]'.format(matriz[1][0]), end='   ')
print('[ {} ]'.format(matriz[1][1]), end='   ')
print('[ {} ]\n'.format(matriz[1][2]))
print('[ {} ]'.format(matriz[2][0]), end='   ')
print('[ {} ]'.format(matriz[2][1]), end='   ')
print('[ {} ]'.format(matriz[2][2]))
print('~O~'*7)
for itu in matriz:
    for posicao, itens in enumerate(itu):
        c += 1
        if 6 >= c > 3:
            if posicao == 0:
                maior = itens
            else:
                if itens > maior:
                    maior = itens
for iteracao in matriz:
    for cada in iteracao:
        if cada % 2 == 0:
            soma += cada
for itei in matriz:
    for item in range(len(itei)):
        i += 1
        if i == 3 or i == 6 or i == 9:
            soma_3 += itei[item]
print('A soma dos valores é: {}'.format(soma))
print('A soma dos valores da terceira linha é: {}'.format(soma_3))
print('O maior valor da segunda linha é: {}'.format(maior))

