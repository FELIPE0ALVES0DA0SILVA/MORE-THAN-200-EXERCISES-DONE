def incomodam(n):
    if n < 1:
        return ''
    return 'incomodam ' + incomodam(n - 1)


def elefantes(n):
    if n < 1:
        return ''
    return '{} '.format(n) + 'elefantes ' + incomodam(n) + 'muita gente\n' + elefantes(n - 1)


print(elefantes(5))
