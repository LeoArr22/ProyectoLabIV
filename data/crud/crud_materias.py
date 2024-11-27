from clase_conexion import Conexion

class CrudMaterias(Conexion):
    def __init__(self):
        super().__init__()
        
#CREATE: Crear una materia
    def crear_materia(self, nombre):
        query = """
            INSERT INTO Materias(nombre)
            VALUES (?)
        """
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (nombre,))
            conn.commit()
            return cursor.lastrowid #Devuelve el ID de la materia
        
        
#READ: Todas las materias
    def obtener_todas(self):
        query = "SELECT * FROM Materias"
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()


#UPDATE: Modificar una materia
    def actualizar_materia(self, materia_id, nombre):
        query = """
            UPDATE Materias
            SET nombre = COALESCE(?, nombre)
            WHERE materiaID = ?
        """
        
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query, materia_id, nombre)
            conn.commit()
            return cursor.rowcount
        
        
#DELETE: Eliminar una materia
    def eliminar_materia(self, materia_id):
        query = """DELETE FROM Materias WHERE materiaID = ?
        """
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (materia_id,))
            conn.commit()
            return cursor.rowcount
        
#DELETE: Eliminar a todos las materias
    def elimnar_todas_materias(self):
        query = "DELETE FROM Materias"
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            return cursor.rowcount #Devuelve el numero de filas eliminadas        
        
    