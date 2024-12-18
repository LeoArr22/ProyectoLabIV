from PIL import ImageTk, Image
import customtkinter as ctk

# Función que lee una imagen de una ruta (path) y redimensiona según una tupla (size).
# Devuelve un objeto compatible con customtkinter.
def leer_imagen(path, size):
    # Abre la imagen, la redimensiona y la convierte en un formato compatible
    imagen_redimensionada = Image.open(path).resize(size, Image.LANCZOS)
    return ctk.CTkImage(dark_image=imagen_redimensionada, size=size)


#ventana.geometry("ancho x alto + posicion_x + posicion_y")
#Define tamañano de la ventana y luego la posicion respecto al borde izquierdo y al borde superior
#Con nuestra funcion centrar_ventana  indicamos el tamaño de la pantalla
#y logramos que se ubique en el centro de la pantalla del usuario, esto gracias
#al calculo realizado en x e y
def centrar_ventana(ventana, aplicacion_ancho, aplicacion_largo):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_largo = ventana.winfo_screenheight()
    x = int((pantalla_ancho/2) - (aplicacion_ancho/2))
    y = int((pantalla_largo/2) - (aplicacion_largo/2)) - 30
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")

#Recibe una ventana, al destruye y la siguiente
def destruir(ventana_actual, proxima_ventana):
        ventana_actual.destroy()  # Cierra la ventana actual
        proxima_ventana()