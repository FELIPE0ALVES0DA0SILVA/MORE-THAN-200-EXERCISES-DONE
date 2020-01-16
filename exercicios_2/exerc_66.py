# Create a program that read several integer numbers for the keyboard.
# The program only will stop when the user digit the value 999,
# that it is the condition of stopped. In the end,
# show how many numbers were entered and what was the sum between them.
c = s = 0
print(''' 
999 PARA STOPPAR.''')
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    c += 1

print('A quantidade de elementos digitados foi {} e a soma entre eles é {}.'.format(c, s))
