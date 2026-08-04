# Ejercicios — Estructuras Condicionales en Python

# Objetivos

Practicar:

- if
- elif
- else
- match-case
- comparaciones
- validación de datos
- condiciones compuestas (`and`, `or`, `not`)
- diseño lógico
- razonamiento con condiciones específicas y generales

---

# Recomendaciones

Antes de programar:

1. Identifica los datos de entrada.
2. Piensa las decisiones en lenguaje humano.
3. Detecta cuáles condiciones son más específicas.
4. Pregunta:
   -las condiciones, ¿unas contienen a otras?
5. Luego traduce la lógica a Python.

---

# NIVEL FÁCIL

---

# Ejercicio 1 — Mayor de edad

Solicita la edad de una persona.

- Si tiene 18 o más → mostrar:
  `"Eres mayor de edad"`
- Si no → mostrar:
  `"Eres menor de edad"`

## Tip

Piensa qué conjunto representa:

```python
edad >= 18
```

---

# Ejercicio 2 — Temperatura

Solicita una temperatura.

- Si es mayor a 30 → mostrar:
  `"Hace calor"`

## Tip

Aquí solo necesitas un `if`.

---

# Ejercicio 3 — Contraseña básica

Pide una contraseña.

- Si la contraseña es `"python123"`:
  mostrar `"Acceso permitido"`
- Si no:
  mostrar `"Contraseña incorrecta"`

## Tip

Usa:

```python
==
```

para comparar textos.

---

# Ejercicio 4 — Número positivo o negativo

Solicita un número.

- Si es positivo → mostrar:
  `"Número positivo"`
- Si es negativo → mostrar:
  `"Número negativo"`
- Si es cero → mostrar:
  `"Es cero"`

## Tip

Observa cómo las condiciones son independientes, no hay subconjuntos.

---

# Ejercicio 5 — Semáforo

Solicita un color:

- `"rojo"`
- `"amarillo"`
- `"verde"`

Inventa una acción para cada color y muestra la acción correspondiente.

## Tip

Puedes resolverlo con `if-elif` o con `match-case`.

---

# Ejercicio 6 — Sistema de notas

Solicita una nota.

- 4.5 o más → `"Excelente"`
- 3.0 o más → `"Aprobado"`
- menos de 3.0 → `"Reprobado"`

## Tip importante

Las condiciones más específicas deben ir primero.

---

# Ejercicio 7 — Sistema de descuentos

Solicita el valor de una compra.

- mayor a 500 → 30% descuento
- mayor a 100 → 10% descuento
- cualquier otro caso → sin descuento

Mostrar:

- descuento aplicado
- total a pagar

## Tip

Piensa en subconjuntos o subrangos contenidos unos dentro de otros.

---

# NIVEL INTERMEDIO

---

# Ejercicio 8 — Login de plataforma

Solicita:

- usuario
- contraseña

Reglas:

- Si el usuario es `"admin"` y la contraseña es `"1234"`:
  mostrar `"Bienvenido administrador"`
- Si el usuario existe pero la contraseña es incorrecta:
  mostrar `"Contraseña incorrecta"`
- Si el usuario no existe:
  mostrar `"Usuario no encontrado"`

## Tip

Aquí aparecen condiciones compuestas.

---

# Ejercicio 9 — Cajero automático

Solicita:

- saldo disponible
- valor a retirar

Reglas:

- Si el retiro es mayor que el saldo:
  mostrar `"Fondos insuficientes"`
- Si el retiro es igual al saldo:
  mostrar `"Retiro realizado. Cuenta vacía"`
- Si el retiro es menor:
  mostrar saldo restante
- Si el retiro es negativo:
  mostrar `"Valor inválido"`

## Tip

La validación del número negativo debe ir primero porque los datos inválidos deben bloquear el resto del sistema.

---

# Ejercicio 10 — Clasificación de usuarios

Solicita la edad.

Clasificar:

- menor de 13 → niño
- menor de 18 → adolescente
- menor de 60 → adulto
- cualquier otro caso → adulto mayor

## Tip

Piensa en rangos contenidos.

---

# Ejercicio 11 — Streaming de películas

Solicita:

- edad
- tipo de contenido

Reglas:

- contenido `"terror"` requiere 18 años
- contenido `"acción"` requiere 13 años
- contenido `"infantil"` disponible para todos

Mostrar si puede acceder o no.

## Tip

Usa condiciones compuestas con `and`.

---

# Ejercicio 12 — Validación de correo

Solicita un correo electrónico.

Reglas:

- Si contiene `"@"` y `"."`
  → `"Correo válido"`
- Si no:
  → `"Correo inválido"`

## Tip

Usa:

```python
in
```

---

# Ejercicio 13 — Menú interactivo

Mostrar:

```text
1. Ver perfil
2. Configuración
3. Ayuda
4. Salir
```

Solicitar opción y responder según el caso.

## Tip

Ideal para practicar `match-case`.

---

