def soma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + soma_lista(lista[1:])


a = [x for x in range(10)]
print(soma_lista(a))
