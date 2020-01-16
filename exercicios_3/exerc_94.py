# Create a program that read name, sex and age of several peoples, saving the data of each people in a dictionary and all the dictionary in a list. In the end, show:

# A) How many peoples were signed up
# B) The average of each in the group
# C) The list with all the woman
# D) A list with all the peoples with age above of the average
grupo = []
pessoas = {}
while True:
    nome = str(input('Nome: '))
    pessoas['nome'] = nome
    while True:
        sexo = str(input('Sexo: [ M|F ] ')).strip().upper()[0]
        if sexo in 'MF':
            if sexo == 'M':
               pessoas['sexo'] = sexo
               break
            else:
                pessoas['sexo'] = sexo
                break
        else:
            print('Tente novamente.', end='')
    idade = int(input('Idade: '))
    pessoas['idade'] = idade
    grupo.append(pessoas.copy())
    while True:
        pergunta = str(input('Tu queres continuar? ')).strip().upper()[0]
        if pergunta in 'SN':
            break
        else:
            print('Resposta inválida, tente novamente', end=' ')
    if pergunta == 'N':
        break
i = s = m = z = 0
for c in range(0, len(grupo)):
    i = c
print('Pessoas do sexo feminino são: ', end='')
for c in grupo:
    for k, g in enumerate(c):
        if g == 'idade':
            z += 1
            s += c[g]
            m = s / z
        if g == 'sexo':
            if c[g] == 'F':
                print('{}'.format(c['nome']), end=' ')
print()
print('A soma de todas as idades é: {}'.format(s))
print('A média entre todas as idade recebidas é: {}'.format(m))
print('As pessoas com idade maior que a média de idades do grupo são: ', end='')
for c in grupo:
    for v, b in enumerate(c):
        if b == 'idade':
            if c[b] > m:
                print('{}'.format(c['nome']), end=' ')
