class Sabor:

    __idsabor : int
    __ingredientes : str
    __nombresabor : str

    def __init__(self, idsabor=-1, ingredientes="x", nombresabor="x"):
        self.__idsabor = int(idsabor)
        self.__ingredientes = str(ingredientes)
        self.__nombresabor = str(nombresabor)

    def getidsabor(self):
        return self.__idsabor