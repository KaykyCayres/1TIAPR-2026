class Animal:
    def __init__(self, especie, raca, nome, cor):
        self.especie = especie
        self.raca = raca
        self.nome = nome
        self.cor = cor

class Cachorro(Animal):
    def __init__(self, especie, raca, nome, cor, garras_expostas):
        super().__init__(especie, raca, nome, cor)
        self.garras_expostas = garras_expostas

class Gato(Animal):
    def __init__(self, especie, raca, nome, cor, miado):
        super().__init__(especie, raca, nome, cor)
        self.miado = miado

class Macaco(Animal):
    def __init__(self, especie, raca, nome, cor, polegar):
        super().__init__(especie, raca, nome, cor)
        self.polegar = polegar