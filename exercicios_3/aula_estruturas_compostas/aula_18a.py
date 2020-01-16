#test = list()
#test.append('Gustavo')
#test.append(40)
#print(test)

#galera = list()
#galera.append(test[:])
#test[0] = 'Maria'
#test[1] = 22
#galera.append(test[:])
#print(galera)

#galera = [['joão', 19], ['ana', 33], ['Joaquina', 13], ['maria', 45]]
#for p in galera:
#    print(p)

galera = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Digite seu nome: ')))
    dado.append(int(input('Digite sua idade: ')))
    galera.append(dado[:])
    dado.clear()
for pessoa in galera:
    if pessoa[1] > 20:
        print('{} é maior de idade.'.format(pessoa))
    else:
        print('{} pe menor de idade.'.format(pessoa))