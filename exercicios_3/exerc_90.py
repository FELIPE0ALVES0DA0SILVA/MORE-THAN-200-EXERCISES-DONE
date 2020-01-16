# Make a program that read name and average of a student,
# saving also the situation in a dictionary.
# In the end, show the content of the structure in the screen.

dicionario = {}


dicionario['nome'] = str(input('Nome: '))
for c in dicionario.values():
    media = float(input('Média de {}: '.format(c)))
    dicionario['Média'] = media
    if media >= 7:
        for c, k in dicionario.items():
            if c == 'nome:':
                print('{} é igual a {}.'.format(c, k))
            else:
                print('{} é igual a {}.'.format(c, k))
        print('Você foi aprovado.')
    else:
        for c, k in dicionario.items():
            if c == 'nome:':
                print('{} é igual a {}.'.format(c, k))
            else:
                print('{} é igual a {}.'.format(c, k))
        print('Você foi reprovado.')
    break

