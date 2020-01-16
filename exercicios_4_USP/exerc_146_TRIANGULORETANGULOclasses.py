class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def retangulo(self):
        import math
        calculo = self.a**2 + self.b**2
        calculo = math.sqrt(calculo)
        if calculo % 1 != 0 and calculo != self.c:
            return False
        else:
            return True
