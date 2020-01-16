# Create a program taht create a array of 3X3 dimension and fullfil with values readied for the keyboard.

# In the end, show the array in the screen, with the correct formation.
matriz = [[], [], []]
for contagem in range(1, 10):
    numeros = int(input('Digite o {} valor da matriz 3X3: '.format(contagem)))
    if contagem <= 3:
        matriz[0].append(numeros)
    if 6 >= contagem > 3:
        matriz[1].append(numeros)
    if 9 >= contagem > 6:
        matriz[2].append(numeros)
print('[ {} ]'.format(matriz[0][0]), end='   ')
print('[ {} ]'.format(matriz[0][1]), end='   ')
print('[ {} ]\n'.format(matriz[0][2]))
print('[ {} ]'.format(matriz[1][0]), end='   ')
print('[ {} ]'.format(matriz[1][1]), end='   ')
print('[ {} ]\n'.format(matriz[1][2]))
print('[ {} ]'.format(matriz[2][0]), end='   ')
print('[ {} ]'.format(matriz[2][1]), end='   ')
print('[ {} ]'.format(matriz[2][2]))