# Ejercicio 14 — Clasificación de batería

Solicita porcentaje de batería.

- 80 o más → `"Batería alta"`
- 30 a 79 → `"Batería media"`
- 1 a 29 → `"Batería baja"`
- 0 → `"Dispositivo apagado"`

## Tip

Piensa cómo ordenar las condiciones.

---

# Ejercicio 15 — Validación de acceso a evento

Solicita:

- edad
- si tiene boleta (`si/no`)

Reglas:

- Solo entra si:
  - tiene 18 o más
  - y posee boleta

Mostrar:
- acceso permitido
- acceso denegado

## Tip

Usa:

```python
and
```

---

# NIVEL AVANZADO

---

# Ejercicio 16 — Sistema de envío de paquetes

Solicita:

- peso del paquete
- tipo de envío

Reglas:

## Envío nacional

- hasta 1kg → $5
- hasta 5kg → $10
- más de 5kg → $20

## Envío internacional

- hasta 1kg → $15
- hasta 5kg → $30
- más de 5kg → $50

## Tip

Combina `match-case` con `if`.

---

# Ejercicio 17 — Sistema de autenticación bancaria

Solicita:

- usuario
- contraseña
- código de seguridad

Reglas:

- Usuario correcto:
  `"cliente"`
- Contraseña correcta:
  `"banco123"`
- Código correcto:
  `"9999"`

Mensajes posibles:

- acceso completo
- contraseña incorrecta
- código inválido
- usuario no encontrado

## Tip

Piensa en decisiones jerárquicas.

---

# Ejercicio 18 — Diagnóstico básico médico

Solicita:

- temperatura corporal
- si tiene tos (`si/no`)
- si tiene dificultad respiratoria (`si/no`)

Reglas:

- fiebre + tos + dificultad respiratoria
  → `"Atención médica urgente"`
- fiebre + tos
  → `"Posible infección"`
- solo fiebre
  → `"Monitorear síntomas"`
- ningún síntoma
  → `"Estado estable"`

## Tip

Aquí las condiciones pueden superponerse.

---

# Ejercicio 19 — Sistema de niveles de videojuego

Solicita:

- vida
- energía
- armadura

Reglas:

- vida <= 0
  → `"Game Over"`
- vida < 20 y armadura == 0
  → `"Estado crítico"`
- energía < 10
  → `"Energía baja"`
- cualquier otro caso
  → `"Jugador estable"`

## Tip

Las condiciones más específicas primero.

---

# Ejercicio 20 — Plataforma de descuentos premium

Solicita:

- valor de compra
- si es miembro premium
- si tiene cupón

Reglas:

- compra > 1000 y premium
  → 40% descuento
- compra > 500 o tiene cupón
  → 20% descuento
- compra > 100
  → 10% descuento
- cualquier otro caso
  → sin descuento

Mostrar:

- descuento
- total final

## Tip

Aquí practicarás:

- subconjuntos
- condiciones compuestas
- orden lógico

---

# Ejercicio 21 — Asistente virtual

Solicita un comando:

- `"hora"`
- `"fecha"`
- `"clima"`
- `"salir"`

Usa `match-case`.

Además:

- si el comando está vacío:
  mostrar `"Entrada inválida"`

## Tip

Valida antes del `match`.

---

# Ejercicio 22 — Clasificador de triángulos

Solicita tres lados.

Reglas:

- todos iguales → equilátero
- dos iguales → isósceles
- todos diferentes → escaleno

Validar además:

- ningún lado puede ser menor o igual a cero

## Tip

Aquí aparecen múltiples comparaciones.

---

# Ejercicio 23 — Sistema de permisos

Solicita:

- rol
- estado de cuenta

Reglas:

## admin
- acceso total

## editor
- acceso parcial

## visitante
- solo lectura

Pero:

- si la cuenta está suspendida:
  bloquear acceso completamente

## Tip

La suspensión debe evaluarse primero.

---

# Ejercicio 24 — Plataforma educativa

Solicita:

- nota
- porcentaje de asistencia

Reglas:

- nota >= 4.5 y asistencia >= 80
  → `"Aprobado con honores"`
- nota >= 3.0 y asistencia >= 60
  → `"Aprobado"`
- nota >= 3.0 y asistencia < 60
  → `"Reprobado por inasistencia"`
- cualquier otro caso
  → `"Reprobado"`

## Tip

Las condiciones compiten entre sí.

---

# Ejercicio 25 — Sistema de recomendaciones musicales

Solicita:

- estado de ánimo

Opciones:

- feliz
- triste
- relajado
- motivado

Mostrar recomendación musical diferente para cada caso usando `match-case`.

Agregar:

- caso por defecto para estados desconocidos.

---

# Reflexión final

Las estructuras condicionales permiten que los programas:

- reaccionen,
- clasifiquen,
- validen,
- interpreten situaciones,
- y tomen decisiones inteligentes.

Son uno de los pilares fundamentales de toda aplicación real.
