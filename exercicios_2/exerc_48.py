
# Make a program that calculate the sum between
# all the odds numbers that it is multiples of three and they meet in the range of from 1 to 500.
# CREATE TO VARIABLES WITH THE VALUE EQUAL ZERO
# MAKE A FOR LOOP THAT COUNT OF 0 TO 500 AND IN 2 BY 2
#           DECLARE A CONDITION FI COUNTED NUMBER OF THE LOOP EQUAL ZERO:
#                       USE ONE OF THE VARIABLE CREATED AGO AND MAKE A ITERATON COUNTING 1 BY 1 UNTIL 500
#                       USE ANOTHER AND LAST VARIABLE TO MAKE A ITERATION TO SUM ALL THE VALUES TAKEN
# PRINT THE SU OF ALL VALUES TAKEN AND ALL THE VALUES COUNTED WITHIN THE LOOP AND THE CONDITION

s = 0
cont = 0
for c in range(1, 500 + 1, 2):
    if c % 3 == 0:
        cont += 1
        s += c  # This iteration calculate the result of C plus S, and the result stay saved in S
print(s)
print('Valores contados {}.'.format(cont))
