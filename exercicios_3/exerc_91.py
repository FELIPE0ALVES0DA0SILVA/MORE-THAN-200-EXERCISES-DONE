# Create a program where four players play a rock and having randomly results.
# Save this eresults in a dictionary. In the end, put this dictionary in order,
# knowing that the winner take the major number in the rock.

from random import randint
from time import sleep
jogadas = {}
print('Valores sorteados:')
sleep(1)
for c in range(0,4):
    ran = randint(0,100)
    jogadas['jogador {}'.format(c + 1)] = ran
    print('     O {}° jogador tirou {}'.format(c + 1, ran))
    sleep(1)
print('Ranking dos jogadores: ')
sleep(1)
i = 0
for k in sorted(jogadas, key= jogadas.get, reverse= True):
    i += 1
    print('     {}° luagr: {} com {}'.format(i ,k , jogadas[k]))
    sleep(1)
