from clases.mision import Mision

class Fumigacion(Mision):
    def __init__(self, codigo, cliente, piloto, hectareas, tipo_fertil):
        super().__init__(codigo, cliente, piloto)
        self.hectareas = hectareas
        self.tipo = tipo_fertil
        
    def ejecutar(self):
        self.mostrar_informacion()
        print("ejecutando la mision")
        print("mision de fumigar terminada")