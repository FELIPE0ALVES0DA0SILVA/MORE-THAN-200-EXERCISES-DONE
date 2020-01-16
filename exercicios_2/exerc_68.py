# Make a program that play pair or odd with the computer.
# The game only will break when the player lose,
# showing the total of connectives victories that he conquered in the final match.
from random import randint
x = c = c1 = s = 0
while True:
    s = c + c1
    if x == 1:
        print('Você ganhou {} vezes.'.format(s))
        break
    player = int(input('Digite um valor: '))
    computer = randint(0, 10)
    choice_computer = ''
    choice_player = ''
    while choice_player != 'P' and choice_player != 'I':
        choice_player = str(input('PAR OU ÍMPAR? [ P/I ]')).strip().upper()[0]
    if choice_player == 'P':
        choice_computer = 'I'
    if choice_player == 'I':
        choice_computer = 'P'
    soma = player + computer
    if soma % 2 == 0:
        if choice_computer == 'P' and choice_player == 'I':
            print('Você escolheu {} e o computador escolheu {}'.format(choice_player, choice_computer))
            print('Você jogou {} e o computador {}. Total deu {}, PAR'.format(player, computer, soma))
            print('Você perdeu!!')
            x += 1
        elif choice_computer == 'I' and choice_player == 'P':
            print('Você escolheu {} e o computador escolheu {}'.format(choice_player, choice_computer))
            print('Você jogou {} e o computador {}. Total deu {}, PAR'.format(player, computer, soma))
            print('Você ganhou!!')
            c += 1
    else:
        if choice_computer == 'I' and choice_player == 'P':
            print('Você escolheu {} e o computador escolheu {}'.format(choice_player, choice_computer))
            print('Você jogou {} e o computador {}. Total deu {}, ÍMPAR'.format(player, computer, soma))
            print('Você perdeu!')
            x += 1
        elif choice_computer == 'P' and choice_player == 'I':
            print('Você escolheu {} e o computador escolheu {}'.format(choice_player, choice_computer))
            print('Você jogou {} e o computador {}. Total deu {}, ÍMPAR'.format(player, computer, soma))
            print('Você ganhou!')
            c1 += 1
