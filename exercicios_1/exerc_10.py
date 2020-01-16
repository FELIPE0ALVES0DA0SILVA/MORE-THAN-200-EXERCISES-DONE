# Make a program that read the value, in real, to be converted, and show the money converted in EURO, US, YUAN, SWISS, POUND in the screen.

# MAKE A DICTIONARY WITH ALL THE NEED COLORS.
# CREATE A VARIABLE THAT INPUT THE SUM TO BE CONVERTED.
# CREATE VARIABLES WITH THE RESPECTIVELY PRICE OF ALL PAIRS TOWARDS THE BRAZILIAN REAL.
# MAKE ALL THE OPERATION TO CONVERT THE VALUE.
# PRINT ALL THE CONVERSIONS IN THE SCREEN.

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

wallet = float(input('{}How many Reais you have is your wallet?{} R$'.format(cores['roxo_branco'], cores['fim'])))

onedollar = 4.14
oneeuro = 4.58
oneyuan = 0.59
oneswiss = 4.20
onepound = 5.45


conversion1 = wallet/onedollar
conversion2 = wallet/oneeuro
conversion3 = wallet/oneyuan
conversion4 = wallet/oneswiss
conversion5 = wallet/onepound


print('{}You can buy precisely:{}'
      ' \n{}US {}{}{:.2f}{}'
      ' \n{}EURO {}{}{:.2f}{}'
      ' \n{}YUAN {}{}{:.2f}{}'
      ' \n{}CHF {}{}{:.2f}{}'
      ' \n{}LIBRA {}{}{:.2f}{}'
      .format(
            cores['cyen_preto'], cores['fim'],

            cores['verde_branco'], cores['fim'] ,
            cores['branco_amarelo'], conversion1, cores['fim'],

            cores['verde_branco'], cores['fim'] ,
            cores['branco_amarelo'], conversion2, cores['fim'],

            cores['verde_branco'], cores['fim'] ,
            cores['branco_amarelo'], conversion3, cores['fim'],

            cores['verde_branco'], cores['fim'] ,
            cores['branco_amarelo'], conversion4, cores['fim'],

            cores['verde_branco'], cores['fim'] ,
            cores['branco_amarelo'], conversion5, cores['fim']))
