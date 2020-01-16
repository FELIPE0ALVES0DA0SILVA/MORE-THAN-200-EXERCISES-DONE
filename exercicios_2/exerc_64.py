# Make a program that read several integer numbers for the keyboard.
# The program only will stop when the user digit the value 999, that it is the stopped condition. In the and,
# show how many numbers was digited and what was the sum between them.

i = s = n = 0

while n != 999:
    n = int(input('Enter a integer number, please: '))
    if n != 999:
        s = s + n
        i += 1
print('You digited {} times and the sum of the digited numbers is {}.'.format(i, s))
