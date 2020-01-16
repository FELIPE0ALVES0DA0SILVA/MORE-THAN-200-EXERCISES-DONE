# Make a program that show the kilometer, hectometer, decameter, centimeter, milimeter, respectively.

# MAKE A DICTIONARY WITH COLORS.
# CREATE A VARIABLE THAT WILL INPUT THE VALUE TO BE CONVERTED.
# CREATE ALL THE VARIABLES THAT WILL CONTAIN THE OPERATIONS TO EACH CONVERSION TO BE DONE.
# PRINT ALL THE RESULT OF EACH CONVERSION GOT, COLORIZED.

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


meter = float(input('{}Enter the measurement in meters:{} '.format(cores['amarelo_preto'], cores['fim'])))


kilometer = meter/1000
hectometer = meter/100
decameter = meter/10
decimeter = meter*10
centimeter = meter*100
milimeter = meter*1000

print('{}The measure in meters, convert to:{}'
      '\n{}kilometers is {}{}{}{}'
      '\n{}hectometers is {}{}{}{}'
      '\n{}decameters is {}{}{}{}'
      '\n{}decameters is {}{}{}{}'
      '\n{}centimeters is {}{}{}{}'
      '\n{}milimeters is {}{}{}{}'
      .format(cores['roxo_branco'], cores['fim'],
              cores['preto_branco'], cores['fim'],
              cores['marinho_branco'], kilometer, cores['fim'],
              cores['preto_branco'], cores['fim'],
              cores['marinho_branco'], hectometer, cores['fim'],
              cores['preto_branco'], cores['fim'],
              cores['marinho_branco'], decameter, cores['fim'],
              cores['preto_branco'], cores['fim'],
              cores['marinho_branco'], decimeter, cores['fim'],
              cores['preto_branco'], cores['fim'],
              cores['marinho_branco'],  centimeter, cores['fim'],
              cores['preto_branco'], cores['fim'],
              cores['marinho_branco'], milimeter, cores['fim']))
