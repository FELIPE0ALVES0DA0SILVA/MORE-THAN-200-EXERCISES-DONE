# Make a program tha read two float numbers and show in the screen the average between the two values.

# MAKE A DICTIONARY WITH THE NEED COLORS.
# CREATE THE FIRST VARIABLE THAT WILL INPUT THE FLOAT VALUE.
# CREATE THE SECOND VARIABLE THAT WILL INPUT THE FLOAT VALUE.
# MAKE THE OPERATION THAT WILL GIVE THE AVERAGE BETWEEN THE TWO VALUES.
# PRINT THE AVERAGE BETWEEN THE TWO VALUES.

cores = {'fim':'\033[m', 'vermelho_branco': '\033[1;31;40m',
         'cyen_branco': '\033[1;34;40m',
         'roxo_branco': '\033[1;30;45m',
         'branco_cinza': '\033[1;30;47m',
         'branco_amarelo': '\033[1;30;43m',
         'verde_branco': '\033[1;32;40m',
         'preto_branco': '\033[7;30m',
         'marinho_branco': '\033[1;36;40m',
         'vermelho_marinho': '\033[1;36;41m',
         'branco_preto': '\033[7;40m',
         'amarelo_preto': '\033[1;33m',
         'preto_amarelo': '\033[7;30;43m',
         'cyen_preto': '\033[7;34m'}


not1 = float(input('{}Enter the first note:{} '.format(cores['amarelo_preto'], cores['fim'])))

not2 = float(input('{}Enter the second note:{} '.format(cores['marinho_branco'], cores['fim'])))

media = (not1 + not2) / 2

print('{}The average between the two notes informed is {}{}{}{}{}.{}'
      .format(cores['vermelho_marinho'], cores['fim'], cores['vermelho_branco'], media, cores['fim'], cores['vermelho_marinho'], cores['fim']))
