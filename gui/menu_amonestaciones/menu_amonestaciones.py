import customtkinter as ctk
from tkinter.font import BOLD
from gui.util.gestion_ventanas import centrar_ventana, destruir


class MenuAmonestaciones:
    def __init__(self):
        self.ventana = ctk.CTk()  # Crea la ventana principal
        self.ventana.title('Menú Amonestaciones')
        self.ventana.configure(bg="#F0F0F0")  # Color de fondo de la ventana
        centrar_ventana(self.ventana, 1300, 650)
        self.ventana.resizable(width=0, height=0)

        # Crear un Frame de fondo con color para cubrir toda la ventana
        self.frame_fondo = ctk.CTkFrame(self.ventana, fg_color="#22272E")  # Fondo oscuro
        self.frame_fondo.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center")  # Cubre toda la ventana

        # Título en la parte superior
        self.titulo = ctk.CTkLabel(self.frame_fondo, text="Menú de Amonestaciones", font=('Carlito', 40, 'bold'),
                                   text_color="#FFFFFF", fg_color="#22272E")
        self.titulo.place(relx=0.5, rely=0.05, anchor="center")  # Centrado en la parte superior

        # Botón para volver atrás (flecha)
        btn_volver = ctk.CTkButton(self.frame_fondo, text="←", font=('Helvetica', 25, 'bold'),
                                   text_color="#FFFFFF", fg_color="#1F2C5D", hover_color="#4B5B7A",
                                   command=lambda: self.volver(self.ventana))
        btn_volver.place(x=10, y=10)  # Coloca la flecha en la esquina superior izquierda

        # Crear un Frame para los botones
        self.frame_botones = ctk.CTkFrame(self.frame_fondo)  # Frame para los botones (ahora dentro del fondo)
        self.frame_botones.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.6, relheight=0.4)  # Cubre el 60% del ancho y 40% de la altura

        # Configuración de columnas
        for i in range(2):
            self.frame_botones.grid_columnconfigure(i, weight=1)  # Ajusta las columnas para que ocupen el espacio disponible

        # Configuración de filas
        self.frame_botones.grid_rowconfigure(0, weight=1)  # Asegura que la fila ocupe el espacio disponible

        # Crear las columnas con sus botones centrados
        # Primera columna (Rojo oscuro)
        self.columna_1 = ctk.CTkFrame(self.frame_botones, fg_color="#C62828")  # Rojo oscuro
        self.columna_1.grid(row=0, column=0, sticky="nsew")  # Expande en todas las direcciones

        btn_ver_amonestaciones = ctk.CTkButton(self.columna_1, text="Ver Amonestaciones", font=('Helvetica', 30, 'bold'),
                                               text_color="#FFFFFF", fg_color="#C62828", hover_color="#E53935",
                                               command=lambda: destruir(self.ventana, self.abrir_ver_amonestaciones))
        btn_ver_amonestaciones.grid(row=0, column=0, sticky="nsew")  # Rellenar el espacio

        # Segunda columna (Rojo claro)
        self.columna_2 = ctk.CTkFrame(self.frame_botones, fg_color="#E53935")  # Rojo claro
        self.columna_2.grid(row=0, column=1, sticky="nsew")  # Expande en todas las direcciones

        btn_agregar_amonestaciones = ctk.CTkButton(self.columna_2, text="Agregar\nAmonestaciones", font=('Helvetica', 30, 'bold'),
                                                   text_color="#FFFFFF", fg_color="#E53935", hover_color="#EF5350",
                                                   command=lambda: destruir(self.ventana, self.abrir_agregar_amonestaciones))
        btn_agregar_amonestaciones.grid(row=0, column=0, sticky="nsew")  # Rellenar el espacio

        # Ejecutar la ventana
        self.ventana.mainloop()

    def volver(self, ventana_actual):
        from gui.menu_principal.menu_principal import MenuPrincipal
        destruir(ventana_actual, MenuPrincipal)

    def abrir_ver_amonestaciones(self):
        # Aquí se abre la ventana de "Ver Amonestaciones"
        print("Se abre la ventana de Ver Amonestaciones")

    def abrir_agregar_amonestaciones(self):
        # Aquí se abre la ventana de "Agregar Amonestaciones"
        print("Se abre la ventana de Agregar Amonestaciones")
