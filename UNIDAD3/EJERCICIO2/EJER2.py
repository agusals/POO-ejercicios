from Modulos.ManejaSabor import manejasabor
from Modulos.ManejaHelado import manejahelado

if __name__ == "__main__":

    driverhelado = manejahelado()
    driversabor = manejasabor()

    gramos = input("Ingrese gramos\n")
    precio = input("Ingrese precio\n")
    idsabor = input("Ingrese id sabor\n")

    driverhelado.ventahelado(float(gramos), float(precio), int(idsabor))

