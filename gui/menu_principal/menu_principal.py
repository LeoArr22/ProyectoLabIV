import customtkinter as ctk
from tkinter.font import BOLD
from gui.util.gestion_ventanas import centrar_ventana, destruir
from gui.menus_alumnos.menu_alumnos import MenuAlumnos
from gui.menu_materias.menu_materias import MenuMaterias
from gui.menu_faltas.menu_faltas import MenuFaltas
from gui.menu_amonestaciones.menu_amonestaciones import MenuAmonestaciones

class MenuPrincipal:
    def __init__(self):
        self.ventana = ctk.CTk()  # Crea la ventana principal
        self.ventana.title('Ventana Principal')
        self.ventana.configure(bg="#F0F0F0")  # Color de fondo de la ventana
        centrar_ventana(self.ventana, 1300, 650)
        self.ventana.resizable(width=0, height=0)

        # Crear un Frame de fondo con color para cubrir toda la ventana
        self.frame_fondo = ctk.CTkFrame(self.ventana, fg_color="#22272E") 
        self.frame_fondo.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center")  # Cubre toda la ventana

        # Título en la parte superior
        self.titulo = ctk.CTkLabel(self.frame_fondo, text="Gestión de Curso", font=('Carlito', 40, 'bold'), 
                                   text_color="#FFFFFF", fg_color="#22272E")
        self.titulo.place(relx=0.5, rely=0.05, anchor="center")  # Centrado en la parte superior

        # Crear un Frame para los botones
        self.frame_botones = ctk.CTkFrame(self.frame_fondo)  # Frame para los botones (ahora dentro del fondo)
        self.frame_botones.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.7)  # Cubre el 90% de la ventana

        # Definir las columnas del grid
        for i in range(4):
            self.frame_botones.grid_columnconfigure(i, weight=1, minsize=250)  # Ajusta el tamaño de las columnas

        # Definir las filas para que ocupen todo el espacio vertical
        self.frame_botones.grid_rowconfigure(0, weight=1)  # Solo una fila

        # Crear las columnas con sus botones centrados
        # Primera columna (Azul)
        self.columna_1 = ctk.CTkFrame(self.frame_botones, fg_color="#1F2C5D")  # Azul
        self.columna_1.grid(row=0, column=0, sticky="nsew")

        btn_alumnos = ctk.CTkButton(self.columna_1, text="Alumnos", font=('Helvetica', 30, 'bold'),
                                    text_color="#FFFFFF", fg_color="#1F2C5D", hover_color="#4B5B7A",
                                    command=lambda: destruir(self.ventana, MenuAlumnos))
        btn_alumnos.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)  # Rellenar el espacio

        # Segunda columna (Verde)
        self.columna_2 = ctk.CTkFrame(self.frame_botones, fg_color="#28A745")  # Verde
        self.columna_2.grid(row=0, column=1, sticky="nsew")

        btn_materias = ctk.CTkButton(self.columna_2, text="Materias", font=('Helvetica', 30, 'bold'),
                                     text_color="#FFFFFF", fg_color="#28A745", hover_color="#3DAe55",
                                     command=lambda: destruir(self.ventana, MenuMaterias))
        btn_materias.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)  # Rellenar el espacio

        # Tercera columna (Amarillo)
        self.columna_3 = ctk.CTkFrame(self.frame_botones, fg_color="#FFC107")  # Amarillo
        self.columna_3.grid(row=0, column=2, sticky="nsew")

        btn_faltas = ctk.CTkButton(self.columna_3, text="Faltas", font=('Helvetica', 30, 'bold'),
                                   text_color="#FFFFFF", fg_color="#FFC107", hover_color="#FFCA28",
                                   command=lambda: destruir(self.ventana, MenuFaltas))
        btn_faltas.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)  # Rellenar el espacio

        # Cuarta columna (Rojo)
        self.columna_4 = ctk.CTkFrame(self.frame_botones, fg_color="#DC3545")  # Rojo
        self.columna_4.grid(row=0, column=3, sticky="nsew")

        btn_amonestaciones = ctk.CTkButton(self.columna_4, text="Amonestaciones", font=('Helvetica', 30, 'bold'),
                                           text_color="#FFFFFF", fg_color="#DC3545", hover_color="#E74C3C",
                                           command=lambda: destruir(self.ventana, MenuAmonestaciones))
        btn_amonestaciones.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)  # Rellenar el espacio

        # Ejecutar la ventana
        self.ventana.mainloop()

