
#    Read a program to approve a banl loan to a buy of a house.
#    The program will ask the value of the house, the salary of the buyer, and in
#    how many years he will pays.

#    declare the variables

#    set up the operation to calculate what is request

#    mount and declare the condition for the program run
#       declare the result expected within the variables




value_home = int(input('What is the value of the house: '))
salary = int(input('What is your salary monthly? '))
year_pay = int(input('For how many years in want to pay this house: '))

months_pay = year_pay*12
divided_home = value_home/months_pay
a1 = salary * (30 / 100)
exceed = a1 - divided_home

if divided_home > a1:
    print()
    print(' The value to pay per month exceed US {:.2f} dollars of 30% of your income. '
          'The loan was denied.'.format(-1*exceed))
else:
    print()
    print('Your profile was verified. The loan was accept, congratulations.')