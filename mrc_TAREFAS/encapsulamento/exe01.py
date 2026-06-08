class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def set_nome(self, nome):
        self.__nome = nome

    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco

p = Produto("Mouse", 50)

print(p.get_nome())
print(p.get_preco())