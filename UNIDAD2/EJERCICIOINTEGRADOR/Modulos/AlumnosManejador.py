class Alumno:
    __dni : int
    __apellido : str
    __nombre : str
    __carrera : str
    __aniocursado : int

    def __init__(self, DNI=-1, Apellido="x", Nombre="x", Carrera="x", AnioCursado=-1):
        self.__dni = DNI
        self.__apellido = Apellido
        self.__nombre = Nombre
        self.__carrera = Carrera
        self.__aniocursado = AnioCursado
    
    def getNombre(self) -> str:
        return self.__nombre

    def getApellido(self) -> str:
        return self.__apellido
    
    def getDNI(self) -> int:
        return self.__dni
