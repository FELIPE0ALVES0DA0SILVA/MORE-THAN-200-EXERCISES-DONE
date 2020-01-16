# Make a program that read the name of a person, and output a greetings of welcoming.

# MAKE A DICTIONARY WITH THE COLORS.
# CREATE A VARIABLE WITH THE INPUT COMMAND, AND WITH THE RESPECTIVELY COLORS
# PRINT THE GREETINGS REFERRING THE NAME INPUTTED FOR THE VARIABLE AND THE COLORS.

cores = {'fim':'\033[m', 'vermelho_branco':'\033[1;31;40m',
         'cyen_branco':'\033[1;34;40m',
         'roxo_branco':'\033[1;35;40m'}

nome = input('{}What is your name?{} '.
             format(cores['vermelho_branco'], cores['fim']))

print('{}Welcome, Glad to meet you, {}{}{}{}.{}'
      .format(cores['roxo_branco'],
              cores['cyen_branco'], nome,
              cores['fim'], cores['roxo_branco'], cores['fim']))






