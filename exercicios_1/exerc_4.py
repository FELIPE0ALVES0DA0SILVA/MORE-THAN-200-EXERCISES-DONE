# Make a program that utilize all the methods, give any value, and show in the screen if the value is true or false.

# MAKE A DICTIONARY WITH ALL THE COLORS.
# CREATE A VARIABLE THAT WILL INPUT ANY VALUE.
# PRINT IF THE LOGIC ADOPT IN EACH PRINT IS TRUTH OR FALSE.

cores = {'fim':'\033[m',
         'vermelho_branco': '\033[1;31;40m',
         'cyen_branco': '\033[1;34;40m',
         'roxo_branco': '\033[1;30;45m',
         'branco_cinza': '\033[1;30;47m',
         'branco_amarelo': '\033[1;30;43m',
         'verde_branco': '\033[1;32;40m',
         'preto_branco': '\033[7;30m',
         'marinho_branco': '\033[1;36;m',
         'preto_marinho': '\033[7;30;46m',
         'branco_preto': '\033[7;40m',
         'amarelo_preto': '\033[1;33m',
         'preto_amarelo': '\033[7;30;43m',
         'cyen_preto': '\033[7;34m'}

n = input('{}Enter with something else:{} '.format(cores['vermelho_branco'], cores['fim']))

print('{}The number is alpha:{}{}{}{} '.format(cores['cyen_branco'], cores['fim'], cores['roxo_branco'], n.isalpha(), cores['fim']))
print('{}The number is identifier:{}{}{}{} '.format(cores['branco_cinza'], cores['fim'], cores['roxo_branco'], n.isidentifier(), cores['fim']))
print('{}The number is decimal:{}{}{}{} '.format(cores['branco_amarelo'], cores['fim'], cores['roxo_branco'], n.isdecimal(), cores['fim']))
print('{}The number is upper:{}{}{}{} '.format(cores['verde_branco'], cores['fim'], cores['roxo_branco'], n.isupper(), cores['fim']))
print('{}The number is title:{}{}{}{} '.format(cores['marinho_branco'], cores['fim'], cores['roxo_branco'], n.istitle(), cores['fim']))
print('{}The number is space:{}{}{}{} '.format(cores['preto_marinho'], cores['fim'], cores['roxo_branco'], n.isspace(), cores['fim']))
print('{}The number is printable:{}{}{}{} '.format(cores['branco_preto'], cores['fim'],cores['roxo_branco'], n.isprintable(), cores['fim']))
print('{}The number is lower:{}{}{}{} '.format(cores['amarelo_preto'], cores['fim'], cores['roxo_branco'], n.islower(), cores['fim']))
print('{}The number is digit:{}{}{}{} '.format(cores['preto_amarelo'], cores['fim'], cores['roxo_branco'], n.isdigit(), cores['fim']))
print('{}The number is alphanumeric:{}{}{}{} '.format(cores['cyen_preto'], cores['fim'], cores['roxo_branco'], n.isalnum(), cores['fim']))




