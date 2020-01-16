# Develop a program that read six integers numbers and show the sum only of that were pairs. If the value digit  was odd, disconsider it.

# CREATE TWO VARIABKES THE WILL INOUT ZERO WITH VALUES
# MAKE A FOR LOOP OF 1, 7 AND COUNT OF 1 BY 1:
#           CREATE A VARIABLE THAT INPUT A INTEGER NUMBER
#           IF THIS NUMBER BE PAIR:
#                       MAKE TWO ITERATION, ONE BY SUM OF ALL VALUES AND OTHER BY COUNT THE VALUES
# PRINT THE SUM AND THE COUNTABLE OF THE VALUES.

cont = 0
s = 0
for c in range(1, 7):
    n = int(input('Enter the {}° integer number: '.format(c)))
    if n % 2 == 0:
        s += n
        cont += 1
print('You informed {} pair numbers and the sum was {}'.format(cont, s))
