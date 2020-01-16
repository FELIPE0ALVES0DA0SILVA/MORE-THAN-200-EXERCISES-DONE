# Create a program that read two values and show a menu in the screen:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa

escolha = 0
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))

while escolha != 5:

    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa ''')
    print('')
    escolha = int(input('Escolha uma das opções de operação abaixo: '))
    if escolha == 5:
        print('Obrigado por ter jogado nosso jogo.')
        break
    if escolha in [1, 2, 3, 4, 5]:
        if escolha == 1:
            somar = a + b
            print('~}{~'*10)
            print('O valor da soma de {} e {} é {}.'.format(a, b, somar))
            print('~}{~'*10)
        elif escolha == 2:
            multiplicar = a * b
            print('~}{~'*10)
            print('O valor da multiplicação de {} e {} é {}.'.format(a, b, multiplicar))
            print('~}{~'*10)
        elif escolha == 3:
            if a > b:
                print('~}{~'*10)
                print('O valor {} é maior que o valor {}.'.format(a, b))
                print('~}{~'*10)
            elif a == b:
                print('~}{~'*10)
                print('Os dois valores são iguais.')
                print('~}{~'*10)
            else:
                print('~}{~'*10)
                print('O valor {} é maior que o valor {}.'.format(b, a))
                print('~}{~'*10)
        elif escolha == 4:
            a = float(input('Digite o valor de a: '))
            b = float(input('Digite o valor de b: '))
            if escolha == 1:

                somar = a + b
                print('~}{~'*10)
                print('O valor da soma de {} e {} é {}.'.format(a, b, somar))
                print('~}{~'*10)
            elif escolha == 2:
                multiplicar = a * b
                print('~}{~'*10)
                print('O valor da multiplicação de {} e {} é {}.'.format(a, b, multiplicar))
                print('~}{~'*10)
            elif escolha == 3:
                if a > b:
                    print('~}{~'*10)
                    print('O valor {} é maior que o valor {}.'.format(a, b))
                    print('~}{~'*10)
                elif a == b:
                    print('~}{~'*10)
                    print('Os dois valores são iguais.')
                    print('~}{~'*10)
                else:
                    print('~}{~'*10)
                    print('O valor {} é maior que o valor {}.'.format(b, a))
                    print('~}{~'*10)
    else:
        print('Escolha inválida.')




