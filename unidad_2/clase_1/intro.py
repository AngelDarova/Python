"""
#Video 1
v1_titulo = "Aprende POO con"
v1_autor = "Dev senior code"
v1_likes = 1500
v1_reproduciendo = False

#Video 2
v2_titulo = "Curso avanzado de Spring"
v2_autor = "Dev java channel"
v2_likes = 670
v2_reproduciendo = False

v3_titulo = "Curso avanzado de Spring"
v3_likes = 670
v3_reproduciendo = False

def dar_like(likes_actuales, titulo_video):
    print(f"Le diste like a {titulo_video}!")
    return likes_actuales + 1

v2_likes = dar_like(v2_likes, v2_titulo)
"""

#Solucion
class Video:
    #Constructor
    def __init__(self, titulo_ingresado, autor_ingresado):
        self.titulo = titulo_ingresado
        self.autor = autor_ingresado
        self.likes = 0
        
    def dar_like(self):
        self.likes += 1
        print(f"Alguien ha dado like a {self.titulo}, total de likes: {self.likes}")
        


video_tutorial = Video("Clase 1 POO", "Profe_python")
video_musical = Video("Mi cancion favorita", "Artista Latam")

video_tutorial.dar_like()
video_tutorial.dar_like()
video_tutorial.dar_like()

video_musical.dar_like()


print(f"Se ha subido: {video_tutorial.titulo} por {video_tutorial.autor}")
print(f"Se ha subido: {video_musical.titulo} por {video_musical.autor}")



