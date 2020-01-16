# Write a program that read any integer number N zncd show in the screen the first N elements of a fibonacci sequence.

print('|'*70)
f = int(input(' Digite o último número da sequência fibonacci que tu quiseres: '))
f1 = int(input('Digite o ante penúltimo número da sequência fibonacci em relação ao último: '))
print('|'*70)
f2 = 1
f0 = 0
print()
print()
print()
i = 0

a = f1
b = f
print('~O~'*32)
print('{} -> {} -> '.format(b, a), end='')
while f2 >= 1:
    f2 = f - f1
    f = f1
    f1 = f2
    i += 1
    print('{} -> '.format(f2), end='')
print('. Está é a sequência de fibonacci reversa.')
print('~O~'*32)
