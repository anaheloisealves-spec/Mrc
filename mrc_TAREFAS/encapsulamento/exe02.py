class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def set_nome(self, nome):
        if nome != "":
            self.__nome = nome

    def set_idade(self, idade):
        if 0 <= idade <= 120:
            self.__idade = idade

    def apresentar(self):
        print(self.__nome, self.__idade)

p = Pessoa("Ana", 20)

p.apresentar()