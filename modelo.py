class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._like = 0

        @property
        def likes(self):
            return self._likes

        def dar_like(self):
            self._likes += 1

        @property
        def nome(self):
            return self._nome

        @nome.setter
        def nome(self, novo_nome):
            self._nome = novo_nome.title()

        def __str__(self):
            return f" {self._nome} - {self.ano} : {self._like} Likes"

class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f" {self._nome} - {self.ano} - {self.duracao} Minutos: {self._like} Likes"

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f" {self._nome} - {self.ano} - {self.temporadas} Temporadas: {self._like} Likes"

class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)

vingadores = Filme('vingadores', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
got = Serie("Game of Thrones", 2013, 8)
bat = Filme("Batman", 2008, 140)
lor = Filme("Lord of Rings", 2004, 240)


filmes_e_series = [vingadores, atlanta, got, bat, lor ]

playlist_do_fim_de_semana = Playlist("fim de semana", filmes_e_series)

for programa in playlist_do_fim_de_semana.programas:
    print(programa)