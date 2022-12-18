import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Model.Inventario_dao import crear_tabla, borrar_tabla, Inventario, guardar, tabla, editar, eliminar

class Frame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.pack()
        self.config(width=500, height=500)

        self.articulo = ""

        self.Labels()
        self.Entry()
        self.Bottons()
        self.Tabla()

        self.habilitar_campos()
        self.deshabilitar_campos()

    def Labels(self):
        ##Texto de orientacion para las entradas##
        self.label_Articulos = tk.Label(self, text = "Articulos: ")
        self.label_Articulos.config(font=("Arial", 12, "bold"))
        self.label_Articulos.grid(row=0, column=0, padx=10, pady=5)

        self.label_Precio = tk.Label(self, text="Precio: ")
        self.label_Precio.config(font=("Arial", 12, "bold"))
        self.label_Precio.grid(row=1, column=0, padx=10, pady=5)

        self.label_Porcentaje = tk.Label(self, text="Porcentaje: ")
        self.label_Porcentaje.config(font=("Arial", 12, "bold"))
        self.label_Porcentaje.grid(row=3, column=0, padx=10, pady=5)

    def Entry(self):
        ##Entradas de datos##
        self.mi_Articulo = tk.StringVar()
        self.entry_Articulos = tk.Entry(self, textvariable=self.mi_Articulo)
        self.entry_Articulos.config(width=50, font=("Arial", 12), state="disabled")
        self.entry_Articulos.grid(row=0, column=1, padx=10, pady=5, columnspan=2)

        self.mi_Precio = tk.IntVar()
        self.entry_Precio = tk.Entry(self, textvariable=self.mi_Precio)
        self.entry_Precio.config(width=50, font=("Arial", 12), state="disabled")
        self.entry_Precio.grid(row=1, column=1, padx=10, pady=5, columnspan=2)

        self.mi_Porcentaje = tk.IntVar()
        self.entry_Porcentaje = tk.Entry(self, textvariable=self.mi_Porcentaje)
        self.entry_Porcentaje.config(width=50, font=("Arial", 12), state="disabled")
        self.entry_Porcentaje.grid(row=3, column=1, padx=10, pady=5, columnspan=2)

    def Bottons(self):
        ##Botones##
        color = "#146EDA"
        self.button_Agregar = tk.Button(self, text="Agregar", command=self.habilitar_campos)
        self.button_Agregar.config(width=20, cursor="hand2", bg=color, activebackground=color, font=("Arial", 12, "bold"))
        self.button_Agregar.grid(row=5, column=0, padx=10, pady=5)

        self.button_Guardar = tk.Button(self, text="Guardar", command=self.guardar_datos)
        self.button_Guardar.config(width=20, cursor="hand2", bg="#0C5AB8", activebackground="#146EDA", font=("Arial", 12, "bold"), state="disabled")
        self.button_Guardar.grid(row=5, column=1, padx=10, pady=5)

        self.button_Cancelar = tk.Button(self, text="Cancelar", command=self.deshabilitar_campos)
        self.button_Cancelar.config(width=20, cursor="hand2", bg="#0C5AB8", activebackground="#146EDA", font=("Arial", 12, "bold"), state="disabled")
        self.button_Cancelar.grid(row=5, column=2, padx=10, pady=5)

        self.button_Editar = tk.Button(self, text="Editar", command=self.editar_datos)
        self.button_Editar.config(width=20, cursor="hand2", bg="#0C5AB8", activebackground="#146EDA", font=("Arial", 12, "bold"))
        self.button_Editar.grid(row=7, column=0, padx=10, pady=5)

        self.button_Eliminar = tk.Button(self, text="Eliminar", command=self.eliminar_datos)
        self.button_Eliminar.config(width=20, cursor="hand2", bg="#0C5AB8", activebackground="#146EDA", font=("Arial", 12, "bold"))
        self.button_Eliminar.grid(row=7, column=1, padx=10, pady=5)

    def habilitar_campos(self):
        self.entry_Articulos.config(state="normal")
        self.entry_Precio.config(state="normal")
        self.entry_Porcentaje.config(state="normal")

        self.button_Guardar.config(state="normal")
        self.button_Cancelar.config(state="normal")

        self.mi_Articulo.set("")
        self.mi_Precio.set(0)
        self.mi_Porcentaje.set(0)

    def deshabilitar_campos(self):
        self.articulo = ""
        self.entry_Articulos.config(state="disabled")
        self.entry_Precio.config(state="disabled")
        self.entry_Porcentaje.config(state="disabled")

        self.button_Guardar.config(state="disabled")
        self.button_Cancelar.config(state="disabled")

        self.mi_Articulo.set("")
        self.mi_Precio.set(0)
        self.mi_Porcentaje.set(0)

    def guardar_datos(self):
        Precio_al_Publico = round(((self.mi_Precio.get() * self.mi_Porcentaje.get()) / 100) + self.mi_Precio.get())
        inve = Inventario(self.mi_Articulo.get(), self.mi_Precio.get(), self.mi_Porcentaje.get(), Precio_al_Publico)

        if self.articulo == "":
            guardar(inve)
        else:
            editar(inve, self.articulo)

        self. Tabla()
        self.deshabilitar_campos()

    def Tabla(self):
        self.tabla_inve = tabla()
        self.tabla_inve.reverse()
        self.tabla = ttk.Treeview(self, columns=("Articulo", "Precio", "Porcentaje", "Precio al Publico"))
        self.tabla.grid(row=6, column=0, columnspan=3, sticky="nse")
        self.tabla.heading("#0", text="Articulo")
        self.tabla.heading("#1", text="Precio")
        self.tabla.heading("#2", text="Precio al Publico")
        self.tabla.heading("#3", text="Porcentaje")

        for p in self.tabla_inve:
            self.tabla.insert("", 0, text=p[0], values=(p[1], p[2], p[3]))

        self.scroll = ttk.Scrollbar(self, orient="vertical", command=self.tabla.yview)
        self.scroll.grid(row=6 , column=4, sticky="nse")
        self.tabla.configure(yscrollcommand=self.scroll.set)

    def editar_datos(self):
        try:
            self.articulo = self.tabla.item(self.tabla.selection())['text']
            self.precio = self.tabla.item(self.tabla.selection())['values'][0]
            self.porcentaje = self.tabla.item(self.tabla.selection())['values'][2]
            
            self.habilitar_campos()

            self.entry_Articulos.insert(0, self.articulo)
            self.entry_Precio.insert(0, self.precio)
            self.entry_Porcentaje.insert(0, self.porcentaje)
        except:
            titulo = "Editar Registro"
            mensaje = "No seleccionaste ningun registro"
            messagebox.showerror(titulo, mensaje)

    def eliminar_datos(self):
        try:
            self.articulo = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.articulo)
            self.Tabla()
            self.articulo = ""
        except:
            titulo = "Eliminar Registro"
            mensaje = "No seleccionaste ningun registro"
            messagebox.showerror(titulo, mensaje)        

def Top_Menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    MenuInicio = tk.Menu(barra_menu, tearoff=0)
    MenuConfig = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Inicio", menu=MenuInicio)
    barra_menu.add_cascade(label="Configuracion", menu=MenuConfig)
    barra_menu.add_cascade(label="Ayuda")

    MenuInicio.add_command(label="Crear Tabla", command=crear_tabla)
    MenuInicio.add_command(label="Eliminar Tabla", command=borrar_tabla)
    MenuInicio.add_command(label="Salir", command=root.destroy)

    MenuConfig.add_command(label="Color")