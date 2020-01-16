# Make a program that have a function called write(),
# that input any text like a parameter and show a message with the adoptable size.


def escreve(oracao):
    print('¨'*len(oracao))
    print(oracao)
    print('_'*len(oracao))


for c in range(0, 3):
    escreve(str(input('Digite a oração desejada: ').capitalize().strip()))

