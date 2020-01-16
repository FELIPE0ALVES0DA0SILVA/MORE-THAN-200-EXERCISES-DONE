
# MAKE A DICTIONARY WITH COLORS.
# CREATE A VARIABLE TO THE WEIGHT.
# CREATE A VARIABLE TO THE HIGH.
# CALCULATE THE AREA OF THE OBJECT.
# CALCULATE THE INK OF THE OBJECT.
# PRINT ALL THE EXPECTED RESULTS.

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
weight = float(input('{}Enter the weight of your wall:{} '.format(cores['roxo_branco'], cores['fim'])))
high = float(input('{}Enter the high of your wall:{} '.format(cores['branco_amarelo'], cores['fim'])))
area = weight*high
ink = area/2
print('{}The Area of your wall is {}{}{}{}{} square meters and you can{}\n'
      '{}paint the wall with {}{}{}{}{} liters of ink.{}'
      .format(cores['vermelho_branco'], cores['fim'],
              cores['branco_cinza'], area, cores['fim'],
              cores['vermelho_branco'], cores['fim'], cores['vermelho_branco'],cores['fim'],
              cores['verde_branco'], ink, cores['fim'],
              cores['verde_branco'], cores['fim']))
