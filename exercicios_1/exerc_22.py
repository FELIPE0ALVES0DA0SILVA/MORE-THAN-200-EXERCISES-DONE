# CREATE A VARIABLE TO THE NAME
# NAKE THIS NAME IN UPPERCASE
# MAKE THIS NAME IN LOWERCASE
# SPLIT THE NAME
# SPLIT THE NAME AND THEN, TAKE THE INK OF THE NAME

name = str(input('Enter your full name: '))    # type str

uppercase = name.upper()
print('The name with all uppercase letters:'
      ' {}.'.format(uppercase))
lowercase = name.lower()
print('The name with all lowercase letters:'
      ' {}.'.format(lowercase))

# Just one answer
letter = name.split()
letter = ''.join(letter)
count = len(letter)
print('The amount letters without spaces '
      'is {}.'.format(count))
# Just one answer

first_name = name.split()
first_name = first_name[0]
first_name = len(first_name)
print('The amount of letter in the first '
      'name informed is {}.'.format(first_name))
