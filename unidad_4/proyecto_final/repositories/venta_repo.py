import json

from models.venta import Venta
from models.producto import Producto

class VentaRepository:
    
    def __init__(self, archivo: str): #este str representa la ruta del archivo: data/ventas
        self.archivo = archivo
        
    def guardar(self, ventas):
        datos = []
        
        for venta in ventas:
            datos.append({
                "codigo_producto": venta.producto.codigo,
                "nombre_producto": venta.producto.nombre,
                "cantidad": venta.cantidad
                "precio_unitario": venta.precio_unitario
                "total": venta.calcular_total
            })
            
        with open(self.archivo, "w", encoding= "utf-8") as archivo:
            json.dump(datos,archivo, ident=4, ensure_ascii=False)
            
    def cargar(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as archivo: #leemos el archivo
                datos = json.load(archivo) #cargamos los datos crudos del archivo
        except FileNotFoundError: 
            return[]#si hay alguna falla en la lectura del archivo, se manda una lista vacia
        
        #una vez tenemos los datos crudos en formato JSON
        #los pasamos a python:
        ventas = []
        for dato in datos: #recorremos los datos crudos, para ir creando de uno a uno de json --> python
            producto = Producto( #estos datos se los pasamos al constructor Producto
                dato["codigo_producto"],
                dato["nombre_producto"],
                dato["precio_unitario"],
                0
            ) # como proceso resultante obtenemos una lista de objetos productos: python.
            #Luego, agregamos el producto a la venta
            venta = Venta( #creamos la venta
                            producto,
                            dato["cantidad"]
            )
            ventas.append(venta) #obtenemos asi una lista completa de ventas en python.
        return ventas #se retorna para que el ventas.service lo use
