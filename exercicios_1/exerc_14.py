# MAKE A DICTIONARY WITH COLORS.
# CREATE A VARIABLE THAT READ THE TEMPERATURE IN CELSIUS.
# MAKE THE OPERATION TO CONVERT THE CELSIUS DEGREES TO FAHRENHEIT DEGREES.
# PRINT THE RESULT IN FAHRENHEIT DEGREES.

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

celsius = float(input('{}Enter with the temperature in '
                      'celsius degree:{} '.format( cores['verde_branco'], cores['fim'])))

formula = 32 + ((9 * celsius)/5)

print('{}The temperature in fahrenheit is: {}{}{}{}'
      .format( cores['roxo_branco'], cores['fim'],
               cores['branco_amarelo'], formula, cores['fim']))
