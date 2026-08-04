# Proyecto: Centro de Misiones para Drones

## Descripción

La empresa **SkyMission** presta servicios con drones para diferentes
tipos de clientes. Cada día llegan solicitudes de misiones que deben ser
ejecutadas según su propósito.

El sistema que desarrollarás permitirá al operador del centro
seleccionar una misión desde un menú y observar cómo se ejecuta. Aunque
todas las misiones pertenecen a la misma empresa, **cada una tiene un
comportamiento diferente**, por lo que será necesario aplicar los
conceptos de **herencia** y **polimorfismo**.

El proyecto debe estar organizado en varios archivos para simular la
estructura de un proyecto profesional.

## Objetivos de aprendizaje

-   Crear una jerarquía de clases utilizando herencia.
-   Sobrescribir métodos para implementar polimorfismo.
-   Separar un proyecto Python en múltiples archivos.
-   Importar clases entre módulos.
-   Construir un programa interactivo mediante un menú de opciones.

## Estructura del proyecto

``` text
centro_drones/
│
├── clases/
│   ├── mision.py
│   ├── entrega.py
│   ├── vigilancia.py
│   ├── fotografia.py
│   └── fumigacion.py
│
├── menu.py
└── main.py
```

## Lógica del negocio

La empresa ofrece cuatro tipos de misiones:

1.  **Entrega de medicamentos**
    -   Peso del paquete.
    -   Destino.
2.  **Vigilancia**
    -   Zona.
    -   Duración del patrullaje.
3.  **Fotografía aérea**
    -   Cantidad de fotografías.
    -   Resolución.
4.  **Fumigación agrícola**
    -   Cantidad de hectáreas.
    -   Tipo de fertilizante.

## Clase base

### Mision

Atributos: - Código de la misión. - Nombre del cliente. - Nombre del
piloto.

Métodos mínimos:

``` python
mostrar_informacion()
ejecutar()
```

Todas las clases hijas deberán sobrescribir `ejecutar()`.

## Clases hijas

### EntregaMedicamentos

Hereda de `Mision`.

Atributos: - Peso del paquete. - Destino.

### Vigilancia

Hereda de `Mision`.

Atributos: - Zona. - Duración.

### FotografiaAerea

Hereda de `Mision`.

Atributos: - Cantidad de fotografías. - Resolución.

### Fumigacion

Hereda de `Mision`.

Atributos: - Hectáreas. - Tipo de fertilizante.

Cada clase deberá implementar su propia versión del método `ejecutar()`.

## Menú del sistema

``` text
====================================

    CENTRO DE MISIONES SKYMISSION

====================================

1. Ejecutar misión de entrega
2. Ejecutar misión de vigilancia
3. Ejecutar misión fotográfica
4. Ejecutar misión de fumigación
5. Salir

Seleccione una opción:
```

## Funcionamiento

Cuando el usuario seleccione una opción:

1.  Crear un objeto de la misión correspondiente.
2.  Mostrar la información de la misión.
3.  Ejecutar la misión.

Ejemplo:

``` python
mision.mostrar_informacion()
mision.ejecutar()
```

El programa siempre invocará los mismos métodos sobre objetos
diferentes, demostrando el uso del **polimorfismo**.

## Reto adicional

Implementa una quinta misión creada por ti que herede de `Mision` y
sobrescriba `ejecutar()`. Integra la nueva misión agregando una opción
al menú.
