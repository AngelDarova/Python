"""def registrar_usuario(nombre, edad):
    print(f"usuario: {nombre}")
    print("edad:  {edad}")
    
mi_nombre = input("Nombre: ")
mi_edad = input("Edad: ")

registrar_usuario(mi_nombre, mi_edad)"""

def calcular_impuesto(precio):
    resultado = precio * 0.15 # aqui almaceno el 15% del precio
    return resultado
    
precio_producto = 200 # 200 + 30.0
total_a_pagar = precio_producto + calcular_impuesto(precio_producto)
print(f"El total a pagar es: ${total_a_pagar}")