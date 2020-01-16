
# Create a program that have a tuple with several words ( without accents).
# After of this, you should show, for each word, which is yours veals.

lista = ('BALA', 'REFRI', 'COCA', 'CEBOLA', 'CARRO', 'STR', 'NTC', 'PEIDO')
for c in lista:
    print('\nAs vogais da palavra {} são: '.format(c), end='')
    for l in c:
        if l in 'AEIOU':
            print('{}'.format(l.lower()), end=' ')
    if 'A' not in c and 'E' not in c and 'I' not in c and 'O' not in c and 'U' not in c:
        print('Não há vogais nesta palavra.')
