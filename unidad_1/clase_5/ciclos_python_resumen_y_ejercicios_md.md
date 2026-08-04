# Clase: Ciclos en Python (`for`, `while`, `break`, `continue`, contadores y acumuladores)

# 1. Ciclo `for`

## ¿Qué es?

El ciclo `for` se utiliza para recorrer elementos uno por uno de manera automática.

Se usa especialmente cuando:
- sabemos qué elementos recorrer
- conocemos la cantidad de repeticiones
- trabajamos con listas, textos o rangos de números

---

## Idea clave

> El `for` recorre elementos automáticamente.

---

## Ejemplo de uso real

### Mostrar productos de una tienda

```python
productos = ["Mouse", "Teclado", "Monitor"]

for producto in productos:
    print(producto)
```

Salida:

```text
Mouse
Teclado
Monitor
```

---

# 2. Ciclo `while`

## ¿Qué es?

El ciclo `while` repite instrucciones mientras una condición sea verdadera.

Se usa especialmente cuando:
- no sabemos cuántas repeticiones habrá
- dependemos de una condición
- esperamos acciones del usuario o eventos externos

---

## Idea clave

> El `while` continúa mientras algo siga siendo verdadero.

---

## Ejemplo de uso real

### Pedir contraseña hasta acertar

```python
clave = ""

while clave != "python123":
    clave = input("Ingrese la contraseña: ")

print("Acceso permitido")
```

---

# 3. `break`

## ¿Qué es?

`break` permite detener un ciclo inmediatamente.

---

## Idea clave

> `break` rompe el ciclo por completo.

---

## Ejemplo de uso real

### Buscar un producto agotado

```python
productos = ["Pan", "Leche", "Huevos", "Agua"]

for producto in productos:

    if producto == "Huevos":
        print("Producto agotado")
        break

    print(producto)
```

---

# 4. `continue`

## ¿Qué es?

`continue` permite saltar una iteración específica sin detener todo el ciclo.

---

## Idea clave

> `continue` salta solamente una vuelta del ciclo.

---

## Ejemplo de uso real

### Ignorar comentarios vacíos

```python
comentarios = ["Excelente", "", "Muy bueno", ""]

for comentario in comentarios:

    if comentario == "":
        continue

    print(comentario)
```

---

# 5. Contadores

## ¿Qué son?

Un contador es una variable que aumenta o disminuye normalmente de uno en uno.

---

## Idea clave

> Un contador lleva la cuenta de algo.

---

## Ejemplo de uso real

### Contar usuarios conectados

```python
usuarios_conectados = 0

for usuario in range(5):
    usuarios_conectados += 1

print(usuarios_conectados)
```

---

# 6. Acumuladores

## ¿Qué son?

Un acumulador guarda resultados parciales y los va sumando durante un ciclo.

---

## Idea clave

> Un acumulador reúne valores poco a poco.

---

## Ejemplo de uso real

### Total de compras

```python
total = 0

precios = [12, 5, 30]

for precio in precios:
    total += precio

print(total)
```

---

# Situaciones para debatir: ¿`for` o `while`?

## ¿Qué ciclo usarías?

### 1. El sensor de lluvia

Quieres que los limpiaparabrisas del coche funcionen mientras el sensor detecte gotas de agua en el vidrio.

---

### 2. El carrito de compras

Quieres aplicar un 10% de descuento a cada uno de los 7 productos que el usuario ya tiene seleccionados.

---

### 3. La descarga de un archivo

Quieres mostrar una animación de carga mientras el archivo no se haya descargado por completo desde internet.

---

### 4. Pase de lista

Tienes una carpeta con 30 exámenes y necesitas escribir la nota de cada uno en el sistema.

---

### 5. Control de temperatura

Quieres que un ventilador se mantenga encendido mientras la temperatura de la habitación sea mayor a 24°C.

---

### 6. Instagram Feed

Quieres mostrar las últimas 20 fotos publicadas por los amigos de un usuario.

---

### 7. Cajero automático

Quieres pedirle al usuario su clave de seguridad y volver a pedírsela si se equivoca, hasta que por fin la escriba bien.

---

### 8. Editor de texto

Quieres cambiar todas las letras `"a"` por el símbolo `"@"` en un párrafo que escribió el usuario.

---

### 9. Batería del celular

Quieres que el teléfono muestre una alerta de "Ahorro de energía" mientras el nivel de batería sea menor al 15%.

---

### 10. Maratón

Quieres contar y mostrar los números del 1 al 42 para representar cada kilómetro recorrido por un corredor.

---

### 11. Sala de espera virtual

Quieres que una página siga mostrando “Esperando jugadores…” mientras no se hayan conectado suficientes personas.

---

### 12. Playlist de música

Quieres mostrar una por una las canciones guardadas en una lista de reproducción.

---

### 13. Semáforo inteligente

Quieres que el semáforo permanezca en rojo mientras detecte peatones cruzando la calle.

---

### 14. Corrección automática

Quieres revisar cada palabra escrita por un usuario para detectar errores ortográficos.

---

### 15. Juego de adivinanza

Quieres que el usuario siga intentando adivinar el número secreto hasta acertar.

---

