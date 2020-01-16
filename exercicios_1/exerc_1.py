# Digit the famous phrase: HALLO, WORLD!

#  MAKE A DICTIONARY WITH COLORS
# CREATE A VARIABLE WITH THE PHRASE
# PRINT THE VARIABLE OVERWHELMED TO THE COLORS VARIABLES

cores = {'fim':'\033[m', 'vermelho_branco':'\033[1;31;40m'}
msg = 'Olá, Mundo!'
print('{}{}.{}'.format(cores['vermelho_branco'], msg, cores['fim']))

