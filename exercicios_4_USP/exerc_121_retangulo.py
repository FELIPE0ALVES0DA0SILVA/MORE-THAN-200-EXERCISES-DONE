# Write a program that receive like input two
# integer numbers correspondent to the width and to the high of a rectangle, respectively. The program should print a
# characters chain that represent the rectangle informed with characters '#' in the output.

largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
coluna = linha = 1
while coluna <= altura:
    while linha <= largura:
        print('#', end='')
        linha += 1
    coluna += 1
    print()
    linha = 1
