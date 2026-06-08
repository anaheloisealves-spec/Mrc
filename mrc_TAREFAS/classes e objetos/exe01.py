class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

p1 = Produto("Mouse", 50)
p2 = Produto("Teclado", 100)

print(p1.nome, p1.preco)
print(p2.nome, p2.preco)