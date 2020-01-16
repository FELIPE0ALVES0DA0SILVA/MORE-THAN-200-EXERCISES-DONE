class Musica:
    def __init__(self, titulo, interprete, compositor, ano):
        self.titulo = titulo
        self.interprete = interprete
        self.compositor = compositor
        self.ano = ano


class Buscador:
    def busca_por_titulo(self, sequencial, titulo):
        for i in range(len(sequencial)):
            if sequencial[i].titulo == titulo:
                return i
        return -1

    def vamos_buscar(self):
        playlist = [Musica('Ponta de Areia', 'Milton nascimento', 'Milton nascimento', 1975),
                    Musica('Podres poderes', 'Caetano veloso', 'Caetano veloso', 1984),
                    Musica('Baby', 'Gal costa', 'Caetano veloso', 1969)]
        onde_achou = self.busca_por_titulo(playlist, 'porcarias')
        if onde_achou == -1:
            print('Minha música preferida não está na playlist')
        else:
            preferida = playlist[onde_achou]
            print(preferida.titulo, preferida.interprete, preferida.compositor, preferida.ano)


b = Buscador()
b.vamos_buscar()