class Video:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.ator = autor
        
class Short(Video):
    def __init__(self, titulo, autor,  duracion, imagen):
        super().__init__(titulo, autor, duracion)
        self.imagen = imagen

class Largo(Video):
    def __init__(self, titulo, autor, duracion, likes):
        super().__init__(titulo, autor, duracion)
        self.likes = likes
        
short1 = Short("Aprendiendo Python", "Dev Senior", 25, "/imagen.png")
        
    