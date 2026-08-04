a = 5
b = 2
c = 4
print(a ** b)
print(a % b)


#Operadores de asignación compuesta
b = b + 10 # aumentamos a en 10
b+= 10
a = a - 2 # disminuimos a en 2
a-=2

c*= 5  # c = c * 5

c/=2 # c = c / 2   --> 10.0


# Imagina que calculamos el total de una tienda ¿Dónde hay una promoción de compra por cajas
#datos iniciales

productos = 22
capacidad_cajas = 5
precio_unitario = 10.5

#1. ¿Cuántas cajas llenas tenemos?
cajas_llenas = productos // capacidad_cajas

#2. ¿Cuantos productos quedaron sueltos?
sueltos = productos % 5

# 3. Costo total de los productos
total = productos * precio_unitario

print(f"Tienes {cajas_llenas} cajas llenas y {sueltos} productos sueltos")
print(f"El total a pagar es: {total}")

ventas1 = 100
ventas2 = 50

promedio = 100 + 50 / 2
print(f"promedio: {promedio}")