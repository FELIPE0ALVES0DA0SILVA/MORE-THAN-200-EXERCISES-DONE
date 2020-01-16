# IMPORT THE RANDOM LIBRARY
# CREATE ALL THE VARIABLE THAT WILL CAN THE NAME OF EACH STUDENT
# CREATE A COMPOUNDS VARIABLE WITH ALL STUDENTS VARIABLES TOGETHER.
# MAKE THE OPERATIONS WITH THE METHOD CHOICE.
# PRINT THE RESULTS.

import random

aluno1 = input('Enter with the name of the student one: ')
aluno2 = input('Enter with the name of the student second: ')
aluno3 = input('Enter with the name of the student third: ')
aluno4 = input('Enter with the name of the student fourth: ')

student = (aluno1, aluno2, aluno3, aluno4)
ran = random.choice(student)

print('The aluno choosen to erase '
      'the blackboard is {}.'.format(ran))
