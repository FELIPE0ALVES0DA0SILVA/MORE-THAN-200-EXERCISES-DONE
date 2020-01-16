# CREATE A VARIABLE TAHT WILL CONTAIN THE CITY OF THE USER
# STRIP THE CITY VARIABLE
# UPPERCASE THE STRIPPED VARIABLE
# SPLIT THE UPPERCASE STRIPPED VARIABLE
# SEE IF THE FIRST WORD OF THIS  PROCESSED VARIABLE IS WITHIN OF THE STRING 'SANTOS'
# AND PRINT IT.
city = str(input('Enter the name of your city: '))

strip = city.strip()
uppercase = strip.upper()
split = uppercase.split()
split = split[0]
final = 'SANTOS' in split

print(final)
