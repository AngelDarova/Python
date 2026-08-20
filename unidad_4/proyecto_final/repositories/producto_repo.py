import json

class ProductoRepository:
    
    def __init__(self, archivo: str):
        self.archivo = archivo
        
    def guardar(self, productos):
        datos = []
        
        # 1) serializamos toda la lista recibida
        for producto in productos:
            datos.append({
                "codigo": producto.codigo,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "stock": producto.stock
            })
            
        #guardar esa lista serializada en el archivo
        with open (self.archivo, "w", encoding="utf-8") as archivo:
            json.dump(
                datos,
                archivo, 1
                indent=4
                ensure_ascii= False
            )
            
    def cargar(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            return[]
        
        productos = []
        
        for dato in datos:
            producto = Producto(
                dato["codigo"],
                dato["nombre"],
                dato["precio"],
                dato["stock"]
            )
            productos.append(producto)
        return productos