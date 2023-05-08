import os
import numpy as np
from Modulos.Lector import Lector
from Modulos.Funciones import Funciones


def cls():
    os.system("CLS" if os.name == "nt" else "clear")

def menu():
    print("Elija una opcion:\n")
    print("1_ Revisar promedio de alumno\n")
    print("2_ Listado de alumnos promocionados\n")
    print("3_ Listado de alumnos cursando\n")
    print("4_ Salir\n")

    return(int(input()))


if __name__ == "__main__":

    alumnos_array = 0
    materias_lista = []
    
    cls()

    alumnos_array = Lector.generarArrayAlumnos(alumnos_array)
    materias_lista = Lector.generarListaMaterias(materias_lista)
    print("--------------")

    eleccion = menu()

    while eleccion != 4:
        if eleccion == 1:
            cls()
            Funciones.obtenerPromedio(alumnos_array, materias_lista)
        
        cls()
        eleccion = menu()