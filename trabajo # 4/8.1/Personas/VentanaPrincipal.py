import tkinter as tk
from tkinter import messagebox
from ListaPersonas import ListaPersonas
from Persona import Persona

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Personas")

        self.lista = ListaPersonas()

        self.geometry("400x400")
        self.contenedor = tk.Frame(self)
        self.contenedor.pack(padx=10, pady=10)

        self.nombre = tk.Label(self.contenedor, text="Nombre")
        self.apellidos = tk.Label(self.contenedor, text="Apellidos")
        self.telefono = tk.Label(self.contenedor, text="Teléfono")
        self.direccion = tk.Label(self.contenedor, text="Dirección")

        self.campoNombre = tk.Entry(self.contenedor)
        self.campoApellidos = tk.Entry(self.contenedor)
        self.campoTelefono = tk.Entry(self.contenedor)
        self.campoDireccion = tk.Entry(self.contenedor)

        self.anadir = tk.Button(self.contenedor, text="Añadir", command=self.anadir_persona)
        self.eliminar = tk.Button(self.contenedor, text="Eliminar", command=self.eliminar_persona)
        self.borrarLista = tk.Button(self.contenedor, text="Borrar Lista", command=self.borrar_lista)

        self.modelo = tk.StringVar(value=[])
        self.listaNombres = tk.Listbox(self.contenedor, listvariable=self.modelo, height=10, width=50)
        self.scrollLista = tk.Scrollbar(self.contenedor, orient="vertical", command=self.listaNombres.yview)
        self.listaNombres.config(yscrollcommand=self.scrollLista.set)

        self.nombre.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.campoNombre.grid(row=0, column=1, padx=5, pady=5)
        self.apellidos.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.campoApellidos.grid(row=1, column=1, padx=5, pady=5)
        self.telefono.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.campoTelefono.grid(row=2, column=1, padx=5, pady=5)
        self.direccion.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.campoDireccion.grid(row=3, column=1, padx=5, pady=5)
        self.anadir.grid(row=4, column=0, padx=5, pady=5)
        self.eliminar.grid(row=4, column=1, padx=5, pady=5)
        self.borrarLista.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        self.listaNombres.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
        self.scrollLista.grid(row=6, column=2, sticky="ns", padx=5, pady=5)

    def anadir_persona(self):
        persona = Persona(self.campoNombre.get(), self.campoApellidos.get(), self.campoTelefono.get(), self.campoDireccion.get())
        self.lista.agregar_persona(persona)
        
        elementos = list(self.modelo.get())
        elementos.append(f"{self.campoNombre.get()} - {self.campoApellidos.get()} - {self.campoTelefono.get()} - {self.campoDireccion.get()}")
        elementos.sort()
        self.modelo.set(elementos)
        self.listaNombres.config(listvariable=self.modelo)
        
        self.campoNombre.delete(0, tk.END)
        self.campoApellidos.delete(0, tk.END)
        self.campoTelefono.delete(0, tk.END)
        self.campoDireccion.delete(0, tk.END)

    def eliminar_persona(self):
        indice = self.listaNombres.curselection()
        if indice:
            idx = indice[0]
            self.lista.eliminar_persona(idx)
            elementos = list(self.modelo.get())
            elementos.pop(idx)
            elementos.sort()
            self.modelo.set(elementos)
            self.listaNombres.config(listvariable=self.modelo)
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una persona para eliminar.")

    def borrar_lista(self):
        self.lista.borrar_lista()
        self.modelo.set(())
        self.listaNombres.config(listvariable=self.modelo)

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
