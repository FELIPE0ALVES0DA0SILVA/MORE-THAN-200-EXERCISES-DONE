# Make a program that read a tuple fulfilled with a count by extent, from zero to twenty,
# Your program will should read a number for the keyboard ( between zero and twenty) and show them per extent.
numbers = ('zero','one' ,'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
           'ten', 'eleven', 'twelve', 'thrirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
while True:
    while True:
        user = int(input('Digite um número de zero à vinte: '))
        if 20 >= user >= 0:
            print('O número que você digitou por extenso e em inglês é {}.'.format(numbers[user]))
            break
        elif user > 20 or user < 0:
            print('Tente novamente')
    while True:
        pergunta = str(input('Tu queres continuar? [ S | N ]')).upper().strip()
        if pergunta not in 'SN':
            print('Resposta inválida.')
        elif pergunta == 'N':
            break
        else:
            break
    if pergunta == 'N':
        break
