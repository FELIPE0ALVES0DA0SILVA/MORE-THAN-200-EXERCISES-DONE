# make a program that read a value and show the antecessor and predecessor of this value.

# MAKE A DICTIONARY WITH THE COLORS.
# CREATE A VARIABLE THAT WILL INPUT A INTEGER VALUE.
# MAKE THE OPERATIONS TO ARRIVE IN THE EXPECTED RESULT.
# PRINT THE VALUES IN THE SCREEN WITH THE COLORS.

cores = {'fim':'\033[m', 'vermelho_branco': '\033[1;31;40m',
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

n1 = int(input('{}Enter with a integer number:{} '.format(cores['branco_amarelo'], cores['fim'])))

R1 = n1-1
R2 = n1+1


print('{}O sucessor de {}{}{}{}{} é {}{}{}{}{}, e o antecesor de {}{}{}{}{} é {}{}{}{}{}.{}'.
      format(cores['amarelo_preto'], cores['fim'],
             cores['branco_amarelo'], n1, cores['fim'],
             cores['amarelo_preto'], cores['fim'],
             cores['cyen_preto'], R2, cores['fim'],
             cores['amarelo_preto'], cores['fim'],
             cores['verde_branco'], n1, cores['fim'],
             cores['amarelo_preto'], cores['fim'],
             cores['roxo_branco'], R1, cores['fim'],
             cores['amarelo_preto'], cores['fim']))
