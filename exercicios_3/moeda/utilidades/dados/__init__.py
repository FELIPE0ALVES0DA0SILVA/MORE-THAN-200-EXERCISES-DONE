def leiadinheiro(valor1):
    while True:
        valor = str(input(valor1))
        if valor == '':
            print('Valor inválido, tente novamente')
        elif valor[0] in '0123456789':
            valores = []
            for p, v in enumerate(valor):
                valores.append(v)
                for i, n in enumerate(valores):
                    if n == ',':
                        valores[i] = '.'
            valor = ''
            for p, v in enumerate(valores):
                valor += str(v)
            valor = float(valor)
            return valor

        else:
            print('Valor inválido, tente novamente')
