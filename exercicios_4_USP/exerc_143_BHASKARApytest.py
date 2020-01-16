import math


class Bhaskara:

    def delta(self, a, b, c):
        return b ** 2 - 4 * a * c

    def Main(self):
        a = float(input('Digite o valor de a: '))
        b = float(input('Digite o valor de b: '))
        c = float(input('Digite o valor de c: '))
        print(self.calcular(a, b, c))

    def calcular(self, a, b, c):
        delta = self.delta(a, b, c)
        if delta == 0:
            x1 = (-b + math.sqrt(delta)) / 2
            return 1, x1
        elif delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            return 2, x1, x2
        else:
            return 0
