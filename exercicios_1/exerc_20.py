# IMPORT THE RANDOM LIBRARY
# CREATE ALL THE VARIABLES TO INPUT THE NAME OF EACH STUDENT
# MAKE THE OPERATIONS WTH RANDOM METHOD.
# PRINT THE RESULTS.

import random

aluno1 = str(input('Enter with the name of the student one: '))
aluno2 = str(input('Enter with the name of the student second: '))
aluno3 = str(input('Enter with the name of the student third: '))
aluno4 = str(input('Enter with the name of the student fourth: '))

student1 = (aluno1, aluno2, aluno3, aluno4)
ran1 = random.sample(student1, 4)

print('The sequence of the presentation is {}'.format(ran1))



