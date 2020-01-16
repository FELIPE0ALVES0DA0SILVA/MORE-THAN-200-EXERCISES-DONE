
# Make a jôken pô game that the user can play against the computer and the choice of the computer be random.

# Import the libraries required: random and time
# Create the list that the computer will use to choice the play randomly of each round
# Declare the constants the will enable the condition work and will link the choices of the user in each round
# Declare the variables of a initial value to the conditions accept this values
# Create the first condition to ask if the user want to play with the computer
#       Create the condition If yes:
#               Create the conditions that will enable the program calculate who wins the first round
#                       Create the calculus that will calculate, according to who wins the round, the points that the winner won, by win the round
#                       Print the result of the round, with the score between the two players
#               Create the conditions that will enable the program calculate who wins the second round
#                       Create the calculus that will calculate, according to who wins the round, the points that the winner won, by win the round
#                       Print the result of the round, with the score between the two players
#               Create the conditions that will enable the program calculate who wins the third round
#                       Create the calculus that will calculate, according to who wins the round, the points that the winner won, by win the round
#                       Print the result of the round, with the score between the two players
#               Create the greetings of the computer to the user for possiblity the battle between them
#               Create the calculus to calculate the final result of the three rounds
#               Create the conditions to each result of the rounds: Winners, Losers and Draw
#                       Print the answer accordingly to what result was appointed
#       Create the condition Else:
#               print the answer accordingly
# Create the condition if the user dont want to play with the computer
#       Print the answer accordingly with the condition



import random
import time

colors = {'fim':'\033[m', 'red':'\033[1;31m',
         'cyen':'\033[1;34m',
         'yellow':'\033[1;33m',
         'green':'\033[1;32m',
          'bold':'\033[1m'}

choices = ['ROCK', 'PAPER', 'SCISSOR', 'ROCK', 'PAPER', 'SCISSOR']

rock = 'ROCK'
paper = 'PAPER'
scissor = 'SCISSOR'
U3 = 0
U2 = 0
U = 0
C = 0
C2 = 0
C3 = 0
print('You are ready to play with me, your favorite computer? ')
print()

