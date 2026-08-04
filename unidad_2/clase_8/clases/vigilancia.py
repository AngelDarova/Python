
from clases.mision import Mision

class Vigilancia(Mision):
    def __init__(self, codigo, cliente, piloto, zona, direccion):
        super().__init__(codigo, cliente, piloto)
        self.zona = zona
        self.direccion = direccion
        
    def ejecutar(self):
        self.mostrar_informacion()
        print("ejecutando mision de vigilancia")
        print("finalizando mision de vigilancia")