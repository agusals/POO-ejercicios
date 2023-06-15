from Modulos.PersonalClase import Personal

class Investigador(Personal):

    __area : str
    __tipoinv : str


    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, area, tipoinv):
        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad)
        self.__area = str(area)
        self.__tipoinv = str(tipoinv)