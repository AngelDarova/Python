from models.venta import Venta
from services.inventario import Inventario
class Ventas:
    def __init__(self):
        """
            Decidi almacenar en una lista ya que me interesa mantener registro y orden cronologico
            y en orden de llegada cada venta realizada
        """
        self.ventas = [] #va a coleccionar objetos de tipo Venta
        
    def registrar_venta(self, inventario: Inventario, codigo_producto, cantidad):
        producto = inventario.buscar_producto(codigo_producto)
        
        #Primera validación: verificar existencia del producto
        if producto is None:
            print("Producto no encontrado")
            return #significa que el método acaba aqui
        
        #Segunda validación: verificar el stock adecuado
        if not producto.hay_stock(cantidad):
            print("Stock insuficiente para la venta.")
            return
        
        #Procedemos a la venta porque paso las 2 validaciones
        producto.disminuir_stock(cantidad)
        venta = Venta(producto, cantidad)
        self.ventas.append(venta)
        print("Venta registrada correctamente")
        
        
    def listar_ventas(self):
        if self.ventas.__len__== 0:
            print("No hay ventas registradas.")
            return
        
        print("\nHISTORIAL DE VENTAS")
        print("-"*40)
        
        for venta in self.ventas:
            venta.mostrar
            print("-"*40)
            
        
    def total_vendido(self):
        gran_total = 0
        
        for venta in self.ventas:
            gran_total += venta.calcular_total()
            
        print(f"Total vendido: ${gran_total}")
        