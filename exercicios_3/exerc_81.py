# Create a program that read several numbers and put in a list.

# After of this, show:

# A) how many numbers were entered.
# B) The list of values ordered in a decreased way.
# C) If the value 5 was entered and be or not in the list.
i = 0
valores = list()
while True:
    i += 1
    numeros = int(input('Digite o {}° número: '.format(i)))
    while True:
        pergunta = str(input('Tu queres continuar: [ S | N ]')).upper().strip()
        if pergunta not in 'SN':
            print('Resposta inválida, digite novamente.')
        elif pergunta == 'N':
            break
        else:
            break
    valores.append(numeros)
    if pergunta == 'N':
        break
print('{} números foram digitados.'.format(len(valores)))
if 5 in valores:
    print('O valor 5 foi faz parte da lista. E aparece {} vezes nas posições: '.format(valores.count(5)), end='')
    for posicao, item in enumerate(valores):
        if 5 == item:
            print('{}...'.format(posicao), end='')
else:
    print('O valor 5 não faz parte da lista.')
valores.sort(reverse=True)
print('\nA lista de valores ordenada de forma decrescente: {}'.format(valores))
