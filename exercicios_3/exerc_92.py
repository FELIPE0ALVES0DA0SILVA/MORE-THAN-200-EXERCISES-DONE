# Create a progrm that read name,
# year of born and the worker wallet and sign up them ( with age)
# in a dictionary and is in case the CTPS be different of zero,
# the document will input also the year of hiring and the salary.
# Calculate and add, beyond of the age, with how many years the person will retire itseld.

from datetime import  datetime
neguin = {}

year = datetime.now().year
nome = str(input('Nome: ')).upper().strip()
neguin['Nome'] = nome
born = int(input('Ano de nascimento: '))
age = year - born
neguin['Idade'] = age
cpts = int(input('Identificação da sua CTPS: [ DIGITE ZERO, PARA NÃO TENHO] '))
neguin['ctps'] = cpts
if cpts > 0:
    contratacao = int(input('Ano de contratação: '))
    aposentadoria = 35 + (contratacao - born)
    neguin['contratação'] = contratacao
    salario = float(input('Quanto você ganha: R$ '))
    neguin['Salário'] = salario

    neguin['Aposentadoria'] = aposentadoria
print(neguin)
for c, k in neguin.items():
    if c == 'Nome':
        print('{} tem o valor {}.'.format(c, k))
for c, k in neguin.items():
    if c == 'Idade':
        print('{} tem o valor {}.'.format(c, k))
for c, k in neguin.items():
    if c == 'ctps':
        if k > 0:
            print('{} tem o valor {}.'.format(c, k))
for c, k in neguin.items():
    if c == 'contratação':
        print('{} tem o valor {}.'.format(c, k))
for c, k in neguin.items():
    if c == 'Salário':
        print('{} tem o valor {}.'.format(c, k))
for c, k in neguin.items():
    if c == 'Aposentadoria':
        print('{} tem o valor {}.'.format(c, k))
