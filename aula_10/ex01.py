class Pessoa:
    
    def __init__(self, nome, idade, peso, altura, sexo):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.sexo = sexo

    def descrever(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}\nAltura: {self.altura}\nSexo: {self.sexo}"

    def envelhecer(self):
        return f"Passou um ano, agora o {self.nome} tem {self.idade + 1} anos."
