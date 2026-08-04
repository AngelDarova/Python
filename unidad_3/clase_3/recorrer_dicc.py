producto = {
    "id": 1204,
    "nombre": "Audifonos Gamer",
    "precio": 89.99,
    "disponible": True
}

print("---PROPIEDADES DEL PRODUCTO---")
for llave in producto:
    print(f"propiedad: {llave}")
    
print("---DATOS DEL PRODUCTO---")
for valor in producto.values():
    print(f"Dato: {valor}")
    
print("---FICHA TECNICA---")
for clave, valor in producto.items():
    print(f"{clave.upper()}: {valor}")
