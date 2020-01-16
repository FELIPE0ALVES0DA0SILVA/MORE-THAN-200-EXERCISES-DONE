# Thrive the game of the challenge 28 where the computer will think in a
# number between 0 and 10. But now the player will try to guess  until hit.
# Showing in the and how many guesses was needs to win.

# IMPORT THE RANDOM LIBRARY
# CREATE THREE VARIABLES, TWO THE WILL INPUT ZERO AND OTHER THAT WILL INPUT A RANDINT OF 1 TO 10
# WHILE USER BE DIFFERENT OF THE COMPUTER:
#               CREATE A VARIABLE THAT WILL CAN TO THE USER CHOOSE A NUMBER
#               MAKE A ITERATION TO CONT THE LOOPS
#               IF THE COMPUTER CHOICE BE DIFFERENT OF THE USER:
#                               PRINT IF IT IS ABOVE OR UNDER OF THE CHOICE COMPUTER NUMBER, THE NUMBER THAT THE USER CHOSEN
#               ELIF COMPUTER NUMBER BE MINOR THAN THE USER NUMBER:
#                               PRINT THAT THE NUMBER USER CHOSEN IS UNDER OF THE COMPUTER NUBER
#               ELIF COMPUTER NUMBER BE EQUAL TO USER NUMBER:
#                               PRINT THAT THE NUMBER CHOSEN BY THE USER IS EQUAL THE NUMBER CHOSEN BY THE COMPUTER. AND ALL ATTEMPTS THAT THE USER TRY ASSERT.

from random import randint

print('I am thinking in a integer number, right now,from 0 until 10 try guess.')
s = 0
computer = randint(0, 10)
user = 0
while user != computer:
    user = int(input('Enter the chosen number: '))
    s += 1
    if computer > user:
        print('O número que eu pensei é maior que o digitado.')
    elif computer < user:
        print('O número que eu pensei é menor que o digitado.')
    elif computer == user:
        print('O número que eu pensei foi o {}.'.format(computer))
        print('You needed {} attempts to get to guess.'.format(s))
