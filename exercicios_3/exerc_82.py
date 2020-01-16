# Create a program that read several numbers and put in a list.

# After of this, create two extra lists that will save
# just the pair and the odd numbers entered in the original list.

# In the end, show the content of the three lists generated.
original = list()
pares = list()
impares = list()
i = 0
while True:
    i += 1
    numeros = int(input('Digite o {}° número inteiro da lista: '.format(i)))
    while True:
        pergunta = str(input('Tu queres continuar? ')).strip().upper()
        if pergunta not in 'SN':
            print()
            print('Valor digitado inválido, digite novamente: ')
            print()
        elif pergunta == 'N':
            break
        else:
            break
    original.append(numeros)
    if pergunta == 'N':
        break
for posicao, item in enumerate(original):
    if item % 2 == 0:
        pares.append(item)
    else:
        impares.append(item)
original.sort()
impares.sort()
pares.sort()
print('A lista gerada pelos números dados é : {}'.format(original))
print('A lista de todos os seus números ímpares é: {}'.format(impares))
print('A lista de todos os seus números pares é : {}'.format(pares))