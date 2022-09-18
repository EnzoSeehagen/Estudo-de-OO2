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

class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(f" {vingadores._nome} - {vingadores.duracao} : {vingadores._like}")

atlanta = Serie('atlanta', 2018, 2)
print(f'{atlanta._nome} - {atlanta.ano} : {atlanta.temporadas}')

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    detalhes = programa.duracao if hasattr(programa, "duracao" ) else programa.temporadas
    print(f"{programa._nome} -{detalhes} - {programa._like}")