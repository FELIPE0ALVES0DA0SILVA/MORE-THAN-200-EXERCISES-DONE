# MAKE A DICTIONARY THAT WILL CONTAIN THE COLORS.
# MAKE THE VARIABLE THAT WILL CONTAIN THE SALARY
# MAKE THE OPERATION TO CALCULATE THE INCREASE UNDER THE SALARY.
# PRINT THE NEW SALARY WITH THE INCREASE.

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

salary = float(input('{}Enter the actual salary: US{} '.format( cores['verde_branco'], cores['fim'])))

increase = salary*(15/100)

print('{}The new salary with the increase of 15 percent is  {}{}{:.2f}{}{} dollars.{}'
      .format( cores['roxo_branco'], cores['fim'],
               cores['vermelho_branco'], salary+increase, cores['fim'],
               cores['roxo_branco'], cores['fim']))
