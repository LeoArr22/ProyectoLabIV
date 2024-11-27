import sqlite3
import os

class Conexion:
    def __init__(self):
        # Ruta a la base de datos
        self.db_path = os.path.join("data", "Curso.db")
        
    def abrir_conexion(self):
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # Activamos las restricciones de claves foráneas
        return conn    