
def maiusculas(frase):
    coisa = ''
    for unidade in frase:
        if ord('Z') > ord(unidade) > ord('A'):
            coisa += unidade
    return coisa



