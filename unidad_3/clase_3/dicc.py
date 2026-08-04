

perfil_vacio = {} #inicializo un diccionario

usuario_intagram = {
    "username" : "@JuanPro",
    "seguidores" : 4353,
    "verificado" : True,
    "post_guardados" : ["foto_playa", "meme_python"]
}

producto = {"nombre": "teclado mecanico", "precio": 76.99, "stock": 45}

# 1.Leer un valor (acceso)

print(usuario_intagram["username"]) #resultado: "@JuanPro"
print(usuario_intagram["verificado"]) #resultado: True

# Modificar un valor
usuario_intagram["seguidores"] = 4600 #actualizamos el valor de la llave corres.
usuario_intagram["seguidores"] += 1
print(usuario_intagram["seguidores"]) #resultado: 4601

#Agregar un nuevo valor clave: valor
usuario_intagram["edad"] = 25 #si no existe la llave "edad" se crea
usuario_intagram["edad"] = 34 #si ya existe, se sobreescribe el valor

print(usuario_intagram)

#Eliminar
del usuario_intagram["post_guardados"]

print(usuario_intagram)
