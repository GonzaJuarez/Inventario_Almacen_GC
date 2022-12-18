from .ConexionDB import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexionDB()

    sql = '''
    CREATE TABLE inventario (
        Articulo VARCHAR(100),
        Precio INTEGER,
        Precio_al_publico INTEGER,
        Porcentaje INTEGER
    );'''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = "Crear Tabla"
        mensaje = "Tabla crada correctamente"
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = "Crear Tabla"
        mensaje = "La tabla ya existe"
        messagebox.showwarning(titulo, mensaje)

def borrar_tabla():
    conexion = ConexionDB()
    sql = "DROP TABLE inventario"
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = "Eliminar Tabla"
        mensaje = "Tabla eliminada correctamente"
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = "Eliminar Tabla"
        mensaje = "La tabla no existe"
        messagebox.showerror(titulo, mensaje)

class Inventario():
    def __init__(self,articulo, precio, porcentaje, precio_al_publico):
        self.articulo = articulo
        self.precio = precio
        self.porcentaje = porcentaje
        self.precio_al_publico = precio_al_publico

    def __str__(self):
        return f"Inventario[{self.articulo}, {self.precio}, {self.porcentaje}, {self.precio_al_publico}]"

def guardar(inventario):
    conexion = ConexionDB()

    sql = f"""INSERT INTO inventario (Articulo, Precio, Precio_al_Publico, Porcentaje)
    VALUES('{inventario.articulo}', '{inventario.precio}', '{inventario.precio_al_publico}', '{inventario.porcentaje}');"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = "Crear Tabla"
        mensaje = "La tabla no existe"
        messagebox.showerror(titulo, mensaje)

def tabla ():
    conexion = ConexionDB()

    tabla_inve = []
    sql = "SELECT * FROM inventario"
    try:
        conexion.cursor.execute(sql)
        tabla_inve = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = "Crear Tabla"
        mensaje = "La tabla no existe"
        messagebox.showwarning(titulo, mensaje)

    return tabla_inve

def editar (inventario, articulo):
    conexion = ConexionDB()
    sql = f"""UPDATE inventario
    SET Articulo = '{inventario.articulo}', Precio = '{inventario.precio}',
    Precio_al_publico = '{inventario.precio_al_publico}', Porcentaje = '{inventario.porcentaje}'
    WHERE Articulo = '{articulo}'
    """
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = "Editar Registro"
        mensaje = "No se pudo editar el registro"
        messagebox.showerror(titulo, mensaje)

def eliminar(articulo):
    conexion = ConexionDB()
    sql = f"DELETE FROM inventario WHERE Articulo = '{articulo}'"
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = "Eliminar Registro"
        mensaje = "No se pudo eliminar el registro"
        messagebox.showerror(titulo, mensaje)