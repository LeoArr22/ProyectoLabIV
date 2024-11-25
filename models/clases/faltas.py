from util.validadores import *

class Falta:
    def __init__(self, fecha, justificativo, observaciones=None):
        self.fecha = fecha
        self.justificativo = justificativo
        self.observaciones = observaciones

    # FECHA
    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, nueva_fecha):
        validadores = [
            lambda fecha: valida_fecha(fecha)  # Validador para fechas
        ]
        recorre_validadores(validadores, nueva_fecha)
        self.__fecha = nueva_fecha

    # JUSTIFICATIVO
    @property
    def justificativo(self):
        return self.__justificativo

    @justificativo.setter
    def justificativo(self, nuevo_valor):
        validadores = [
            lambda valor: solo_numero(valor),
            lambda valor: dentro_rango(valor, 0, 1)  # Solo 0 o 1
        ]
        recorre_validadores(validadores, nuevo_valor)
        self.__justificativo = nuevo_valor

    # OBSERVACIONES
    @property
    def observaciones(self):
        return self.__observaciones

    @observaciones.setter
    def observaciones(self, nueva_observacion):
        if nueva_observacion is not None:
            validadores = [
                lambda texto: longitud_palabra(texto, 0, 255)  # Longitud máxima opcional
            ]
            recorre_validadores(validadores, nueva_observacion)
        self.__observaciones = nueva_observacion
