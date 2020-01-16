from time import time


def bolha(lista):
    fim = len(lista)
    for cada in range(fim-1, 0, -1):
        for item in range(cada):
            if lista[item] > lista[item + 1]:
                lista[item], lista[item + 1] = lista[item + 1], lista[item]
    return lista



def bolha_curta(lista):
    fim = len(lista)
    for cada in range(fim-1, 0, -1):
        condicao = False
        for item in range(cada):
            if lista[item] > lista[item + 1]:
                lista[item], lista[item + 1] = lista[item + 1], lista[item]
                condicao = True
        if not condicao:
            return lista

n = 500
b = [x for x in range(n)]
b[n//10] = -500

antes_1 = time()
bolha_curta(b)
depois_1 = time()
print('O tempo gasto neste algoritmo foi {}'.format(depois_1 - antes_1))
antes_2 = time()
bolha(b)
depois_2 = time()
print('O tempo gasto neste algoritmo foi {}'.format(depois_2 - antes_2))