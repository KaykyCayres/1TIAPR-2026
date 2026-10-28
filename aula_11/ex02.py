class Produto:
    def __init__(self, nome, marca, modelo, tipo):
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo

class Computador(Produto):
    def __init__(self, nome, marca, modelo, tipo, processador, placa_mae):
        super().__init__(nome, marca, modelo, tipo)
        self.processador = processador
        self.placa_mae = placa_mae

    def especificacoes_tecnicas(self):
        return f'Computador {self.nome}, marca {self.marca}, processador {self.processador}, placa-mae {self.placa_mae}'

class Vassoura(Produto):
    def __init__(self, nome, marca, modelo, tipo, cabo, fios):
        super().__init__(nome, marca, modelo, tipo)
        self.cabo = cabo
        self.fios = fios

    def observacoes_vassoura(self):
        return f'{self.cabo} é feito de madeira, a vassoura tem 1500 {self.fios}'
