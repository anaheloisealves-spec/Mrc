class ContaBancaria:
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor

    def get_saldo(self):
        return self.__saldo

    def extrato(self):
        print(self.__titular, self.__saldo)

conta = ContaBancaria("Ana")

conta.depositar(500)
conta.sacar(200)

print(conta.get_saldo())
conta.extrato()