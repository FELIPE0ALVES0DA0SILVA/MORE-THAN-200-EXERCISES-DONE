
noem = str(input('Qual é o seu nome? '))

if noem == 'Felipe':
    print('Que nome bonito {}.'.format(noem))
elif noem == 'Pedro' or noem == 'Paulo' or noem == 'Juliana':
    print('Seu nome é bem popular no Brasil')
elif noem in 'Karina noronha de paula':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal, cara ')
print('Tenha um bom dia {}.'.format(noem))

