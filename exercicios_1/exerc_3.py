# CREATE A PROGRAM THAT SUM TWO VALUES AND SHOW IN THE SCREEN.

# MAKE THE DICTIONARY WITH THE COLORS
# CREATE THE FIRST VARIABLE THAT IT IS A INTEGER NUMBER.
# CREATE THE SECOND VARIABLE THAT IT IS A INTEGER NUMBER.
# PRINT THE WITH THE COLORS IN THE SCREEN.

cores = {'fim':'\033[m', 'vermelho_branco':'\033[1;31;40m',
         'cyen_branco':'\033[1;34;40m',
         'roxo_branco':'\033[1;35;40m',
         'branco_cinza':'\033[1;30;47m',
         'branco_amarelo':'\033[1;30;43m'}

n1 = int(input('{}Enter with the desired number:{} '
               .format(cores['vermelho_branco'], cores['fim'])))

n2 = int(input('{}Enter with the desired number:{} '
               .format(cores['roxo_branco'], cores['fim'])))

print('{}The sum between {}{}{}{}{}'
      ' and {}{}{}{}{} is {}{}{}{}{}.{}'.
      format(cores['branco_amarelo'], cores['fim'],
             cores['vermelho_branco'], n1,
             cores['fim'], cores['branco_amarelo'],
             cores['fim'], cores['roxo_branco'],
             n2, cores['fim'], cores['branco_amarelo'],
             cores['fim'], cores['branco_cinza'], (n1+n2),
             cores['fim'], cores['branco_amarelo'],
             cores['fim']))

