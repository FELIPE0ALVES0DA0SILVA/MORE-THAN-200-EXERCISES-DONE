# Make a program that have a function notas()
# that can input several notes of students and will
# return a dictionary with the following information:

#               - The amount of notes
#               - The major note
#               - The average of the class
#               - The situation( optional)

# Add also the docstrings of the function

final = {}
status = ''


def notas(resutado, condicao=False):
    """
    -> CALCULA A MÉDIA, QUAL É O MAIOR VALOR DENTRO DE UMA LISTA E A QUANTIDADE DE VALORES DENTRO DA MESMA LISTA.
    ; param resultado: Carrega a lista com os valores a serem operados
    ; param condicao: Carrega a resposta do usuário, se ele quer ou não ver a situação média da classe.
    ; return: None
    """
    global status
    contagem = maior = somar = 0
    for contagem, valor in enumerate(resutado):
        somar += valor
        if contagem == 0 or valor > maior:
            maior = valor
    if not condicao:
        print(resutado)
    else:
        if somar/(contagem + 1) <= 5:
            status = 'RUIM PRA CARAMBA, BICHO!'
            print('RUIM PRA CARAMBA, BICHO!')
        elif 7 >= somar/(contagem + 1) > 5:
            status = 'MAIS OU MENOR...MAIS OU MENOS'
            print('MAIS OU MENOS...MAIS OU MENOS')
        else:
            status = 'AÍ SIM GAROTÃO!'
            print('AÍ SIM GAROTÃO!')
    final['Situação'] = status
    final['Total'] = contagem + 1
    final['Média'] = somar/(contagem + 1)
    final['Maior'] = maior
    print('A média entre os valores da lista é: {}.'.format(somar / (contagem + 1)))
    print('O maior valor da lista é {}.'.format(maior))
    print('O total de valores da lista é: {}.'.format(contagem + 1))
    print()
    print(final)


lista_nota = []
i = 0
while True:
    i += 1
    if i <= 2:
        for c in range(0, 2):
            while True:
                nota = float(input('Digite todas as notas dos alunos: '))
                if 10 >= nota >= 0:
                    break
                else:
                    print('Quê??? VOLTA! ')
            lista_nota.append(nota)
    while True:
        pergunta = str(input('Tu queres continuar: [ S | N ] ')).strip().upper()[0]
        if pergunta in 'SN':
            if pergunta == 'N':
                break
            else:
                while True:
                    nota = float(input('Digite todas as notas dos alunos: '))
                    if 10 >= nota >= 0:
                        break
                    else:
                        print('Quê??? VOLTA! ')
                lista_nota.append(nota)
        else:
            print('Resposta inválida, cabação!')
    if pergunta == 'N':
        while True:
            situacao = str(input('Tu também queres saber a situação da classe? [ S | N ] ')).strip().upper()[0]
            if situacao in 'SN':
                if situacao == 'S':
                    situacao = True
                    break
                else:
                    situacao = False
                    break
            else:
                print('RESPOSTA INVÁLIDA, MISERÁVI!!!')
        break

notas(lista_nota, situacao)
help(notas)
