class Helado:

    __gramos : float
    __precio : float
    __sabor : object

    def __init__(self, gramos, precio, sabor):
        self.__gramos = float(gramos)
        self.__precio = float(precio)
        self.__sabor = sabor

    def setsabor(self, sabor):
        self.__sabor = sabor