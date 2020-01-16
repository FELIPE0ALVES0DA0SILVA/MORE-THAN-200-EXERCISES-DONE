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
            return pergunta


def linha(tam=42):
    return '_' * tam


def cabecalho(text):
    print(linha())
    print(text.center(42))
    print(linha())


def menu(lista):

    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print('{} - {}'.format(c, item))
        c += 1
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc
