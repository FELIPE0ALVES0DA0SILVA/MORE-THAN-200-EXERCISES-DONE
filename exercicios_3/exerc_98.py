# Make a program that have a function called contador(),
# that input three parameters: start, end and pass and realize the count;
# Your program have that realize three counts through of the function created:

# A) From 1 to 10, of 1 in 1.
# B) From 10 to 0, of 2 in 2.
# A personalized counted.

from time import sleep


def contador(inicio, fim):
    print('Contagem de 1 até 10 de 1 em 1.')
    sleep(2.5)
    for progressao in range(inicio, fim + 1):
        print('{}'.format(progressao), end=' ', flush=True)
        sleep(0.5)
    print('fim')
    print('Contagem de 10 até 0, de 2 em 2.')
    for regressiva in range(10, 0 - 2, -2):
        sleep(0.5)
        print(regressiva, end=' ', flush=True)
    print('fim')
    print('Agora é sua vez de personalizar a contagem!')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    if inicio < fim:
        if passo > 0:
            for progressao in range(inicio, fim + passo, passo):
                sleep(0.5)
                print(progressao, end=' ', flush=True)
            print('fim')
        elif passo < 0:
            for progressao in range(inicio, fim + passo, -1 * passo):
                sleep(0.5)
                print(progressao, end=' ', flush=True)
            print('fim')
        else:
            while True:
                pergunta = str(input('Contagem regressiva ou progressiva? [ R | P ] ')).strip().capitalize()
                if pergunta in 'RP':
                    break
                else:
                    print('Valor inválido!!')
            if pergunta == 'R':
                for regressiva in range(fim, inicio - 1, -1):
                    sleep(0.5)
                    print(regressiva, end=' ', flush=True)
                print('fim')
            else:
                for progressao in range(inicio, fim + 1):
                    sleep(0.5)
                    print(progressao, end=' ', flush=True)
                print('fim')
    elif inicio > fim:
        if passo > 0:
            for regressiva in range(inicio, fim - passo, -1 * passo):
                sleep(0.5)
                print(regressiva, end=' ', flush=True)
            print('fim')
        elif passo < 0:
            for regressiva in range(inicio, fim + passo, passo):
                sleep(0.5)
                print(regressiva, end=' ', flush=True)
            print('fim')
        else:
            for regressiva in range(inicio, fim - 1, -1):
                sleep(0.5)
                print(regressiva, end=' ', flush=True)
            print('fim')


contador(0, 10)
