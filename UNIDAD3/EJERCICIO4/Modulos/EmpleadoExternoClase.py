from Modulos.EmpleadoClase import Empleado

class EmpleadoExterno(Empleado):

    __tarea : str
    __fechainicio : str
    __fechafin : str
    __montoviatico : float
    __obracosto : float
    __segurovidacosto : float

    def __init__(self, **kwargs):
        
        super().__init__(kwargs["dni"], kwargs["nombre"], kwargs["direccion"], kwargs["telefono"])
        self.__tarea = str(kwargs["tarea"])
        self.__fechainicio = str(kwargs["fechainicio"])
        self.__fechafin = str(kwargs["fechafin"])
        self.__montoviatico = float(kwargs["montoviatico"])
        self.__obracosto = float(kwargs["obracosto"])
        self.__segurovidacosto = float(kwargs["segurovidacosto"])

