class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c




    def __new__(cls, a, b, c):
        lista = []
        lista.append(a)
        lista.append(b)
        lista.append(c)
        return lista


    def semelhante(self, triangulo):
        lista = []
        resultado = 0
        lista.append(self.a)
        lista.append(self.b)
        lista.append(self.c)
        for cada in range(len(triangulo)):
            if triangulo[cada] == lista[cada]:
                resultado += 1
        if resultado == 3:
            return True
        else:
            return False

t2 = Triangulo(2, 4, 6)
t = Triangulo(1,10,3)
print(t.semelhante(t2))
