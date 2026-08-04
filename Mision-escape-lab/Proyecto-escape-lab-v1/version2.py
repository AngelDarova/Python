
"""

    ESTADO DEL JUEGO

"""

juego_activo = True

habitacion_actual = True

inventario = []

energia = False

codigo_descubierto = False

tarjeta_obteida = False

salida_abierta = False

while juego_activo == True:

    if habitacion_actual == "Recepcion":

        print("="* 40)

        print("RECEPCION")

        print("="* 40)

        print("Te encuentras en la entrada del laboratorio")

        print()

        print("¿Qué deseas hacer?:")

        print("1. Ir al almacén")

        print("2. Ir a la sala de servidores")

        print("3. Revisar inventario")

        print("4. Salir del juego")

        opcion = input("Opcion; ")

        if opcion == "1":

            habitacion_actual = "Almacen"

        elif opcion == "2":

            habitacion_actual = "Sala de servidores"

        elif opcion == "3":

            print()

            if len(inventario) == 0:

                print("Tu inventario está vacío")

            else: 

                for objeto in inventario:

                    print("-", objeto)

        elif opcion == "4":

            juego_activo = False

        else:

            print("Opcion no valida")

    

    elif habitacion_actual == "Almacen":

        print()

        print("="* 40)

        print("ALMACEN")

        print("="* 40)  

    elif habitacion_actual == "Sala de servidores":

        ...

    

    elif habitacion_actual == "Laboratorio de IA":

        ...

    

    elif habitacion_actual == "Salida":

        ...
