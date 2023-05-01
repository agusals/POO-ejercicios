import os
import csv
from emailmod import Email as e

def menu() -> int:
    print("¿Qué desea hacer?\n")
    print("1_ Ingresar email\n")
    print("2_ Cambiar contraseña\n")
    print("3_ Registrar email\n")
    print("4_ Leer archivo\n")
    print("5_ Salir\n")
    
    return int(input())

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def opcion1(lista):
    nombreuser = input("Ingrese nombre del usuario: ")
    cls()
    idcuenta = input("Ingrese identificador de cuenta: ")
    cls()
    dominio = input("Ingrese dominio: ")
    cls()
    tipodominio = input("Ingrese tipo de dominio: ")
    cls()
    contra = input("Ingrese contraseña: ")
    cls()
    
    email = e(idcuenta, dominio, tipodominio, contra)
    lista.append(email)

    print("Estimado {}, te enviaremos tus mensajes a la dirección {}.".format(nombreuser, email.retornaEmail()))
    input()

def opcion2(lista):
    contraxd = input("Ingrese contraseña: ")
    if contraxd == lista[0].getContra():
        print("Contraseña correcta!\n")
        contranueva = input("Ingrese nueva contraseña:")
        lista[0].setContra(contranueva)

        input()

def opcion3(lista):
    
    emailnuevo = str(input("Ingrese dirección de correo: "))
    email = e()
    lista.append(email.crearCuenta(emailnuevo))
    input()

def opcion4(listacsv):
    archivo = open("UNIDAD2\EJERCICIO1\cuentas.csv")
    reader = csv.reader(archivo, delimiter=",", skipinitialspace=True)
    
    for fila in reader:
        for i in range(len(fila)):
            listacsv.append(e())
        for i in range(len(fila)):
            mail = fila[i]
            listacsv[i].crearCuenta(str(mail))
             
        
    archivo.close()

    idcuenta = input("Ingrese identificador de cuenta a buscar: ")
    print(" ")
    cls()
    
    i = 0
    fin = False
    while i != len(listacsv) and fin == False:
        if listacsv[i].getIDcuenta() == idcuenta:
            print("ID de cuenta encontrado!!\n")
            print("{email}".format(email = listacsv[i].retornaEmail()))
            fin = True
        i+=1

    if fin == False:
        print("ID no encontrado\n")

    input()
        


#--------- MAIN ----------------

if __name__ == "__main__":
    cls()
    respuesta = menu()
    lista = []
    listacsv = []

    while respuesta != 5:
        cls()
        if respuesta == 1:
            opcion1(lista)
        elif respuesta == 2:
            opcion2(lista)
        elif respuesta == 3:
            opcion3(lista)
        elif respuesta == 4:
            opcion4(listacsv)
    
        cls()
        respuesta = menu()
    
    cls()
    print("Programa finalizado.")