import customtkinter as ctk
from tkinter.font import BOLD
from gui.util.gestion_ventanas import centrar_ventana, destruir
from gui.menu_materias.nueva_materia import CrearMateria
from gui.menu_materias.asignar_materias import CrearNota


class MenuMaterias:
    def __init__(self):
        self.ventana = ctk.CTk()  # Crea la ventana principal
        self.ventana.title('Menú Materias')
        self.ventana.configure(bg="#F0F0F0")  # Color de fondo de la ventana
        centrar_ventana(self.ventana, 1300, 650)
        self.ventana.resizable(width=0, height=0)

        # Crear un Frame de fondo con color para cubrir toda la ventana
        self.frame_fondo = ctk.CTkFrame(self.ventana, fg_color="#22272E")  # Fondo oscuro
        self.frame_fondo.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center")  # Cubre toda la ventana

        # Título en la parte superior
        self.titulo = ctk.CTkLabel(self.frame_fondo, text="Menú de Materias", font=('Carlito', 40, 'bold'),
                                   text_color="#FFFFFF", fg_color="#22272E")
        self.titulo.place(relx=0.5, rely=0.05, anchor="center")  # Centrado en la parte superior

        # Botón para volver atrás (flecha)
        btn_volver = ctk.CTkButton(self.frame_fondo, text="←", font=('Helvetica', 25, 'bold'), 
                                   text_color="#FFFFFF", fg_color="#1F2C5D", hover_color="#4B5B7A",
                                   command=lambda: self.volver(self.ventana))
        btn_volver.place(x=10, y=10)  # Coloca la flecha en la esquina superior izquierda

        # Crear un Frame para los botones
        self.frame_botones = ctk.CTkFrame(self.frame_fondo)  # Frame para los botones (ahora dentro del fondo)
        self.frame_botones.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.5)  # Ajustar proporciones

        # Configuración de columnas
        for i in range(3):  # Ahora hay 3 columnas
            self.frame_botones.grid_columnconfigure(i, weight=1)  # Ajusta las columnas para que ocupen el espacio disponible

        # Configuración de filas
        self.frame_botones.grid_rowconfigure(0, weight=1)  # Asegura que la fila ocupe el espacio disponible

        # Primera columna (Verde oscuro)
        self.columna_1 = ctk.CTkFrame(self.frame_botones, fg_color="#28A745")  # Verde
        self.columna_1.grid(row=0, column=0, sticky="nsew")  # Expande en todas las direcciones

        btn_ver_materias = ctk.CTkButton(self.columna_1, text="Ver Materias", font=('Helvetica', 30, 'bold'),
                                         text_color="#FFFFFF", fg_color="#28A745", hover_color="#5A9E69",
                                         command=lambda: destruir(self.ventana, self.abrir_ver_materias))
        btn_ver_materias.grid(row=0, column=0, sticky="nsew")  # Rellenar el espacio

        # Segunda columna (Verde más claro)
        self.columna_2 = ctk.CTkFrame(self.frame_botones, fg_color="#4CAF50")  # Verde más claro
        self.columna_2.grid(row=0, column=1, sticky="nsew")  # Expande en todas las direcciones

        btn_agregar_materias = ctk.CTkButton(self.columna_2, text="Agregar\nMaterias", font=('Helvetica', 30, 'bold'),
                                             text_color="#FFFFFF", fg_color="#4CAF50", hover_color="#80E27E",
                                             command=lambda: destruir(self.ventana, CrearMateria))
        btn_agregar_materias.grid(row=0, column=0, sticky="nsew")  # Rellenar el espacio

        # Tercera columna (Azul)
        self.columna_3 = ctk.CTkFrame(self.frame_botones, fg_color="#007BFF")  # Azul
        self.columna_3.grid(row=0, column=2, sticky="nsew")  # Expande en todas las direcciones

        btn_asignar_materias = ctk.CTkButton(self.columna_3, text="Asignar\nMateria", font=('Helvetica', 30, 'bold'),
                                             text_color="#FFFFFF", fg_color="#007BFF", hover_color="#5A9EFD",
                                             command=lambda: destruir(self.ventana, CrearNota))
        btn_asignar_materias.grid(row=0, column=0, sticky="nsew")  # Rellenar el espacio

        # Ejecutar la ventana
        self.ventana.mainloop()

    def volver(self, ventana_actual):
        from gui.menu_principal.menu_principal import MenuPrincipal
        destruir(ventana_actual, MenuPrincipal)

    def abrir_ver_materias(self):
        # Aquí se abre la ventana de "Ver Materias"
        print("Se abre la ventana de Ver Materias")
