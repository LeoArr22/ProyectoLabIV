from util.validadores import *

class Alumno:
    def __init__(self, nombre, apellido, documento, telefono, direccion):
        self.__nombre=nombre
        self.apellido=apellido
        self.documento=documento
        self.telefono=telefono
        self.direccion=direccion
        
    @property
    def nombre (self):
        return self.__nombre
    
   
    def set_nombre(self, nuevo_nombre):
        # Lista de validadores con sus parámetros
        validadores = [
            lambda palabra: longitud_palabra(palabra, 5, 10), #Usamos lambda para capturar el return de las funciones validadoras
            lambda palabra: solo_letras(palabra)
        ]

        for validador in validadores:     
            valido=[]                       
            valido=validador(nuevo_nombre)
            if not valido[0]:
                return False, valido[1]  # Retorna el error si falla una validación

        self.__nombre = nuevo_nombre
        return True, ""  # Todo válido
            

# alumno1=Alumno("laslaslaslalsasllsa", "arr", 386092, 22222, "sanabria")

# valido=[]
# valido=alumno1.set_nombre("dario")

# if not valido[0]:
#     print(valido[1])
    
# print(alumno1.nombre)
