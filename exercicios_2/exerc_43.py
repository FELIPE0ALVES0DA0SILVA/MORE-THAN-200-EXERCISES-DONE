
# Develop a logic that read the weight of a person, calculate your Index of mass body and show your status,
# according with the bottom table:
#           Under of 18.5: Under of the correct weight
#           Between 18.5 and 25: weight ideal
#           25 until 30: overweight
#           30 until 40: obesity
#           above of 40: morbid obesity

# CREATE A VARIABLE THAT WILL READ THE WEIGHT OF A OBJECT
# CREATE A VARIABLE THAT WILL READ THE HIGH OF A OBJECT
# CALCULATE THE IMC WITH THIS MEASURES
# IF THE IMC BE MINOR THAN 18.5:
#           PRINT THAT THE OBJECT IF UNDERWEIGHTED OF THE CORRECT WEIGHT
# ELIF THE IMC BE BETWEEN 18.5 AND 25:
#           PRINT THAT THE OBJECT IS IN THE IDEAL WEIGHT
# ELIF THE IMC BE BETWEEN 25 ADN 30:
#           PRINT THAT THE OBJECT IS OVERWEIGHTED OF THE CORRECT WEIGHT
# ELIF THE IMC BE BETWEEN 30 AND 40:
#           PRINT THAT THE OBJECT IS IN OBESITY
# ELIF THE IMC IS ABOVE 40:
#           PRINT THE THE OBJECT IS IN MORBID OBESITY


weight = float(input('Enter with your weight: '))
high = float(input('Enter with your high: '))

imc = weight/high**2

if imc < 18.5:
    print('Under of the correct weight.')
elif 18.5 >= imc <= 25:
    print('weight ideal')
elif 25 > imc <= 30:
    print('overweight')
elif 30 > imc <= 40:
    print('obesity')
elif weight > 40:
    print('morbid obesity')
