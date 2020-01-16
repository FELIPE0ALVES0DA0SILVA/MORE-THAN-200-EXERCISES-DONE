# Create the program that simulate the operation of a cash machine.
# In the end, ask to the user what will be the value to be withdrawn (integer numbers)
# and the program will informed how many cells of each value will be delivered.

# Obs: consider that the cash machine has cells of US 50, US 20, US 10 and US 1.

while True:
    print('='*35)
    print('BANCO NOSSA SENHORA DAS GRAÇAS')
    print('='*35)
    withdrawn = int(input('Qual será o valor a ser sacado? US '))
    if withdrawn >= 50:
        cells = withdrawn // 50
        withdrawn = withdrawn % 50
        print('Total de {} células de US 50.'.format(cells))

    if 50 > withdrawn >= 20:
        cells_1 = withdrawn // 20
        withdrawn = withdrawn % 20
        print('Total de {} células de US 20.'.format(cells_1))

    if 20 > withdrawn >= 10:
        cells_2 = withdrawn // 10
        withdrawn = withdrawn % 10
        print('Total de {} células de US 10.'.format(cells_2))

    if 10 > withdrawn >= 1:
        print('Total de {} células de US 1.'.format(withdrawn))
        withdrawn = withdrawn % 1

    print('=' * 35)
    print('Volte sempre ao Banco Nossa senhora das graças! Tenha um bom dia.')
    if withdrawn % 1 == 0:
        break
