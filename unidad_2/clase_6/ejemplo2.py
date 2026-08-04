class Personaje:
    pass

#clases hijas
class Guerrero(Personaje):
    def atacar(self):
        print("Golpea con espada")
        
class Mago(Personaje):
    def atacar(self):
        print("Lanza hechizo")
        
class Escudero(Personaje):
    def atacar(self):
        print("Crear barrera holografica alv")
        
#controlador del juego
def iniciar_ataque (personaje: Personaje):
    personaje.atacar()
    
iniciar_ataque(Guerrero())
iniciar_ataque(Mago())
iniciar_ataque(Escudero())