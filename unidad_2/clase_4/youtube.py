from autor import Autor
from video import Video

#============
#Programa principal
#============

autor1 = Autor("Dev Senior", 250000, "Colombia", True)
video1 = Video("Aprende Python desde 0", "18:30", 125000, autor1)
print(video1.autor.nombre)
print(video1.autor.pais)

video1.autor.nombre = "Dev Senior Code LLC"

video1.autor.set_suscriptores(-3555)
autor1.mostrar_info()
