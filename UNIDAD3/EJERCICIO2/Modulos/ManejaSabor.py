import csv
from Modulos.Sabor import Sabor


class manejasabor:

    __listasabores = []

    def lector(self):

        archivo = open("UNIDAD3/EJERCICIO2/sabores.csv")
        reader = csv.reader(archivo, delimiter=";")

        for fila in reader:
            
            self.__listasabores.append(Sabor(fila[0], fila[1], fila[2]))

        archivo.close()
    

