import random


class Generico():
    def generarRandom():
        generarRandom = random.randint(0, 2)
        if generarRandom == 0:
            genericoMedicamento = "true"
        else:
            genericoMedicamento = "false"
        return genericoMedicamento


class Prospecto():
    def generarProspecto():
        prospectoLoco = " "
        generarProspecto = random.randint(10, 80)
        for i in range(0, generarProspecto):
            prospectoLoco += "p"
        return prospectoLoco


class AlmacenLoco():
    def generarNombreAlmacen():
        nombresalmacenes = ["Almacen Magico", "Almacen BuenoBonitoBarato", "AlmacenVacio", "AlmacenCerrado",
                            "AlmacenTapadera"]
        generaralmacen = random.choice(nombresalmacenes)
        return generaralmacen


class DireccionCrazy():
    def generarDireccionCrazy():
        nombrescalles = ["Calle de la Piruleta", "Calle Me falta un tornillo", "Calle de los gorrones",
                         "Calle del ojo seco", "Plaza del Tieso", "Calle de la Duda", "Calle Cilla"]
        elegirCalle = random.randint(0, 5)
        generardireccion = nombrescalles[elegirCalle]
        return generardireccion
