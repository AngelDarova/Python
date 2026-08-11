from models.producto import Producto

class Inventario:
    
    def __init__(self):
        """
        Aqui represento el inventario en una estructura de lista porque me interesa el orden de insercion
        """
        self.productos = [] # Es clave no perder de vista el atributo de la clase
        
    def registrar_producto(self):
        """
            Permite agregar productos al inventario
        """
        
        
    def listar_producto(self):
        
        print("\n[Inventario]")
        print("Listar productos (pendiente)")
        
    def buscar_producto(self):
        print("\n[Inventario]")
        print("Buscar producto (pendiente)")
        
    def eliminar_producto(self):
        print("\n[Inventario]")
        print("Eliminar producto (pendiente)")
        
    def mostrar_cantidad_productos(self):
        """
            Se puede implementar si necesitamos conocer cuantos productos tenemos en el inventario
        """
        print("mostrar cantidad de productos pendiente")