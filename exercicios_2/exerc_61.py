# Make a program that read the first term and the reason of a PA.
# In the end, show the 10 first terms of this progression, but now, using while loop.


first_term = int(input('Enter the first term of your arithmetic progression: '))
reason_AP = int(input('Enter the reason of your arithmetic progression: '))
q = 0
while q < 10:
    print(first_term, end='->')
    first_term += reason_AP
    q += 1


# for c in range(first_term, (reason_AP* 10) + first_term, reason_AP):
#    print(c, end=' -> ')

print(' OVER')
