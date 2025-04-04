class Musica:
    musica = []
    def __init__(self, nome='', artista='', duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musica.append(self)

    def __str__(self):
        return f'Música: {self.nome} - Banda: {self.artista} - Duração: {self.duracao}'

    def listar_musicas():
        for musica in Musica.musica:
            print(f'Música: {musica.nome} - Banda: {musica.artista} - Duração: {musica.duracao}')

musica1 = Musica('Satisfaction', 'Rolling Stones', 100)
musica2 = Musica('Aline Barros', 'Jeová Jirem', 200)

Musica.listar_musicas()