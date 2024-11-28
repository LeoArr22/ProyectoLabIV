import customtkinter as ctk
from tkinter import StringVar
from models.clases.util.validadores import *
from gui.util.gestion_ventanas import centrar_ventana
from models.clases.alumnos import Alumno  
from data.crud.crud_alumnos import CrudAlumnos

class CrearAlumno:
    def __init__(self):
        self.ventana = ctk.CTk()
        self.ventana.title("Crear Alumno")
        centrar_ventana(self.ventana, 500, 700)
        self.ventana.resizable(width=0, height=0)

        # Variables de entrada
        self.nombre_var = StringVar()
        self.apellido_var = StringVar()
        self.documento_var = StringVar()
        self.telefono_var = StringVar()
        self.direccion_var = StringVar()

        # Títulos
        ctk.CTkLabel(self.ventana, text="Crear Alumno", font=("Carlito", 30, "bold")).pack(pady=10)

        # Campos de entrada
        self.campos = [
            ("Nombre", self.nombre_var),
            ("Apellido", self.apellido_var),
            ("Documento", self.documento_var),
            ("Telefono", self.telefono_var),
            ("Direccion", self.direccion_var)
        ]
        self.labels_error = {}  # Almacena los mensajes de error para cada campo

        # Frame para los campos de entrada
        frame_campos = ctk.CTkFrame(self.ventana)
        frame_campos.pack(pady=20, padx=20, fill="x")

        for campo, var in self.campos:
            self.crear_campo(frame_campos, campo, var)

        # Frame para los botones
        frame_botones = ctk.CTkFrame(self.ventana)
        frame_botones.pack(pady=20, padx=20, fill="x")

        # Botón Crear Alumno
        ctk.CTkButton(
            frame_botones,
            text="Crear Alumno",
            command=self.crear_alumno,
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

        # Botón Aceptar (limpiar campos)
        ctk.CTkButton(
            frame_botones,
            text="Aceptar",
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
        label_error = ctk.CTkLabel(frame, text="", text_color="#FF0000", anchor="w")
        label_error.pack(fill="x")
        # Usamos el nombre del campo tal como aparece (con mayúscula y acento) como clave en el diccionario
        self.labels_error[nombre] = label_error  

    def validar_y_instanciar(self):
        """Valida los datos y crea una instancia del alumno si son válidos"""
        alumno = Alumno()
        campos = ["nombre", "apellido", "documento", "telefono", "direccion"]
        valores = [self.nombre_var.get(), self.apellido_var.get(),
                   self.documento_var.get(), self.telefono_var.get(),
                   self.direccion_var.get()]

        errores = {}
        for campo, valor in zip(campos, valores):
            try:
                setattr(alumno, campo, valor)  # Intenta setear el valor en el objeto Alumno
                # Usamos el nombre exacto del campo (con acento) para acceder al mensaje de error
                self.labels_error[campo.capitalize()].configure(text="")  # Limpia el error si fue válido
            except Exception as e:
                errores[campo] = str(e)  # Captura el error de validación
                # Muestra el error usando el nombre exacto del campo que se utiliza en labels_error
                self.labels_error[campo.capitalize()].configure(text=str(e))  

        if errores:
            return None  # Si hay errores, no se crea el alumno
        return alumno  # Retorna el objeto Alumno si todo está bien

    def crear_alumno(self):
        """Intenta crear el alumno en la base de datos"""
        alumno = self.validar_y_instanciar()
        if not alumno:
            return  # Si hay errores, no procede

        # Validar si es completo
        if not alumno.es_completo():
            ctk.CTkLabel(
                self.ventana,
                text="Por favor completa todos los campos.",
                text_color="#FF0000"
            ).pack()
            return

        # Crear en la base de datos
        crud = CrudAlumnos()
        try:
            crud.crear_alumno(
                alumno.nombre,
                alumno.apellido,
                alumno.documento,
                alumno.telefono,
                alumno.direccion
            )
            ctk.CTkLabel(
                self.ventana,
                text="Alumno creado con éxito.",
                text_color="#28A745"
            ).pack()
            self.limpiar_campos()  # Limpia los campos tras creación exitosa
        except Exception as e:
            ctk.CTkLabel(
                self.ventana,
                text=f"Error al crear el alumno: {e}",
                text_color="#FF0000"
            ).pack()

    def limpiar_campos(self):
        """Limpia todos los campos después de una operación"""
        for var in [self.nombre_var, self.apellido_var, self.documento_var, self.telefono_var, self.direccion_var]:
            var.set("")

    def volver(self, ventana_actual):
        """Destruye la ventana actual y abre el menú principal"""
        from gui.menu_principal.menu_principal import MenuPrincipal
        ventana_actual.destroy()
        MenuPrincipal()
