# Create a program that read the name, age and sex of four persons. In the end of the program, show:
# The average of the ages of the group
# Which is the name of the men ore elderly
# How many woman have less than 20 years.

# MAKE FOUR VARIABLES THAT, THREE WILL BE EMPTY INTEGERS AND THE LAST WILL BE EMPTY STRINGS
# MAKE A FOR LOOP OF 1 TO 5 AND COUNT 1 BY 1:
#               CREATE A FLOAT VARIABLE THAT CONTAIN THE AGE OF EACH PERSON PER LOOP:
#               CREATE A VARIABLE BY NAME
#               CREATE A VARIABLE BY SEX
#               MAKE A ITERABLE THAT CONTAIN THE AGE OF ALL PERSONS IN THE END OF THE LOOP FOR
#               IF COUNTABLE BE EQUAL ONE AND SEX BE EQUAL 'M':
#                               TAKE A VARIABLE AND SAVE THE NAME
#                               TAKE ANOTHER VARIABLE AND SAVE THE AGE
#               ELIF AGE MAJOR THAT VARIABLE CONTAINED THAT FIRST AGE AND SEX BE EQUAL 'M':
#                               UPDATED THE VALUE OF THE VARIABLE THAT CONTAIN THE NAME
#                               UPDATED THE VALUE OF THE VARIABLE THAT CONTAIN THE AGE
#               ELIF SEX BE EQUAL 'F' AND AGE MINOR TAN 20:
#                               MAKE A ITERATION THAT COUNT THE TIMES THAT THE LOOP PASSED BY THERE.
# PRINT THE AVERAGE BETWEEN THE INFORMED AGES
# PRINT THE NAME OF THE MOST ELDERLY MEN
# PRINT THE AMOUNT OF WOMAN WITH MINUS THAN 20 YEARS

plus = 0
saved = 0
elderly = ''
major_age = 0
for c in range(1, 5):
    age = float(input('What is the  age of the {}° person? '.format(c)))
    name = str(input('What is your name? ')).upper()
    sex = str(input('What is your sex [ M / F ]? ')).upper()
    saved = saved + age
    if c == 1 and sex == 'M':
        elderly = name
        major_age = age
    elif age > major_age and sex == 'M':
        elderly = name
        major_age = age
    elif sex == 'F' and age < 20:
        plus += 1
print('The average between the four ages informed is {}.'.format(saved/c))
print('The name of the most elderly senior is {}.'.format(major_age))
print('The amount of woman with less than 20 years is {}.'.format(plus))

