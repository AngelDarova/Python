
class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        """
        
        En mi sistema todo producto tendra los siguientes atributos:
        *Código
        *Nombre
        *Precio
        *Stock
        """
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        
    def mostrar(self):
        """
            Muestra la informacipon del producto        
        """
        print(f"Código {self.codigo}")
        print(f"Nombre {self.nombre}")
        print(f"Precio {self.precio}")
        print(f"Stock {self.stock}")
        
    print("Método mostrar () pendiente de implementar")
    
    def aumentar_stock(self, cantidad):
        """
        Aumenta el stock disponible.
        """
        self.stock += cantidad
        
    def disminuir_stock(self, cantidad):
        """
            Disminuye el stock disponible
        """
        
        if self.hay_stock(cantidad):
            self.stock -= cantidad
            return True #esta operacion salio exitosa
                
        return False
        
    def disminuir_en_uno(self):
        self.stock -= 1
        
    def hay_stock(self, cantidad):
        """
            Verifica si existe stock suficiente
        """
        return self.stock >= cantidad

