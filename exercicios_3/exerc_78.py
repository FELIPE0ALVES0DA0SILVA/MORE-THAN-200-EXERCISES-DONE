# Make a program that read five nummeric values and saved them in a list.

# In the end, show what was the major and the minor entered value and yours respective positions in the list.

num = list()
maior = menor = 0
for c in range(0, 5):
    a = int(input('Digite o número da posição {}: '.format(c)))
    num.append(a)
    if c == 0:
        maior = menor = a
    else:
        if a > maior:
            maior = a
        if a < menor:
            menor = a
print('A lista com os números digitado é: {}'.format(num))
print('O maior valor da lista NUM é o {} e a sua posição é '.format(maior), end='')
for posicao, itens in enumerate(num):
    if itens == maior:
        print('{}'.format(posicao), end=' ')
print('\nO menor valor da lista NUM é o {} e a sua posição é '.format(menor), end='')
for posicao, itens in enumerate(num):
    if itens == menor:
        print('{}'.format(posicao), end=' ')
