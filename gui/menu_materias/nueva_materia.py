import customtkinter as ctk
from tkinter import StringVar
from models.clases.util.validadores import *  # Asegúrate de que esto apunte a tus validadores
from gui.util.gestion_ventanas import centrar_ventana
from models.clases.materias import Materia  # Clase Materia con validaciones
from data.crud.crud_materias import CrudMaterias  # CRUD para la tabla Materias

class CrearMateria:
    def __init__(self):
        self.ventana = ctk.CTk()
        self.ventana.title("Crear Materia")
        centrar_ventana(self.ventana, 600, 600)
        self.ventana.resizable(width=0, height=0)

        # Variable de entrada
        self.nombre_var = StringVar()

        # Títulos
        ctk.CTkLabel(self.ventana, text="Crear Materia", font=("Carlito", 30, "bold")).pack(pady=10)

        # Frame para los campos de entrada
        frame_campos = ctk.CTkFrame(self.ventana)
        frame_campos.pack(pady=20, padx=20, fill="x")

        # Campo Nombre
        self.crear_campo(frame_campos, "Nombre", self.nombre_var)

        # Frame para los botones
        frame_botones = ctk.CTkFrame(self.ventana)
        frame_botones.pack(pady=20, padx=20, fill="x")

        # Botón Crear Materia
        ctk.CTkButton(
            frame_botones,
            text="Crear Materia",
            command=self.crear_materia,
            fg_color="#1F7A1F",
            hover_color="#28A745",
        ).pack(side="left", padx=10)

        # Botón Cancelar
        ctk.CTkButton(
            frame_botones,
            text="Cancelar",
            command=lambda: self.volver(self.ventana),
            fg_color="#FF0000",
            hover_color="#B22222",
        ).pack(side="left", padx=10)

        # Botón Limpiar Campos
        ctk.CTkButton(
            frame_botones,
            text="Limpiar Campos",
            command=self.limpiar_campos,
            fg_color="#007BFF",
            hover_color="#0056B3",
        ).pack(side="left", padx=10)

        # Mantener la ventana abierta
        self.ventana.mainloop()

    def crear_campo(self, parent, nombre, variable):
        """Crea un campo de entrada con un label y espacio para mensajes de error"""
        frame = ctk.CTkFrame(parent)
        frame.pack(pady=5, padx=5, fill="x")
        ctk.CTkLabel(frame, text=nombre, anchor="w").pack(fill="x")

        entry = ctk.CTkEntry(frame, textvariable=variable)
        entry.pack(fill="x", pady=5)

        # Label para mensajes de error (inicia vacío)
        self.label_error = ctk.CTkLabel(frame, text="", text_color="#FF0000", anchor="w")
        self.label_error.pack(fill="x")

    def validar_y_instanciar(self):
        """Valida los datos y crea una instancia de la materia si son válidos"""
        materia = Materia()
        try:
            materia.nombre = self.nombre_var.get()  # Valida el nombre
            self.label_error.configure(text="")  # Limpia cualquier mensaje de error si es válido
        except Exception as e:
            self.label_error.configure(text=str(e))  # Muestra el error
            return None
        return materia

    def crear_materia(self):
        """Intenta crear la materia en la base de datos"""
        materia = self.validar_y_instanciar()
        if not materia:
            return  # Si hay errores, no procede

        # Validar si está completo
        if not materia.es_completo():
            self.label_error.configure(text="Por favor, completa todos los campos.")
            return

        # Crear en la base de datos
        crud = CrudMaterias()
        try:
            crud.crear_materia(materia.nombre)
            ctk.CTkLabel(
                self.ventana,
                text="Materia creada con éxito.",
                text_color="#28A745"
            ).pack()
            self.limpiar_campos()  # Limpia los campos tras creación exitosa
        except Exception as e:
            self.label_error.configure(text=f"Error al crear la materia: {e}")

    def limpiar_campos(self):
        """Limpia todos los campos después de una operación"""
        self.nombre_var.set("")
        self.label_error.configure(text="")

    def volver(self, ventana_actual):
        """Destruye la ventana actual y abre el menú principal"""
        from gui.menu_principal.menu_principal import MenuPrincipal
        ventana_actual.destroy()
        MenuPrincipal()
