import time

NUM_ELEMENTOS = 1_000_000

OBJETIVO = "elemento_999999"

print("Creando estructura de datos")

lista_datos = {f"elemento_{i}" for i in range(NUM_ELEMENTOS)}

diccionario_datos = {f"elemento_{i}": True for i in range(NUM_ELEMENTOS)}

print("Estructuras creadas con exito.\n")

inicio = time.perf_counter()

encontrado_lista = OBJETIVO in lista_datos

fin = time.perf_counter()
tiempo_lista = fin - inicio


inicio = time.perf_counter()

encontrado_dicc = OBJETIVO in diccionario_datos

fin = time.perf_counter()
tiempo_dicc = fin - inicio


print("=" * 45)
print(f" RESULTADOS DE BUSQUEDA ({NUM_ELEMENTOS:,} elementos)")
print("=" * 45)
print(f"Lista de")

