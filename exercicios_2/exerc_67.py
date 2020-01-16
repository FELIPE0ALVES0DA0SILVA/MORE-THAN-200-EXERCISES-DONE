# Make a program the show the times table of several numbers,
# for each value digited for the user,
# the program will be break when the number requested be a negative.

while True:
    n = float(input('Tu queres ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('=-=' * 12)
    m = c = 0
    while c < 10:
        m = n
        c += 1
        m *= c
        print('{:.2f} X {:.2f} = {:.2f} '.format(n, c, m))
    print('=-=' * 12)
print('PROGRAMA TABUADA ENCERRADO, VOLTE SEMPRE.')
