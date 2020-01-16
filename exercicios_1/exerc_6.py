# Make a program that read a float value and show in the screen:
# The squad number
# The cubic number
# The square root of the number.

# MAKE A DICTIONARY WITH THE COLORS
# CREATE A VARIABLE THE INPUT THE FLOAT VALUE
# MAKE THE RESPECTIVELY OPERATION TO OBTAIN THE RESULT DESIRED AND THE COLORS.

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

num = float(input('{}Enter the real number:{} '.format(cores['preto_marinho'], cores['fim'])))

d1 = num*2

d2 = num*3

d3 = num ** (1/2)

print('{}O dobro de {}{}{}{}{} é {}{}{}{}{}, o triplo de {}{}{}{}{} é {}{}{}{}{}, e a raiz de {}{}{}{}{} é {}{}{}{}{}.{}'
      .format(cores['preto_amarelo'], cores['fim'],
              cores['branco_amarelo'], num, cores['fim'],
              cores['preto_amarelo'], cores['fim'],
              cores['branco_amarelo'], d1, cores['fim'],
              cores['preto_amarelo'], cores['fim'],
              cores['branco_amarelo'], num, cores['fim'],
              cores['preto_amarelo'], cores['fim'],
              cores['branco_amarelo'], d2, cores['fim'],
              cores['preto_amarelo'], cores['fim'],
              cores['branco_amarelo'], num, cores['fim'],
              cores['preto_amarelo'], cores['fim'],
              cores['branco_amarelo'], d3, cores['fim'],
              cores['preto_amarelo'], cores['fim']))

