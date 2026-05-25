class Carro:
    def __init__(self, marca, modelo, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade = self.velocidade + 10
        print(f"Velocidade atual: {self.velocidade} km/h")

    def frear(self):
        # Evita que a velocidade fique negativa
        if self.velocidade >= 10:
            self.velocidade = self.velocidade - 10
        else:
            self.velocidade = 0
        print(f"Velocidade atual: {self.velocidade} km/h")

carro1 = Carro("Ferrari", 2010, 100)

while True:
   
    escolha = int(input("Escolha o que você quer fazer: \n1 - Acelerar \n2 - Frear \n3 - Sair\nOpção: "))
    
    if escolha == 1:
        carro1.acelerar()  
    elif escolha == 2:
        carro1.frear()     
    elif escolha == 3:
        print("Saindo do programa...")
        break
    else:
        print("Valor indefinido, digite algo válido.")
