from Modulos.EmpleadoClase import Empleado

class EmpleadoPlanta(Empleado):

    __sueldobasico : float
    __antiguedad : int

    def __init__(self, **kwargs):
        
        super().__init__(kwargs["dni"], kwargs["nombre"], kwargs["direccion"], kwargs["telefono"])
        self.__sueldobasico = float(kwargs["sueldobasico"])
        self.__antiguedad = int(kwargs["antiguedad"])