def mostrar_menu():
    """
    
    Muestra las opciones disponibles para el juego
    """
    pass

def explorar(vida, nivel):
    """
        El aventurero explora la cueva
        
        Parametros
        vida (int): vida actual del jugador
        nivel(int): nivel actual del jugador
    
        retorna:
            Dos valores que son vida y nuevo nivel (tupla)
    """
    pass

def buscar_tesoro(vida, oro):
    """
        El aventurero busca el tesoro
        
        Parametros
        vida (int): vida actual del jugador
        oro(int): oro actual del jugador
    
        retorna:
        Nueva vida y nueva cantidad de oro (tupla)
    """
    pass

def descansar(vida):
    """
        Recupera 15 puntos de vida del jugador.
    
        Parametros:
        vida(int): 
        vida actual del jugador
    
        retorna:
        int: nueva vida del jugador (-15)
    """
    pass

def mostrar_estado(vida, nivel, oro):
    """
        Muestra la informacion actual del jugador
    
        Parametros:
        nombre(str): nombre del jugador
        vida(int): vida actual
        oro(int): oro actual
        nivel(int): nivel actual
    """
    pass

def main():
    """
        Funcion principal del programa
        
        Aqui se crearan las variables iniciales,
        se ejecutara el menu y se coordinara toda
        la logica del juego
    """
    nombre=input("Ingrese el nombredel aventurero: ")
    vida= 100
    oro=0
    nivel=1
    
    jugando=True
    
    while jugando and vida>0:
        mostrar_menu()
        
    opcion =input("Seleccione una opcion: ")
    
    if opcion == "1":
        vida, nivel = explorar(vida, nivel)
    elif opcion == "2":
        vida, oro = buscar_tesoro(vida, oro)
    elif opcion == "3":
        vida = descansar(vida)
    elif opcion == "4":
        mostrar_estado(nombre, vida, oro, nivel)
    elif opcion == "5":
        print("\nGracias por jugar")
        jugando = False
        
    else:
        print("\nOpcion invalida")


#punto de arranque de la aplicacion
main()