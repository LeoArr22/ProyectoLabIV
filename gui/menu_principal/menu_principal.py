import customtkinter as ctk
from tkinter.font import BOLD
from gui.util.utils_gui import centrar_ventana

class MenuPrincipal:
    def __init__(self):
        self.ventana = ctk.CTk()  #Crea la ventana principal
        self.ventana.title('Login')
        centrar_ventana(self.ventana, 1300, 650)
        self.ventana.resizable(width=0, height=0)
        self.etiqueta_error_login = None
        
        self.frame_fondo = ctk.CTkFrame(self.ventana, width=700, height=500)
        self.frame_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        
        #Etiqueta de bienvenida
        etiqueta_bienvenida = ctk.CTkLabel(self.frame_fondo, text="BIENVENIDO", text_color="#FFFFFF",
                                           fg_color="#22242B", font=('Carlito', 50, BOLD))
        etiqueta_bienvenida.place(relx=0.57, rely=0.1)  # Ajuste de posición
        
        
        #Boton de login
        btn_login = ctk.CTkButton(self.frame_fondo, font=('Helvetica', 25, BOLD), text="Ingresar", 
                                  text_color="#FFFFFF", fg_color='#22242B', hover_color="#7B878D",
                                  border_width=2, border_color="#FFFFFF")
        btn_login.place(relx=0.65, rely=0.7) 
        
        # Ejecutar la ventana
        self.ventana.mainloop()
        
  