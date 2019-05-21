import random

class Generico():
    def generarRandom():
        generarRandom = random.randint(0, 2)
        if generarRandom == 0:
            genericoMedicamento = "True"
        else:
            genericoMedicamento = "False"
        return genericoMedicamento


class Prospecto():
    def generarProspecto():
        prospectoLoco = " "
        generarProspecto = random.randint(10, 80)
        for i in range (0, generarProspecto):
            prospectoLoco += "p"
        return prospectoLoco
