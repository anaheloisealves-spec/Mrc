class Funcionario:
    # Construtor da classe mãe
    def __init__(self, nome, matricula, salario):
        self.__nome = nome
        self.__matricula = matricula
        self.__salario = salario

    # Getters
    def get_nome(self):
        return self.__nome

    def get_matricula(self):
        return self.__matricula

    def get_salario(self):
        return self.__salario

    # Setter com validação
    def set_salario(self, salario):
        if salario >= 0:
            self.__salario = salario
        else:
            print("Salário inválido")

    # Método que será sobrescrito pelas filhas
    def calcular_salario(self):
        return self.__salario


class CLT(Funcionario):
    def __init__(self, nome, matricula, salario):
        super().__init__(nome, matricula, salario)

    def calcular_salario(self):
        return self.get_salario()

    def exibir(self):
        print(
            f"Nome: {self.get_nome()} | "
            f"Matricula: {self.get_matricula()} | "
            f"Tipo: CLT | "
            f"Salario: R$ {self.calcular_salario():.2f}"
        )


class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario, vendas):
        super().__init__(nome, matricula, salario)
        self.vendas = vendas

    def calcular_salario(self):
        return self.get_salario() + self.vendas * 0.10

    def exibir(self):
        print(
            f"Nome: {self.get_nome()} | "
            f"Matricula: {self.get_matricula()} | "
            f"Tipo: Vendedor | "
            f"Salario: R$ {self.calcular_salario():.2f}"
        )


class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario):
        super().__init__(nome, matricula, salario)

    def calcular_salario(self):
        return self.get_salario() + 1500

    def exibir(self):
        print(
            f"Nome: {self.get_nome()} | "
            f"Matricula: {self.get_matricula()} | "
            f"Tipo: Gerente | "
            f"Salario: R$ {self.calcular_salario():.2f}"
        )


f1 = CLT("Ana", "001", 3000)
f2 = Vendedor("Bruno", "002", 2000, 12000)
f3 = Gerente("Carla", "003", 5000)

funcionarios = [f1, f2, f3]

for funcionario in funcionarios:
    funcionario.exibir()