# IMPORT THE  MATH LIBRARY
# CREATE A VARIABLE THAT INPUT A REAL VALUE.
# MAKE THE OPERATION UTILIZING THE METHOD IMPORTED.
# PRINT THE VALUE TRUNKED.

from math import trunc
num = float(input('Enter with the real number: '))

num1 = trunc(num)

print('The number {} have the integer part {}.'.format(num, num1))
