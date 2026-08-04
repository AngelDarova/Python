
# Clase padre
class Contenido:
    def reproducir(self):
        pass
    
#Clases hijas
class Video(Contenido):
    def reproiducir(self):
        print("Reproduciendo video")
    
class Short(Contenido):
    def reproducir(self):
        print("Reproduciendo Short")
        
class Podcast(Contenido):
    def reproducir(self):
        print("Reproduciendo podcast")
        
class Publicidad(Contenido):
    def reproducir(self):
        print("Reproduciendo publicidad")
        
class ContenidoX:
    pass

#Significa que diferentes objetos pueden responder al mismo mensaje de maneras distintas

def reproductor(contenido: Contenido):
    contenido.reproducir()
    
reproductor(Video())
reproductor(Short())
reproductor(Publicidad())
