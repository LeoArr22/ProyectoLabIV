import re #Importamos modulo re para trabajar con expresiones regulares
from datetime import datetime



#RECORRE LA LISTA DE VALIDADORES CORRESPONDIENTES
def recorre_validadores(validadores, valor):
        for validador in validadores:
            valido, mensaje = validador(valor)
            if not valido:
                raise ValueError(mensaje) 



#VALIDADORES DE STRING

def longitud_palabra(palabra, min, max):
    if len(palabra) > max:
        return (False, f"Superó la longitud máxima de {max} caracteres")
    elif len(palabra) < min:
        return (False, f"No alcanzó la longitud mínima de {min} caracteres")
    else:
        return (True, "") 

def solo_letras(palabra):
    # La siguiente es una expresion regular. 
    # fullmatch controla si en cualquier momento de la cadena se cumple con la condicion de 
    # a-zA-Z (todas las letras minus y mayus) y \s (los espacios)
    # la r inicial indica que se trata de una cadena sin procesar para evitar problemas con el guion invertido
    # El + indica uno o mas del conjunto anterior
    if re.fullmatch(r"[a-zA-ZñÑ\s]+", palabra):
        return (True, "")
    else:
        return (False, "Solo se permiten letras y espacios")
            
            
#VALIDADORES DE INT

def longitud_numero(numero, min, max):
    numero=str(numero)
    if len(numero) > max:
        return (False, f"Superó la longitud máxima de {max} números")
    elif len(numero) < min:
        return (False, f"No alcanzó la longitud mínima de {min} números")
    else:
        return (True, "")

def solo_numero(numero):
    numero=str(numero)
    if re.fullmatch("[0-9]+", numero):
        return (True, "")    
    else:
        return (False, "Solo se permiten numeros")
    
def dentro_rango(numero, min, max):
    if numero < min or numero > max:
        return (False, f"Fuera de rango (de {min} a {max})")
    else:
        return (True, "")
    
    
# VALIDADOR DE FECHA

def valida_fecha(fecha, formato=r"%Y-%m-%d"):
    try:
        datetime.strptime(fecha, formato)
        return (True, "")
    except ValueError:
        return (False, "Fecha no valida (YYYY-MM-DD)")