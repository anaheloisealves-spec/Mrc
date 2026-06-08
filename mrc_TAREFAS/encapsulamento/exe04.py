class Sensor:
    def __init__(self, temperatura):
        self.__temperatura = temperatura

    def set_temperatura(self, temperatura):
        if -50 <= temperatura <= 150:
            self.__temperatura = temperatura

    def status(self):
        if self.__temperatura <= 80:
            return "Normal"
        elif self.__temperatura <= 120:
            return "Alerta"
        else:
            return "Critico"

s = Sensor(25)

for t in (30, 90, 130, 70):
    s.set_temperatura(t)
    print(t, s.status())