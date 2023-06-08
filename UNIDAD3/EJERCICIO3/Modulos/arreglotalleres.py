import numpy as np
import csv
from Modulos.TallerCapacitacion import tallercapacitacion

class arrtaller:

    __arreglo = np.empty(3, dtype=tallercapacitacion)

    def lector(self):

        archivo = open("UNIDAD3/EJERCICIO3/Talleres.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)

        for fila in reader:

            self.__arreglo[int(fila[0])]= tallercapacitacion(fila[0], fila[1], fila[2], fila[3])

        archivo.close()

        print("grabado!\n")