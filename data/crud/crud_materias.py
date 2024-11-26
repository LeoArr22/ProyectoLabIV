import sqlite3
import os

class CrudMaterias:
    def __init__(self):
        # Ruta a la base de datos
        self.db_path = os.path.join("data", "Curso.db")
        
        
#CREATE: Crear una materia
    def crear_materia(self, nombre):
        query = """
            INSERT INTO Materias(nombre)
            VALUES (?)
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, (nombre,))
            conn.commit()
            return cursor.lastrowid #Devuelve el ID de la materia
        
        
#READ: Todas las materias
    def obtener_todas(self):
        query = "SELECT * FROM Materias"
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()


#UPDATE: Modificar una materia
    def actualizar_materia(self, materia_id, nombre):
        query = """
            UPDATE Materia
            SET nombre = COALESCE(?, nombre)
            WHERE materiaID = ?
        """
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, materia_id, nombre)
            conn.commit()
            return cursor.rowcount
        
        
#DELETE: Eliminar una materia
    def eliminar_materia(self, materia_id):
        query = """DETELE FROM Materias WHERE materiaID = ?
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, (materia_id,))
            conn.commit
            return cursor.rowcount
        
    