def menor_nome(list):
    lista_nomes = {}
    for cada in list:
        lista_nomes[cada.strip().capitalize()] = cada.strip().capitalize()
    for valor, nome in lista_nomes.items():
        valor = valor.replace(' ', '')
        tamanho = len(valor)
        lista_nomes[nome] = tamanho
    for nome, valor in lista_nomes.items():
        if min(lista_nomes.values()) == valor:
            return nome


print(menor_nome(['maria', ' josé ', '   PAULO', 'Catarina   ']))