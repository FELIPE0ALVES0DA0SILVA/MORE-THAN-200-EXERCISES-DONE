# CREATE THREE FLOAT VARIABLES THAT READ ONE NUMBER OF STRAIGHT PER EACH VARIABLE
# MAKE THE FORMULAS THAT WILL CALCULATE IF WITH THE THREE VALUES IS POSSIBLE FORMER A TRIANGLE
# IF BE POSSIBLE:
#           PRINT TAHT ITS POSSIBLE FORMER A TRIANGLE
# ELSE:
#           PRINT TAHT ITS NOT POSSIBLE FORMER A TRIANGLE

length1 = float(input('Enter the first straight value: '))
length2 = float(input('Enter the second straight value: '))
length3 = float(input('Enter the third straight value: '))

formula_1 = (length1 + length2)
formula_2 = (length2 + length3)
formula_3 = (length1 + length3)

if formula_1 > length3 or formula_2 > length1 or formula_3 > length2 :
    print('It is possible former a triangle.')
else:
    print('With the values especified, do not is possible former a triangle.')
