import csv
import numpy as np
import os
from Modulos.AlumnosManejador import Alumno
from Modulos.MateriasManejador import Materia

class Lector:

    def generarArrayAlumnos(arr):
        archivo = open("UNIDAD2/EJERCICIOINTEGRADOR/alumnos.csv")
        reader = csv.reader(archivo, delimiter=";", skipinitialspace=True)
        next(reader)
        i = 0

        #------ Verificar cantidad alumnos

        for fila in reader:
            if type(int(fila[0])) == int:
                i += 1

        #------ Crear array de alumnos

        arr = np.empty([i], dtype=Alumno)
        
        
        #------ Llenar array de alumnos

        archivo.seek(0)
        next(reader)
        i = 0
        
        for fila in reader:
            arr[i] = Alumno(int(fila[0]), str(fila[1]), str(fila[2]), str(fila[3]), int(fila[4]))
            i+=1

        archivo.close()
                   
        if type(arr[0].getApellido()) == str:
            print("ALUMNOS ARREGLO generado exitosamente!")
            return arr

        

    

    def generarListaMaterias(lista):
        archivo = open("UNIDAD2/EJERCICIOINTEGRADOR/materiasAprobadas.csv")
        reader = csv.reader(archivo, delimiter=";", skipinitialspace=True)
        next(reader)

        for fila in reader:

            lista.append(Materia(int(fila[0]), str(fila[1]), str(fila[2]), int(fila[3]), str(fila[4])))
            
        archivo.close()

        if type(lista[0].getNombre()) == str:
            print("MATERIAS LISTA generada exitosamente!")
            return lista