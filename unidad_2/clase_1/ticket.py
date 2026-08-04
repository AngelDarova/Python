class Ticket:
    # constructor
    def __init__(self, origen, destino, pasajero):
        self.origen = origen
        self.destino = destino
        self.pasajero = pasajero
        self.asiento = None
        
    def reservar_asiento(self, numero_asiento):
        self.asiento = numero_asiento
        print(f"Asiento {self.asiento} asignado con exito a {self.pasajero}")

# instanciamos la clase Ticket
ticket1 = Ticket("Santiago", "Miami", "Alfredo")
ticket2 = Ticket("Bruselas", "Cartagena", "Alicia")

ticket1.asignar_asiento("22C")    