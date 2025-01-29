class ListaPersonas:
    def __init__(self):
        self.listaPersonas = []
    
    def agregar_persona(self, p):
        self.listaPersonas.append(p)
    
    def eliminar_persona(self, i):
        self.listaPersonas.pop(i)
    
    def borrar_lista(self):
        self.listaPersonas.clear()
