# CREATE A FLOAT VARIABLE THAT READ THE DISTANCE OF A TRAVEL IN KILOMETERS
# CREATE TWO VARIABLE WITH THE COST PER KILOMETER
# IF THE DISTANCE WAS EQUAL OR MINOR OF 200 KILOMETER:
#           CALCULATE THE VALUE TO BE PAYED
#           PRINT THE VALUE TO BE PAYED IN DOLLARS
# ELSE:
#           CALCULATE THE VALUE TO BE PAYED
#           PRINT THE VALUE TO BE PAYED IN DOLLARS

distance = float(input('What is the distance of your travel, in KM? '))

bill1 = 0.5
bill2 = 0.45

if distance <= 200:
    value = distance*bill1
    print('You will pay US {} dollars.'.format(value))
else:
    value = distance*bill2
    print('You will pay US {} dollars.'.format(value))