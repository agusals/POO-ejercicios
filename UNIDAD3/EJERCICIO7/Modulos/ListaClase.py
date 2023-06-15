from Modulos.NodoClase import Nodo

class Lista:

    __comienzo : Nodo 

    def __init__(self):
        self.__comienzo = None

    def agregarLista(self, vehiculo):

        nodo = Nodo(vehiculo)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo