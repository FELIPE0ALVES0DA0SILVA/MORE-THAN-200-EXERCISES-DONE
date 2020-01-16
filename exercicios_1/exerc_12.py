# MAKE A DICTIONARY WITH COLORS.
# CREATE A VARIABLE THAT WILL READ THE PRICE.
# MAKE THE OPERATIONS TO CONVERT FOR EACH BILLS.
# PRINT ALL THE VALUES ALREADY CONVERTED.

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

price = float(input('{}Enter the price of your product: R${} '.format( cores['branco_amarelo'], cores['fim'])))

discount = 95/100
percent = price*discount

print("{}The new price of your product with 15 percent of{}\n"
      "{}discount is {}{}{:.4f}{}{} reals.{}"
      .format( cores['vermelho_branco'], cores['fim'],
               cores['vermelho_branco'], cores['fim'],
               cores['verde_branco'], percent, cores['fim'],
               cores['vermelho_branco'], cores['fim']))

