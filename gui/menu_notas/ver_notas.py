import customtkinter as ctk
from tkinter import ttk, messagebox
from data.crud.crud_notas import CrudNotas
from data.crud.crud_alumnos import CrudAlumnos
from data.crud.crud_materias import CrudMaterias
from models.clases.notas import Nota
from gui.util.gestion_ventanas import destruir


class MenuNotas:
    def __init__(self):
        self.crud_notas = CrudNotas()
        self.crud_alumnos = CrudAlumnos()
        self.crud_materias = CrudMaterias()
        self.ventana = ctk.CTk()
        self.ventana.title("Visualización de Notas")
        self.ventana.geometry("1200x700")
        self.ventana.resizable(False, False)

        # Crear un frame principal
        self.frame_principal = ctk.CTkFrame(self.ventana, fg_color="#F5F5F5")
        self.frame_principal.pack(fill="both", expand=True, padx=10, pady=10)

        # Título
        self.titulo = ctk.CTkLabel(
            self.frame_principal, text="Listado de Notas",
            font=("Helvetica", 24, "bold"), text_color="#333333",
        )
        self.titulo.pack(pady=10)

        # Crear Treeview para mostrar las notas
        self.treeview = ttk.Treeview(self.frame_principal, columns=(
            "Nombre Completo", "DNI", "Materia ID", "Nota 1", "Nota 2",
            "Recuperatorio 1", "Recuperatorio 2", "Nota Final", "Estado"
        ), show="headings", height=20)
        self.treeview.pack(fill="both", expand=True, padx=20, pady=10)

        # Definir encabezados
        for col in self.treeview["columns"]:
            self.treeview.heading(col, text=col)
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

        # Botón para volver atrás
        self.boton_atras = ctk.CTkButton(
            self.frame_principal, text="← Atrás", command=lambda: self.volver(self.ventana))
        
        self.boton_atras.pack(side="right", padx=10, pady=10)

        # Mostrar la ventana
        self.ventana.mainloop()

    def volver(self, ventana_actual):
        from gui.menu_principal.menu_principal import MenuPrincipal
        destruir(ventana_actual, MenuPrincipal)

    def cargar_notas(self):
        """Carga las notas desde el CRUD, mostrando el nombre de la materia en lugar del ID."""
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        # Este método debe unirse con la tabla de materias para incluir el nombre de la materia
        notas = self.crud_notas.obtener_notas_con_alumno_y_materia()
        for nota in notas:
            self.treeview.insert("", "end", values=nota)

    def eliminar_nota(self):
        """Elimina una nota seleccionada usando el DNI."""
        seleccionado = self.treeview.focus()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione una nota para eliminar.")
            return

        confirmar = messagebox.askyesno(
            "Confirmar", "¿Está seguro de que desea eliminar esta nota?"
        )
        if not confirmar:
            return

        datos = self.treeview.item(seleccionado, "values")
        dni, nombre_materia = datos[1], datos[2]

        alumno = self.crud_alumnos.obtener_por_documento(dni)
        if alumno is None:
            messagebox.showerror("Error", "No se encontró el alumno.")
            return

        alumno_id = alumno[0]
        materia = self.crud_materias.obtener_materia_por_nombre(nombre_materia)
        if materia is None:
            messagebox.showerror("Error", "No se encontró la materia.")
            return

        materia_id = materia[0]
        filas_afectadas = self.crud_notas.eliminar_nota(alumno_id, materia_id)
        if filas_afectadas > 0:
            messagebox.showinfo("Éxito", "Nota eliminada correctamente.")
            self.cargar_notas()
        else:
            messagebox.showerror("Error", "No se pudo eliminar la nota.")

    def _convertir_a_int(self, valor):
        """Convierte un valor a entero, permitiendo valores None."""
        valor = valor.strip() if valor else ""
        if valor == "" or valor == "None":
            return None
        try:
            return int(valor)
        except ValueError:
            raise ValueError(f"El valor '{valor}' no es un número entero válido.")

    def modificar_nota(self):
        """Modifica una nota seleccionada."""
        seleccionado = self.treeview.focus()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione una nota para modificar.")
            return

        datos = self.treeview.item(seleccionado, "values")
        nombre_completo, dni, materia_id, nota1, nota2, rec1, rec2, nota_final, estado = datos
        alumno = self.crud_alumnos.obtener_por_documento(dni)
        if alumno is None:
            messagebox.showerror("Error", "No se encontró el alumno.")
            return

        alumno_id = alumno[0]
        materia = self.crud_materias.obtener_materia_por_nombre(materia_id)
        if materia is None:
            messagebox.showerror("Error", "No se encontró la materia.")
            return

        materia_id = materia[0]
        ventana_edicion = ctk.CTkToplevel(self.ventana)
        ventana_edicion.title("Modificar Nota")
        campos = {
            "Nota 1": nota1,
            "Nota 2": nota2,
            "Recuperatorio 1": rec1,
            "Recuperatorio 2": rec2,
            "Nota Final": nota_final,
            "Estado": estado,
        }
        entradas = {}
        for idx, (campo, valor) in enumerate(campos.items()):
            label = ctk.CTkLabel(ventana_edicion, text=campo)
            label.grid(row=idx, column=0, padx=10, pady=5)
            entrada = ctk.CTkEntry(ventana_edicion)
            entrada.insert(0, valor)
            entrada.grid(row=idx, column=1, padx=10, pady=5)
            entradas[campo] = entrada

        def guardar_cambios():
            try:
                nueva_nota = Nota(
                    nota1=self._convertir_a_int(entradas["Nota 1"].get()),
                    nota2=self._convertir_a_int(entradas["Nota 2"].get()),
                    recuperatorio1=self._convertir_a_int(entradas["Recuperatorio 1"].get()),
                    recuperatorio2=self._convertir_a_int(entradas["Recuperatorio 2"].get()),
                    nota_final=self._convertir_a_int(entradas["Nota Final"].get()),
                    estado=entradas["Estado"].get().strip() or None
                )
                filas_afectadas = self.crud_notas.actualizar_nota(
                    alumno_id, materia_id,
                    nueva_nota.nota1, nueva_nota.nota2,
                    nueva_nota.recuperatorio1, nueva_nota.recuperatorio2,
                    nueva_nota.nota_final, nueva_nota.estado
                )
                if filas_afectadas > 0:
                    messagebox.showinfo("Éxito", "Nota modificada correctamente.")
                    self.cargar_notas()
                    ventana_edicion.destroy()
                else:
                    messagebox.showerror("Error", "No se pudo modificar la nota.")
            except ValueError as e:
                messagebox.showerror("Error de Validación", f"Error en los datos: {e}")
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")

        boton_guardar = ctk.CTkButton(ventana_edicion, text="Guardar Cambios", command=guardar_cambios)
        boton_guardar.grid(row=len(campos), column=0, columnspan=2, pady=10)
