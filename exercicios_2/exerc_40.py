
# Create a program that read two notes of a student and calculate your average.
# Showing a messenge in the end. According with the tagered average:
#    -- The average is under of 5.0:
#    REPPROVED
#    -- The average is betwwen 5.0 and 6.9:
#    RECOVERING
#    -- The average is 7.0 or above:
#   APPROVED

# Variables
# Formula
# IF elif
#    Print result


note_one = float(input('Enter the first not: '))
note_two = float(input('Enter the second not: '))

average = (note_one + note_two)/2       # FLOAT ALWAYS CALCULATE ALL DECIMALS WITHIN A INTERVAL OF NUMBERS.

if average < 5:
    print('REPPROVED')
elif 7 > average >= 5:
    print('RECOVERING')
elif average > 7:
    print('APPROVED')
