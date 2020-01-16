# Create a program that manager the enjoyment of a player of soccer.
# The program will read the name of the player and how many matches he played.
# Then will read the amount of goals make by each match.
# In the end, all this will be saved in a dictionary,
# including the total of goals make during the champion.
futebol = {}
goal = []
futebol['gols'] = goal
s = 0
print('-='*20)
nome = str(input('Digite o nome do jogador: '))
futebol['Nome'] = nome
partidas = int(input('Quantas partidas ele jogou: '))
futebol['Partida'] = partidas
for c in range(0, partidas):
    goals = int(input('Quantos goals ele fez na {}° partida? '.format(c + 1)))
    s += goals
    goal.append(goals)
futebol['total'] = s
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