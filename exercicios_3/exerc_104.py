# create a program that have the function leiaint(), that will work in
# a similar way of a function input() of the python,
# but doing the validation to accept just a numeric value

color = {'fim': '\033[m', 'vermelho': '\033[1;31m',
         'amarelo': '\033[1;33m'}


def leiaint(frase):
    while True:
        pergunta = input(frase)
        if pergunta.isnumeric():
            print('{}O valor {} é um valor da classe int.{}'.format(color['amarelo'], pergunta, color['fim']))
            break
        else:
            print('{}DIGITE UM NÚMERO INTEIRO!!!{}'.format(color['vermelho'], color['fim']))


leiaint('Digite um número: ')
