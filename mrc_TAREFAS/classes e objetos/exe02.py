class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        return self.preco - self.preco * percentual / 100

p = Produto("Mouse", 100)

print(p.desconto(10))