# In this game, N parts are initially willing in a table or board.
# Two players playing alternately, pulling out at least 1 and in the
# maximum M parts each one. Who take the possibles parts parts win the game.


def cabecalho(nome, booleano=0):
    if booleano:
        print('*' * 4, end='')
        print(' {} {} '.format(nome, booleano), end='')
        print('*' * 4)
    else:
        print('*' * 4, end='')
        print(' {} '.format(nome), end='')
        print('*' * 4)


def escolha():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print()
    while True:
        try:
            uma_partida = int(input('1 - para jogar uma partida isolada\n2 - para jogar um campeonato '))
        except:
            print('Resposta inválida.')
        else:
            if uma_partida == 1 or uma_partida == 2:
                return uma_partida
            else:
                print('Valor inválido.')


def usuario_escolhe_jogada(pecas, limite):
    while True:
        while True:
            try:
                user = int(input("Quantas peças você vai tirar? "))
                print()
            except:
                print('Resposta inválida!')
            else:
                break
        if limite >= user > 0 and user <= pecas:
            print("Você tirou", user, "peças")
            pecas -= user
            print("Agora restam", pecas, "peças no tabuleiro.")
            print()
            break
        else:
            print("Oops! Jogada inválida! Tente de novo.")
            print()
    return user


def computador_escolhe_jogada(pecas, limite):
    if pecas != 0:
        if pecas % (limite + 1) != 0:
            jogada = (pecas % (limite + 1)) - pecas - (- pecas)
            if jogada == 1:
                print("O computador tirou uma peça.")
                pecas = pecas - jogada
            else:
                print("O computador tirou", jogada, "peças.")
                pecas = pecas - jogada
            if pecas > 0:
                print("Agora restam", pecas, "peças no tabuleiro.")
                print()
        else:
            jogada = limite
            print("O computador tirou", jogada, "peças.")
            pecas = pecas - jogada
            if pecas > 0:
                print("Agora restam", pecas, "peças no tabuleiro.")
                print()
        return jogada


def partida():
    pecas = int(input('Quantas peças? '))
    limite = int(input('Limite de peças por jogada? '))
    if pecas % (limite + 1) == 0:
        print()
        print('Você começa!')
        print()
        while pecas > limite:
            user = usuario_escolhe_jogada(pecas, limite)
            pecas -= user
            if pecas > limite:
                jogada = computador_escolhe_jogada(pecas, limite)
                pecas = pecas - jogada
        jogada = computador_escolhe_jogada(pecas, limite)
        pecas = pecas - jogada
        if pecas == 0:
            print('Fim do jogo! O computador ganhou!')
    else:
        print()
        print('Eu começo!')
        print()
        while pecas > limite:
            jogada = computador_escolhe_jogada(pecas, limite)
            pecas = pecas - jogada
            if pecas > limite:
                user = usuario_escolhe_jogada(pecas, limite)
                pecas -= user
        jogada = computador_escolhe_jogada(pecas, limite)
        pecas = pecas - jogada
        if pecas == 0:
            print('Fim do jogo! O computador ganhou!')


def campeonato():
    for quantidade in range(0, 3):
        print()
        cabecalho('RODADA', quantidade + 1)
        print()
        partida()
    return 'FIM DO CAMPEONATO'


def principal():
    if escolha() == 1:
        return partida()

    else:
        print()
        print('Voce escolheu um campeonato!')
        print()
        campeonato()
        print()
        cabecalho('Final do campeonato!')
        print()
        return 'Placar: Você 0 X 3 Computador'


print(principal())
