# Make a microsystem that utlize the interactive helping of the python.
# The user will digit the prompt and the manual will appear.
# When the user entered the word 'Fim', the program wrap up itself.

cores = {'fim': '\033[m', 'vermelho': '\033[;41m', 'negrito': '\033[1m', 'amarelo': '\033[;44m', 'branco': '\033[7;30m'}


def ajuda(commando):
    """
    -> Ajuda a encontrar a documentação de qualquer função ou biblioteca desejada.
    ; param comando: Recebe uma frase de início para o programa começar.
    ; return: None
    """
    print('DIGITE " FIM " PARA SAIR DO PROGRAMA.')
    while True:
        print()
        print('{}'.format(cores['vermelho']))
        print('~'*len(commando))
        print('{}{}{}{}'.format(cores['negrito'], commando, cores['fim'], cores['vermelho']))
        print('{}'.format(cores['vermelho']))
        print('~'*len(commando))
        print()
        print('{}'.format(cores['fim']))
        while True:
            pergunta = input('Função ou Biblioteca > ')
            if pergunta.upper()[0] not in 'ABCDEFGHIJKLMNOPQRSTUVXWYZ':
                print('Digite uma função...')
            else:
                break
        if pergunta.upper() == 'FIM':
            print('EXIT')
            break
        print()
        print('{}'.format(cores['amarelo']))
        print('~' * len(commando))
        print('{}{}{}{}'.format(cores['negrito'], commando, cores['fim'], cores['amarelo']))
        print('{}'.format(cores['amarelo']))
        print('~' * len(commando))
        print()
        print('{}'.format(cores['fim']))
        print(cores['branco'])
        help(pergunta.lower())
        print(cores['fim'])


ajuda('SISTEMA DE AJUDA PYHELP')
