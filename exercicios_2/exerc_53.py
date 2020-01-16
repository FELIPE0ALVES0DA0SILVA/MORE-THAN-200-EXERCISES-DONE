# Create a program that read any phrase and say if it is a palindrome, disconsider the spaces.

# CREATE A VARIABLE THAT CONTAIN A STRING VALUE
# ANOTHER VARIABLE THAT BE EMPTY STRINGED
# MAKE A FOR LOOP THE GO TO THE LNGTH OF THE VARIABLE ONE UNTIL ZERO AN OF 1 BY 1 IN REGRESSIVE COUNTABLE
#           MAKE A ITERATION WITH THE CONTABLE IN REGRESSION
#           MAKE ANOTHER ITERATION WITH THE EMPTY VARIABLE INPUT THE FIRST VARIABLE IN EACH LOOP
#           IF INVERSE EQUAL FIRST VARIABLE:
#                           PRINT PALINDROMO
#           ELSE:
#                           PRINT ITS NOT A PALINDROMO

word = str(input('Enter the desired word: ')).upper().strip().replace(" ", "")
inverso = ''
for c in range(len(word), 0, -1):                   # To generate a loop of string, should convert the string for a integer number, throughout a len, and then put the len in a range.
    c = c - 1                                       # The iteration will not saved all the values generated, so, it should save the results of iteration within a key, and this key should is correlated with the original string that generate their.
    inverso = inverso + word[c]                     # it should to have a variable outside of the loop for to saved the new phrase inverse and compare the old right phrase with the new inverse phrase.
if inverso == word:
    print('Palíndromo')
else:
    print('Não é um palíndromo')
