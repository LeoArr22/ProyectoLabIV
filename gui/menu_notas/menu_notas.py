import customtkinter as ctk
from tkinter import ttk, messagebox  # Para ventanas emergentes y alertas
from data.crud.clase_conexion import Conexion
from data.crud.crud_notas import CrudNotas
from data.crud.crud_alumnos import CrudAlumnos


class MenuNotas(Conexion):
    def __init__(self):
        super().__init__()
        self.crud_notas = CrudNotas()
        self.crud_alumnos = CrudAlumnos()
        self.ventana = ctk.CTk()
        self.ventana.title("Visualización de Notas")
        self.ventana.geometry("1200x700")
        self.ventana.resizable(False, False)

        # Crear un frame principal
        self.frame_principal = ctk.CTkFrame(self.ventana, fg_color="#F5F5F5")
        self.frame_principal.pack(fill="both", expand=True, padx=10, pady=10)

        # Título
        self.titulo = ctk.CTkLabel(
            self.frame_principal,
            text="Listado de Notas",
            font=("Helvetica", 24, "bold"),
            text_color="#333333",
        )
        self.titulo.pack(pady=10)

        # Crear Treeview para mostrar las notas
        self.treeview = ttk.Treeview(self.frame_principal, columns=(
            "Nombre Completo", "Materia ID", "Nota 1", "Nota 2",
            "Recuperatorio 1", "Recuperatorio 2", "Nota Final", "Estado"
        ), show="headings", height=20)
        self.treeview.pack(fill="both", expand=True, padx=20, pady=10)

        # Definir encabezados
        self.treeview.heading("Nombre Completo", text="Nombre Completo")
        self.treeview.heading("Materia ID", text="Materia ID")
        self.treeview.heading("Nota 1", text="Nota 1")
        self.treeview.heading("Nota 2", text="Nota 2")
        self.treeview.heading("Recuperatorio 1", text="Recuperatorio 1")
        self.treeview.heading("Recuperatorio 2", text="Recuperatorio 2")
        self.treeview.heading("Nota Final", text="Nota Final")
        self.treeview.heading("Estado", text="Estado")

        # Ajustar el ancho de las columnas
        for col in self.treeview["columns"]:
            self.treeview.column(col, anchor="center", width=120)

        # Botones para las acciones
        self.boton_cargar = ctk.CTkButton(
            self.frame_principal, text="Cargar Notas", command=self.cargar_notas
        )
        self.boton_cargar.pack(side="left", padx=10, pady=10)

        self.boton_eliminar = ctk.CTkButton(
            self.frame_principal, text="Eliminar Nota", command=self.eliminar_nota
        )
        self.boton_eliminar.pack(side="left", padx=10, pady=10)

        self.boton_modificar = ctk.CTkButton(
            self.frame_principal, text="Modificar Nota", command=self.modificar_nota
        )
        self.boton_modificar.pack(side="left", padx=10, pady=10)

        # Mostrar la ventana
        self.ventana.mainloop()

    def cargar_notas(self):
        # Limpiar el Treeview
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        # Consulta SQL para obtener las notas con el nombre completo del alumno
        query = """
            SELECT 
                a.nombre || ' ' || a.apellido AS nombre_completo,
                n.materiaID,
                n.nota1,
                n.nota2,
                n.recuperatorio1,
                n.recuperatorio2,
                n.notaFinal,
                n.estado
            FROM Notas n
            INNER JOIN Alumnos a ON n.alumnoID = a.alumnoID
        """
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            resultados = cursor.fetchall()

        # Insertar los resultados en el Treeview
        for fila in resultados:
            self.treeview.insert("", "end", values=fila)

    def eliminar_nota(self):
        # Obtener la fila seleccionada
        seleccionado = self.treeview.focus()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione una nota para eliminar.")
            return

        # Confirmar eliminación
        confirmar = messagebox.askyesno(
            "Confirmar", "¿Está seguro de que desea eliminar esta nota?"
        )
        if not confirmar:
            return

        # Obtener datos de la fila seleccionada
        datos = self.treeview.item(seleccionado, "values")
        nombre_completo, materia_id = datos[0], datos[1]

        # Eliminar la nota
        alumno_id = self.obtener_alumno_id_por_nombre(nombre_completo)
        filas_afectadas = self.crud_notas.eliminar_nota(alumno_id, materia_id)

        if filas_afectadas > 0:
            messagebox.showinfo("Éxito", "Nota eliminada correctamente.")
            self.cargar_notas()
        else:
            messagebox.showerror("Error", "No se pudo eliminar la nota.")

    def modificar_nota(self):
        # Obtener la fila seleccionada
        seleccionado = self.treeview.focus()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione una nota para modificar.")
            return

        # Obtener datos de la fila seleccionada
        datos = self.treeview.item(seleccionado, "values")
        nombre_completo, materia_id, *valores = datos

        # Ventana emergente para modificar datos
        self.ventana_modificar = ctk.CTkToplevel(self.ventana)
        self.ventana_modificar.title("Modificar Nota")
        self.ventana_modificar.geometry("400x400")

        # Crear campos de entrada para las notas
        etiquetas = ["Nota 1", "Nota 2", "Recuperatorio 1", "Recuperatorio 2", "Nota Final", "Estado"]
        self.campos = {}

        for i, etiqueta in enumerate(etiquetas):
            ctk.CTkLabel(self.ventana_modificar, text=etiqueta).grid(row=i, column=0, pady=5, padx=5)
            entrada = ctk.CTkEntry(self.ventana_modificar)
            entrada.insert(0, valores[i])
            entrada.grid(row=i, column=1, pady=5, padx=5)
            self.campos[etiqueta] = entrada

        # Botón para guardar los cambios
        ctk.CTkButton(
            self.ventana_modificar, text="Guardar", command=lambda: self.guardar_cambios(nombre_completo, materia_id)
        ).grid(row=len(etiquetas), column=0, columnspan=2, pady=10)

    def guardar_cambios(self, nombre_completo, materia_id):
        # Obtener los nuevos valores
        nuevos_valores = [campo.get() for campo in self.campos.values()]
        alumno_id = self.obtener_alumno_id_por_nombre(nombre_completo)

        # Actualizar la nota en la base de datos
        filas_afectadas = self.crud_notas.actualizar_nota(
            alumno_id, materia_id, *nuevos_valores
        )
        if filas_afectadas > 0:
            messagebox.showinfo("Éxito", "Nota actualizada correctamente.")
            self.ventana_modificar.destroy()
            self.cargar_notas()
        else:
            messagebox.showerror("Error", "No se pudo actualizar la nota.")

    def obtener_alumno_id_por_nombre(self, nombre_completo):
        # Obtener el ID del alumno a partir de su nombre completo
        nombre, apellido = nombre_completo.split(" ", 1)
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT alumnoID FROM Alumnos WHERE nombre = ? AND apellido = ?",
                (nombre, apellido),
            )
            resultado = cursor.fetchone()
        return resultado[0] if resultado else None


