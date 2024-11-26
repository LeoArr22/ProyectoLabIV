from util.validadores import *

class Materia:
    def __init__(self, nombre=None):
        self.nombre=nombre
             
    #Vamos a usarlo para el create
    def es_completo(self):
        atributos_requeridos=["nombre"]
        for atributo in atributos_requeridos:
            if getattr(self, atributo) is None:
                return False
        return True
             
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre is not None:
            validadores = [
                lambda palabra: longitud_palabra(palabra, 3, 20)
            ]

            recorre_validadores(validadores, nuevo_nombre)
        self.__nombre = nuevo_nombre  