# Ejercicios progresivos

# Parte 1 — Ciclo `for`

## Nivel básico

### Ejercicio 1 — Mostrar letras

Muestra cada letra de la palabra `"python"` en líneas separadas.

Guía:

```python
for letra in "python":
```

---

### Ejercicio 2 — Lista de videojuegos

Tienes esta lista:

```python
juegos = ["Minecraft", "FIFA", "Mario Kart"]
```

Muestra cada juego en pantalla.

---

### Ejercicio 3 — Contar del 1 al 5

Muestra los números del 1 al 5 usando `range()`.

Guía:

```python
for numero in range():
```

---

## Nivel intermedio

### Ejercicio 4 — Emojis de reacción

Muestra 10 veces el emoji:

```text
🔥
```

Tip:
- Usa `range()`.

---

### Ejercicio 5 — Mostrar nombres largos

Tienes esta lista:

```python
nombres = ["Ana", "Sebastian", "Luis", "Fernanda"]
```

Muestra solamente los nombres que tengan más de 5 letras.

Pista:
- Usa `if`.

---

### Ejercicio 6 — Tabla de multiplicar

Muestra la tabla del 7 del 1 al 10.

Tip:
- Usa multiplicación dentro del ciclo.

---

## Nivel avanzado

### Ejercicio 7 — Contar vocales

Recorre una palabra ingresada por el usuario y cuenta cuántas vocales tiene.

Pistas:
- Usa un contador.
- Revisa si la letra es `"a"`, `"e"`, `"i"`, `"o"` o `"u"`.

---

### Ejercicio 8 — Carrito de compras

Tienes esta lista de precios:

```python
precios = [10, 25, 7, 30]
```

Calcula cuánto pagará el cliente en total.

Pista:
- Usa un acumulador.

---

# Parte 2 — Ciclo `while`

## Nivel básico

### Ejercicio 1 — Contador simple

Muestra los números del 1 al 5 usando `while`.

Guía:

```python
contador = 1
```

---

### Ejercicio 2 — Cuenta regresiva

Muestra una cuenta regresiva desde 5 hasta 1.

Tip:
- El contador debe disminuir.

---

## Nivel intermedio

### Ejercicio 3 — Contraseña

Pide una contraseña hasta que el usuario escriba `"python"` correctamente.

Pista:
- Usa `input()` y `while`.

---

### Ejercicio 4 — Menú interactivo

Pide opciones al usuario hasta que escriba `"salir"`.

---

## Nivel avanzado

### Ejercicio 5 — Acumulando puntos

Un videojuego entrega 15 puntos por ronda.

Usa un `while` para sumar puntos hasta llegar a 100.

Pistas:
- Usa un acumulador.
- El ciclo debe detenerse automáticamente.

---

# Parte 3 — `break`

## Nivel básico

### Ejercicio 1 — Detener conteo

Muestra números del 1 al 10 pero detén el ciclo cuando aparezca el 6.

Guía:

```python
if numero == 6:
    break
```

---

## Nivel intermedio

### Ejercicio 2 — Buscar un producto

Recorre esta lista:

```python
productos = ["Pan", "Leche", "Huevos", "Arroz"]
```

Detén el ciclo cuando encuentres `"Huevos"`.

---

## Nivel avanzado

### Ejercicio 3 — Número secreto

Crea un juego donde el usuario deba adivinar un número secreto.

Cuando acierte:
- muestra `"Ganaste"`
- usa `break`

Pista:
- Combina `while True` con `input()`.

---

# Parte 4 — `continue`

## Nivel básico

### Ejercicio 1 — Saltar número

Muestra números del 1 al 5 pero omite el número 3.

Guía:

```python
if numero == 3:
    continue
```

---

## Nivel intermedio

### Ejercicio 2 — Ignorar negativos

Recorre esta lista:

```python
numeros = [4, -2, 7, -1, 8]
```

Muestra solamente los números positivos.

---

## Nivel avanzado

### Ejercicio 3 — Filtrar comentarios vacíos

Recorre una lista de comentarios y evita mostrar los que estén vacíos.

Pistas:
- Usa `continue`.
- Un comentario vacío es `""`.

---

# Parte 5 — Contadores y acumuladores

## Nivel básico

### Ejercicio 1 — Contador de likes

Simula 8 nuevos likes usando un contador.

Guía:

```python
likes = 0
```

---

### Ejercicio 2 — Acumulador de monedas

Un jugador recoge monedas con valores:

```python
[5, 3, 10, 2]
```

Calcula el total.

---

## Nivel intermedio

### Ejercicio 3 — Contar aprobados

Recorre esta lista de notas:

```python
[4, 2, 5, 1, 3]
```

Cuenta cuántos estudiantes aprobaron.

Pista:
- Aprueba quien tenga nota mayor o igual a 3.

---

## Nivel avanzado

### Ejercicio 4 — Promedio de compras

Pide 5 precios al usuario y calcula:
- suma total
- promedio

Pistas:
- Usa acumulador.
- Usa contador.
- El promedio es:

```python
promedio = total / cantidad
```

[Documentación oficial de Python sobre ciclos](https://docs.python.org/es/3/tutorial/controlflow.html)