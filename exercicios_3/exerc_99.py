# Make a program that have a function called maior(), that input several parameters with integers values.
# Your program have that analyse all the values and say what of them is the major.

from time import sleep


def maior(* valores):
    print('=-'*30)
    print('Analisando os valores processados...')
    for contador, inteiro in enumerate(valores):
        if len(valores) == 1 and inteiro == 0:
            print('Foram informados {} valores ao todo'.format(inteiro))
            print('Não há maior ou menor valor.')
            break
        elif len(valores) == 1 and inteiro > 0:
            grande = posicao = 0
            for posicao, valor in enumerate(valores):
                print(valor, end=' ', flush=True)
                sleep(0.5)
                if posicao == 0 or valor > grande:
                    grande = valor
            print('Foram informados {} valores ao todo.'.format(posicao + 1))
            print('O maior valor informado foi {}.'.format(grande))
            break
        else:
            grande = posicao = 0
            for posicao, valor in enumerate(valores):
                print(valor, end=' ', flush=True)
                sleep(0.5)
                if posicao == 0 or valor > grande:
                    grande = valor
            print('Foram informados {} valores ao todo.'.format(posicao + 1))
            print('O maior valor informado foi {}.'.format(grande))
            break


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(6)
maior(0)
