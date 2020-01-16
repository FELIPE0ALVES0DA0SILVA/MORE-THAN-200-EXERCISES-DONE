# CREATE A INTEGER VARIABLE TAHT READ A INTEGER NUMBER
# CALCULATE THE REST OF THE NUMBER SPLINTED BY TWO AND PUT IN A VARIABLE
# IF THE THIS VARIABLE BE EQUAL ZERO:
#           PRINT THAT THE NUMBER IS PAIR
# ELSE:
# PRINT THAT THE NUMBER IS ODD

number = int(input('Enter the integer number: '))

pair = number%2

if pair == 0:
    print('This number is pair.')
else:
    print('This number is odd.')