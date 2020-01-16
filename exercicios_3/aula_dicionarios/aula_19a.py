#brazil = []
#estado1 = {'uf': 'Rio de janeiro', 'sigla': 'RJ'}
#estado2 = {'uf': 'São paulo', 'sigla': 'SP'}
#brazil.append(estado1)
#brazil.append(estado2)
#print(brazil[0]['uf'])

estado = dict()
brazil = list()

for c in range(0,3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigle do estado: '))
    brazil.append(estado.copy())
for e in brazil:
    for c in e.values():
        print('O campo tem valor {}'.format( c))


