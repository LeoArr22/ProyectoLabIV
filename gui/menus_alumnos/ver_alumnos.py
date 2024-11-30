import customtkinter as ctk
from tkinter import ttk, messagebox
from data.crud.crud_alumnos import CrudAlumnos
from models.clases.alumnos import Alumno
from gui.util.gestion_ventanas import destruir


class VerAlumnos:
    def __init__(self):
        self.crud_alumnos = CrudAlumnos()
        self.ventana = ctk.CTk()
        self.ventana.title("Visualización de Alumnos")
        self.ventana.geometry("1200x700")
        self.ventana.resizable(False, False)

        # Crear un frame principal
        self.frame_principal = ctk.CTkFrame(self.ventana, fg_color="#F5F5F5")
        self.frame_principal.pack(fill="both", expand=True, padx=10, pady=10)

        # Título
        self.titulo = ctk.CTkLabel(
            self.frame_principal, text="Listado de Alumnos",
            font=("Helvetica", 24, "bold"), text_color="#333333",
        )
        self.titulo.pack(pady=10)

        # Crear Treeview para mostrar los alumnos
        self.treeview = ttk.Treeview(self.frame_principal, columns=(
            "Nombre", "Apellido", "DNI", "Teléfono", "Dirección"
        ), show="headings", height=20)
        self.treeview.pack(fill="both", expand=True, padx=20, pady=10)

        # Definir encabezados
        for col in self.treeview["columns"]:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, anchor="center", width=120)

        # Botones para las acciones
        self.boton_cargar = ctk.CTkButton(
            self.frame_principal, text="Cargar Alumnos", command=self.cargar_alumnos
        )
        self.boton_cargar.pack(side="left", padx=10, pady=10)

        self.boton_eliminar = ctk.CTkButton(
            self.frame_principal, text="Eliminar Alumno", command=self.eliminar_alumno
        )
        self.boton_eliminar.pack(side="left", padx=10, pady=10)

        self.boton_modificar = ctk.CTkButton(
            self.frame_principal, text="Modificar Alumno", command=self.modificar_alumno
        )
        self.boton_modificar.pack(side="left", padx=10, pady=10)

        # Botón para volver atrás
        self.boton_atras = ctk.CTkButton(
            self.frame_principal, text="← Atrás", command=lambda: self.volver(self.ventana))
        
        self.boton_atras.pack(side="right", padx=10, pady=10)

        # Mostrar la ventana
        self.ventana.mainloop()

    def volver(self, ventana_actual):
        from gui.menu_principal.menu_principal import MenuPrincipal
        destruir(ventana_actual, MenuPrincipal)

    def cargar_alumnos(self):
        """Carga los alumnos desde el CRUD."""
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        # Obtener todos los alumnos
        alumnos = self.crud_alumnos.obtener_todos_ordenados()
        for alumno in alumnos:
            # Insertar nombre y apellido por separado
            nombre, apellido = alumno[1], alumno[2]  # Suponiendo que el nombre está en el índice 1 y el apellido en el índice 2
            self.treeview.insert("", "end", values=(nombre, apellido, alumno[3], alumno[4], alumno[5]))

    def eliminar_alumno(self):
        """Elimina un alumno seleccionado usando el DNI."""
        seleccionado = self.treeview.focus()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un alumno para eliminar.")
            return

        confirmar = messagebox.askyesno(
            "Confirmar", "¿Está seguro de que desea eliminar este alumno?"
        )
        if not confirmar:
            return

        datos = self.treeview.item(seleccionado, "values")
        dni = datos[2]  # Documento (DNI) del alumno

        # Obtener alumno por documento
        alumno = self.crud_alumnos.obtener_por_documento(dni)
        if alumno is None:
            messagebox.showerror("Error", "No se encontró el alumno.")
            return

        alumno_id = alumno[0]

        # Eliminar alumno
        filas_afectadas = self.crud_alumnos.eliminar_alumno(alumno_id)
        if filas_afectadas > 0:
            messagebox.showinfo("Éxito", "Alumno eliminado correctamente.")
            self.cargar_alumnos()
        else:
            messagebox.showerror("Error", "No se pudo eliminar el alumno.")

    def modificar_alumno(self):
        """Modifica un alumno seleccionado."""
        seleccionado = self.treeview.focus()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un alumno para modificar.")
            return

        # Obtener datos de la fila seleccionada
        datos = self.treeview.item(seleccionado, "values")
        nombre, apellido, dni, telefono, direccion = datos

        # Obtener alumno por DNI
        alumno = self.crud_alumnos.obtener_por_documento(dni)
        if alumno is None:
            messagebox.showerror("Error", "No se encontró el alumno.")
            return

        alumno_id = alumno[0]

        # Crear ventana emergente para editar
        ventana_edicion = ctk.CTkToplevel(self.ventana)
        ventana_edicion.title("Modificar Alumno")

        # Campos para modificar
        campos = {
            "Nombre": nombre,
            "Apellido": apellido,
            "DNI": dni,
            "Teléfono": telefono,
            "Dirección": direccion,
        }
        entradas = {}

        # Crear entradas para cada campo
        for idx, (campo, valor) in enumerate(campos.items()):
            label = ctk.CTkLabel(ventana_edicion, text=campo)
            label.grid(row=idx, column=0, padx=10, pady=5)

            entrada = ctk.CTkEntry(ventana_edicion)
            entrada.insert(0, valor)  # Rellenar con el valor actual
            entrada.grid(row=idx, column=1, padx=10, pady=5)
            entradas[campo] = entrada

        # Botón para guardar cambios
        def guardar_cambios():
            
            try:
            
                # Crear una instancia de Alumno con los valores ingresados
                alumno_modificado = Alumno(
                    nombre=entradas["Nombre"].get(),
                    apellido=entradas["Apellido"].get(),
                    documento=(entradas["DNI"].get()),
                    telefono=(entradas["Teléfono"].get()),
                    direccion=entradas["Dirección"].get()
                )

                # Validar los datos al instanciar la clase `Alumno`
                filas_afectadas = self.crud_alumnos.actualizar_alumno(
                    alumno_id,
                    alumno_modificado.nombre, alumno_modificado.apellido,
                    alumno_modificado.documento, alumno_modificado.telefono,
                    alumno_modificado.direccion
                )

                if filas_afectadas > 0:
                    messagebox.showinfo("Éxito", "Alumno modificado correctamente.")
                    self.cargar_alumnos()
                    ventana_edicion.destroy()
                else:
                    messagebox.showerror("Error", "No se pudo modificar el alumno.")
            except ValueError as e:
                messagebox.showerror("Error de Validación", f"Error en los datos: {e}")
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")

        boton_guardar = ctk.CTkButton(ventana_edicion, text="Guardar Cambios", command=guardar_cambios)
        boton_guardar.grid(row=len(campos), column=0, columnspan=2, pady=10)


