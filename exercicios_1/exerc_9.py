# Make a program that read a real value number, and show the table of the respective number.

# MAKE A DICTIONARY THAT WILL CONTAIN ALL THE NEED COLORS.
# CREATE A VARIABLE THAT WILL INPUT THE NUMBER OF THE USER.
# MAKE THE NEEDS OPERATIONS TO CREATE A TABLE VALUES.
# PRINT THIS TABLE VALUE.

cores = {'fim': '\033[m', 'vermelho_branco': '\033[1;31;40m',
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

num = float(input('{}Enter the desired number:{} '.format(cores['cyen_preto'], cores['fim'])))
space = '='*16
num0 = num*0
num1 = num*1
num2 = num*2
num3 = num*3
num4 = num*4
num5 = num*5
num6 = num*6
num7 = num*7
num8 = num*8
num9 = num*9
num10 = num*10

print('{}The multiplication table of {}{}{}{}{}, respectively:{}'
      ' \n {}{}{}'
      ' \n {}{}{}{} X 0 = {}{}{}{}'
      ' \n {}{}{}{} X 1 = {}{}{}{}'
      ' \n {}{}{}{}X 2 = {}{}{}{}'
      ' \n {}{}{}{} X 3 = {}{}{}{}'
      ' \n {}{}{}{} X 4 = {}{}{}{}'
      ' \n {}{}{}{} X 5 = {}{}{}{}'
      ' \n {}{}{}{} X 6 = {}{}{}{}'
      ' \n {}{}{}{} X 7 = {}{}{}{}'
      ' \n {}{}{}{} X 8 = {}{}{}{}'
      ' \n {}{}{}{} X 9 = {}{}{}{}'
      ' \n {}{}{}{} X 10 = {}{}{}{}'
      ' \n {}{}{}'
      .format(
      cores['vermelho_branco'], cores['fim'],
      cores['marinho_branco'],num,cores['fim'],
      cores['vermelho_branco'], cores['fim'],


      cores['roxo_branco'], space, cores['fim'],


      cores['verde_branco'], num, cores['fim'],
      cores['branco_preto'], cores['fim'],
      cores['preto_branco'],num0, cores['fim'],

      cores['verde_branco'] ,num, cores['fim'],
      cores['branco_preto'], cores['fim'],
      cores['preto_branco'] ,num1, cores['fim'],


      cores['verde_branco'] ,num, cores['fim'],
      cores['branco_preto'], cores['fim'],
      cores['preto_branco'],num2, cores['fim'],


      cores['verde_branco'] ,num, cores['fim'],
      cores['branco_preto'], cores['fim'],
      cores['preto_branco'],num3, cores['fim'],


      cores['verde_branco'] , num, cores['fim'],
      cores['branco_preto'], cores['fim'],
      cores['preto_branco'],num4, cores['fim'],


      cores['verde_branco'] ,num, cores['fim'],
      cores['branco_preto'], cores['fim'],
      cores['preto_branco'],num5, cores['fim'],


      cores['verde_branco'] ,num, cores['fim'],
      cores['branco_preto'], cores['fim'],
      cores['preto_branco'],num6, cores['fim'],


      cores['verde_branco'] ,num, cores['fim'],
      cores['branco_preto'], cores['fim'],
      cores['preto_branco'],num7, cores['fim'],


      cores['verde_branco'] ,num, cores['fim'],
      cores['branco_preto'], cores['fim'],
      cores['preto_branco'],num8, cores['fim'],


      cores['verde_branco'] ,num, cores['fim'],
      cores['branco_preto'], cores['fim'],
      cores['preto_branco'],num9, cores['fim'],


      cores['verde_branco'] ,num, cores['fim'],
      cores['branco_preto'], cores['fim'],
      cores['preto_branco'],num10, cores['fim'],
      cores['roxo_branco'], space, cores['fim']))

