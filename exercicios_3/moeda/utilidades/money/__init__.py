def aumentar(valor, mais=False, condicao=False):
    if condicao:
        res = valor + (valor * mais / 100)
        return 'R$ {}'.format(res)
    else:
        return valor + (valor * mais / 100)


def diminuir(valor, menos=False, condicao=False):
    if condicao:
        res = valor - (valor * menos / 100)
        return 'R$ {}'.format(res)
    else:
        return valor - (valor * menos / 100)


def dobra(valor, condicao=False):
    if condicao:
        res = valor * 2
        return 'R$ {}'.format(res)
    else:
        return valor * 2


def metade(valor, condicao=False):
    if condicao:
        res = valor / 2
        return 'R$ {}'.format(res)
    else:
        return valor / 2


def moeda(valor):
    return 'RS {}'.format(valor)


def resumo(valor, mais, menos):
    print('~'*50)
    print('{:^50}'.format('RESUMO DO VALOR'))
    print('~'*50)
    print('Preço analisado: {:>30}'.format(moeda(valor)))
    print('Dobro do preço: {:>30}'.format(dobra(valor, True)))
    print('Dividido pela metade: {:>30}'.format(metade(valor, True)))
    print('Aumento de {} % fica: {:>30}'.format(mais, aumentar(valor, mais, True)))
    print('Desconto de {} % fica: {:>30}'.format(menos, diminuir(valor, menos, True)))
    print('~' * 50)
