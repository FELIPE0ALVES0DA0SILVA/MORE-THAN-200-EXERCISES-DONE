# Make a program that read the first term and the reason of a PA.
# In the end, show the 10 first terms of this progression, but now, using while loop,
# however, now, the program, after finish the operation,
# should to ask for the user if it want continue the program digiting more one AP or if it want to finish.


first_term = int(input('Enter the first term of your arithmetic progression: '))
reason_AP = int(input('Enter the reason of your arithmetic progression: '))

i = 0
q = 0
finish = 0

while finish != 2:
    if q < 10:
        print(first_term, end=' ')

        first_term += reason_AP
        q += 1
    elif q == 10:
        if finish == 1:
            i = int(input('How many terms do you want to be showed: '))
            while i != 0:
                print(first_term, end=' ')
                first_term += reason_AP
                i -= 1
    if q == 10:
        print('''
        [ 1 ] - YES
        [ 2 ] - NO ''')
        finish = int(input('Do you want continue with the AP? [ 1 | 2 ] '))
        if finish != 1 and finish != 2:
            print('Invalid option.')


# for c in range(first_term, (reason_AP* 10) + first_term, reason_AP):
#    print(c, end=' -> ')

print(' OVER')
