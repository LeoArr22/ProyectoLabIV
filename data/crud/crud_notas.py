from data.crud.clase_conexion import Conexion

class CrudNotas(Conexion):
    def __init__(self):
        super().__init__()
    
#CREATE: Crear nota    
    def crear_nota(self, alumno_id, materia_id, nota1, nota2, 
                   recuperatorio1, recuperatorio2, notaFinal, estado):
        query = """
            INSERT INTO Notas (alumnoID, materiaID, nota1, nota2,
            recuperatorio1, recuperatorio2, notaFinal, estado)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (alumno_id, materia_id, nota1, nota2,
                                   recuperatorio1, recuperatorio2, notaFinal, estado))
            conn.commit()
            return cursor.lastrowid #Devuelve el ID de la nota creada
    
    
#READ: Obtener todas las notas ordenadas por campo y en orden   
    def obtener_todos_ordenados(self, campo, orden="ASC"):
        query = f"SELECT * FROM Notas ORDER BY {campo} {orden}"
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall() #devuelve una lista de tuplas con las notas
        
#READ: Obtener por alumno
    def obtener_por_alumno(self, alumno_id):
        query = """SELECT * FROM Notas WHERE alumnoID = ?"""
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (alumno_id,)) #Colocamos coma para indicar que es una tupla
            return cursor.fetchall()
        
#READ: Obtener por materia
    def obtener_por_materia(self, materia_id):
        query = """SELECT * FROM Notas WHERE materiaID = ?"""
        
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (materia_id,))
            return cursor.fetchall()          
        
        
#UPDATE: Modificar una nota
    def actualizar_nota(self, alumno_id, materia_id, nota1, nota2, 
                   recuperatorio1, recuperatorio2, notaFinal, estado):
        query = """
            UPDATE Notas
            SET nota1 = COALESCE(?, nota1),
                nota2 = COALESCE(?, nota2),
                recuperatorio1 = COALESCE(?, recuperatorio1),
                recuperatorio2 = COALESCE(?, recuperatorio2),
                notaFinal = COALESCE(?, notaFinal),
                estado = COALESCE(?, estado)
            WHERE alumnoID = ? AND materiaID = ?   
                """
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (nota1, nota2, recuperatorio1, recuperatorio2,
                                   notaFinal, estado, alumno_id, materia_id))
            return cursor.rowcount #Si devuelve 0 no encontro el registro
        
        
#DELETE: Eliminar una nota
    def eliminar_nota(self, alumno_id, materia_id):
        query = "DELETE FROM Notas WHERE alumnoID = ? AND materiaID = ?"
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (alumno_id, materia_id))
            conn.commit()
            return cursor.rowcount  #Devuelve el numero de fila eliminada, si devuelve 0 no habia registro
        
#DELETE: Eliminar a todas las nota
    def eliminar_todas_notas(self):
        query = "DELETE FROM Notas"
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            return cursor.rowcount #Devuelve el numero de filas eliminadas        