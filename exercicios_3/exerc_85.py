# Create a program where the user can enter seven numeric values and signed up them
# in a unique list that saved separated the pair values and odds too.
# In the end, show the values pairs and odds in raised order.

valores = [[], []]
for contagem in range(0, 7):
    pergunta = int(input('Digite o {}° valor: '.format(contagem + 1)))
    if pergunta % 2 == 0:
        valores[0].append(pergunta)
    else:
        valores[1].append(pergunta)
print('A lista com todos os valores é: {}'.format(valores))
valores[0].sort()
print('A sublist com os valores pares é: {}'.format(valores[0]))
valores[1].sort()
print('A sublist com os valores ímpares é: {}'.format(valores[1]))
