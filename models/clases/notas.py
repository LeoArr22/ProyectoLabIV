from models.clases.util.validadores import *

class Nota:
    def __init__(self, nota1=None, nota2=None, recuperatorio1=None, recuperatorio2=None, nota_final=None, estado=None):
        self.nota1 = nota1
        self.nota2 = nota2
        self.recuperatorio1 = recuperatorio1
        self.recuperatorio2 = recuperatorio2
        self.nota_final = nota_final
        self.estado = estado

#NOTA1
    @property
    def nota1(self):
        return self.__nota1

    @nota1.setter
    def nota1(self, nueva_nota):
        if nueva_nota is not None:
            validadores = [
                lambda numero: solo_numero(numero),
                lambda numero: dentro_rango(numero, 1, 10)
            ]
            recorre_validadores(validadores, nueva_nota)
        self.__nota1 = nueva_nota

#NOTA2
    @property
    def nota2(self):
        return self.__nota2

    @nota2.setter
    def nota2(self, nueva_nota):
        if nueva_nota is not None:
            validadores = [
                lambda numero: solo_numero(numero),
                lambda numero: dentro_rango(numero, 1, 10)
            ]
            recorre_validadores(validadores, nueva_nota)
        self.__nota2 = nueva_nota

#RECUPERATORIO1
    @property
    def recuperatorio1(self):
        return self.__recuperatorio1

    @recuperatorio1.setter
    def recuperatorio1(self, nueva_nota):
        if nueva_nota is not None:
            validadores = [
                lambda numero: solo_numero(numero),
                lambda numero: dentro_rango(numero, 1, 10)
            ]
            recorre_validadores(validadores, nueva_nota)
        self.__recuperatorio1 = nueva_nota

#RECUPERATORIO2
    @property
    def recuperatorio2(self):
        return self.__recuperatorio2

    @recuperatorio2.setter
    def recuperatorio2(self, nueva_nota):
        if nueva_nota is not None:
            validadores = [
                lambda numero: solo_numero(numero),
                lambda numero: dentro_rango(numero, 1, 10)
            ]
            recorre_validadores(validadores, nueva_nota)
        self.__recuperatorio2 = nueva_nota

#NOTA_FINAL
    @property
    def nota_final(self):
        return self.__nota_final

    @nota_final.setter
    def nota_final(self, nueva_nota):
        if nueva_nota is not None:
            validadores = [
                lambda numero: solo_numero(numero),
                lambda numero: dentro_rango(numero, 1, 10)
            ]
            recorre_validadores(validadores, nueva_nota)
        self.__nota_final = nueva_nota

#ESTADO
    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, nuevo_estado):
        if nuevo_estado is not None:
            validadores = [
                lambda estado: solo_letras(estado),
                lambda estado: longitud_palabra(estado, 2, 15)
            ]
            recorre_validadores(validadores, nuevo_estado)
        self.__estado = nuevo_estado

