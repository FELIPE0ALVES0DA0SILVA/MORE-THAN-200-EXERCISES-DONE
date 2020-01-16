# Create a program that have a function factorial() that input two paramters; The first parameter that show the
# number to calculate and the other called show, that will be a logic value (opcional)
# showing if will be showed or not in the screen the process of calculus of the factorial.


def factorial(numero, show=False):
    """
    -> Função cálcula o fatorial de qualquer número.
    ; param numero: Traz o número digitado pelo usuário
    ; param show: Traz o valor True, caso o usuário queira ver a resolução do fatorial,
    ou False, caso o usuário não queira ver a resolução do fatorial respectivamente.
    return: None
    """
    if show:
        if numero == 0 or numero == 1:
            print('O factorial de {} é {}'.format(numero, 1))
        else:
            print('O fatorial de {} é: '.format(numero), end='')
            fac = 1
            for contagem in range(numero, 0, -1):
                fac *= contagem
                while contagem > 1:
                    print(contagem, end=' X ')
                    break
                if contagem < 2:
                    print(contagem, end=' ')
            print('= {}'.format(fac))
    else:
        if numero == 0 or numero == 1:
            print('O factorial de {} é {}'.format(numero, 1))
        else:

            fac = 1
            for contagem in range(numero, 0, -1):
                fac *= contagem
            print('O fatorial de {} é: {}'.format(n, fac))


n = int(input('Digite o número, para calcularmos o seu fatorial: '))
while True:
    pergunta = str(input('Tu queres ver a resolução do fatorial acima? [ S | N ] ')).strip().upper()[0]
    if pergunta in 'SN':
        if pergunta == 'S':
            pergunta = True
            break
        else:
            pergunta = False
            break
    else:
        print('Resposta inválida, cara!')
factorial(n, pergunta)

help(factorial)
