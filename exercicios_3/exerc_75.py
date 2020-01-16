# Develop a program that read four values for the keyboard and saved them in a tupla. In the end, show>

# How many  times appeared the value 9.
# In what position was entered the first value 3.
# Which was the pair numbers,

g = (int(input('Digite um número: ')),
     int(input('Digite OUTRO número: ')),
     int(input('Digite MAIS UM número: ')),
     int(input('Digite O ÚLTIMO número: ')))
print('Você digitou os valores: {}.'.format(sorted(g)))
print('O valor 9 apareceu {} vezes.'.format(g.count(9)))
if 3 in g:
    print('O valor 3 foi digitado na {}° POSIÇÃO da lista.'.format(g.index(3) + 1))
else:
    print('O valor 3 não foi digitado nesta lista.')
print('Os valores pares dos valores digitados são: ', end='')
for x in g:
    if x % 2 == 0:
        print(x, end=' ')
