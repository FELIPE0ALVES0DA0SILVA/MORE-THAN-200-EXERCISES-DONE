# IMPORT THE LIBRARY DATETIME AND TAKE THE METHOD DATE
# CREATE A INTEGER VARIABLE THAT READ THE CORRESPONDENT YEAR
# MAKE THE CALCULUS TO CALCULATE THE BIXESSTUS YEAR
# IF YEAR EQUAL ZERO:
#           PRINT NOTHING AND TAKE THE ACTUAL YEAR
# IF BISSEXTUS EQUAL ZERO AND REST OF THE DIVISION OF THE YEAR BY ONE HUNDRED DIFFERENT OF ZERO:
#           PRINT THE CURRENTLY YEAR IS BISSEXTUS
# ELSE:
#           PRINT THAT THE YEAR IS NOT BISSEXTUS


from datetime import date

year = int(input('Enter the desired year: '))

bissexto_cent = year % 400
bissexto = year % 4
if year == 0:
    year = date.today().year
if bissexto == 0 and year % 100 != 0 or bissexto_cent == 0 :
    print('This year {} is bissextus.'.format(year))
else:
    print('The year {} is NOT bissextus.'.format(year))

