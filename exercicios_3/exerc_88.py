# Make a program tha help a player of the mega sena to create guesses.
# The program will ask  how manu matches eill be generates and will riffle
# six number between one and sixty for each round. Signing up all in a compound list.
from time import sleep
from random import randint
rodadas = []
palpites = []
i = original = 0

pergunta = int(input('Quantas rodadas você irá jogar? '))
while True:
    i += 1
    for contagem in range(0, 6):
        adivinhos = randint(0, 60)
        if contagem == 0:
            original = adivinhos
            palpites.append(original)
        if contagem > 0 and original == adivinhos:
            adivinho = randint(0, 60)
            palpites.append(adivinho)
        if original != adivinhos:
            original = adivinhos
            palpites.append(original)

    rodadas.append(palpites[:])
    palpites.clear()
    if i == pergunta:
        break
print('~O~'*12)
print('{:>8}'.format('LISTA DE SORTEIO'))
print('~O~'*12)
print()
print('^v^'*10)
for numeros, itens in enumerate(rodadas):
    sleep(1)
    print('\nJogo {}: {}'.format(numeros + 1, itens))
print('^v^'*10)
