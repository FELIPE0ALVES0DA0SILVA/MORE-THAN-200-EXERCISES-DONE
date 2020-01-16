def conta_letras(frase, contar='vogais'):
    contar = contar.lower()
    frase = frase.lower()
    conta = 0
    a = ord('a')
    e = ord('e')
    i = ord('i')
    o = ord('o')
    u = ord('u')
    if contar == 'vogais':
        for cada in frase:
            if ord(cada) in [a, e, i, o, u]:
                conta += 1
    else:
        for cada in frase:
            if ord(cada) not in [a, e, i, o, u] and ord('z') > ord(cada) > ord('a'):
                conta += 1
    return conta
