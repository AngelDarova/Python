from autor import Autor #Indica que esta clase necesita la clase Autor

class Video:
    def __init__(self, titulo, duracion, visualizaciones, autor):
        self.titulo = titulo
        self.duracion = duracion
        self.visualizaciones = visualizaciones
        #Aqui almacenamos un objeto autor
        self.autor = autor
        
        
    def mostrar_info(self):
        print("=======Video========")
        print(f"Titulo: {self.titulo}")
        print(f"Duracion: {self.duracion}")
        print(f"Visualizaciones: {self.visualizaciones}")
        self.autor.mostrar_info()

