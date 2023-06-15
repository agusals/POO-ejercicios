from Modulos.PersonalClase import Personal

class Docente(Personal):

    __carrera : str
    __cargo : str
    __catedra : str

    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, carrera, cargo, catedra):
        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad)
        self.__carrera = str(carrera)
        self.__cargo = str(cargo)
        self.__catedra = str(catedra)