
# MAKE THE DICTIONARY WITH THE COLORS.
# CREATE THE FIRST INTEGER VARIABLE THAT WILL READ A VALUE
# CREATE A VARIABLE THAT CAN TO THE USER CHOOSE FOR WHAT BASE HE WANTS TO CONVERTS THE ENTERED NUMBER.
# MAKE THE CALCULUS TO CONVERT THE DECIMAL  BASE TO THE BINARY, OCTAGONAL AND HEXADECIMAL BASE
# IF CHOOSE OF THE USER EQUAL BINARY:
#           PRINT THE NUMBER CONVERTED FOR THE BINARY BASE AND COLORS
# ELIF CHOOSE OF THE USER BE EQUAL TO OCTAGONAL BASE:
#           PRINT THE NUMBER CONVERTED TO THE OCTAGONAL BASE AND COLORS
# ELIF CHOOSE OF THE USER BE EUQAL TO THE HEXADECIMAL BASE:
#           PRINT THE NUMBER CONVERTED TO THE HEXADECIMAL BASE AND COLORS

colors = {'fim':'\033[m', 'text_azul':'\033[1;34m', 'text_bold':'\033[1m', 'text_roxo':'\033[1;35m', 'text_amarelo':'\033[1;33m'}

number = int(input('Enter any integer number to convert for:'))
print()
print('{}If Binary, digit 1.{}'.format(colors['text_amarelo'], colors['fim']))
print('{}If octagonal, digit 2.{}'.format(colors['text_azul'], colors['fim']))
print('{}if hexadecimal, digit 3.{}'.format(colors['text_roxo'], colors['fim']))
chosen = int(input('Enter the number that correspond to one of this systems: '))
print()

binary = bin(number)[2:]  # Don't forget of the slicing, in all this variables I used it.
octagonal = oct(number)[2:]
hexadecimal = hex(number)[2:]

if  chosen == 1:
    print('{}The number in the binary format is{} {}'.format(colors['text_amarelo'], colors['fim'], binary))
elif chosen == 2:
    print('{}The number in the osctagonal format is{} {}'.format(colors['text_azul'], colors['fim'], octagonal))
elif chosen == 3:
    print('{}The number in the hexadecimal format is{} {}'.format(colors['text_roxo'], colors['fim'], hexadecimal))
elif chosen != 1 or 2 or 3:
    print('{}Invalid option.{}'.format(colors['text_bold'], colors['fim']))
