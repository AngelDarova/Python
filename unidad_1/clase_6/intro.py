def dar_bienvenida(nombre):
    print("---------------------")
    print(f"¡Bienvenido al sistema, {nombre}")
    print("Tu sesion se ha iniciado con exito")
    print("---------------------")
    
nombre("Juan")
nombre("Maria")
nombre("Pedro")


def mostrar_precio(precio):
    precio = precio * 2
    print("Precio aumentado al doble", precio)
    
mostrar_precio(500)