# Remake the challenge 9, showing the times table that the user choose. But now using  a FOR loop.

# CREATE TWO VARIABLES, ONE WITH ZERO VALUE AND OTHER THAT WILL INPUT A NUMBER
# MAKE A FOR LOOP THAT WILL GO TO THE 0 UNTIL 10 AND WILL COUNT OF 1 BY 1:
#            MAKE A ITERATION OF TIMES WITH THE COUNTED VALUES OF TH LOOP AND THE NUMBER READIED BY THE VARIABLE ABOVE
#            PRINT THE RESULT OF THIS CALCULUS

t = 0
n = int(input('Enter any number: '))

for c in range(0, 10 + 1):
    t = c * n # This iteration loop is different, because one of the variables don't repeat itself to give start in the iteration loop, is there three different variables that work even in the loop and the iteration.
    print(t)
