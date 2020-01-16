# Give a integer number, major of 1, calculate your decomposition in primes factor.

numero = int(input('Digite um número inteiro: '))
fator = 2
multiplicidade = 0
while numero > 1:
    while numero % fator == 0:
        multiplicidade += 1
        numero /= fator
    if multiplicidade > 0:
        print(' Fator {} multiplicidade: {}'.format(fator, multiplicidade))
        if fator == 2:
            print('O fator {}, é primo!'.format(fator))
        else:
            for contagem in range(2, fator):
                primo = True
                for contar in range(2, contagem):
                    if contagem % contar == 0:
                        primo = False
                        print('Não é primo')
                        break
                if primo:
                    print('O número {}, é primo!'.format(fator))
                    break
    fator += 1
    multiplicidade = 0
