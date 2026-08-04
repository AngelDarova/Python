#Mientras (el PIN sea incorrecto):
#      volver a pedir PIN


#Mientras (el personaje esté dentro de la zona de veneno):
     # Restar 5 puntos de salud

#Mientras (condicion):
   # bloque de instrucciones
"""
contador = 1

while contador <= 3:
    
    print(contador)
    contador += 1


opcion = ""

while opcion != "salir":
    opcion = input("Escriba una opcion: ")
    print("Elegiste: ", opcion)


print("otras instrucciones")
print("otras instrucciones")
print("otras instrucciones")



contador = 0
password = "admin123"
passIngresado = ""

while (passIngresado != password) and (contador < 3):
    passIngresado = input("Ingrese el password: ")
    contador += 1
    print(f"ha intentado {contador} veces")

    if contador == 3:
        print("cuenta bloqueada!")
        

if(contador < 3 ):
    print("accediendo al sistema...")

"""
contador = 0
while True:
    contador+= 1
    print(contador)
    if contador == 3:
        break