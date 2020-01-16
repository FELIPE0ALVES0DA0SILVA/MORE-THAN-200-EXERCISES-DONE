# Improve the challange 093 to that it work with several players.
# Including a system of visualization of details of the improvement of each player.
jogadores = []
futebol = {}
goal = []

s = 0
print('-='*20)
while True:
    nome = str(input('Digite o nome do jogador: '))
    futebol['Nome'] = nome
    partidas = int(input('Quantas partidas ele jogou: '))
    futebol['Partida'] = partidas
    for c in range(0, partidas):
        goals = int(input('Quantos goals ele fez na {}° partida? '.format(c + 1)))
        s += goals
        goal.append(goals)
    futebol['gols'] = goal[:]
    futebol['total'] = s
    jogadores.append(futebol.copy())

    while True:
        pergunta = str(input('Tu queres continuar? [ S|N ] ')).strip().upper()[0]
        if pergunta in 'SN':
            break
        else:
            print('Reesposta inválida, tente novamente. ', end='')
    if pergunta in 'N':
        break

print('COD Nome', end='')
print(' '*18, end='')
print('Gols', end='')
print(' '*18, end='')
print('Total')

for k, v in enumerate(jogadores):
    print('{} '.format(k), end='   ')
    for d in v.values():
        print('{}'.format(str(d)), end='')
        print(' ' * 20, end='')
    print()

while True:
    resp = int(input('Os dados de qual jogador tu queres olhar? [ 999 EXIT ] '))
    if resp == 999:
        break
    if resp < len(jogadores):
        print('Valor inválido... Não existe o jogador o jogador com código {}'.format(resp))
    else:
        print('Levantamento do jogador {}'.format(jogadores[resp]['Nome']))
        for x, n in enumerate(jogadores[resp][goal]):
            print('No jogo {} fez {} gols'.format(x + 1, n))



















'''
print('-='*20)
for c, k in futebol.items():
    if c == 'Nome':
        print('O campo {} tem o valor {}.'.format(c, k))
for c, k in futebol.items():
    if c == 'gols':
        print('O campo {} tem o valor {}.'.format(c, k))

for c, k in futebol.items():
    if c == 'total':
        print('O campo {} tem o valor {}'.format(c, k))
print('-='*20)
for c, k in futebol.items():
    for g, h in futebol.items():
        if c == 'Nome' and g == 'Partida':
            print('O jogador {} jogou {} partidas.'.format(k, h))
            break
print('-='*20)
for g, k in enumerate(goal):
    print('Na partida  {}, fez {} gols.'.format(g, k))
print('-='*20)
'''