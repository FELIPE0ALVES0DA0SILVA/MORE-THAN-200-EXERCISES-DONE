# Create a program where the user can to digit several numeric values and sign up in a list.
# In case the number already exist in there, it dont will be added.
# In the end, will be desplay all the unique values digited, em raised order.
valores = list()
i = 0
while True:
    i += 1
    a = int(input('Digite um valor: '))
    if i == 1:
        valores.append(a)
        print('Valor adicionado com sucesso!')
    else:
        if a not in valores:
            valores.append(a)
            print('Valor adicionado com sucesso!')
        else:
            print('Valor duplicado, não irei adicionar neste banco de dados.')
    ask = str(input('Tu queres continuar: [ S | N ]')).upper().strip()
    if ask not in 'SN':
        print('Resposta inválida.')
    if ask == 'N':
        break
valores.sort()
print('Os valores adicionados no seu banco de dados foram: {}'.format(valores))
