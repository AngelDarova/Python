personaje = {
    "nombre": "Eldrin",
    "clase" : "Mago",
    "vida" : 100,
    "hechizos": ["teletransportacion", "bola de fuego", "invisibilidad"],
    "inventario": ["pocion de vida", "espada", "veneno"]
}

# Acedder a un elemento en especifico
print(f"El tercer hechizo del mago {personaje['nombre']} es {personaje['hechizos'][2]}")

# Agregar elementos a la lista: Linterna magica
personaje["inventario"].append("linterna magica")

print(f"inventario actualizado {personaje['inventario']}")