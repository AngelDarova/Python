producto = {
    "id": 1204,
    "nombre": "Audifonos Gamer",
    "precio": 89.99,
    "disponible": True
}

# el metodo .get() viene a solucionar el problema de KeyError, es decir, permite conectar de forma segura el dicc.
# si la llave existe, te devuelve el valor
# si no existe...
nombre_item = producto["nombre"]
print(nombre_item)

descuento = producto.get("descuento", 0.0)
print(descuento)

precio = producto.get("precio")
print(precio)

#Los metodos extractores
#.keys(): extrae todas las llaves existentes en el dicc (nombre de las propiedades)
#.values(): extrae todos los valores existentes en el dicc (los datos guardados)

propiedades = producto.keys()
print()

datos = 
