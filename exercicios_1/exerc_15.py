# MAKE A DICTIONARY THAT WILL CONTAIN THE COLORS.
# CREATE A VARIABLE THAT WILL CONTAIN THE KILOMETERS RUNS.
# CREATE A VARIABLE THAT WILL CONTAIN THE DAYS RUNS.
# CREATE VARIABLES WITH VALUES OF CONVERSION.
# MAKE THE OPERATIONS TO DISCOVER HOW MANY THE CLIENT WILL PAY BASED IN THE KILOMETERS RUNS AND THE DAYS THAT THE CLIENT STAYED WITH THE CAR.
# PRINT THE EXPECTED RESULT

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

kilometer = float(input('{}How many kilometers the car run?{} '.format( cores['marinho_branco'], cores['fim'])))
days = int(input('{}How many days you run with the car?{} '.format( cores['verde_branco'], cores['fim'])))

# Car information

per_day = 60
per_kilometer = 0.15

# Calculus

car_kilometer = kilometer * per_kilometer
car_day = days * per_day

# Conclusion

print('{}The total price for car rental is: US {}{}{}{}{}.{}'
    .format( cores['branco_amarelo'], cores['fim'],
             cores['vermelho_branco'], car_day + car_kilometer, cores['fim'],
             cores['branco_amarelo'], cores['fim']))