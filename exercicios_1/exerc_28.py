# IMPORT RANDOM LIBRARY
# IMPORT TIME LIBRARY
# PRINT A PHRASE
# CAN TO THE USER ENTER WITH A NUMBER
# RANDOMIZE A NUMBER TO THE COMPUTER
# WAIT SOME SECOND TO SIMULATE A THINKING CHOOSE
# PRINT THE NUMBER RANDOMIZED BY THE COMPUTER
# DECLARE THE CONDITIONS
#           IF THE CHOOSE OF THE USER BE EQUAL TO THE CHOOSE OF THE COMPUTER:
#                       PRINT THAT THE USER WIN
#           IF THE USER CHOOSE NOT TO BE EQUAL TO THE COMPUTER CHOOSE:
#                       PRINT THAT THE USER LOST

import random
import time

print('I am thinking in a integer number, right now, from 0 until 5 try guess.')

user = int(input('Enter the chosen number: '))

numbers = [1, 2, 3, 4, 5, 0]
computer = random.choice(numbers)

print('process...')
time.sleep(3)

print('Pensei no número {}.'.format(computer))

if computer == user:
    print('congratulations, you win.')
else:
    print('Oh no, you lose, LOSER.')
