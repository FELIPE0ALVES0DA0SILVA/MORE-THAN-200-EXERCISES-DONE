# IMPORT THE LIBRARY MATH
# CAN THE ANGLE THROUGHOUT A IMPUTABLE VARIABLE
# CALCULATE THE SIN, COS AND TAN WITH THE ANGLE INPUTTED IN A OPERATION.
# PRINT THE RESULTS OF THE OPERATIONS.

import math


angle = float(input('What is your angle? '))

sin = math.sin(math.radians(angle))
cos = math.cos(math.radians(angle))
tan = math.tan(math.radians(angle))

print(' The sine of {}° is {:.5f}, the cosine is {:.5f} '
      'and the tangent is {:.5f}'.format(angle, sin, cos, tan))

