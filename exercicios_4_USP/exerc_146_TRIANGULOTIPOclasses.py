class Triangulo:
    def __init__(self, a, b, c):
        if a == b == c:
            self.ressultado = 'equilátero'
        elif a == b != c or a != b == c or a == c != b:
            self.ressultado = 'isósceles'
        elif a != b != c:
            self.ressultado = 'escaleno'

    def tipo_lado(self):
        return self.ressultado
