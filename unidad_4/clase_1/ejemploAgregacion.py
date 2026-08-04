class Libro:
    def __init__(self, id_libro: int, titulo: str):
        self.id_libro = id_libro
        self.titulo = titulo
        
    def __repr__(self):
        return f"Libro(ID={self.id}, Titulo= {self.titulo})"
    
class Biblioteca:
    def __init__(self):
        #el unico atributo de la clase
        self.libros = {}
        
    #Create: crear elememtos en la coleccion
    def agregar(self, id_libro: int, titulo: str):
        nuevo = Libro(id_libro, titulo)
        self.libros[id_libro] = nuevo
        print(f"Agregado exitosamente: {nuevo}")
        
    def mostrar_todos(self):
        print("\n Lista de libros:")
        for libro in self.libros.values():
            print(f" -{libro}")
            
    def actualizar(self, id_libro: int, nuevo_titulo: str):
        if id_libro in self.libros:
            self.libros[id_libro] = nuevo_titulo
            print("Actualizado exitosamente")
            
    def eliminar(self, id_libro: str):
        if id_libro in self.libros:
            borrado = self.libros.pop(id_libro)
            print("Libro eliminado")
biblioteca = Biblioteca()

biblioteca.agregar(11, "Las mil y una noches")
biblioteca.agregar(12, "El principito")
biblioteca.agregar(13, "El coronel no tiene quien le escriba")

biblioteca.mostrar_todos()

biblioteca.actualizar(12, "El principito, ultima edición")

biblioteca.mostrar_todos()
biblioteca.eliminar(12)

biblioteca.mostrar_todos()
