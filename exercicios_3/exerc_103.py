# Make a program that have a function called ficha(),
# that input two parameters optionals: the name of a player and how many goals he did.

# The program will should be able to show the token of the player,
# even that some data do  not have been informed correctly.


def ficha(nome='', gols =''):
    print('O nome do jogador é', end=' ')
    if nome == '':
        print('desconhecido', end='')
    if nome != '':
        print(nome, end=' ')
    if gols == '' or gols.upper()[0] in 'ABCDEFGHIJKLMNOPQRSTUVXWYZ':
        print(', fez {} gol(s) no campeonato.'.format(0))
    else:
        print(', fez {} gol(s) no campeonato.'.format(gols))




n = str(input('Digite o nome do jogador: '))
g = input('Digite a quantidade de gols que ele fez no campeonato: ').strip()
ficha(n, g)
