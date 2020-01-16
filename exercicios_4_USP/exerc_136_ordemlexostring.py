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


def menor_string(dict=None):
    if dict == None:
        dict = lista_nome()
    lista = []
    for local, valor in dict.items():
        converter = ord(valor[0])
        lista.append(converter)
        dict[valor] = converter
    lista.sort()
    a = sorted(dict.items())
    for local, valor in a:
        for posicao, cada in enumerate(lista):
            if cada == valor:
                lista[posicao] = local
                break
    return lista


def teste_menor_string():
    dict_1 = {'Amanda':'Amanda', 'Joana':'Joana','jaqueline':'jaqueline','rafeal':'rafeal','odo':'odo',
              'cirilo':'cirilo','madagascar':'madagascar','luuci':'luuci','conhecido':'conhecido',
              'Adael':'Adael','ajeu':'ajeu'}
    dict_2 = {'queiroz': 'queiroz', 'Joana': 'Joana', 'zidane': 'zidane', 'rafeal': 'rafeal', 'odo': 'odo',
              'cirilo': 'cirilo', 'madagascar': 'madagascar', 'ester': 'ester', 'conhecido': 'conhecido',
              'Adael': 'Adael', 'jazael': 'jazael'}
    dict_3 = {'simone': 'simone', 'Joana': 'Joana', 'felipe': 'felipe', 'rafeal': 'rafeal', 'odo': 'odo',
              'simeao': 'simeao', 'madagascar': 'madagascar', 'luuci': 'luuci', 'conhecido': 'conhecido',
              'Azel': 'Azel', 'ajeu': 'ajeu'}
    if menor_string(dict_1) == ['Adael', 'Amanda', 'Joana', 'ajeu', 'cirilo', 'conhecido', 'jaqueline', 'luuci', 'madagascar', 'odo', 'rafeal']:
        print('O teste 1 funcionou.')
    else:
        print('O 1 teste não funcionou.')
    if menor_string(dict_2) == ['Adael', 'Joana', 'cirilo', 'conhecido', 'ester', 'jazael', 'madagascar', 'odo', 'queiroz', 'rafeal', 'zidane']:
        print('O teste 2 funcionou.')
    else:
        print('O 2 teste não funcionou.')
    if menor_string(dict_3) == ['Azel', 'Joana', 'ajeu', 'conhecido', 'felipe', 'luuci', 'madagascar', 'odo', 'rafeal', 'simeao', 'simone']:
        print('O teste 3 funcionou.')
    else:
        print('O 3 teste não funcionou.')
