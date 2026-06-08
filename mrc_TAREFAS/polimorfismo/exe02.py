class Instrumento:
    def tocar(self):
        print("Som")

class Violao(Instrumento):
    def tocar(self):
        print("Plim plim")

class Bateria(Instrumento):
    def tocar(self):
        print("Tum tum")

class Piano(Instrumento):
    def tocar(self):
        print("Tan tan")

instrumentos = [Violao(), Bateria(), Piano()]

for i in instrumentos:
    i.tocar()