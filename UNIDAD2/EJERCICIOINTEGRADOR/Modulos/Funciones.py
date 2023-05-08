from Modulos.AlumnosManejador import Alumno
from Modulos.MateriasManejador import Materia


class Funciones:

    def obtenerPromedio(alumnoarreglo, materiaslista):
        
        dnileido = input("Ingrese DNI del alumno: ")
        
        promedioconaplazo = 0.00
        promediosinaplazo = 0.00
        materiasaprobadas = 0
        materiasrendidas = 0
        contadoraprobadas = 0
        contadorrendidas = 0
        alumnoencontrado = 0
        i = 0

        while i != 8 and alumnoencontrado == 0:
            if alumnoarreglo[i].getDNI() == int(dnileido):
                alumnoencontrado = alumnoarreglo[i]
            i+=1
        
        for materiarendida in materiaslista:
            if materiarendida.getDNI() == alumnoencontrado.getDNI():
                if materiarendida.getNota() >= 4:
                    materiasaprobadas += materiarendida.getNota()
                    contadoraprobadas += 1
                else:
                    materiasrendidas += materiarendida.getNota()
                    contadorrendidas += 1

        if contadoraprobadas != 0:
            promediosinaplazo = materiasaprobadas / contadoraprobadas
        else:
            promediosinaplazo = -1
        if contadorrendidas != 0:
            promedioconaplazo = materiasrendidas / contadorrendidas
        else:
            promedioconaplazo = promediosinaplazo

        print("-----------\n")
        print("Alumno: {a} {b}\n" .format(a=alumnoencontrado.getNombre(), b=alumnoencontrado.getApellido()))
        print("Promedio sin aplazos = {a}\n" .format(a=promediosinaplazo)) 
        print("Promedio con aplazos = {a}\n" .format(a=promedioconaplazo))
        input()


        

