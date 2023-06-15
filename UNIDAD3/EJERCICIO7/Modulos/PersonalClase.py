class Personal:

    __cuil : int
    __apellido : str
    __nombre : str
    __sueldobasico : float
    __antiguedad : int

    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad):
        
        self.__cuil = int(cuil)
        self.__apellido = str(apellido)
        self.__nombre = str(nombre)
        self.__sueldobasico = float(sueldobasico)
        self.__antiguedad = int(antiguedad)