import sqlite3
import os

db_path = os.path.join("data", "Curso.db")

with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Alumnos (
        alumnoID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        documento TEXT NOT NULL UNIQUE,
        telefono INT NOT NULL,
        direccion TEXT NOT NULL
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
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Notas (
        alumnoID INTEGER NOT NULL,
        materiaID INTEGER NOT NULL,
        nota1 INTEGER DEFAULT NULL,
        nota2 INTEGER DEFAULT NULL,
        recuperatorio1 INTEGER DEFAULT NULL,
        recuperatorio2 INTEGER DEFAULT NULL,
        notaFinal INTEGER DEFAULT NULL,
        estado TEXT DEFAULT NULL,
        PRIMARY KEY (alumnoID, materiaID),
        FOREIGN KEY (alumnoID) REFERENCES Alumnos(alumnoID) ON DELETE CASCADE,
        FOREIGN KEY (materiaID) REFERENCES Materias(materiaID) ON DELETE CASCADE
        )
        """)

    
    #justificativo funcionara como un boolean: 1 Para SI, 0 Para NO
    cursor=cursor.execute("""
        CREATE TABLE IF NOT EXISTS Faltas (
        faltaID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
        alumnoID INTEGER NOT NULL, -- Relación con Alumnos
        fecha DATE NOT NULL,
        justificativo INTEGER NOT NULL, -- 1: Sí, 0: No
        observaciones TEXT,
        FOREIGN KEY (alumnoID) REFERENCES Alumnos(alumnoID) ON DELETE CASCADE
        )
        """)
    
    cursor=cursor.execute("""
        CREATE TABLE IF NOT EXISTS Amonestaciones (
        amonestacionID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        alumnoID INTEGER NOT NULL, -- Relación con Alumnos
        fecha DATE NOT NULL,
        motivo TEXT NOT NULL,
        cantidad INTEGER NOT NULL,
        FOREIGN KEY (alumnoID) REFERENCES Alumnos(alumnoID) ON DELETE CASCADE
        )
        """)
    
    
    
    