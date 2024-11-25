from util.validadores import *

class Amonestacion:
    def __init__(self, fecha, motivo, cantidad):
        self.fecha = fecha
        self.motivo = motivo
        self.cantidad = cantidad

#FECHA
    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, nueva_fecha):
        validadores = [
            lambda fecha: valida_fecha(fecha)
        ]
        recorre_validadores(validadores, nueva_fecha)
        self.__fecha = nueva_fecha

#MOTIVO
    @property
    def motivo(self):
        return self.__motivo

    @motivo.setter
    def motivo(self, nuevo_motivo):
        validadores = [
            lambda texto: longitud_palabra(texto, 1, 255)
        ]
        recorre_validadores(validadores, nuevo_motivo)
        self.__motivo = nuevo_motivo

#CANTIDAD
    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        validadores = [
            lambda valor: solo_numero(valor),
            lambda valor: dentro_rango(valor, 1, 20)
        ]
        recorre_validadores(validadores, nueva_cantidad)
        self.__cantidad = nueva_cantidad