# Create a module called exerc_107.py that incorporated aumanto(),
# diminuir(), dobra() and metade().

# Make also a program that import that module and use some of those functions.

from utilidades import money

numero = int(input("Digite o valor a ser calculado: "))
print(money.aumentar(numero))
print(money.diminuir(numero))
print(money.dobra(numero))
print(money.metade(numero))
