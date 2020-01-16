# Create a program that read the age and the sex of several peoples.
# Each pessoa signed up, the program will should ask if the user,
# want or not continue. In the end, show:

# How many peoples have more than 18 years old.
# How many men were signed up.
# How many woman have more than 20 years.
c1 = c = i = 0
user = ''
while True:
    if user == 'N':
        print('{} pessoas tem mais de 18 anos'.format(i))
        print('{} homens foram cadastrados'.format(c))
        print('{} tem menos de 20 anos'.format(c1))
    if user == 'N':
        break

    age = int(input('Digite sua idade: '))

    sex = str(input('Digite seu sexo [ M | F ]: ')).strip().upper()[0]
    while sex != 'M' and sex != 'F':
        print()
        print('Valor inválido!')
        sex = str(input('Digite seu sexo [ M | F ]: ')).strip().upper()[0]
    user = str(input('Tu queres continuar [ S | N ]?')).strip().upper()[0]
    while user != 'S' and user != 'N':
        print()
        print('Valor inválido!')
        user = str(input('Tu queres continuar [ S | N ]?')).strip().upper()[0]
    if sex == 'M':
        c += 1
    if age > 18:
        i += 1
    if sex == 'F':
        if age > 20:
            c1 += 1
