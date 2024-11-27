from clase_conexion import Conexion

class CrudFaltas(Conexion):
    def __init__(self):
        super().__init__() 
        
        
#CREATE: Crear falta
    def crear_falta(self, alumno_id, fecha, justificativo, observaciones):
        query = """
        INSERT INTO Faltas (alumnoID, fecha, justificativo, observaciones)
        VALUES (?, ?, ?, ?)
        """
        with self.abrir_conexion() as conn:
            cursor= conn.cursor()
            cursor.execute(query, (alumno_id, fecha, justificativo, observaciones))
            conn.commit()
            return cursor.lastrowid  #Devuelve el ID de la falta creada
        
        
#READ: Obtener todas las faltas ordenadas por campo y en orden   
    def obtener_todos_ordenados(self, campo, orden="ASC"):
        query = f"SELECT * FROM Faltas ORDER BY {campo} {orden}"
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall() #devuelve una lista de tuplas con las faltas
        
#READ: Obtener por alumno
    def obtener_por_alumno(self, alumno_id):
        query = """SELECT * FROM Faltas WHERE alumnoID = ?"""
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (alumno_id,)) #Colocamos coma para indicar que es una tupla
            return cursor.fetchall()
        
#READ: Obtener por fechas
    def obtener_por_fecha(self, fecha):
        query = """SELECT * FROM Faltas WHERE fecha = ?"""
        
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (fecha,))
            return cursor.fetchall()    
        
        
#UPDATE: Modificar una falta
    def actualizar_falta(self, alumno_id, fecha, justificativo, observaciones):
        query = """
            UPDATE Faltas
            SET fecha = COALESCE(?, fecha),
                justificativo = COALESCE(?, justificativo),
                observaciones = COALESCE(?, observaciones)
            WHERE alumnoID = ?    
                """
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (fecha, justificativo, observaciones, alumno_id))
            return cursor.lastrowid #Si devuelve 0 no encontro el registro
        
#DELETE: Eliminar una falta
    def eliminar_falta(self, falta_id):
        query = "DELETE FROM Faltas WHERE faltaID = ?"
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (falta_id,))
            conn.commit()
            return cursor.rowcount  #Devuelve el numero de fila eliminada
        
#DELETE: Eliminar a todas las faltas
    def eliminar_todas_faltas(self):
        query = "DELETE FROM Faltas"
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            return cursor.rowcount #Devuelve el numero de filas eliminadas