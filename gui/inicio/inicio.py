import sys
import os

# Obtiene el directorio actual del script en ejecución
current_dir = os.path.dirname(os.path.abspath(__file__))

# Obtiene el directorio raíz
proyecto_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))

# Agrega la subcarpeta 'DATA' al path
gui_dir = os.path.join(proyecto_dir, "gui")
sys.path.append(gui_dir)

import customtkinter as ctk
from tkinter.font import BOLD
from util.utils_gui import centrar_ventana, leer_imagen


class LoginApp:
    def __init__(self):
        self.ventana = ctk.CTk()  #Crea la ventana principal
        self.ventana.title('Login')
        centrar_ventana(self.ventana, 700, 500)
        self.ventana.resizable(width=0, height=0)
        self.etiqueta_error_login = None
        
        self.frame_fondo = ctk.CTkFrame(self.ventana, width=700, height=500)
        self.frame_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        #Coloca la imagen de fondo en el Frame
        self.fondo = leer_imagen("./gui/inicio/salon.png", (700, 550))
        self.fondo_label = ctk.CTkLabel(self.frame_fondo, image=self.fondo, text="")
        self.fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        #Etiqueta de bienvenida
        etiqueta_bienvenida = ctk.CTkLabel(self.frame_fondo, text="BIENVENIDO", text_color="#F3920F",
                                           fg_color="#1C2124", font=('Carlito', 50, BOLD))
        etiqueta_bienvenida.place(relx=0.57, rely=0.1)  # Ajuste de posición
        
        
        #Boton de login
        btn_login = ctk.CTkButton(self.frame_fondo, font=('Helvetica', 20, BOLD), text="Iniciar Sesión", 
                                  text_color="#F3920F", bg_color='#1C2124', fg_color='#1C2124', hover_color="#D5D0D4",
                                  border_width=2, border_color="#F3920F")
        btn_login.place(relx=0.65, rely=0.7) 
        
        # Ejecutar la ventana
        self.ventana.mainloop()
        
LoginApp()