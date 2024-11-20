import sqlite3
import os

db_path = os.path.join("data", "Curso.db")

with sqlite3.connect(db_path) as conexion:
    cursor = conexion.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Alumnos (
        alumnoID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        documento TEXT NOT NULL,
        telefono INT NOT NULL,
        direccion TEXT
        )
        """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Materias (
        materiaID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nombre TEXT NOT NULL    
        )
        """)
    
    #Usamos una clve primaria compuesta para evitar registros duplicados para el par de ID alumno y materia
    #Luego indicamos que son claves foraneas haciendo referencia a los ID de alumno y materia
    #Ademas agregamos que se eliminen en cascada en caso de eliminar un alumno o materia
    cursor=cursor.execute("""
        CREATE TABLE IF NOT EXISTS Notas (
        alumnoID INTEGER NOT NULL,
        materiaID INTEGER NOT NULL,
        nota1 REAL NOT NULL,
        nota2 REAL NOT NULL,
        recuperatorio1 REAL,
        recuperatorio2 REAL,
        notaFinal REAL,
        estado TEXT NOT NULL,
        PRIMARY KEY (alumnoID, materiaID),
        FOREIGN KEY (alumnoID) REFERENCES Alumnos(ID) ON DELETE CASCADE,
        FOREIGN KEY (materiaID) REFERENCES Materias(ID) ON DELETE CASCADE
        )
        """)
    
    #justificativo funcionara como un boolean: 1 Para SI, 0 Para NO
    cursor=cursor.execute("""
        CREATE TABLE IF NOT EXISTS Faltas(
        faltaID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
        fecha DATE NOT NULL,
        justificativo INTEGER NOT NULL,
        observaciones TEXT
        )
        """)
    
    cursor=cursor.execute("""
        CREATE TABLE IF NOT EXISTS Amonestaciones(
        amonestacionesID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        fecha DATE NOT NULL,
        motivo TEXT NOT NULL,
        cantidad INTEGER NOT NULL    
        )
        """)
    
    
    