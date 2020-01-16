n = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += n
print('A soma vale {}.'.format(cont))
