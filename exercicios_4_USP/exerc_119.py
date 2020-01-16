while True:
    usuario = int(input('Digite um número: '))
    i = 1
    while usuario > 1:
        i *= usuario
        print(i, end='  ')
        usuario -= 1
    while True:
        try:
            pergunta = str(input('\nTu queres sair do programa: [ S | N ] ')).strip().upper()[0]
        except:
            print('Informe um valor válido.')
        else:
            if pergunta in 'SN':
                break
            print('Digite um dos valores especificados.')
    if pergunta == 'S':
        break
