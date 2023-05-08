class Materia:
    __dni : int
    __nombre : str
    __fecha: str
    __nota : int
    __aprobacion : str

    def __init__(self, dni=-1, nombre="x", fecha="x", nota=-1, aprobacion="x"):
        self.__dni = dni
        self.__nombre = nombre
        self.__fecha = fecha
        self.__nota = nota
        self.__aprobacion = aprobacion

    def getNombre(self):
        return self.__nombre
    
    def getDNI(self) -> int:
        return self.__dni

    def getNota(self) -> int:
        return self.__nota