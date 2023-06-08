from Modulos.Helado import Helado
from Modulos.ManejaSabor import manejasabor

class manejahelado:

    __heladosvendidos = []
    
    def ventahelado(self, gramos, precio, idsabor):

        self.__heladosvendidos.append(Helado(gramos, precio, manejasabor.getsabor(idsabor)))

        print("venta registrada!\n")
    