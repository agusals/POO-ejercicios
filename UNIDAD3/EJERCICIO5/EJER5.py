from zope.interface import Interface
from zope.interface import implementer


class IElemento(Interface):

    def insertarElemento():
        pass

    def agregarElemento():
        pass
    
    def mostrarElemento():
        pass

    def ej():
        pass


@implementer(IElemento)
class otrocoso:

    def ej():
        print("hola mundo\n")

    def ejemplo(otrocoso: IElemento):

        otrocoso.ej()

    @classmethod
    def test(cls):

        cls.ejemplo(IElemento(otrocoso))


if __name__ == "__main__":

    otrocoso.test()