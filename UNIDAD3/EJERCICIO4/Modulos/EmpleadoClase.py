class Empleado:

    __dni : int
    __nombre : str
    __direccion : str
    __telefono : int

    def __init__(self, dni, nombre, direccion, telefono) -> None:
        
        self.__dni = int(dni)
        self.__nombre = int(nombre)
        self.__direccion = str(direccion)
        self.__telefono = int(telefono)