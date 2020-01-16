# Create a program that have a unique tuple with names of products and your respectively prices, in the sequence.

# In the end, show a listing of prices, organizing the data in tabular form.
from typing import Union

lista = ('Feijão', 10, 'Frauda', 23, 'Maça', 1.57, 'bolacha', 0.67, 'Azeite', 17.893)
print('{:-^40}'.format('LISTA DE PRODUTOS'))
for c in range(0, len(lista)):
    if c % 2 == 0:
        print('{:.<30}'.format(lista[c]), end='')
    else:
        print('R$ {:>6.2f}'.format(lista[c]))
print('-'*40)


