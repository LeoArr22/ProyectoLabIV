from util.validadores import *

class Alumno:
    def __init__(self, nombre, apellido, documento, telefono, direccion):
        self.__nombre=nombre
        self.__apellido=apellido
        self.documento=documento
        self.telefono=telefono
        self.direccion=direccion
        
    #NOMBRE    
    @property #Convertimos el metodo en un getter
    def nombre (self):
        return self.__nombre
    
    @nombre.setter #convertimos el metodo en un setter, usamos notacion de punto alumno1.nombre="Nuevo_nombre"
    def nombre(self, nuevo_nombre):
        # Lista de validadores con sus parametros
        validadores = [
            lambda palabra: longitud_palabra(palabra, 5, 10), #Usamos funciones anonimas para validar cada validador
            lambda palabra: solo_letras(palabra) #todas nos van a devolver una tupla de dos valores
        ]
#La tupla obtenida puede ser (False, "mensaje de error") o (True, "")
#valido guarda al booleano, mensaje al string
#en caso de ser falso se activa el if y devuelve como mensaje de error al try para su impresion
        for validador in validadores:
            valido, mensaje = validador(nuevo_nombre) 
            if not valido:
                raise ValueError(mensaje)  # Lanza una excepcion con el mensaje de error

        self.__nombre = nuevo_nombre    
            
        
#FORMA DE UTILIZARLO    
# alumno1=Alumno("laslaslaslalsasllsa", "arr", 386092, 22222, "sanabria")

#EL TRY CAPTURA EL ERROR Y NO PERMITE QUE SE ASIGNE EL VALOR, Y MUESTRA EL ERROR
# try:
#     alumno1.nombre = "Dardo"  # Intenta asignar un nuevo valor válido
# except ValueError as e:
#     print(e)  # Muestra el error si las validaciones fallan

# print(alumno1.nombre)  # Imprime el valor actual del nombre
