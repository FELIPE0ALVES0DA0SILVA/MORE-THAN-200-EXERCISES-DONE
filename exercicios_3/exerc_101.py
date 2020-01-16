# Create a program that have a function called voto()
# that will input how a parameter the year of born of a person,
# returning a literal value showing if a person have vote neglected,
# optional or compulsory in the elections.

from datetime import date


def voto(ano):
    actual = date.today().year
    global idade
    idade = actual - ano_nascimento
    if idade > 0:
        if idade < 16:
            return 'Negado'
        elif 18 > idade >= 16:
            return 'Opcional'
        elif 65 > idade >= 18:
            return 'Obrigatório'
    else:
        print('Tu estás de brincadeira comigo, certo? ')


idade = 0
while True:
    ano_nascimento = int(input('Digite o seu ano de nascimento, por favor: '))
    if 1954 >= ano_nascimento > 1900:
        print('Tu não precisas mais de votar.')
        break
    elif ano_nascimento <= 1900:
        print('Tu estás me tirando, né?\n RESPOSTA INVÁLIDA!!! ')
    else:
        break
if voto(ano_nascimento) == 'Negado':
    print('Vossa idade é de {}. Teu pedido foi indeferido.'.format(idade))
elif voto(ano_nascimento) == 'Opcional':
    print('Vossa idade é de {}. Teu pedido foi deferido, contudo, o comparecimento para se votar, neste caso é OPCIONAL.'.format(idade))
elif voto(ano_nascimento) == 'Obrigatório':
    print('Vossa idade é de {}. Teu pedido foi deferido, e o teu comparecimento é obrigatório.'.format(idade))
