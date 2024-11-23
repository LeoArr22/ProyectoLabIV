#VALIDADORES DE STRING

def longitud_palabra(palabra, min, max):
    if len(palabra) > max:
        return (False, f"Superó la longitud máxima de {max} caracteres")
    elif len(palabra) < min:
        return (False, f"No alcanzó la longitud mínima de {min} caracteres")
    else:
        return (palabra) 

def solo_letras(palabra):
    if not palabra.isalpha():
        return (False, "Solo se permiten caracteres")
    else:
        return palabra
            
    