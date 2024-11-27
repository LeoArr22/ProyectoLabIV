from util.validadores import *

class Amonestacion:
    def __init__(self, fecha=None, motivo=None, cantidad=None):
        self.fecha = fecha
        self.motivo = motivo
        self.cantidad = cantidad

#Vamos a usarlo para el create 
    def es_completo(self):
        atributos_requeridos=["fecha", "motivo", "cantidad"]
        for atributo in atributos_requeridos:
            if getattr(self, atributo) is None:
                return False
        return True    


#FECHA
    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, nueva_fecha):
        if nueva_fecha is not None:
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
        if nuevo_motivo is not None:
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
        if nueva_cantidad is not None:    
            validadores = [
                lambda valor: solo_numero(valor),
                lambda valor: dentro_rango(valor, 1, 20)
            ]
            recorre_validadores(validadores, nueva_cantidad)
            self.__cantidad = nueva_cantidad