# CREATE A VARIABLE THE INPUT A NAME
# SPLIT THE NAME
# TAKE THE FIRST NAME
# TAKE THE LAST NAME
# PRINT THE FIRST AND LAST NAME

name = input('Enter your name: ')

split = name.split()
split_first = split[0]
split_last = split[-1]

print('Your first name is {} and '
      'last {}.'.format(split_first, split_last))
