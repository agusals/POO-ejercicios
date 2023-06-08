from Modulos.Helado import Helado

class manejahelado:

    __heladosvendidos = []
    
    def ventahelado(self, gramos, precio):

        self.__heladosvendidos.append(Helado(gramos, precio))