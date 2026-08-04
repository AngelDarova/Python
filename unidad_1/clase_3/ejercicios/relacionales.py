password_guardado = "secreto123"
password_escrito = input("password: ")

# qué operador usamos para saber si son identicas?

acceso_concedido = password_guardado == password_escrito
print(f"acceso concedido: {acceso_concedido}")


