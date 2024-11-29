import customtkinter as ctk
from tkinter import StringVar, IntVar
from data.crud.crud_materias import CrudMaterias
from data.crud.crud_notas import CrudNotas
from data.crud.crud_alumnos import CrudAlumnos  # Para buscar por DNI


class CrearNota:
    def __init__(self):
        self.ventana = ctk.CTk()  # Crea la ventana principal
        self.ventana.title("Asignar Materia")
        self.ventana.geometry("600x500")
        self.ventana.resizable(False, False)

        # Variables
        self.materia_id_var = IntVar()  # Variable para almacenar el ID de la materia seleccionada
        self.alumno_id_var = StringVar()  # Variable para almacenar el ID del alumno ingresado
        self.dni_var = StringVar()  # Variable para buscar alumno por DNI

        # Flecha para volver al menú anterior
        self.boton_volver = ctk.CTkButton(self.ventana, text="← Volver", command=self.volver)
        self.boton_volver.pack(anchor="w", padx=10, pady=10)

        # Título
        self.titulo = ctk.CTkLabel(self.ventana, text="Asignar Materia a Alumno", font=("Helvetica", 20, "bold"))
        self.titulo.pack(pady=20)
        
        # Campo para buscar alumno por DNI
        self.label_buscar_dni = ctk.CTkLabel(self.ventana, text="Buscar Alumno por DNI:", font=("Helvetica", 14))
        self.label_buscar_dni.pack(pady=(10, 5))
        self.entry_buscar_dni = ctk.CTkEntry(self.ventana, textvariable=self.dni_var, width=300)
        self.entry_buscar_dni.pack(pady=5)
        self.boton_buscar_dni = ctk.CTkButton(self.ventana, text="Buscar", command=self.buscar_alumno_por_dni)
        self.boton_buscar_dni.pack(pady=5)

        # Campo para mostrar el ID del alumno encontrado
        self.label_alumno = ctk.CTkLabel(self.ventana, text="ID del Alumno:", font=("Helvetica", 14))
        self.label_alumno.pack(pady=(10, 5))
        self.entry_alumno = ctk.CTkEntry(self.ventana, textvariable=self.alumno_id_var, width=300)
        self.entry_alumno.pack(pady=5)

        # ComboBox para seleccionar la materia
        self.label_materia = ctk.CTkLabel(self.ventana, text="Seleccionar Materia:", font=("Helvetica", 14))
        self.label_materia.pack(pady=(10, 5))
        self.combo_materias = ctk.CTkComboBox(self.ventana, width=300, command=self.seleccionar_materia)
        self.combo_materias.pack(pady=5)

        # Botón para cargar las materias en el ComboBox
        self.btn_cargar_materias = ctk.CTkButton(self.ventana, text="Cargar Materias", command=self.cargar_materias)
        self.btn_cargar_materias.pack(pady=10)

        # Botón para asignar la materia al alumno
        self.btn_asignar = ctk.CTkButton(self.ventana, text="Asignar Materia", command=self.asignar_materia)
        self.btn_asignar.pack(pady=10)

        # Ejecutar la ventana
        self.ventana.mainloop()

    def cargar_materias(self):
        """Carga las materias disponibles en el combo box"""
        crud_materias = CrudMaterias()
        try:
            materias = crud_materias.obtener_todas()  # Devuelve una lista de tuplas
            nombres_materias = [f"{m[0]} - {m[1]}" for m in materias]  # Asume que la estructura es (id, nombre)
            self.combo_materias.configure(values=nombres_materias)  # Actualiza las opciones del ComboBox
        except Exception as e:
            self.label_alumno.configure(text=f"Error al cargar materias: {e}", text_color="#FF0000")

    def seleccionar_materia(self, value):
        """Selecciona la materia del combo box"""
        try:
            materia_id = int(value.split(" - ")[0])  # Obtiene el ID de la materia
            self.materia_id_var.set(materia_id)  # Guarda el ID en una variable
        except ValueError:
            self.label_alumno.configure(text="Error al procesar la materia seleccionada", text_color="#FF0000")

    def asignar_materia(self):
        """Asigna la materia al alumno ingresado"""
        alumno_id = self.alumno_id_var.get()
        materia_id = self.materia_id_var.get()

        if not alumno_id or not materia_id:
            self.label_alumno.configure(text="Por favor, complete todos los campos.", text_color="#FF0000")
            return

        crud = CrudNotas()
        try:
            crud.crear_nota(alumno_id, materia_id, None, None, None, None, None, None)
            self.label_alumno.configure(text="Materia asignada correctamente.", text_color="#00FF00")
            self.limpiar_campos()
        except Exception as e:
            self.label_alumno.configure(text=f"Error al asignar materia: {e}", text_color="#FF0000")

    def limpiar_campos(self):
        """Limpia los campos después de una asignación exitosa"""
        self.alumno_id_var.set("")
        self.dni_var.set("")
        self.materia_id_var.set(0)
        self.combo_materias.set("")

    def buscar_alumno_por_dni(self):
        """Busca un alumno por DNI y llena el campo ID del Alumno"""
        dni = self.dni_var.get()
        if not dni:
            self.label_alumno.configure(text="Por favor, ingrese un DNI válido.", text_color="#FF0000")
            return

        crud_alumnos = CrudAlumnos()
        try:
            alumno = crud_alumnos.obtener_por_documento(dni)
            if alumno:
                self.alumno_id_var.set(alumno[0])  # Asume que el ID del alumno está en la primera posición
                self.label_alumno.configure(text="Alumno encontrado.", text_color="#00FF00")
            else:
                self.label_alumno.configure(text="No se encontró un alumno con ese DNI.", text_color="#FF0000")
        except Exception as e:
            self.label_alumno.configure(text=f"Error al buscar alumno: {e}", text_color="#FF0000")

    def volver(self):
        """Vuelve al menú anterior"""
        from gui.menu_principal.menu_principal import MenuPrincipal
        self.ventana.destroy()
        MenuPrincipal()
