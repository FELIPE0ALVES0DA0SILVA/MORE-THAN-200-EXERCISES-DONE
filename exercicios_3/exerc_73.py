# Create a tuple fulfilled with the twenty firster places of the table of the soccer brazilian champion,
# in the order of placing. After show:

# Just the 5 first placing.
# The last 4 placing of the table.
# A list with the team in alphabetic order;
# In what position in the table is the team of the chapecoense.

team = ('FLAMENGO', 'SANTOS', 'PALMEIRAS', 'GRÊMIO', 'ATHLETICO - PR', 'SÃO PAULO', 'INTERNACIONAL', 'CORINTHIANS',
        'FORTALEZA', 'GOIÁS', 'BAHIA', 'VASCO DA GAMA', 'ATHLETICO - MG', 'FLUMINENSE', 'BOTAFOGO', 'CEARÁ SC', 'CRUZEIRO', 'CSA', 'CHAPECOENSE', 'AVAÍ')
print('{:+^300}'.format('  CAMPEONATO BRASILERO 2019  '))
print('A lista de times do campeonato brasileiro: {}'.format(team))
print('+'*300)
print()
print('|\|/'*20)
print('Os primeiros cinco colocados do brasileirão 2019 foram {}.'.format(team[:5]))
print('|\|/'*20)
print('Os últimos quatro colocados do brasileirão foram {}.'.format(team[-4:]))
print('|\|/'*50)
print('Os times em ordem alfabética: {}'.format(sorted(team)))
print('|\|/'*50)
print('O time da chapecoense está na posição {}° do campeonato brasileiro.'.format(team.index('CHAPECOENSE') + 1))
print('|\|/'*20)
