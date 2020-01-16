# Make a program that read a sequence of integers number ended to zero and
# when the user enter with the zero, the program print the program in the correct order.


def invertendo_sequencial():
    desordem = []
    while True:
        try:
            numero = int(input('Digite um número: '))
        except:
            print('Erro de sintaxe, tente novamente.')
        else:
            if numero == 0:
                break
            else:
                desordem.append(numero)
                desordem.sort(reverse=True)
    print()
    for i in desordem:
        print(i)


invertendo_sequencial()
