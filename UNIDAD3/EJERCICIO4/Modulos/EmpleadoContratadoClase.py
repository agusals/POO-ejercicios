from Modulos.EmpleadoClase import Empleado

class EmpleadoContratado(Empleado):

    __fechainicio : str
    __fechafin : str
    __horastrabajadas : int
    __horavalor : float

    def __init__(self, **kwargs):
        
        super().__init__(kwargs["dni"], kwargs["nombre"], kwargs["direccion"], kwargs["telefono"])
        self.__fechainicio = str(kwargs["fechainicio"])
        self.__fechafin = str(kwargs["fechafin"])
        self.__horastrabajadas = int(kwargs["horastrabajadas"])
        self.__horavalor = float(kwargs["horavalor"])