# Create a program where the user enter any number that use parentheses. Your app will shoul analyse
# if the expression showed is with the parentheses opened and closed in the correct order.

parenteses = list()
pedacos = list()
esquerda = direita = 0

expressao = str(input('Digite uma expressão para'' analisarmos a ordem dos parênteses: ')).strip().upper().replace(' ', '')
parenteses.append(expressao)
for contagem in parenteses:
    for cada in contagem:
        pedacos.append(cada)
    for extrai in pedacos:
        if extrai in '(':
            direita += 1
        if extrai in ')':
            esquerda += 1
    if esquerda == direita:
        print(' A expressão está correta.')
    else:
        print('A expressão está errada.')
