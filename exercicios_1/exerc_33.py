# CREATE THREE FLOAT VARIABLES THAT WILL INPUT ONE NUMBER PER VARIABLE
# IF THE FIRST VARIABLE BE MAJOR TO THE SECOND VARIABLE AND THE FIRST VARIABLE BE MAJOR TO THE THIRD VARIABLE:
#           PRINT THAT THE MAJOR NUMBER BETWEEN THEM IS THE FIRST NUMBER
# ELSE:
#           IF NUMBER TWO BE MAJOR THAN NUMBER ONE AND NUMBER TWO BE MAJOR THAN NUBER THREE:
#                       PRINT THAT THE MAJOR NUMBER IS THE SECOND NUMBER
#           ELIF THE NUMBER THREE BE MAJOR THAN NUMBER TWO AND NUMBER ONE:
#                       PRINT THAT THE MAJOR NUMBER IS THE THIRD NUMBER
# IF NUMBER ONE BE MINOR THAN NUMBER TWO AND THREE:
#           PRINT TAHT THE MINOR NUMBER IS THE FIRST NUMBER
# ELSE:
#           IF NUMBER TWO BE MINOR THAN NUMBER ONE AND THREE:
#                       PRINT THAT THE MINOR NUMBER IS THE NUMBER TWO
#           ELIF NUMBER THREE BE MINOR THAN NUMBER TWO AND ONE:
#                       PRINT THAT THE MINOR NUMBER IS THE NUMBER THREE

num_1 = float(input('Enter with the first number: '))
num_2 = float(input('Enter with the second number: '))
num_3 = float(input('Enter with the third number: '))

if num_1 > num_2 and num_1 > num_3:
    print('O maior é {}.'.format(num_1))
else:
    if num_2 > num_1 and num_2 > num_3:
        print('O maior é {}.'.format(num_2))
    elif num_3 > num_1 and num_3 > num_2:
        print('O maior é {}.'.format(num_3))


if num_1 < num_2 and num_1 < num_3:
    print('O menor é {}.'.format(num_1))
else:
    if num_2 < num_1 and num_2 < num_3:
        print('O maior é {}.'.format(num_2))
    elif num_3 < num_1 and num_3 < num_2:
        print('o menor é {}.'.format(num_3))
