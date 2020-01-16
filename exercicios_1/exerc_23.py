# CREATE A VARIABLE THE INPUT NUMBERS BETWEEN 0 AND 9999
# CALCULATE YOUR REST
# CALCULATE AND TAKE JSUT THE INTEGER PART OF A DIVISION
# TAKE THE FIRST INTEGER PART CALCULATED AND PUT IN A NEW CYCLE, ALWAYS TAKE THE INTEGER NEW PART
# IN EACH CYCLE,  PRINT THE REST OF THE OPERATION

num = int(input('Enter the number between 0 and 9999: '))

rest1 = num%10
int1 = num//10

print('Unity: {}'.format(rest1))

rest2 = int1%10
int2 = int1//10

print('Dozen: {}'.format(rest2))

rest3 =int2%10
int3 = int2//10

print('Cent: {}.'.format(rest3))

rest4 = int3%10
int4 = int3//10

print('Thousands: {}'.format(rest4))


