#def soma(a, b):
#    print('a = {} e b = {}'.format(a, b))
#    s = a + b
#    print('A soma de a + b = {}'.format(s))


# Programa principal
#soma(b =5,a = 4)

#soma(8, 9)

#soma(2, 1)

#def contador(*num):
#    tam = len(num)
#    print('Os valores {} são {} digitos.'.format(num, tam))


#contador(5, 6, 7, 8, 5)
#contador(1, 3, 5)

#def dobra(lst):
#    pos = 0
#    while pos < len(lst):
#        lst[pos] *= 2
#        pos += 1

#valores = [3, 5, 6, 7, 8]
#dobra(valores)
#print(valores)

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print('SOmando os valores {} times {}'.format(valores, s))


soma(5, 2)
soma(2, 9, 4)