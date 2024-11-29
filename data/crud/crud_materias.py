from data.crud.clase_conexion import Conexion

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

#READ: Busca por ID
    def obtener_por_id(self, materia_id):
        """
        Obtiene el nombre de la materia a partir del ID.
        """
        query = f"SELECT nombre FROM Materias WHERE materiaID = {materia_id}"
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            resultado = cursor.fetchone()
            return resultado[0] if resultado else None
        
    
    def obtener_materia_por_nombre(self, nombre):
        query = "SELECT materiaID FROM Materias WHERE nombre = ?"
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (nombre,))
            return cursor.fetchone()


#UPDATE: Modificar una materia
    def actualizar_materia(self, materia_id, nombre):
        query = """
            UPDATE Materias
            SET nombre = COALESCE(?, nombre)
            WHERE materiaID = ?
        """
        
        with self.abrir_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (nombre, materia_id))
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
        


crud_materias = CrudMaterias()
materias = crud_materias.obtener_todas()

if materias:
    print("Materias obtenidas:")
    for materia in materias:
        print(materia)
else:
    print("No se encontraron materias.")