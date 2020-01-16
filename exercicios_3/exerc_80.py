# Create a program where the user can enter five numeric values and sign up in a list.
# Already in the correct position of insertion( without use the sort()).
# In the end, show the ordered list in the screen.
ordenado = []
for contagem in range(0, 5):
    numero = int(input('Digite 0 {}° número: '.format(contagem + 1)))
    if contagem == 0:
        ordenado.append(numero)
        print('O primeiro número, o {} foi adicionado na lista.'.format(numero))
    elif numero > max(ordenado):
        ordenado.append(numero)
        print('O número {} foi adicionado ao final da lista.'.format(numero))
    else:
        for posicao, valores in enumerate(ordenado):
            if numero <= valores:
                ordenado.insert(posicao, numero)
                print('O número foi adicionado na posição {}.'.format(posicao))
                break
print('A lista com os número ordenadosé está aqui: {}'.format(ordenado))
