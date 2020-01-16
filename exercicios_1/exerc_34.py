# CREATE A FLOAT VARIABLE THAT READ ANY SALARY
# CREATE ONE VARIABLE THAT CONTAIN 10% IN FRACTIONAL NUMBER
# CREATE ANOTHER VARIABLE THAT CONTAIN 15% IN FRACTIONAL NUMBER
# IF SALARY BE MAJOR THAN 1250;
#           CALCULATE A INCREASE OF 10 PERCENT UNDER THE SALARY ABOVE
#           PRINT THE SALARY UPDATED
# ELSE:
#           CALCULATE A IN CREASE OF 15 PERCENT UNDER THE SALARY ABOVE
#           PRINT THE SALARY UPDATED

salary = float(input('What is your salary? '))

percent_one = 10/100
percent_two = 15/100

if salary > 1250:
    increase_one = (percent_one*salary) + salary
    print('Your salary updated is US {:.2f} dollars.'.format(increase_one))
else:
    increase_two = (percent_two*salary) + salary
    print('Your salary updated is US {:.2f} dollars.'.format(increase_two))