# Make a program that read the name and weight, saving all in a list. In the end, show:

# A) How many peoples were signed up.
# B)A listing with the peoples more weighted.
# C) A listing with the peoples more slim.

gente = list()
dados = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append((int(input('Peso: '))))
    gente.append(dados[:])
    dados.clear()
    while True:
        pergunta = str(input('Tu queres continuar? [S|N]')).strip().upper()
        if pergunta not in 'SN':
            print()
            print('Resposta inválida...', end='')
        elif pergunta in 'SN':
            break
    if pergunta == 'N':
        break
maior = menor = 0
for posicao, itens in enumerate(gente):
    if posicao == 0 or itens[1] > maior:
        maior = itens[1]
    if posicao == 0 or itens[1] < menor:
        menor = itens[1]
print('Ao todo você cadastrou-se {} pessoas.'.format(len(gente)))
print('O maior peso foi de {} Kg.'.format(maior), end='')
print(' O peso de ', end='||')
for mais in gente:
    if mais[1] == maior:
        print(mais[0], end=' || ')
print('\nO menor peso foi de {} Kg.'.format(menor), end=' ')
print('O peso de ', end='||')
for mais in gente:
    if mais[1] == menor:
        print(mais[0], end=' || ')
