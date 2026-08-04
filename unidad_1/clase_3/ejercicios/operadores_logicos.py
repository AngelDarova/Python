# and, or, not

# 5 > 3 < 20
# Para pasar de a nivel necesitas tener la llave Y tener más de 100 puntos 

tiene_llaves = True
puntos = 120

pasa_nivel = (tiene_llaves == True) and (puntos > 100)

# Tienes descuento si eres estudiante O si eres mayor de 65 años 
es_estudiante = False
es_mayor_65 = True

descuento = es_estudiante or es_mayor_65


# El sistema de riego se activa si NO está lloviendo 
esta_lloviendo = False
activar_riego = not esta_lloviendo

resultado = not (5 != 3)

resultado = ((5 > 3) and (3 <= 3)) or (3 > 100)

# Un estudiante aprueba si su promedio es mayor a 70 Y no tienes faltas (faltas = 0)
nota1 = 80
nota2 = 40
faltas = 10 // 5 - 2

promedio = (nota1 + nota2) / 2
aprobado = promedio > 70 and faltas == 0

print(f"Promedio: {promedio}, faltas: {faltas}")
print(f"Aprobado: {aprobado}")