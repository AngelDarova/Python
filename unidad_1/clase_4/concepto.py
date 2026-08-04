
"""
    if condicion:
        instrucciones (lo que se ejecuta una vez la condición sea cierta)

nivel = 2
vidas = 20

if nivel >= 10:
    print("Bienvenido a la zona pro!")
else: # en cualquier otro caso...
    print("Nivel insuficiente. Sigue entrenando...")
"""

productos_en_carito = 0

if productos_en_carito > 0:
    print("Proceder a pago")
else:
    print("Tu carrito esta vacío")

"""
    SI ocurre algo
        hacer algo
    SINO
        hacer esto otro
"""
"""
    elif: "Si la condición anterior NO se cumplió, entonces prueba esta otra"

    Sintaxis:
    if condicion_1:
        instrucciones
    elif condicion_2:
        instrucciones
    elif condicion_3:
        instrucciones
    else:
        intrucciones

estado = "preparando"

if estado == "preparando":
    print("El chef está cocinando")
elif estado == "en camino":
    print("el repartidor está cerca")
elif estado == "entregado":
    print("buen provecho!")
else:
    print("Error: No podemos rastrear su pedido en este momento")


nota = 4.7

if nota >= 4.5:
    print("Aprobaste")
elif nota >= 3.0:
    print("Excelente")
else:
    print("Desaprobaste :()")



vida = 120

if vida < 50:
    print("Herido")
elif vida < 10:
    print("critico")

"""
numero = -2
if numero > 0:
    print("positivo")
elif numero < 0:
    print("negativo")
else:
    print("el número es igual a cero")


























