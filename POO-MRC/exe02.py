class Produto:
    def __init__(self,nome,preco):
        self.nome= nome
        self.preco = preco
    
    def desconto(self):
        desc = int(input("Digite quanto de desconto vc irá dar: (e reais)"))
        self.preco =  self.preco - desc

produto1 = Produto("Batata", 100)
produto2 = Produto("Banana", 6769)

produto1.desconto()
print(produto1.nome)
print(produto1.preco)




