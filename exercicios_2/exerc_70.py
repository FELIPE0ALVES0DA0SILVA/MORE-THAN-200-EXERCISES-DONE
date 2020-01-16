# Create a program that read the name and the price of several products.
# Then the program will should ask if the user will continue. In the end, show:

# What is the total price in the shop.
# How many products cost more than US 1000.
# What is the nome of the product more cheap.
user = cheap_name = ''
total = c = unit = cheap = 0

while True:
    name_product = str(input('Qual é o nome do produto [ sem espaços ]? ')).strip()
    price_product = int(input('Qual é o preço desse produto? '))
    user = str(input('Tu irás continuar [ S|N ]: ')).strip().upper()
    while user != 'S' and user != 'N':
        user = str(input('Tu irás continuar [ S|N ]: ')).strip().upper()
    total += price_product
    c += 1
    if price_product > 1000:
        unit += 1
    if c == 1:
        cheap = price_product
        cheap_name = name_product
    else:
        if price_product < cheap:
            cheap = price_product
            cheap_name = name_product
    if user == 'N':
        break

print('O total gasto foi US {}.'.format(total))
print('{} produtos custaram mais de US 1000.'.format(unit))
print('O produto mais barato é o {}, custa US {}.'.format(cheap_name, cheap))