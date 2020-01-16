# IMPORT THE DESIRED METHOD OF THE LIBRARY MATH
# CREATE THE FIRST VARIABLE TO INPUT THE FLOAT NUMBER
# CREATE THE SECOND VARIABLE TO INPUT THE FLOAT NUMBER.
# CREATE THE VARIABLE CONTAIN THE OPERATION TO GIVEN UP THE CORRECT RESULT
# PRINT THE RESULT

import math

cat_oposto = float(input('Enter the value of opposite collet: '))
cat_adjacente = float(input('Enter the value of adjacent collet: '))


hypot = math.sqrt((cat_oposto**2)+(cat_adjacente**2))

print('the value of hypotenuse in your triangle '
      'rectangle is {}.'.format(hypot))
