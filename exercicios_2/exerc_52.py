# Make a program that read a integer number and say if it  is  or  not  a prime number.

# CREATE A VARIABLE THE INPUT A INTEGER NUMBER
# CREATE A VARIABLE OF VALUE ZERO
# MAKE A FOR LOOP THE GO TO 2 UNTIL VARIBLE - 1, AND COUNT OF 1 BY 1:
#           MAKE A ITERATION OF RESTS OF A DIVISION THAT, YOU WILL CALCULATE THE VARIABLE WITH THE COUNTABLE OF THE FOR LOOP
#           IF THE RESULT OF THE ITERATION BE EQUAL ZERO:
#                       PRINT NO PRIME
#           ELSE:
#                       PRINT PRIME

n = int(input('Enter the integer number: '))
i = 0
for c in range(2, n - 1, 1):
    i = n % c    # The iteration should contain three variables to work,
# because we don't want the sum between two variables, but the result of each operation between them.
    if i == 0:
        print('no prime')
        break
    else:
        print(' Prime')
        break

