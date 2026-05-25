class Produto:
    def __init__(self,nome,preco):
        self.nome= nome
        self.preco = preco


produto1 = Produto("Batata", 100)
produto2 = Produto("Banana", 6769)

print(produto1.nome)
print(produto2.preco)
