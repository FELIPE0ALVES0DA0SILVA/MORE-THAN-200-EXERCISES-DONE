# Make a program that read any number and show your factorial.

n = int(input('Digite um numero para calcular o seu fatorial: '))
c = n
print('Calculando {}! = '.format(n), end=' ')
if n > 0:
    while c != 1:
        c -= 1
        n *= c
        print('{}'.format(c), end='')
        print(' X ' if c > 1 else ' = ', end='')
print('{}'.format(n))





