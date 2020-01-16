def main():
    carro1 = carro('brasileiro', 1968, 'Amarelo', 80)
    carro2 = carro('fuscão', 1981, 'Preto',  95)

    carro1.acelera(40)
    carro2.acelera(50)
    carro1.acelera(80)
    carro1.pare()
    carro2.acelera(100)


class carro:
    def __init__(self, modelo, ano, cor, vel_maxima):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0
        self.vel_maxima = vel_maxima

    def imprima(self):
        if self.velocidade == 0:
            print('{} {} {}'.format(self.modelo, self.cor, self.ano))
        elif self.velocidade < self.vel_maxima:
            print('{} {} indo a {} km/h'.format(self.modelo, self.cor, self.velocidade))
        else:
            print('{} {} indo muito raapiiidooo!!!!'.format(self.modelo, self.cor))

    def acelera(self, vel):
        self.velocidade = vel
        if self.velocidade > self.vel_maxima:
            self.velocidade = self.vel_maxima
        self.imprima()

    def pare(self):
        self.velocidade = 0
        self.imprima()


main()
