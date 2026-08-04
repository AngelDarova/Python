"""
    Uba tienda tiene diferentes tipos de clientes:
    . Cliente normal --> sin descuento
    . Cliente frecuente --> descuento del 10%
    . Cliente premium --> descuento del 25%
    
    El sistema debe calcular el valor final de la compra: recibimos la info. --> tipo cliente y compra.
"""

"""
    #Sin polimorfismo
def calcular_total(tipo_cliente, compra)
    if tipo_cliente == "normal":
        return compra
        
    elif tipo_cliente == "frecuente":
        return compra * 0.9
        
    elif tipo_cliente == "premium":
        return compra * 0.75
        
print(calcular_total("frecuente", 100))
"""

class Cliente:
    def calcular_compra(self, valor_compra):
        pass
    
class ClienteNormal(Cliente):
    def calcular_compra(self, valor_compra):
        return valor_compra
    
class Frecuente(Cliente):
    def calcular_compra(self, valor_compra):
        return valor_compra * 0.9
    
class Premium(Cliente):
    def calcular_compra(self, valor_compra):
        return valor_compra * 0.75
    
class VIP(Cliente):
    def calcular_compra(self, valor_compra):
        return valor_compra * 0.5
    
def procesar_compra(cliente: Cliente, valor):
    total = cliente.calcular_compra()
    print(f"Total a pagar{total}")
    
procesar_compra(Premium(), 100)
procesar_compra(Frecuente(), 200)
procesar_compra(VIP(), 1000)