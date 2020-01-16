
# The confederation of national swimming need of a program that re
# ad the year of born of a athlete and show your category, accordingly to the age:
#       until 9 years: Little
#       until 9 years: Childish
#       until 9 years: Junior
#       until 9 years: Senior
#       Above: Master

# Import the library required: datetime
# Create the variable asking for the user the year that he born.
# Create the variable of the current year.
# Create the calculus to arrive in the age of the user
# Create the conditions to say in what category the user belongs.
#       Print the answer to the user of what category he belongs.

from datetime import date
year_born = int(input('What tear you was born? '))
actual = date.today().year
current_year = actual
age = current_year - year_born

if age <= 9:
    print('Little')
elif age <= 14:
    print('Childish')
elif age <= 19:
    print('Junior')
elif age == 20:
    print('Senior')
elif age > 20:
    print('Master')
