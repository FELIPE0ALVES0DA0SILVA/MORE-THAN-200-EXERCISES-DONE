

'''for c in range(1, 10):
    print(c)'''


n = 1
p = i = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            p += 1
        else:
            i += 1
print('tu digitaste  {} numeros pares e {} impares.'.format(p, i))