import csv
from viajeromod import ViajeroFrecuente as vf

class Lector:

    def generarLista(listacsv):
        archivo = open("UNIDAD2/EJERCICIO2/viajeros.csv")
        reader = csv.reader(archivo, delimiter=",", skipinitialspace=True)
    
        for fila in reader:
            listacsv.append(vf(int(fila[0]), str(fila[1]), str(fila[2]), str(fila[3]), int(fila[4])))
             
        archivo.close()