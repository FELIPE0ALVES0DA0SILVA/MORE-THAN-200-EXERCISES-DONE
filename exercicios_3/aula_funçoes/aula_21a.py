# def contador(i, f, p):
#    """
#    -> Faz uma contagem e mostra na tela.
#    ; param i: início da contagem
#    ; param f: fim da contagem
#    ; param p: passo da contagem
#    função criada por FELIPE ALVES DA SILVA.

#    """

#    while i <= f:
#        print('{}'.format(i), end='..')
#      i += p
#   print('Fim!')


# help(contador)


# def somar(a=0, b=0, c=0):
#   s = a + b + c
#   print('{} e {} e {}'.format(a, b, c))
#   print('A soma vale {}'.format(s))


# somar(3, 2, 5)
# somar(a=8, c=4)
# somar()


# def teste():
#    global n
#    n = 3
#    x = 8
#    print('Na função teste, n vale {}'.format(n))
#    print('Na função teste, x vale {}'.format(x))


# n = 2
# teste()
# print('No programa principal, n vale {}'.format(n))

# def somar(a=0, b=0, c=0):
#    s = a + b + c
#    return s


# r1 = somar(2, 3, 6)
# r2 = somar(1, 6)
# r3 = somar()
# print('Os resultados foram {}, {} e {}.'.format(r1, r2, r3))

# def fatorial(num):
#    f = 1
#    for c in range(num, 0, -1):
#        f *= c
#    return f

# n = int(input('Digite um número: '))
# print('O fatorial de {} é igual a {}.'.format(n, fatorial(n)))


def par(n = 0):
    if n % 2 == 0:
        return  True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('Par')
else:
    print('ìmpar')
