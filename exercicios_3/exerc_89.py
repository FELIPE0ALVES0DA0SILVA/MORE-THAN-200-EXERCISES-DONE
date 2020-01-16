# Create a program that read name and two notes of several students and save all in a compound list. In the end,
# show a school report keeping the average of each one and
# allow that the user can show the notes of each student individually.
classe = []
alunos = []
notas = []

while True:
    nome = str(input('Digite o nome do aluno: ')).upper().strip()
    nota_1 = float(input('Digite a 1° nota: '))
    nota_2 = float(input('Digite a 2° nota: '))
    alunos.append(nome)
    notas.append(nota_1)
    notas.append(nota_2)
    alunos.append(notas[:])
    classe.append(alunos[:])
    alunos.clear()
    notas.clear()
    while True:
        pergunta = str(input('Tu queres continuar? ')).strip().upper()
        if pergunta not in 'SN':
            print('Resposta inválida...', end='')
        else:
            break
    if pergunta == 'N':
        break
for k in classe:
    for j, l in enumerate(k):
        if j == 0:
            print('{}  {}'.format(j, l), end='')
            print('.'*20, end='')
soma = media = h = 0
for a in classe:
    for e in a[1]:



        for o, u in enumerate(e):
            if o > 1:
                h += 1
                soma += u
print(soma / h)
while True:
    outra = str(input('Tu queres ver as notas de quais alunos? ')).strip().upper()
    if outra not in 'SN':
        print('Valor inválido...', end='')
    else:
        if outra == 'N':
            break
        elif outra == 'S':
            for i in classe:
                for p, v in enumerate(i):
                    if p == 0:
                        print('As notas do {} foram: '.format(v), end='')
                        print('.'*40, end='')
                    if p > 0:
                        print(v)
