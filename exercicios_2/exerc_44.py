
# Elaborate a program that calculate the value to be payed for a product.
# Considering your normal price and payment condition:
#           In cash in money 10 percent off
#           In cash in the credit card: 5 percent off
#           In until 2 times in the credit card: normal price
#           3 times or more in the credit card: 20% of interest

# Import the library: time
# Create a list of colors or textual features to implement in your program
# Create a variable of input to the user digit the value of the product
# Declare the constants that will be used to direct the choice of the user to a if elif
# Create a variable the will ask to the user what way of payment he wants
# Create the conditionals to the program link the choice of the user with each If elif
#       Create the calculus to calculate the value of the product, according with the choice of payment that the client chosen.
#       Print the result, according with each if elif


import time

colors = {'fim':'\033[m', 'red':'\033[1;31m',
         'cyen':'\033[1;34m',
         'yellow':'\033[1;33m',
         'green':'\033[1;32m',
          'bold':'\033[1m'}

value_product = float(input('What is the price of your product, please? '))

in_cash_money = 1
print('{}Digit {}>>>  1  <<<{} if you want pay with in cash with money.{}'
      .format(colors['red'], colors['fim'], colors['red'], colors['fim']))
print('{}You will win 10% in discount.{}'.format(colors['red'], colors['fim']))
time.sleep(1)
print('')

in_cash_credit = 2
print('{}Digit {}>>>  2  <<<{} if you want pay with in cash with creditcard.{}'
      .format(colors['green'], colors['fim'], colors['green'], colors['fim']))
print('{}You will win 5% in discount.{}'.format(colors['green'], colors['fim']))
time.sleep(1)
print('')

parcel_2 = 3
print('{}Digit {}>>>  3  <<<{} if you want pay  parceled two times with creditcard.{}'
      .format(colors['cyen'], colors['fim'], colors['cyen'], colors['fim']))
print('{}The value of the product will be the same.{}'.format(colors['cyen'], colors['fim']))
time.sleep(1)
print('')

parcel_more = 4
print('{}Digit {}>>>  4  <<<{} if you want pay parceled with creditcard more them twice times.{}'
      .format(colors['yellow'], colors['fim'], colors['yellow'], colors['fim']))
print('{}You will pay 20% of interest.{}'.format(colors['yellow'], colors['fim']))
time.sleep(1)
print('')

choice = int(input('{}How do you think pay?{} '.format(colors['bold'], colors['fim'])))

cash_money = value_product*(90/100)
cash_credit = value_product*(95/100)
times_2 = value_product
times_more = value_product*(120/100)

if in_cash_money == choice:
    print('{}In cash in money 10 percent off, the price is US {:.2f} dollars.{}'.format( colors['red'], cash_money, colors['fim']))
elif in_cash_credit == choice:
    print('{}In cash in the creditcard: 5 percent off, the price is US {:.2f} dollars.{}'.format(colors['yellow'], cash_credit, colors['fim']))
elif parcel_2 == choice:
    parcelled_2 = times_2 / 2
    print('{}In until 2 times in the creditcard: normal price, the price is {:.2f} dollars.{}'.format(colors['cyen'], times_2, colors['fim']), end='')
    print('{}You will pay {:.2f} dollars per month.{}'.format(colors['cyen'],parcelled_2, colors['fim']))
elif parcel_more == choice:
    more = int(input('How many parcels do you will want parcel your product? '))
    parcelled_more = times_2 / more
    print('{}3 times or more in the creditcard: 20% of interest, the price is {}{:.2f}{} dollars.{}'.format(colors['green'], colors['fim'], times_more, colors['green'], colors['fim']), end='')
    print('{} You will pay {}{:.2f}{} dollars per month.{}'.format(colors['green'], colors['fim'], parcelled_more, colors['green'], colors['fim']))
