import sqlite3
import os

class CrudAlumnos:
    def __init__(self, db_path=None):
        # Ruta a la base de datos
        self.db_path = db_path or os.path.join("data", "Curso.db")
    
    
#CREATE:
    def crear_alumno(self, nombre, apellido, documento, telefono, direccion=None):
        query = """
            INSERT INTO Alumnos (nombre, apellido, documento, telefono, direccion)
            VALUES (?, ?, ?, ?, ?)
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, (nombre, apellido, documento, telefono, direccion))
            conn.commit()
            return cursor.lastrowid  # Devuelve el ID del alumno creado

#READ: todos los alumnos
    def obtener_todos(self):
        query = "SELECT * FROM Alumnos"
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()  # Devuelve una lista de tuplas con los alumnos

    # READ: Obtener un alumno por ID
    def obtener_por_id(self, alumno_id):
        query = "SELECT * FROM Alumnos WHERE alumnoID = ?"
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, (alumno_id,))
            return cursor.fetchone()  # Devuelve una tupla con los datos del alumno o None

    # UPDATE: Modificar un alumno
    def actualizar_alumno(self, alumno_id, nombre=None, apellido=None, documento=None, telefono=None, direccion=None):
        query = """
            UPDATE Alumnos
            SET nombre = COALESCE(?, nombre),
                apellido = COALESCE(?, apellido),
                documento = COALESCE(?, documento),
                telefono = COALESCE(?, telefono),
                direccion = COALESCE(?, direccion)
            WHERE alumnoID = ?
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, (nombre, apellido, documento, telefono, direccion, alumno_id))
            conn.commit()
            return cursor.rowcount  # Devuelve el número de filas actualizadas

    # DELETE: Eliminar un alumno
    def eliminar_alumno(self, alumno_id):
        query = "DELETE FROM Alumnos WHERE alumnoID = ?"
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, (alumno_id,))
            conn.commit()
            return cursor.rowcount  # Devuelve el número de filas eliminadas

nuevo=CrudAlumnos()
nuevo.crear_alumno("Leo", "Arr", 38609203, 1122334455, "Sanabria")