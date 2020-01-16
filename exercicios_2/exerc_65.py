
# Make a program that read several integer numbers for the keyboard.
# In the end of the execution, show the average between all the values and the minor and major values readied.
# The program should ask to the user if he want or not continue to digit values.


maior = menor = soma = iteration = media = 0
print('''
DIGITE [ 0 ] PARA STOPPAR A OPERAÇÃO''''')
escolhe_stop = str(input('TU QUERES CONTINUAR/COMEÇAR [ Y/N ]: ')).upper().strip()
if escolhe_stop == 'N':
    print('')
elif escolhe_stop != 'Y' and escolhe_stop != 'N':
    print('!'*20)
    print('VALOR INVÁLIDO.')
    print('!' * 20)
elif escolhe_stop == 'Y':
    escolhe = int(input('Escolha em número: '))
    while escolhe_stop != 'N':
        if escolhe != 0:
            soma = soma + escolhe
            iteration += 1
        if escolhe != 0:
            if iteration == 1:
                maior = escolhe
            elif escolhe > maior:
                maior = escolhe
            if iteration == 1:
                menor = escolhe
            elif escolhe < menor:
                menor = escolhe
        escolhe = int(input('Escolha em número: '))
        if escolhe == 0:
            escolhe_stop = str(input('TU QUERES CONTINUAR [ Y/N ]: ')).upper().strip()


if escolhe_stop == 'N' and escolhe_stop != 'Y' and iteration == 0:
    print('TUDO BEM, BYE')
elif escolhe_stop != 'Y' and escolhe_stop != 'N':
    print('')
else:
    media = soma/iteration
    print('O valor de média é {}.'.format(media))
if escolhe_stop == 'N' and escolhe_stop != 'Y' and iteration == 0:
    print('', end='')
elif escolhe_stop != 'Y' and escolhe_stop != 'N':
    print('')
else:
    print('O menor e maior valores são {} e {} respectivamente.'.format(menor, maior))
if escolhe_stop == 'N' and escolhe_stop != 'Y' and iteration == 0:
    print('', end='')
elif escolhe_stop != 'Y' and escolhe_stop != 'N':
    print('')
else:
    print('A quantidade de elementos somados foi {}.'.format(iteration))
if escolhe_stop == 'N' and escolhe_stop != 'Y' and iteration == 0:
    print('', end='')
elif escolhe_stop != 'Y' and escolhe_stop != 'N':
    print('')
else:
    print('A soma de todos os valores é {}.'.format(soma))
