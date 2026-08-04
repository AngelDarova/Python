"""
numeros = [32,45,72,2345,565,231,454,565]

objetivo = 231
encontrado = False

for numero in numeros:
    if numero == objetivo:
        encontrado = True
        break
print(f"El numero fue encontrado? {encontrado}")
"""

def buscar(objetivo, lista):
    posicion = -1
    for numero in lista:
        posicion += 1
        if numero == objetivo:
            posicion = True
            break
    
    return posicion

numeros = [32,45,72,2345,565,231,454,565]

resultado = buscar(1000, numeros)

if resultado == -1:
    print("El resultado no esta en la lista")
else:
    print(f"El número a buscar está en la lista en la posición: {resultado}")