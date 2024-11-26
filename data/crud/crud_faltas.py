import sqlite3
import os

class CrudFaltas:
    def __init__(self):
        # Ruta a la base de datos
        self.db_path = os.path.join("data", "Curso.db")
        
#CREATE: Crear falta
    def crear_falta(self, alumno_id, fecha, justificativo, observaciones):
        query = """
        INSERT INTO Faltas (alumnoID, fecha, justificativo, observaciones)
        VALUES (?, ?, ?, ?)
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor= conn.cursor()
            cursor.execute(query, (alumno_id, fecha, justificativo, observaciones))
            conn.commit()
            return cursor.lastrowid  #Devuelve el ID de la falta creada
        
#READ: Obtener todas las faltas        
    def obtener_todos(self):
        query = "SELECT * FROM Faltas"
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall #devuelve una lista de tuplas con las faltas
        
#READ: Obtener por alumno
    def obtener_por_alumno(self, alumno_id):
        query = """SELECT * FROM Faltas WHERE alumnoID = ?"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, (alumno_id,)) #Colocamos coma para indicar que es una tupla
            return cursor.fetchall()
        
#UPDATE: Modificar faltas
                