# Create a program that read the year of born  of seven peoples.
# In the end, show how many peoples yet don't reach the majority and how many already are adults.

# IMPORT DATETIME
# CREATE TWO VARIABLES WITH ZERO VALUE
# MAKE A FOR LOOP THAT COUNT OF 1 TO 8 AND 1 BY 1:
#               CREATE ANOTHER VARIABLE THAT CONTAIN THE YEAR OF BORN
#               TAKE A METHOD TO EXTRACT THE CURRENT YEAR
#               MAKE A OPERATION TO TAKE THE AGE
#               IF AGE MAJOR OR EQUAL AT 18:
#                               MAKE A ITERATION COUNT 1+ IN EACH LOOP THAT BE TRUTH
#               ELIF YEAR BORN MAJOR AT TODAY:
#                               PRINT A MESSAGE
#               ELSE:
#                               MAKE ANOTHER ITERATION COUNT 1+ IN EACH LOOP THAT BE TRUTH
# PRINT THE RESULT
from datetime import date
s = 0
s1 = 0
for c in range(1, 8):
    year_born = int(input('What year the {}° you born? '.format(c)))
    today = date.today().year
    age = today - year_born
    if age >= 18:
        s += 1
    elif year_born > today:
        print('You kidding me, right? ')
    else:
        s1 += 1
print(' {} people are adult and {} are under age.'.format(s, s1))
