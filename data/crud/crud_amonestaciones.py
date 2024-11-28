from clase_conexion import Conexion

class CrudAmonestaciones(Conexion):
    def __init__(self):
        super().__init__() 
    
#CREATE: Crear una amonestacion
    def crear_amonestacion(self, alumno_id, fecha, motivo, cantidad):
        query = """
            INSERT INTO Amonestaciones (alumnoID, fecha, motivo, cantidad)
            VALUES (?, ?, ?, ?)
        """
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (alumno_id, fecha, motivo, cantidad))
            conn.commit()
            return cursor.lastrowid  #Devuelve el ID del alumno creado

#READ: todas las amonestaciones
    def obtener_todos_ordenados(self, campo, orden="ASC"): #Mediante desplegables enviamos campo y orden
        query = f"SELECT * FROM Amonestaciones ORDER BY {campo} {orden}"
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()  #devuelve una lista de tuplas con los alumnos

#READ: Obtener por alumno
    def obtener_por_alumno(self, alumno_id):
        query = """SELECT * FROM Amonestaciones WHERE alumnoID = ?"""
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (alumno_id,)) #Colocamos coma para indicar que es una tupla
            return cursor.fetchall()
        
#READ: Obtener por fechas
    def obtener_por_fecha(self, fecha):
        query = """SELECT * FROM Amonestaciones WHERE fecha = ?"""
        
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (fecha,))
            return cursor.fetchall()    
        
        
#UPDATE: Modificar una falta
    def actualizar_amonestacion(self, alumno_id, fecha, motivo, cantidad):
        query = """
            UPDATE Amonestacion
            SET fecha = COALESCE(?, fecha),
                motivo = COALESCE(?, motivo),
                cantidad = COALESCE(?, cantidad)
            WHERE alumnoID = ?    
                """
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (fecha, motivo, cantidad, alumno_id))
            return cursor.lastrowid #Si devuelve 0 no encontro el registro
        
#DELETE: Eliminar una falta
    def eliminar_amonestacion(self, amonestacion_id):
        query = "DELETE FROM Amonestaciones WHERE amonestacionID = ?"
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (amonestacion_id,))
            conn.commit()
            return cursor.rowcount  #Devuelve el numero de fila eliminada
        
#DELETE: Eliminar  todas las amonestaciones
    def eliminar_todas_amonestaciones(self):
        query = "DELETE FROM Amonestaciones"
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            return cursor.rowcount #Devuelve el numero de filas eliminadas