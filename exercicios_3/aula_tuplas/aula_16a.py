lanche = ('hambúrguer', 'suco', 'pizza', 'pudim', 'refrigerante')
# Tuplas são imutáveis
for p, c in enumerate(lanche):
    print('Eu vou comer {} na posição {}.'.format(c, p))

for c in range(len(lanche)):
    print('Eu vou comer {} na posição {}.'.format(lanche[c], c))

for c in lanche:
    print('Eu vou comer {}'.format(c))


print('Comi pra burro!!')

print()
print()

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.count(9))
print(c.index(5, 1))