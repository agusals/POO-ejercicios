from Modulos.VehiculoClase import Vehiculo

class Nodo:

    __vehiculo : Vehiculo
    __siguiente : object

    def __init__(self, vehiculo):
        self.__vehiculo = vehiculo
        self.__siguiente = None

    def setSiguiente(self, sig):
        self.__siguiente = sig

    def getSiguiente(self):
        return self.__siguiente
    
    def getDato(self):
        return self.__vehiculo