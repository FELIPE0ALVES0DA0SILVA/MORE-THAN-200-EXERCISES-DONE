
value = float(input('Enter the total price: US '))
months = int(input('How many months you will should pay the installments? '))
interest = float(input('The fee per month of the interest: '))


interest1 = interest/100
amount = value*((1 + interest1) ** months)


print('The real total value that you will need pay,'
      ' will be: US {:.4f}.'.format(amount))
