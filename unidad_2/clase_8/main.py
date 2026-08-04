from clases.entrega import EntregaMedicamentos
from menu import mostrar_menu

def play():
    while True:
        mostrar_menu()
        opcion = input()
        if(opcion == "5" ):
            print("saliendo del programa...")
            break
        elif opcion in ["1", "2", "3", "4"]:
            print("opcion valida elegida")
            
            if opcion == "1":
                codigo = input("Codigo: ")
                cliente = input("Cliente: ")
                piloto = input("Piloto: ")
                peso = input("Peso: ")
                destino = input("Destino: ")
                entrega = EntregaMedicamentos(codigo, cliente, piloto, peso, destino)
                entrega.ejecutar()
            elif opcion == "2":
                pass
        
        
        else:
            print("opcion no valida")
    
play()