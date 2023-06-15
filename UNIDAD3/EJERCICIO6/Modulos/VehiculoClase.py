class Vehiculo:

    __modelo : set
    __puertas : int
    __color : str
    __preciobase : float
    __estado : str
    __marca : str
    __patente : str
    __anio : int
    __kilometraje : int
    __version : str

    def __init__(self, **kwargs):

        self.__modelo = kwargs["modelo"]
        self.__puertas = kwargs["puertas"]
        self.__color = kwargs["color"]
        self.__preciobase = kwargs["preciobase"]
        self.__estado = kwargs["estado"]
        self.__marca = kwargs["marca"]
        self.__patente = kwargs["patente"]
        self.__anio = kwargs["anio"]
        self.__kilometraje = kwargs["kilometraje"]
        self.__version = kwargs["version"]