# CREATE A VARIABLE THAT INPUT THE FULL NAME OF A PERSON
# UPPERCASE THIS VARIABLE
# SPLIT THIS VARIABLE
# AND IF EXIST THE NAME 'SILVA' IN ANY PART OF THE FULL NAME SPLINTED, PRINT IT.

name = str(input('Enter with your full name: ')).strip()

uppercase = name.upper()
split = uppercase.split()
final = 'SILVA' in split

print(final)