# Create a program that will generate five random numbers and it in a tuple. After it, show the listable of numbers generate and also show the minor and the major value that it is in the tuple.

from random import randint

g = (randint(-999, 999),
    randint(-999, 999),
    randint(-999, 999),
    randint(-999, 999),
    randint(-999, 999))
print('A listagem dos números gerados aleatoriamente é: ', end=' ')
for i in range(0, len(g)):
    print(g[i], end=' ')
print('\nO menor valor da lista acima é {}.'.format(sorted(g)[0]))
print('O maior valor da lista acima: {}'.format(sorted(g)[-1]))
