class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R$ {valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente")

    def extrato(self):
        print("--- Extrato Bancário ---")
        print(f"Titular: {self.titular}")
        print(f"Saldo atual: R$ {self.saldo}")
        print("------------------------")