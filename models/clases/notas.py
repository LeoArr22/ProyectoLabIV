from util.validadores import *

class Notas:
    def __init__(self, nombre):
        self.nombre=nombre
             
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        validadores = [
            lambda palabra: longitud_palabra(palabra, 3, 20)
        ]

        recorre_validadores(validadores, nuevo_nombre)
        self.__nombre = nuevo_nombre  