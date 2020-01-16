# Make a program that read the sex of a person, but just accept the values 'M' or 'F'. In caso to be wrong, ask the digitation again until have a correct value.


# CREATE A VARIABLE THAT WILL CONTAIN A VALUE DIFFERENT OF 'M F'
# MAKE A WHILE LOOP THAT WILL STOP WHEN THE VARIABLE CREATED BE EQUAL TO 'M' AND 'F':
#               CREATE A VARIABLE THAT ASK TO THE USER THE GENDER OF HIM
# WHEN BREAK THE WHILE, PRINT THAT ALL RUNS WELL

n = 'w'
while n != 'M' and n != 'F':
    n = str(input('Enter your gender here [ M/F ]: ')).strip().upper()[0]
print('You digited the correct value.')
