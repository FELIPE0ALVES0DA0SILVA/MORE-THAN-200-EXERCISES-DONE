# CREATE A FLOAT VARIABLE THAT READ THE SPEED OF A CAR
# IF THE SPEED BE MORE THAN 80 KILOMETER PER HOUR:
#           PRINT THAT THE USER WAS FINED
#           CALCULATE THE FINED
#           PRINT HOW MUCH WILL COST THE FINED IN DOLLARS

speed = float(input('What is your speed in the '
                    'car, right now? '))

if speed > 80:
    print('Sorry, you was fined')
    fined = (speed - 80)*7
    print('the fined it will cost you US {:.2f} dollars.'.format(fined))

