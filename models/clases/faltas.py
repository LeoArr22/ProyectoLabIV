from util.validadores import *

class Falta:
    def __init__(self, fecha=None, justificativo=None, observaciones=None):
        self.fecha = fecha
        self.justificativo = justificativo
        self.observaciones = observaciones

#Vamos a usarlo para el create    
    def es_completo(self):
        atributos_requeridos=["fecha", "justificativo"]
        for atributo in atributos_requeridos:
            if getattr(self, atributo) is None:
                return False
        return True    

    # FECHA
    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, nueva_fecha):
        if nueva_fecha is not None:    
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
    def justificativo(self, nuevo_justificativo):
        if nuevo_justificativo is not None:    
            validadores = [
                lambda justificativo: solo_numero(justificativo),
                lambda justificativo: dentro_rango(justificativo, 0, 1)  # Solo 0 o 1
            ]
            recorre_validadores(validadores, nuevo_justificativo)
            self.__justificativo = nuevo_justificativo

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
        else:
            self.__observaciones = "Sin Observaciones"
