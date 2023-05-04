import os
from lectorcsv import Lector 
from viajeromod import ViajeroFrecuente as vf


def menu() -> str:
    print("¿Qué desea hacer?\n")
    print("a_ Consultar cant millas\n")
    print("b_ Acumular millas\n")
    print("c_ Canjear millas\n")
    print("d_ Salir\n")

    
    return str(input())

def cls():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":

    cls()

    listaviajeros = []

    Lector.generarLista(listaviajeros)
    print("Lista creada! (Presione cualquier tecla para continuar)")
    input()
    cls()

    inp = int(input("Ingrese n° de viajero: "))
    viajerocorrecto = vf()
    band = False
    i = 0
   
    while i != len(listaviajeros) and band == False:
        if listaviajeros[i].getNumviajero() == inp:        
            viajerocorrecto = listaviajeros[i]
            band = True
        i += 1

    if band:
        opcion = menu()
    else:
        print("\nViajero no encontrado\n")
        input()
        opcion = 'd'

    while opcion != 'd':
        cls()
        if opcion == 'a':
            print("Millas acumuladas: ", viajerocorrecto.cantidadTotalMillas())
            input()
        if opcion == 'b':
            acum = viajerocorrecto.acumularMillas(int(input("Ingrese millas a acumular: ")))
            print("Millas acumuladas actualizadas = ", acum)
            input()
        if opcion == 'c':
            millas = viajerocorrecto.canjearMillas(int(input("Ingrese millas a canjear: ")))
            print("Millas acumuladas actualizadas = ", millas)
            input()

        cls()
        opcion = menu()
    
    cls()

    print("Lista cargada con 4 viajeros: ", hex(id(listaviajeros)))