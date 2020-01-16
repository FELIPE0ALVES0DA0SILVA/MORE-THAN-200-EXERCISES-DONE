# Adopt the code of the desafio 107, creating a function additional called moeda() that get show the values like a monetary value formated.

from exercicios_3.moeda.utilidades import money

numero = int(input('Digite o valor em reais a ser calculado: R$ '))

print('O valor {} com um aumento de 10% fica: {}.'.format(money.moeda(numero), money.moeda(money.aumentar(numero))))
print('O valor {} com um desconto de 10% fica: {}.'.format(money.moeda(numero), money.moeda(money.diminuir(numero))))
print('O valor {} dobrado fica: {}.'.format(money.moeda(numero), money.moeda(money.dobra(numero))))
print('O valor {} dividido pela metade fica: {}.'.format(money.moeda(numero), money.moeda(money.metade(numero))))
