from models.producto import Producto

class Venta:
    def __init__(self, producto: Producto, cantidad: int):
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = producto.precio
        pass
    
    def calcular_total(self):
        return self.cantidad * self.precio_unitario
        
        
    def mostrar(self):
        print(f"Producto: {self.producto.nombre}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Precio unitario: {self.precio_unitario}")
        print(f"Total: {self.calcular_total()}")