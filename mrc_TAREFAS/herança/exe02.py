class Veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def informacoes(self):
        print(self.marca, self.ano)

class Carro(Veiculo):
    def __init__(self, marca, ano, portas):
        super().__init__(marca, ano)
        self.portas = portas

class Moto(Veiculo):
    def __init__(self, marca, ano, cilindradas):
        super().__init__(marca, ano)
        self.cilindradas = cilindradas

c = Carro("Ford", 2020, 4)
m = Moto("Honda", 2022, 160)

c.informacoes()
print(c.portas)

m.informacoes()
print(m.cilindradas)