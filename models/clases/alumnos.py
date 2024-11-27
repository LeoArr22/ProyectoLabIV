from util.validadores import *

#Todos nuestros atributos tendran de valor predeterminado None
#De esta forma vamos a poder actualizar atributos de manera individual
class Alumno:
    def __init__(self, nombre=None, apellido=None, documento=None, telefono=None, direccion=None):
        self.nombre=nombre
        self.apellido=apellido
        self.documento=documento
        self.telefono=telefono
        self.direccion=direccion
        
#Vamos a usarlo para el create    
    def es_completo(self):
        atributos_requeridos = ["nombre", "apellido", "documento", "telefono", "direccion"]
        for atributo in atributos_requeridos:
            if getattr(self, atributo) is None:  #getattr: obtiene el valor de cada atributo. Si alguno es None 
                return False                     #significa que nuestro modelo aun no esta completo y nos devuelve False
        return True 
     
        
#NOMBRE    
    @property #Convertimos el metodo en un getter
    def nombre (self):
        return self.__nombre
    
    @nombre.setter #convertimos el metodo en un setter, usamos notacion de punto alumno1.nombre="Nuevo_nombre"
    def nombre(self, nuevo_nombre):
        if nuevo_nombre is not None:
        # Lista de validadores con sus parametros
            validadores = [
                lambda palabra: longitud_palabra(palabra, 2, 20), #Usamos funciones anonimas para validar cada validador
                lambda palabra: solo_letras(palabra) #todas nos van a devolver una tupla de dos valores
            ]
    #La tupla obtenida puede ser (False, "mensaje de error") o (True, "")
    #valido guarda al booleano, mensaje al string
    #en caso de ser falso se activa el if y devuelve como mensaje de error al try para su impresion
            recorre_validadores(validadores, nuevo_nombre)
            self.__nombre = nuevo_nombre 
            
            
#APELLIDO    
    @property 
    def apellido (self):
        return self.__apellido
    
    @apellido.setter 
    def apellido(self, nuevo_apellido):
        if nuevo_apellido is not None:
    
            validadores = [
                lambda palabra: longitud_palabra(palabra, 1, 20),
                lambda palabra: solo_letras(palabra) 
            ]

            recorre_validadores(validadores, nuevo_apellido)
            self.__apellido = nuevo_apellido     
        

#DOCUMENTO    
    @property 
    def documento (self):
        return self.__documento
    
    @documento.setter 
    def documento(self, nuevo_documento):
        if nuevo_documento is not None:
            validadores = [
                lambda numero: longitud_numero(numero, 8, 8),
                lambda numero: solo_numero(numero) 
            ]

            recorre_validadores(validadores, nuevo_documento)
            self.__documento = nuevo_documento
        
        
#TELEFONO    
    @property 
    def telefono (self):
        return self.__telefono
    
    @telefono.setter 
    def telefono(self, nuevo_telefono):
        if nuevo_telefono is not None:
            validadores = [
                lambda numero: longitud_numero(numero, 6, 15),
                lambda numero: solo_numero(numero)
            ]

            recorre_validadores(validadores, nuevo_telefono)
            self.__telefono = nuevo_telefono       
        

#DIRECCION    
    @property 
    def direccion (self):
        return self.__direccion
    
    @direccion.setter 
    def direccion(self, nuevo_direccion):
        if nuevo_direccion is not None:
            validadores = [
                lambda palabra: longitud_palabra(palabra, 6, 15),
            ]

            recorre_validadores(validadores, nuevo_direccion)
            self.__direccion = nuevo_direccion          


alumno1=Alumno()
        
        
#FORMA DE UTILIZARLO    
# EL TRY CAPTURA EL ERROR Y NO PERMITE QUE SE ASIGNE EL VALOR, Y MUESTRA EL ERROR
# try:
#     alumno1=Alumno("laslaslaslalsasllsa", "arrd adsadsadsads", 38609203, 22222, "sanabria")  # Intenta asignar un nuevo valor válido
# except ValueError as e:
#     print(e)  # Muestra el error si las validaciones fallan

# print(alumno1.apellido)  # Imprime el valor actual del nombre
