# Adopt the code of the desafio 107, creating a function additional called
# moeda() that get show the values like a monetary value formatted.

from exercicios_3.moeda.utilidades import money

numero = int(input('Digite o valor em reais a ser calculado: R$ '))
mais = int(input('Digite o aumento que o salário receberá: '))
menos = int(input('Digite o desconto que o salário receberá: '))
print(money.resumo(numero, mais, menos))
