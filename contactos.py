import sqlite3

class Contactos: 
    def Abrir(self):
        conexion = sqlite3.connect('B:\\OpenBootCamp\\Python\\python_basico\\extra_01\\ejercicio02\\agenda_contacto.db')
        return conexion

    def agendado(self, datos):
        cone = self.Abrir()
        cursor = cone.cursor()
        query = 'insert into contactos (nombre, apellido, telefono) values (?, ?, ?)'
        cursor.execute(query, datos)
        cone.commit()
        cone.close()
    
    def consulta(self, datos):
        try:
            cone= self.Abrir()
            cursor = cone.cursor()
            query = 'select * from contactos where apellido =?'
            cursor.execute(query, datos)
            return cursor.fetchall()
        
        finally:
            cone.commit()
            cone.close()
    
    def agenda_completa(self):
        try:
            cone = self.Abrir()
            cursor = cone.cursor()
            query = 'select nombre, apellido, telefono from contactos'
            cursor.execute(query)
            return cursor.fetchall()
        finally:
            cone.commit()
            cone.close()