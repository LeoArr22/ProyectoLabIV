import customtkinter as ctk
from tkinter import ttk, messagebox
from data.crud.crud_materias import CrudMaterias
from models.clases.materias import Materia
from gui.util.gestion_ventanas import destruir


class VerMaterias:
    def __init__(self):
        self.crud_materias = CrudMaterias()
        self.ventana = ctk.CTk()
        self.ventana.title("Visualización de Materias")
        self.ventana.geometry("600x400")
        self.ventana.resizable(False, False)

        # Crear un frame principal
        self.frame_principal = ctk.CTkFrame(self.ventana, fg_color="#F5F5F5")
        self.frame_principal.pack(fill="both", expand=True, padx=10, pady=10)

        # Título
        self.titulo = ctk.CTkLabel(
            self.frame_principal, text="Listado de Materias",
            font=("Helvetica", 24, "bold"), text_color="#333333",
        )
        self.titulo.pack(pady=10)

        # Crear Treeview para mostrar las materias
        self.treeview = ttk.Treeview(self.frame_principal, columns=("Nombre",), show="headings", height=10)
        self.treeview.pack(fill="both", expand=True, padx=20, pady=10)

        # Definir encabezados
        for col in self.treeview["columns"]:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, anchor="center", width=200)

        # Botones para las acciones
        self.boton_cargar = ctk.CTkButton(
            self.frame_principal, text="Cargar Materias", command=self.cargar_materias
        )
        self.boton_cargar.pack(side="left", padx=10, pady=10)

        self.boton_eliminar = ctk.CTkButton(
            self.frame_principal, text="Eliminar Materia", command=self.eliminar_materia
        )
        self.boton_eliminar.pack(side="left", padx=10, pady=10)

        self.boton_modificar = ctk.CTkButton(
            self.frame_principal, text="Modificar Materia", command=self.modificar_materia
        )
        self.boton_modificar.pack(side="left", padx=10, pady=10)

        # Botón para volver atrás
        self.boton_atras = ctk.CTkButton(
            self.frame_principal, text="← Atrás", command=lambda: self.volver(self.ventana)
        )
        self.boton_atras.pack(side="right", padx=10, pady=10)

        # Mostrar la ventana
        self.ventana.mainloop()

    def volver(self, ventana_actual):
        from gui.menu_principal.menu_principal import MenuPrincipal
        destruir(ventana_actual, MenuPrincipal)

    def cargar_materias(self):
        """Carga las materias desde el CRUD y las muestra en el Treeview."""
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        # Obtener todas las materias
        materias = self.crud_materias.obtener_todas()
        for materia in materias:
            materia_id = materia[0]  # ID de la materia (suponiendo que el ID está en el índice 0)
            nombre = materia[1]  # Nombre de la materia (suponiendo que el nombre está en el índice 1)
            
            # Insertar en el treeview, donde los valores son solo los campos visibles
            self.treeview.insert("", "end", values=(nombre,), tags=(materia_id,))

    def eliminar_materia(self):
        """Elimina una materia seleccionada usando el ID."""
        seleccionado = self.treeview.focus()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione una materia para eliminar.")
            return

        confirmar = messagebox.askyesno(
            "Confirmar", "¿Está seguro de que desea eliminar esta materia?"
        )
        if not confirmar:
            return

        # Obtener el ID de la materia seleccionada
        materia_id = self.treeview.item(seleccionado, "tags")[0]

        # Eliminar la materia
        filas_afectadas = self.crud_materias.eliminar_materia(materia_id)
        if filas_afectadas > 0:
            messagebox.showinfo("Éxito", "Materia eliminada correctamente.")
            self.cargar_materias()
        else:
            messagebox.showerror("Error", "No se pudo eliminar la materia.")

    def modificar_materia(self):
        """Modifica una materia seleccionada."""
        seleccionado = self.treeview.focus()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione una materia para modificar.")
            return

        # Obtener el ID de la materia seleccionada
        materia_id = self.treeview.item(seleccionado, "tags")[0]
        
        # Obtener datos de la fila seleccionada
        datos = self.treeview.item(seleccionado, "values")
        nombre = datos[0]

        # Crear ventana emergente para editar
        ventana_edicion = ctk.CTkToplevel(self.ventana)
        ventana_edicion.title("Modificar Materia")

        # Campo para modificar el nombre
        label_nombre = ctk.CTkLabel(ventana_edicion, text="Nombre")
        label_nombre.grid(row=0, column=0, padx=10, pady=5)

        entrada_nombre = ctk.CTkEntry(ventana_edicion)
        entrada_nombre.insert(0, nombre)  # Rellenar con el valor actual
        entrada_nombre.grid(row=0, column=1, padx=10, pady=5)

        # Botón para guardar cambios
        def guardar_cambios():
            try:
                # Crear una instancia de Materia con los valores ingresados
                materia_modificada = Materia(
                    nombre=entrada_nombre.get()
                )
                print(materia_modificada.nombre)
                if not materia_modificada.es_completo():
                    raise ValueError("El nombre es obligatorio y debe tener entre 3 y 20 caracteres.")

                # Actualizar la materia
                filas_afectadas = self.crud_materias.actualizar_materia(materia_id, materia_modificada.nombre)

                if filas_afectadas > 0:
                    messagebox.showinfo("Éxito", "Materia modificada correctamente.")
                    self.cargar_materias()
                    ventana_edicion.destroy()
                else:
                    messagebox.showerror("Error", "No se pudo modificar la materia.")
            except ValueError as e:
                messagebox.showerror("Error de Validación", f"Error en los datos: {e}")
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")

        boton_guardar = ctk.CTkButton(ventana_edicion, text="Guardar Cambios", command=guardar_cambios)
        boton_guardar.grid(row=1, column=0, columnspan=2, pady=10)
