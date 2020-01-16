color = {'fim': '\033[m', 'vermelho': '\033[1;31m',
         'amarelo': '\033[1;33m'}


def leiaint(frase):
    while True:
        try:
            pergunta = int(input(frase))
        except ValueError:
            print('Valor inválido')
            continue
        except (KeyboardInterrupt):
            print('Teclado interrompeu a operação acima.')
            continue
        else:
            return '{}O valor {} é um valor da classe int.{}'.format(color['amarelo'], pergunta, color['fim'])


def leiafloat(frase):
    while True:
        try:
            pergunta_float = float(input(frase))
        except (KeyboardInterrupt):
            print('Teclado interrompeu a operação acima.')
            continue
        except (ValueError):
            print('Valor inválido')
            continue
        else:
            return '{}O valor {} é um valor da classe float.{}'.format(color['vermelho'], pergunta_float, color['fim'])



print(leiaint('Digite um número da classe int: '))
print(leiafloat('Digite um número da classe float: '))