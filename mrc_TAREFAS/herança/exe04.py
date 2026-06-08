class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def apresentar(self):
        print(self.nome, self.idade, self.matricula)

class Professor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def apresentar(self):
        print(self.nome, self.idade, self.salario)

lista = [
    Aluno("Ana", 17, "122223"),
    Professor("Carlos", 40, 5000)
]

for pessoa in lista:
    pessoa.apresentar()