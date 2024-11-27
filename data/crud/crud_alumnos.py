from clase_conexion import Conexion

class CrudAlumnos(Conexion):
    def __init__(self):
        super().__init__() 
    
#CREATE: Crear un alumno
    def crear_alumno(self, nombre, apellido, documento, telefono, direccion):
        query = """
            INSERT INTO Alumnos (nombre, apellido, documento, telefono, direccion)
            VALUES (?, ?, ?, ?, ?)
        """
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (nombre, apellido, documento, telefono, direccion))
            conn.commit()
            return cursor.lastrowid  #Devuelve el ID del alumno creado

#READ: todos los alumnos
    def obtener_todos(self, campo="nombre", orden="ASC"): #Mediante desplegables enviamos campo y orden
        query = f"SELECT * FROM Alumnos ORDER BY {campo} {orden}"
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()  #devuelve una lista de tuplas con los alumnos

#READ: Obtener un alumno por ID
    def obtener_por_id(self, alumno_id):
        query = "SELECT * FROM Alumnos WHERE alumnoID = ?"
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (alumno_id,))
            return cursor.fetchone()  #devuelve una tupla con los datos del alumno o None
        
#READ: Obtener un alumno por documento
    def obtener_por_documento(self, documento):
        query = "SELECT * FROM Alumnos WHERE documento = ?"
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (documento,)) #cursor espera una lista o una tupla. Como solo estamos pasando
                                    #un unico atributo debemos colocar una coma para que python entienda que se trata de una tupla
            return cursor.fetchone()
            
#UPDATE: Modificar un alumno
    def actualizar_alumno(self, alumno_id, nombre, apellido, documento, telefono, direccion):
        query = """
            UPDATE Alumnos
            SET nombre = COALESCE(?, nombre),
                apellido = COALESCE(?, apellido),
                documento = COALESCE(?, documento),
                telefono = COALESCE(?, telefono),
                direccion = COALESCE(?, direccion)
            WHERE alumnoID = ?
        """
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (nombre, apellido, documento, telefono, direccion, alumno_id))
            conn.commit()
            return cursor.rowcount  #Devuelve el numero de filas actualizadas

#DELETE: Eliminar un alumno
    def eliminar_alumno(self, alumno_id):
        query = "DELETE FROM Alumnos WHERE alumnoID = ?"
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (alumno_id,))
            conn.commit()
            return cursor.rowcount  #Devuelve el numero de filas eliminadas
        
#DELETE: Eliminar a todos los alumnos
    def eliminar_todos_alumnos(self):
        query = "DELETE FROM Alumnos"
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            return cursor.rowcount #Devuelve el numero de filas eliminadas