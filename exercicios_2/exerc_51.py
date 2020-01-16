# Make a program that read the first term and the reason of a PA. In the end, show the 10 first terms of this progression.

# CREATE TWO VARIABLES THAT READ ONE OF THEM, THE FIRST TERM OF A AP ADN THE LAST THE PROPORTIONAL REASON OF A AP.
# MAKE A FOR LOOP THE GO OF FIRST TERM UNTIL REASON OF A AP TIMES TO TEM AND  PLUS WITH THE FIRST TERM OF A AP, AND COUNT WITH THE REASON OF A AP.
#           PRINT THE COUNTABLE OF THIS LOOP
# END WITH OVER


first_term = int(input('Enter the first term of your arithmetic progression: '))
reason_AP = int(input('Enter the reason of your arithmetic progression: '))

for c in range(first_term, (reason_AP* 10) + first_term, reason_AP):
    print(c, end=' -> ')

print(' OVER')

