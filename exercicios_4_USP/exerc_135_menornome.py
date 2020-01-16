def lista_nome():
    lista = {}
    while True:
        try:
            nome = str(input('Digite um nome qualquer:')).strip().capitalize()
        except:
            print('Valor inválido! Tente novamente')
        else:
            lista[nome] = nome
        while True:
            pergunta = ''
            try:
                pergunta = str(input('Tu queres continuar? [ S|N ] ')).strip().upper()
            except:
                print('Erro de sintaxe! tente novamente')
            if pergunta == 'S' or pergunta == 'N':
                break
            else:
                print('Resposta inválida! Digite novamente.')
        if pergunta == 'N':
            return lista


def menor_nome(dict=None):
    condicao = dict
    if condicao == None:
        lista_nomes = lista_nome()
    else:
        lista_nomes = condicao
    for valor, nome in lista_nomes.items():
        valor = valor.replace(' ', '')
        tamanho = len(valor)
        lista_nomes[nome] = tamanho
    for nome, valor in lista_nomes.items():
        if min(lista_nomes.values()) == valor:
            return nome


def test_mais_curto():
    teste_1 = {'Ana':'Ana','Rafael':'Rafael','Marsconcelos':'Marsconcelos','Felipe alves da silva':'Felipe alves da silva','Genserico':'Genserico','Tiazinha':'Tiazinha'}
    teste_2 = {'Rafael':'Rafael','Marsconcelos':'Marsconcelos','Felipe alves da silva':'Felipe alves da silva','Genserico':'Genserico','Tiazinha':'Tiazinha','Odo':'Odo'}
    teste_3 = {'Rafael':'Rafael','Marsconcelos':'Marsconcelos','Felipe alves da silva':'Felipe alves da silva','Genserico':'Genserico','Tiazinha':'Tiazinha','Aje':'Aje'}
    teste_4 = {'Rafael':'Rafael','Marsconcelos':'Marsconcelos','Felipe alves da silva':'Felipe alves da silva','Genserico':'Genserico','Tiazinha':'Tiazinha','Gui':'Gui'}
    teste_5 = {'Rafael':'Rafael','Marsconcelos':'Marsconcelos','Felipe alves da silva':'Felipe alves da silva','Genserico':'Genserico','Tiazinha':'Tiazinha','Quio':'Quio'}
    if menor_nome(teste_1) == 'Ana':
        print('Teste 1 deu certo')
    else:
        print('Erro no teste 1')
    if menor_nome(teste_2) == 'Odo':
        print('Teste 2 deu certo')
    else:
        print('Erro no teste 2')
    if menor_nome(teste_3) == 'Aje':
        print('Teste 3 deu certo')
    else:
        print('Erro no teste 3')
    if menor_nome(teste_4) == 'Gui':
        print('Teste 4 deu certo')
    else:
        print('Erro no teste 4')
    if menor_nome(teste_5) == 'Quio':
        print('Teste 5 deu certo')
    else:
        print('Erro no teste 5')