yes = str(input("if YES, digit 'yes' in your laptop: ")).upper()
if yes == 'YES':
    print('OKAY')
    print('You choice only one thing in each road, and their is: rock, paper or scissor. '
    'We will play four rounds to see who is the better, I guarantee myself, and you...too?? lol')
    print('READY???')
    print()
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print(' ROCK, PAPER OR SCISSOR!!!!')
    user = str(input('{}PLAY FASTER THAN YOU CAN!!! {}'.format(colors['yellow'], colors['fim'])).upper())
    computer = random.choice(choices)


    if computer == rock and user == scissor or computer == paper and user == rock or computer == scissor and user == paper:
        C = 0 + 1
        print('I choice {}{}{} and you {}{}{}'.format(colors['red'], computer.upper(), colors['fim'], colors['cyen'], user.upper(), colors['fim']))
        print('{}I win this round..Huhull{}'.format(colors['red'], colors['fim']))

    elif user == rock and computer == scissor or user == paper and computer == rock or user == scissor and computer == paper:
        U = 0 + 1
        print('I choice {}{}{} and you {}{}{}'.format(colors['red'], computer.upper(), colors['fim'], colors['cyen'], user.upper(), colors['fim']))
        print('{}You is the winner, in the first round{}'.format(colors['cyen'], colors['fim']))
    elif user == scissor and computer == scissor or user == paper and computer == paper or user == rock and computer == rock:
        print('I choice {}{}{} and you {}{}{}'.format(colors['red'], computer.upper(), colors['fim'], colors['cyen'], user.upper(), colors['fim']))
        print('{}We draw the match...Oh no, come on!!!{}'.format(colors['green'], colors['fim']))

    time.sleep(2)

    print('This first round was {} for you and {} for me, that the Better wins!!!'.format(U, C))
    print( 'Now we will start the second round. Are you ready, NOOB!?!')
    y = str(input("digit 'Yes' if yes: ")).upper()
    if y == 'YES':
        print('fine')
        print()
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        print('GO!!!')
        user = str(input('{}PLAY FASTER THAN YOU CAN!!! {}'.format(colors['yellow'], colors['fim'])).upper())
        computer = random.choice(choices)
        if computer == rock and user == scissor or computer == paper and user == rock or computer == scissor and user == paper:
            C2 = 0 + 1
            print('I choice {}{}{} and you {}{}{}'.format(colors['red'], computer.upper(), colors['fim'], colors['cyen'], user.upper(), colors['fim']))
            print('{}I win this round..Huhull{}'.format(colors['red'], colors['fim']))

        elif user == rock and computer == scissor or user == paper and computer == rock or user == scissor and computer == paper:
            U2 = 0 + 1
            print('I choice {}{}{} and you {}{}{}'.format(colors['red'], computer.upper(), colors['fim'], colors['cyen'], user.upper(), colors['fim']))
            print('{}You is the winner, in the second round{}'.format(colors['cyen'], colors['fim']))
        elif user == scissor and computer == scissor or user == paper and computer == paper or user == rock and computer == rock:
            print('I choice {}{}{} and you {}{}{}'.format(colors['red'], computer.upper(), colors['fim'], colors['cyen'], user.upper(), colors['fim']))
            print('{}We draw the match...Oh no, come on!!!{}'.format(colors['green'], colors['fim']))

        time.sleep(1)

        print('This second round finish, the game score in this round was {} for you and {} for me, '
              'now is the ultimate!!!'.format(U2, C2))
        print(' Now, no one of us have the right to choice this round, is question of honor!!!')
        print()
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        print('GO!!!')
        user = str(input('{}PLAY FASTER THAN YOU CAN!!! {}'.format(colors['yellow'], colors['fim'])).upper())
        computer = random.choice(choices)
        if computer == rock and user == scissor or computer == paper and user == rock or computer == scissor and user == paper:
            C3 = 0 + 1
            print('I choice {}{}{} and you {}{}{}'.format(colors['red'], computer.upper(), colors['fim'], colors['cyen'], user.upper(), colors['fim']))
            print('{}I win this round..Huhull{}'.format(colors['red'], colors['fim']))

        elif user == rock and computer == scissor or user == paper and computer == rock or user == scissor and computer == paper:
            U3 = 0 + 1
            print('I choice {}{}{} and you {}{}{}'.format(colors['red'], computer.upper(), colors['fim'], colors['cyen'], user.upper(), colors['fim']))
            print('{}You is the winner, in the third round{}'.format(colors['cyen'], colors['fim']))
        elif user == scissor and computer == scissor or user == paper and computer == paper or user == rock and computer == rock:
            print('I choice {}{}{} and you {}{}{}'.format(colors['red'], computer.upper(), colors['fim'], colors['cyen'], user.upper(), colors['fim']))
            print('{}We draw the match...Oh no, come on!!!{}'.format(colors['green'], colors['fim']))


        print('The game score in this round was {} for you and {} for me.'.format(U3, C3))
        time.sleep(1)
        print('We finish for here, was a good play, friend yet, right? LOL I am just kidding... The game score was....')
        time.sleep(3)
        print("I'm nervous rsrs")
        time.sleep(2)
        print('3')
        time.sleep(2)
        print('2')
        time.sleep(2)
        print('1')
        time.sleep(3)
        Ut = U + U2 + U3
        Ct = C + C2 + C3
        if Ut > Ct:
            print('{}{}{} to {}{}{}.'.format(colors['cyen'], Ut, colors['fim'], colors['red'], Ct, colors['fim']))
            time.sleep(1)
            print('{}HOOOOOOO....NOOOOOO, YOU WIN??? Never speak to me again, THIS GAME IS BORING!{}'.format(colors['cyen'], colors['fim']))
        elif Ut == Ct:
            print('{}{}{} to {}{}{}.'.format(colors['cyen'], Ut, colors['fim'], colors['red'], Ct, colors['fim']))
            time.sleep(1)
            print('Was a good battle, see you again, Boddy')
        elif Ut < Ct:
            time.sleep(1)
            print('{}{}{} to {}{}{}.'.format(colors['cyen'], Ut, colors['fim'], colors['red'], Ct, colors['fim']))
            time.sleep(1)
            print("{}I win...wait... I WIN!!! HUHULLLLL... I want say{}"
                  "{}... of course I win, who are you to win of me, mere human!!!{}".format(colors['red'], colors['fim'], colors['red'], colors['fim']))
            print('{}BYEEEEE!!! LOSEEEEER.{}'.format(colors['red'], colors['fim']))
    else:
        print('It is OKAY, I win so.')
elif yes != 'YES':
    print('Oh, no...I dont want though, loser.')


