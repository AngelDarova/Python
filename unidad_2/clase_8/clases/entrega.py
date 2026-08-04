
from clases import Mision

class EntregaMedicamentos(Mision):
    def __init__(self, codigo, cliente, piloto, peso, destino):
        super().__init__(codigo, cliente, piloto)
        self.peso = peso
        self.destino = destino
        
    def ejecutar(self):
        self.mostrar_informacion()
        print("Ejecutando mision de entrega")
        print("finalizando la mision de entrega")