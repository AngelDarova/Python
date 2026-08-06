from utils.menu import mostrar_menu
from services.inventario import Inventario
from services.ventas import Ventas

def main():
    
    #Dependencias de la clase main
    inventario = Inventario() #instanciamos la clase inventario
    ventas = Ventas() #Instanciamos la clase ventas
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            inventario.registrar_producto()
            
        elif opcion == "2":
            inventario.listar_producto()
            
        elif opcion == "3":
            inventario.buscar_producto()
            
        elif opcion == "4":
            inventario.eliminar_producto()
        
        elif opcion == "5":
            ventas.registrar_venta()
            
        elif opcion == "6":
            ventas.listar_ventas()
            
        elif opcion == "7":
            ventas.total_vendido()
            
        elif opcion == "8":
            print("\nGracias por utilizar el sistema")
            break
        
        else:
            print("\nOpcion invalida.")
            
main()
    